"""Synthetic audio sources for early ICA experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

InstrumentKind = Literal["harmonic", "snare_noise"]


@dataclass(frozen=True)
class InstrumentSpecOld:
  '''
  Specification for one synthetic source.
  '''

  name: str
  
  fundamental_hz: float
  partials: tuple[float, ...]
  
##endof:  class InstrumentSpec


@dataclass(frozen=True)
class InstrumentSpec:
  '''
  Specification for one synthetic source.

  Harmonic instruments use `fundamental_hz` and `partials`.
  Snare-like transient sources use `center_hz`, noise/tone weights,
  and decay settings.
  '''

  name: str
  kind: InstrumentKind
  
  fundamental_hz: float
  partials: tuple[float, ...]
  
  center_hz: float | None=None
  noise_weight: float=0.90
  tone_weight: float=0.10
  decay_rate: float=35.0
  hit_duration_s: float=0.20
  seed: int=0
  
##endof:  class InstrumentSpec


def one_second_on_off_envelope(
      duration_s: float,
      sample_rate: int,
      on_s: float = 1.0,
      off_s: float = 1.0,
    ) -> np.ndarray:
  '''
  Return an envelope that alternates one second on and one second off.
  '''
  
  num_samples = int(round(duration_s * sample_rate))
  t = np.arange(num_samples) / sample_rate
  period = on_s + off_s
  envelope = (np.mod(t, period) < on_s).astype(float)

  # Tiny fade to reduce clicks.
  fade_len = max(1, int(0.01 * sample_rate))
  kernel = np.linspace(0.0, 1.0, fade_len)
  for start in range(0, num_samples, int(round(period * sample_rate))):
    stop = min(start + fade_len, num_samples)
    envelope[start:stop] *= kernel[: stop - start]
  ##endof: for

  return envelope
##endof:  one_second_on_off_envelope


def make_source_from_spec(
      spec: InstrumentSpec,
      duration_s: float,
      sample_rate: int,
    ) -> np.ndarray:
  '''
  Create one synthetic source from an InstrumentSpec.
  '''

  if spec.kind == "harmonic":
    if spec.fundamental_hz is None:
      raise ValueError("harmonic source requires fundamental_hz.")
    ##endof:  if

    if spec.partials is None:
      raise ValueError("harmonic source requires partials.")
    ##endof:  if

    return make_harmonic_source(
      duration_s=duration_s,
      sample_rate=sample_rate,
      fundamental_hz=spec.fundamental_hz,
      partials=spec.partials,
    )
  ##endof:  if

  if spec.kind == "snare_noise":
    if spec.center_hz is None:
      raise ValueError("snare_noise source requires center_hz.")
    ##endof:  if

    return make_snare_hit_source(
      duration_s=duration_s,
      sample_rate=sample_rate,
      hit_duration_s=spec.hit_duration_s,
      center_hz=spec.center_hz,
      seed=spec.seed,
    )
  ##endof:  if

  raise ValueError(f"Unknown instrument kind: {spec.kind}")
##endof:  function make_source_from_spec


def harmonic_source(
      spec: InstrumentSpec,
      duration_s: float,
      sample_rate: int,
      envelope: np.ndarray | None = None,
    ) -> np.ndarray:
  '''
  Synthesize a harmonic source from sine partials.
  '''
  
  num_samples = int(round(duration_s * sample_rate))
  t = np.arange(num_samples) / sample_rate
  signal = np.zeros(num_samples, dtype=float)

  for harmonic_idx, coeff in enumerate(spec.partials, start=1):
    signal += coeff * np.sin(
      2.0 * np.pi * harmonic_idx * spec.fundamental_hz * t
    )
  ##endof: for

  if envelope is not None:
    if len(envelope) != num_samples:
      raise ValueError("envelope length must match source length")
    ##endof: if
    signal = signal * envelope
  ##endof: if

  max_abs = np.max(np.abs(signal))
  if max_abs > 0:
    signal = signal / max_abs
  ##endof: if

  return signal
##endof:  harmonic_source

def make_snare_source(
      t: np.ndarray,
      center_hz: float=261.63,
      noise_weight: float=0.90,
      tone_weight: float=0.10,
      decay_rate: float=35.0,
      seed: int=0,
    ) -> np.ndarray:
  '''
  Create a simple snare-like source.

  The snare is modeled as a broadband noise burst with a short decay,
  plus a weak C4-centered resonant tone.
  
  Building a harmonic instrument is pretty straightforward, but here
  is the math of the snare. (The math for each is gone over elsewhere,
  in the README.
  
  So the synthetic model should be:

  $$
  s_{\mathrm{snare}}(t)
  =
  e(t)\left[
  \alpha n(t)
  +
  \beta \sin\left(2\pi f_c t\right)
  \right].
  $$

  where:

  $n(t)$ is random noise,  
  $e(t)$ is a fast decay envelope,  
  $f_c \approx 261.63\,\mathrm{Hz}$ for C4,  
  $\alpha$ is large,  
  $\beta$ is small.

  In words:

  The snare is a short noisy burst, lightly colored by a C4-centered
  resonance.
  '''

  rng = np.random.default_rng(seed)

  noise = rng.normal(loc=0.0, scale=1.0, size=t.shape)
  tone = np.sin(2.0 * np.pi * center_hz * t)

  envelope = np.exp(-decay_rate * t)

  snare = envelope * (
    noise_weight * noise
    + tone_weight * tone
  )

  peak = np.max(np.abs(snare))
  if peak > 0:
    snare = snare / peak
  ##endof:  if

  return snare
##endof:  make_snare_source


def make_snare_hit_source(
      duration_s: float,
      sample_rate: int,
      hit_duration_s: float=0.20,
      center_hz: float=261.63,
      seed: int=0,
    ) -> np.ndarray:
  '''
  Create a full-length snare source with one short hit at the start.
  '''

  n_samples = int(duration_s * sample_rate)
  n_hit = int(hit_duration_s * sample_rate)

  source = np.zeros(n_samples, dtype=float)

  t_hit = np.arange(n_hit, dtype=float) / sample_rate
  hit = make_snare_source(
    t=t_hit,
    center_hz=center_hz,
    seed=seed,
  )

  source[:n_hit] = hit

  return source
##endof:  make_snare_hit_source




def default_instruments() -> list[InstrumentSpec]:
  '''
  Return the first C-add-9-ish synthetic ensemble.
  
  Note, matches the mix in run_synthetic_0p0.py
  '''
  
  return [
    InstrumentSpecOld("piano_bass", 65.41, (1.00, 0.35, 0.18, 0.10, 0.05)),
    InstrumentSpecOld("guitar", 196.00, (1.00, 0.50, 0.30, 0.18, 0.08)),
    InstrumentSpecOld("voice", 329.63, (1.00, 0.55, 0.25, 0.10, 0.05)),
    InstrumentSpecOld("violin", 587.33, (1.00, 0.75, 0.55, 0.35, 0.20)),
    InstrumentSpecOld("snare_tone", 261.63, (1.00, 0.15, 0.08, 0.03, 0.02)),
  ]
##endof:  default_instruments


DEFAULT_INSTRUMENTS = [
  InstrumentSpec(
    name="piano_bass",
    kind="harmonic",
    fundamental_hz=65.41,
    partials=[1.00, 0.35, 0.18, 0.10, 0.05],
  ),
  InstrumentSpec(
    name="guitar",
    kind="harmonic",
    fundamental_hz=196.00,
    partials=[1.00, 0.50, 0.30, 0.18, 0.08],
  ),
  InstrumentSpec(
    name="voice",
    kind="harmonic",
    fundamental_hz=329.63,
    partials=[1.00, 0.55, 0.25, 0.10, 0.05],
  ),
  InstrumentSpec(
    name="violin",
    kind="harmonic",
    fundamental_hz=587.33,
    partials=[1.00, 0.75, 0.55, 0.35, 0.20],
  ),
  InstrumentSpec(
    name="snare",
    kind="snare_noise",
    center_hz=261.63,
    noise_weight=0.90,
    tone_weight=0.10,
    decay_rate=35.0,
    hit_duration_s=0.20,
    seed=123,
  ),
]
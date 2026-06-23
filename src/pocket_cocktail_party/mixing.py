'''
This is a module specifically for downmixing/rendering observations,
including investigations of things like information loss.

It can own functions like:

mix_sources()
mix_to_stereo()
build_pentagon_mixing_matrix()
build_center_mic_row()
build_overhead_mic_row()
normalize_audio()

Then later, if it grows, I reserve the right to split it:

src/pocket_cocktail_party/
  geometry.py       # pentagon positions, distances
  sources.py        # synthetic instruments
  mixing.py         # A^m_i construction and stereo downmixes
  ica.py            # FastICA wrappers
  audio_io.py       # wav read/write
  plotting.py       # waveform/spectrogram plots

'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np


@dataclass
class StereoPan:
  '''
  Left/right weights for a mono source sent to stereo.
  '''

  left: float
  right: float
##endof:  class StereoPan


DEFAULT_PAN_RULES: Mapping[str, StereoPan] = {
  "bass": StereoPan(0.5, 0.5),
  "piano": StereoPan(0.5, 0.5),
  "piano_bass": StereoPan(0.5, 0.5),
  "bass_drum": StereoPan(0.5, 0.5),
  "kick": StereoPan(0.5, 0.5),
  "guitar": StereoPan(1.0, 0.0),
  "lead_guitar": StereoPan(1.0, 0.0),
  "rhythm_guitar": StereoPan(0.0, 1.0),
  "voice": StereoPan(0.0, 1.0),
  "vocal": StereoPan(0.0, 1.0),
  "violin": StereoPan(0.5, 0.5),
  "snare": StereoPan(2.0 / 3.0, 1.0 / 3.0),
}


def mix_to_stereo(
      sources: np.ndarray,
      source_names: list[str],
      pan_rules: Mapping[str, StereoPan]=DEFAULT_PAN_RULES,
    ) -> np.ndarray:
  '''
  Mix mono source rows down to a two-channel stereo signal.
  
  Lossy observation-generation step.

  Parameters
  ----------
  sources:
    Array with shape `(n_sources, n_samples)`.

  source_names:
    Names matching the rows of `sources`.

  Returns
  -------
  np.ndarray
    Stereo array with shape `(2, n_samples)`, where row 0 is left
    and row 1 is right.
  '''

  if sources.ndim != 2:
    raise ValueError("sources must have shape (n_sources, n_samples).")
  ##endof:  if

  if len(source_names) != sources.shape[0]:
    raise ValueError("source_names length must match source rows.")
  ##endof:  if

  stereo = np.zeros((2, sources.shape[1]), dtype=float)

  for source, name in zip(sources, source_names):
    key = name.lower().strip()
    pan = pan_rules.get(key, StereoPan(0.5, 0.5))

    stereo[0] += pan.left * source
    stereo[1] += pan.right * source
  ##endof:  for

  peak = np.max(np.abs(stereo))
  if peak > 0:
    stereo = stereo / peak
  ##endof:  if

  return stereo
##endof:  function mix_to_stereo


def mix_to_mono(
      sources: np.ndarray,
      weights: np.ndarray | None=None,
      do_normalize: bool=True,
    ) -> np.ndarray:
  '''
  Mix source rows down to a single mono observation.

  Parameters
  ----------
  sources:
    Array with shape `(n_sources, n_samples)`.

  weights:
    Optional source weights with shape `(n_sources,)`.

  do_normalize:
    If True, scale the result so its peak absolute value is 1.
  '''

  if sources.ndim != 2:
    raise ValueError("sources must have shape (n_sources, n_samples).")
  ##endof:  if

  if weights is None:
    weights = np.ones(sources.shape[0], dtype=float)
  ##endof:  if

  weights = np.asarray(weights, dtype=float)

  if weights.shape != (sources.shape[0],):
    raise ValueError("weights must have shape (n_sources,).")
  ##endof:  if

  mono = weights @ sources

  if do_normalize:
    peak = np.max(np.abs(mono))
    if peak > 0:
      mono = mono / peak
    ##endof:  if
  ##endof:  if

  return mono
##endof:  function mix_to_mono

#!/usr/bin/env python3

'''
Run the first synthetic FastICA smoke test.
'''

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.optimize import linear_sum_assignment

from pocket_cocktail_party.geometry import pentagon_bleed_matrix
from pocket_cocktail_party.ica import run_fastica
from pocket_cocktail_party.metrics import absolute_correlation_matrix
from pocket_cocktail_party.sources import (
  InstrumentSpecOld,
  harmonic_source,
  one_second_on_off_envelope,
)


def main() -> None:
  sample_rate = 16_000
  duration_s = 6.0
  envelope = one_second_on_off_envelope(duration_s, sample_rate)

  # Keep the Experiment 0.0 configuration local and reproducible.
  specs = [
    InstrumentSpecOld("piano_bass", 65.41, (1.00, 0.35, 0.18, 0.10, 0.05)),
    InstrumentSpecOld("guitar", 196.00, (1.00, 0.50, 0.30, 0.18, 0.08)),
    InstrumentSpecOld("voice", 329.63, (1.00, 0.55, 0.25, 0.10, 0.05)),
    InstrumentSpecOld("violin", 587.33, (1.00, 0.75, 0.55, 0.35, 0.20)),
    InstrumentSpecOld("snare_tone", 261.63, (1.00, 0.15, 0.08, 0.03, 0.02)),
  ]

  sources = np.vstack(
    [
      harmonic_source(spec, duration_s, sample_rate, envelope)
      for spec in specs
    ]
  )

  if sources.shape != (5, int(duration_s * sample_rate)):
    raise RuntimeError(f"Unexpected source shape: {sources.shape}")

  output_root = Path("data/processed/synthetic_0p0")

  sources_dir = output_root / "sources_1s"
  sources_dir.mkdir(parents=True, exist_ok=True)

  for source_index, spec in enumerate(specs, start=1):
    sample = sources[source_index - 1, :sample_rate].copy()

    # Fade out the cropped excerpt to prevent an ending click.
    fade_len = max(1, int(0.01 * sample_rate))
    sample[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)

    source_peak = float(np.max(np.abs(sample)))
    if source_peak > 0.0:
      sample *= 0.95 / source_peak

    output_path = sources_dir / f"{source_index:02d}_{spec.name}.wav"
    wavfile.write(output_path, sample_rate, sample.astype(np.float32))
    print(f"Wrote {output_path}")

  mixing = pentagon_bleed_matrix()
  mixtures = mixing @ sources

  if mixtures.shape != sources.shape:
    raise RuntimeError(
      f"Expected mixture shape {sources.shape}; got {mixtures.shape}."
    )

  mixtures_dir = output_root / "mixtures"
  mixtures_dir.mkdir(parents=True, exist_ok=True)

  # One scale factor prevents clipping while preserving relative microphone
  # levels across the complete five-channel group.
  mixtures_peak = float(np.max(np.abs(mixtures)))
  playable_mixtures = mixtures.copy()

  if mixtures_peak > 0.0:
    playable_mixtures *= 0.95 / mixtures_peak

  for mic_index, spec in enumerate(specs, start=1):
    output_path = (
      mixtures_dir
      / f"{mic_index:02d}_mic_near_{spec.name}.wav"
    )
    wavfile.write(
      output_path,
      sample_rate,
      playable_mixtures[mic_index - 1].astype(np.float32),
    )
    print(f"Wrote {output_path}")

  recovered = run_fastica(mixtures, n_components=5)

  if recovered.shape != sources.shape:
    raise RuntimeError(
      f"Expected recovered shape {sources.shape}; got {recovered.shape}."
    )

  separated_dir = output_root / "separated"
  separated_dir.mkdir(parents=True, exist_ok=True)

  # ICA component order, sign, and scale are indeterminate. Normalize each
  # component independently for listening. Correlations use the raw arrays.
  for component_index, component in enumerate(recovered, start=1):
    playable_component = component.copy()
    component_peak = float(np.max(np.abs(playable_component)))

    if component_peak > 0.0:
      playable_component *= 0.95 / component_peak

    output_path = (
      separated_dir
      / f"{component_index:02d}_ica_component.wav"
    )
    wavfile.write(
      output_path,
      sample_rate,
      playable_component.astype(np.float32),
    )
    print(f"Wrote {output_path}")

  corr = absolute_correlation_matrix(sources, recovered)

  print("Mixing matrix:")
  print(np.round(mixing, 3))

  print("Absolute correlation matrix:")
  print(np.round(corr, 3))

  source_rows, component_columns = linear_sum_assignment(-corr)

  print("Optimal one-to-one source/component assignment:")
  for source_index, component_index in zip(
      source_rows,
      component_columns,
      strict=True,
  ):
    print(
      f"  {specs[source_index].name}"
      f" -> component {component_index + 1:02d}"
      f"  |corr|={corr[source_index, component_index]:.6f}"
    )

  print(f"Wrote Experiment 0.0 outputs beneath {output_root}")
##endof:  main()


if __name__ == "__main__":
  main()
##endof:  if __name__ == "__main__"

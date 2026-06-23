'''Run the first synthetic FastICA smoke test.'''

from __future__ import annotations

import numpy as np

from pocket_cocktail_party.geometry import pentagon_bleed_matrix
from pocket_cocktail_party.ica import run_fastica
from pocket_cocktail_party.metrics import absolute_correlation_matrix
from pocket_cocktail_party.synthesis import (
  InstrumentSpecOld,
  harmonic_source,
  one_second_on_off_envelope,
)


def main() -> None:
  sample_rate = 16_000
  duration_s = 6.0
  envelope = one_second_on_off_envelope(duration_s, sample_rate)

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

  mixing = pentagon_bleed_matrix()
  mixtures = mixing @ sources
  recovered = run_fastica(mixtures, n_components=5)
  corr = absolute_correlation_matrix(sources, recovered)

  print("Absolute correlation matrix:")
  print(np.round(corr, 3))
##endof:  main()


if __name__ == "__main__":
  main()
##endof:  if __name__ == "__main__"

"""Pocket Cocktail Party.

Blind source separation experiments through geometry, harmonics, and signal
mixing.
"""

from .geometry import pentagon_bleed_matrix
from .synthesis import (
  InstrumentSpec,
  InstrumentSpecOld,
  make_source_from_spec,
  one_second_on_off_envelope,
  harmonic_source,
  make_snare_source,
  make_snare_hit_source,
  
)
from .mixing import (
  StereoPan,
  mix_to_stereo,
  mix_to_mono,
)

__all__ = [
  "InstrumentSpec",
  "InstrumentSpecOld",
  "StereoPan",
  "harmonic_source",
  "make_snare_source",
  "make_snare_hit_source",
  "make_source_from_spec",
  "one_second_on_off_envelope",
  "pentagon_bleed_matrix",
  "mix_to_stereo",
  "mix_to_mono",
]

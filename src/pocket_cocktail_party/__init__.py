"""Pocket Cocktail Party.

Blind source separation experiments through geometry, harmonics, and signal
mixing.
"""

from importlib.metadata import PackageNotFoundError, version

from .geometry import pentagon_bleed_matrix
from .sources import (
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


try:
  __version__ = version("pocket-cocktail-party")
except PackageNotFoundError:
  __version__ = "0.0.0+not-installed"
##endof: try/except

__all__ = [
  "__version__",
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

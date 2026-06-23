'''
Audio alignment helpers for real microphone recordings.
'''

from __future__ import annotations

import numpy as np


def find_loudest_peak(signal: np.ndarray) -> int:
  '''
  Return the index of the largest absolute-amplitude sample.
  '''

  if signal.ndim != 1:
    raise ValueError("signal must be one-dimensional")
  ##endof: if

  return int(np.argmax(np.abs(signal)))


def trim_to_common_length(signals: list[np.ndarray]) -> np.ndarray:
  '''
  Stack one-dimensional signals after trimming to the shortest length.
  '''

  if not signals:
    raise ValueError("signals must not be empty")
  ##endof: if

  min_len = min(len(signal) for signal in signals)
  return np.vstack([signal[:min_len] for signal in signals])

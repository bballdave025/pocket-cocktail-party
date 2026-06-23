'''
Geometry-derived mixing matrices.
'''

from __future__ import annotations

import numpy as np


def pentagon_bleed_matrix(
  self_gain: float = 1.0,
  adjacent_gain: float = 0.2,
) -> np.ndarray:
  '''
  Return a symmetric five-source/five-mic pentagon bleed matrix.

  The diagonal is the own-microphone gain. Adjacent vertices get
  ``adjacent_gain``. Next-nearest vertices get ``adjacent_gain / phi``,
  where ``phi`` is the golden ratio.

  Returns:
    A matrix ``A`` with shape ``(5, 5)`` where ``X = A @ S``.
  '''
  
  phi = (1.0 + np.sqrt(5.0)) / 2.0
  next_nearest_gain = adjacent_gain / phi

  matrix = np.full((5, 5), next_nearest_gain, dtype=float)

  for idx in range(5):
    matrix[idx, idx] = self_gain
    matrix[idx, (idx - 1) % 5] = adjacent_gain
    matrix[idx, (idx + 1) % 5] = adjacent_gain
  ##endof: for

  return matrix
##endof:  pentagon_bleed_matrix


def add_equal_room_mic(
  matrix: np.ndarray,
  room_gain: float = 0.3,
) -> np.ndarray:
  """Append an equal-gain center/overhead microphone row."""
  if matrix.ndim != 2:
    raise ValueError("matrix must be two-dimensional")
  ##endof: if

  num_sources = matrix.shape[1]
  room_row = np.full((1, num_sources), room_gain, dtype=float)

  return np.vstack([matrix, room_row])
##endof:  add_equal_room_mic

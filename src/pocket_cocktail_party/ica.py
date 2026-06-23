'''
Thin wrappers around FastICA for project experiments.
'''

from __future__ import annotations

import numpy as np
from sklearn.decomposition import FastICA


def run_fastica(
  mixtures: np.ndarray,
  n_components: int | None = None,
  random_state: int = 42,
) -> np.ndarray:
  '''
  Run FastICA on channel-by-time mixtures.

  Args:
    mixtures: Array with shape ``(channels, samples)``.
    n_components: Number of independent components to estimate.
    random_state: Reproducibility seed.

  Returns:
    Estimated source array with shape ``(components, samples)``.
  '''
  
  if mixtures.ndim != 2:
    raise ValueError("mixtures must have shape (channels, samples)")
  ##endof: if

  model = FastICA(
    n_components=n_components,
    whiten="unit-variance",
    random_state=random_state,
    max_iter=1000,
    tol=1e-4,
  )
  recovered = model.fit_transform(mixtures.T).T

  return recovered

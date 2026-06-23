'''
Evaluation helpers for synthetic source recovery.
'''

from __future__ import annotations

import numpy as np


def absolute_correlation_matrix(
      true_sources: np.ndarray,
      recovered_sources: np.ndarray,
    ) -> np.ndarray:
  '''
  Compare true and recovered sources by absolute correlation.
  '''
  
  true_centered = true_sources - true_sources.mean(
        axis=1, 
        keepdims=True
  )
  rec_centered = recovered_sources - recovered_sources.mean(
        axis=1,
        keepdims=True,
  )

  true_norm = np.linalg.norm(true_centered, axis=1, keepdims=True)
  rec_norm = np.linalg.norm(rec_centered, axis=1, keepdims=True)

  corr = (rec_centered @ true_centered.T) / (rec_norm @ true_norm.T)
  return np.abs(corr)
##endof:  absolute_correlation_matrix
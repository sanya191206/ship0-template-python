from __future__ import annotations
from typing import Iterable
import numpy as np

def mean_length(items: Iterable[str]) -> float:
    lengths = np.array([len(s) for s in items], dtype=float)
    return float(lengths.mean()) if lengths.size else 0.0

"""Stats helpers (TO IMPLEMENT)."""
from __future__ import annotations
from typing import Iterable
import numpy as np

def mean_length(items: Iterable[str]) -> float:
    """Return the mean character length of strings in `items`.
    Use NumPy arrays; return 0.0 for empty iterables.
    """
    # TODO: implement with numpy
    # raise NotImplementedError
    arr = np.array([len(s) for s in items], dtype=float)
    return float(arr.mean()) if arr.size else 0.0

"""Storage helpers (TO IMPLEMENT).
Functions here should read/write JSON entries at data/log.json.
Each entry is a dict: { "t": ISO_TIMESTAMP, "v": TEXT }.
Newest entries should come first in the list.

Tips:
- Create the parent folder if it doesn't exist.
- Keep writes idempotent: always write the full array to disk.
- Use environment variable SHIP0_DATA_PATH to override the default path.
"""
from __future__ import annotations
import json, os, time
from pathlib import Path
from typing import List, Dict

REPO_ROOT = Path(__file__).resolve().parents[2]

def _default_data_path() -> Path:
    env = os.environ.get("SHIP0_DATA_PATH")
    if env:
        return Path(env)
    return REPO_ROOT / "data" / "log.json"

def data_path() -> Path:
    """Return the Path to the JSON log file, creating the folder/file if needed."""
    p = _default_data_path()
    # TODO: create parent folder, create file with [] if missing
    raise NotImplementedError

def load_entries() -> List[Dict]:
    """Return a list of entries (newest first)."""
    # TODO: read JSON safely and return []
    raise NotImplementedError

def save_entries(data: List[Dict]) -> None:
    """Write the full list back to disk (pretty-printed JSON)."""
    # TODO: write JSON with indent=2
    raise NotImplementedError

def add_entry(text: str) -> None:
    """Insert a new entry at the start of the list with current timestamp."""
    # TODO: implement
    raise NotImplementedError

def clear_entries() -> None:
    """Erase all entries (write an empty list)."""
    # TODO: implement
    raise NotImplementedError

from __future__ import annotations
import json, time, os
from pathlib import Path
from typing import List, Dict

REPO_ROOT = Path(__file__).resolve().parents[2]

def _default_data_path() -> Path:
    env = os.environ.get("SHIP0_DATA_PATH")
    if env:
        return Path(env)
    return REPO_ROOT / "data" / "log.json"

def data_path() -> Path:
    p = _default_data_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text("[]", encoding="utf-8")
    return p

def load_entries() -> List[Dict]:
    p = data_path()
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_entries(data: List[Dict]) -> None:
    p = data_path()
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def add_entry(text: str) -> None:
    data = load_entries()
    data.insert(0, {"t": time.strftime("%Y-%m-%d %H:%M:%S"), "v": text})
    save_entries(data)

def clear_entries() -> None:
    save_entries([])

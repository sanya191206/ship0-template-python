from pathlib import Path
from ship0.storage import add_entry, load_entries, clear_entries, data_path
import os, json

def test_add_and_list(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("SHIP0_DATA_PATH", str(tmp_path / "log.json"))
    clear_entries()
    add_entry("alpha")
    add_entry("beta")
    entries = load_entries()
    assert len(entries) == 2
    assert entries[0]["v"] == "beta"  # newest first
    assert entries[1]["v"] == "alpha"

def test_clear(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("SHIP0_DATA_PATH", str(tmp_path / "log.json"))
    add_entry("x")
    assert load_entries()
    clear_entries()
    assert load_entries() == []

"""Baseline environment check.
This script prints your name, Python version, NumPy version,
and the first line of goals.txt.
"""
import sys, pathlib
import numpy as np

# TODO: set your actual name here
NAME = "REPLACE_ME"

def first_line_of_goals() -> str:
    p = pathlib.Path("goals.txt")
    if not p.exists():
        return "(goals.txt not found)"
    lines = [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]
    return lines[0] if lines else "(goals.txt is empty)"

def main() -> None:
    print(f"Name: {NAME}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"NumPy: {np.__version__}")
    print(f"Goal: {first_line_of_goals()}")

if __name__ == "__main__":
    main()

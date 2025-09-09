import sys, pathlib
import numpy as np

# TODO: replace with your actual name
NAME = "REPLACE_ME"

goals_path = pathlib.Path("goals.txt")
if goals_path.exists():
    first_line = goals_path.read_text(encoding="utf-8").splitlines()[0] if goals_path.read_text(encoding="utf-8").splitlines() else ""
else:
    first_line = "(goals.txt not found)"

print(f"Name: {NAME}")
print(f"Python: {sys.version.split()[0]}")
print(f"numpy: {np.__version__}")
print(f"Goal: {first_line}")

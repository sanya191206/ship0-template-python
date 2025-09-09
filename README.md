# Ship 0 — Python (CLI + Persistence + Tests)

**Purpose:** Go beyond “env check.” You’ll ship a tiny CLI that persists entries to disk and comes with a couple of tests.

## What you’ll build
A command-line “Ship Log”:
- `python -m ship0 add "Wrote my first script"` → appends an entry
- `python -m ship0 list` → prints newest-first
- `python -m ship0 stats` → prints count + average entry length (uses `numpy`)
- `python -m ship0 clear -y` → clears the log

Data is stored in `data/log.json` (overridable via the env var `SHIP0_DATA_PATH`).

## Prereqs
- Python **3.11** (and `venv`)
- `pip`

## Quick start
```bash
# macOS/Linux
python3 -V
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Try it
python -m ship0 add "hello world"
python -m ship0 list
python -m ship0 stats
```

```powershell
# Windows (PowerShell)
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

python -m ship0 add "hello world"
python -m ship0 list
python -m ship0 stats
```

## What to edit
- Open `src/ship0/cli.py` and set `DEFAULT_NAME = "Your Name"` (optional, used in greeting).
- Edit the first line of `goals.txt` with a **one‑sentence** semester goal.
- Add a terminal screenshot at `screenshots/run.png`.
- Add your run commands + output under **Run Output** below.

## Pass criteria
- CLI commands **work** and persist to `data/log.json` (or `SHIP0_DATA_PATH`).
- `pytest` runs **and passes**.
- `stats` prints both **count** and **mean length** (as a number) using `numpy`.
- Screenshot present at `screenshots/run.png` (or embedded).
- **≥2 commits**.
- Repo name exactly: `edge-f25-ship0-<onyen-or-last-first>`.

## Run tests
```bash
# Env must be active; then:
pytest -q
```

## Run Output (paste here)
```
<paste your terminal output here>
```

---

### Why this is “a little harder”
- You touch **argparse**, **file I/O**, **JSON**, **numpy**, and **pytest**.
- You learn to run a module via `python -m ship0`.

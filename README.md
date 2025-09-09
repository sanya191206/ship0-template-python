# Ship 0 — Python (Env Check + Mini Task)

**Purpose:** Confirm Python 3.11 + venv work, `numpy` installs, and you can run a simple script.

## Quick start
```bash
# macOS/Linux
python3 -V
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python env_check.py
```

```powershell
# Windows (PowerShell)
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python env_check.py
```

## What to edit
- Open `env_check.py` and set `NAME = "Your Name"`
- Edit the first line of `goals.txt` with a 1‑sentence semester goal
- Add a terminal screenshot at `screenshots/run.png`
- Add your run commands + pasted output to this `README.md` under **Run Output**

## Pass criteria
- `env_check.py` prints your **name**, Python version, `numpy` version, and the first line of `goals.txt`
- Screenshot present at `screenshots/run.png` (or embedded in README)
- **≥2 commits**
- Repo name is exactly: `edge-f25-ship0-<onyen-or-last-first>`

## Run Output (paste here)
```
<paste your terminal output here>
```

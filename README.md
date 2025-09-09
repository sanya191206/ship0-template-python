# Ship 0 — Python

**Two tracks in one repo:** a gentle **Baseline** to verify your setup, and an optional **Hard Mode** that asks you to build a tiny CLI with persistence and tests.

## Why you’re doing this
- To prove your computer can run modern Python (3.11) and packages.
- To learn **what** each command does — not just copy-paste incantations.
- To get comfortable with **virtual environments**, **pip**, **modules**, **JSON**, **tests**, and **Git**.

---

## Get the code (fork or template)

**Pick one (don’t do both). Your repo must be named exactly:**  
`edge-f25-ship0-<onyen-or-last-first>`

### A) Use this template (preferred)
1. Open the Ship 0 Python template in the Edge Carolina org.
2. Click **Use this template** → **Create a new repository**.
3. **Owner:** your personal GitHub account  
   **Name:** `edge-f25-ship0-<onyen-or-last-first>`  
   **Visibility:** Public (or grant org read access).
4. Click **Create repository**.
5. Clone it locally:

   ```bash
   # HTTPS
   git clone https://github.com/<you>/edge-f25-ship0-<onyen-or-last-first>.git
   cd edge-f25-ship0-<onyen-or-last-first>

   # Or SSH (if you use SSH keys)
   git clone git@github.com:<you>/edge-f25-ship0-<onyen-or-last-first>.git
   ```

### B) Fork (also fine)
1. Open the Ship 0 Python template in the Edge Carolina org.
2. Click **Fork**.
3. **Owner:** your personal GitHub account.
4. **Repository name:** change to `edge-f25-ship0-<onyen-or-last-first>`.
5. Click **Create fork**.
6. Clone it locally (same commands as above).

### After cloning
- **Baseline:** create and activate a virtual environment, then install requirements (see steps below).
- **Hard Mode:** create a file named `HARDMODE` at repo root (enables tests/CI). Run inside your venv:
  ```bash
  pip install -r requirements.txt
  pytest -q
  ```
- **Commit & push (both paths):**
  ```bash
  git add -A
  git commit -m "Ship 0: baseline work"
  git push -u origin main
  ```

---

## What is a virtual environment (venv), really?
A **virtual environment** is a self-contained folder that holds its own Python interpreter and installed packages. It keeps your project’s dependencies isolated from the rest of your machine so one project’s install doesn’t break another’s.

- Creating a venv: `python3 -m venv .venv` creates a `.venv/` folder in your repo.
- Activating it: `source .venv/bin/activate` (macOS/Linux) or `\.venv\Scripts\activate` (Windows).
- Why activate? So `python` and `pip` point **inside** the venv. You can confirm with `which python` (macOS/Linux) or `where python` (Windows).

When you’re done, deactivate with `deactivate` or just close the terminal. You can delete a venv by removing the `.venv/` folder and recreating it later.

---

## What is `pip`?
`pip` is Python’s package installer. It grabs packages from the Python Package Index (PyPI).
- Upgrade it inside your venv: `python -m pip install --upgrade pip`
- Install from a list: `pip install -r requirements.txt`

We use **NumPy** for a tiny stat calculation and **pytest** for tests.

---

## What does `python -m` do?
The `-m` flag runs a **module** by name (like `ship0`) instead of a file path. It tells Python to treat the current directory as a package, look up `ship0/__main__.py`, and execute it. This is how you’ll run your CLI in Hard Mode: `python -m ship0`.

---

## Baseline (Required) — Environment Check
You’ll run a small script that prints:
- your name,
- Python version,
- NumPy version,
- your 1-sentence semester goal read from `goals.txt`.

**Files you’ll touch**
- `env_check.py` — the script (already written)
- `goals.txt` — put your one-sentence goal on the **first line**
- `README.md` — paste your run output under **Run Output**

**Run it (read the comments in each step)**
```bash
# 1) Create a fresh virtual environment in this repo
python3 -m venv .venv                     # Windows: py -3.11 -m venv .venv

# 2) Activate it (this changes your PATH so 'python' points inside .venv)
source .venv/bin/activate                 # Windows: .\.venv\Scripts\activate

# 3) Upgrade pip and install the project requirements into THIS venv
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4) Edit the first line of goals.txt with your one-sentence goal
#    Then run the script:
python env_check.py
```

**Pass (Baseline) if all true**
- Script prints your **name**, **Python version**, **NumPy version**, and **goal**.
- Screenshot saved at `screenshots/run.png` **or** embedded in this README.
- **≥2 commits** with meaningful messages.
- Repo name: `edge-f25-ship0-<onyen-or-last-first>`.

Paste your terminal output here:
```
<Run Output: paste the lines printed by env_check.py>
```

---

## Hard Mode (Optional, Scored) — CLI + Persistence + Tests
Build a tiny **Ship Log** command-line app. You’ll implement a few functions and wire them into a CLI.

**Commands (after implementation)**
- `python -m ship0 add "text"` — append a timestamped entry
- `python -m ship0 list` — print newest-first
- `python -m ship0 stats` — print **count** and **mean entry length** (uses NumPy)
- `python -m ship0 clear -y` — clear the log without a confirmation prompt

**Data**
- Stored at `data/log.json` (auto-created). Override with env var `SHIP0_DATA_PATH=/tmp/mylog.json`.

**Where to write code**
- `src/ship0/storage.py` — implement `load_entries`, `save_entries`, `add_entry`, `clear_entries`
- `src/ship0/stats.py` — implement `mean_length`
- `src/ship0/cli.py` — the `argparse` CLI is scaffolded for you; minimal edits may be needed

**Tests**
- Run: `pytest -q` (inside your venv). Two tests are provided.
- You pass if both tests are **green** and the CLI behaves as specified.

**Opt-in CI for Hard Mode**
- Create an empty file named `HARDMODE` (no extension) in the repo root **when you’re ready**. Our GitHub Action will detect it and run `pytest`. No `HARDMODE` file = light checks only (baseline students won’t see a scary red X).

---

## Conceptual checkpoints (answer to yourself)
- Can you explain what **activating a venv** changes on your system?
- Can you show that `pip list` inside the venv differs from global `pip list`?
- Why does `python -m ship0` work without a file path?
- What are **idempotent** file writes, and why do we create the `data/` folder if missing?
- What makes a good test small and reliable?

---

## Troubleshooting
- **Windows execution policy**: if activation fails, run PowerShell as Admin once:
  ```powershell
  Set-ExecutionPolicy RemoteSigned
  ```
  Then reactivate: `\.venv\Scripts\activate`
- **“pip not found”** inside venv: use `python -m pip ...`
- **NumPy build errors on Linux**: `pip install --upgrade pip setuptools wheel`
- **pytest can’t import ship0**: ensure you’re running tests from the repo root and your venv is active.

---

## What to submit
- Repo URL
- Screenshot
- Track (Baseline only **or** Hard Mode)
- Minutes spent + biggest blocker

Submit [here](https://forms.gle/uoAQkv48QDkEM81m9)

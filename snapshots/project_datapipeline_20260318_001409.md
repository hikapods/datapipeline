---
name: DataPipeline project overview
description: Key facts about the DataPipeline ETL project in this repo
type: project
---

A lightweight Python ETL pipeline that reads a CSV, filters out rows where the `value` column is empty, and writes the cleaned data to an output CSV.

**Entry point:** `src/main.py` — CLI via argparse (`--input`, `--output`)
**Defaults:** `data/input.csv` → `data/output.csv` (set in `src/config.py`)
**CSV I/O:** `src/utils.py` (`load_csv`, `save_csv` using stdlib `csv`)

**Known weaknesses identified (2026-03-18):**
- No error handling in `load_csv`/`save_csv` (FileNotFoundError, malformed CSV, missing output dir)
- Both test files (`tests/test_main.py`, `tests/test_utils.py`) are empty stubs (`pass`)
- `LOG_LEVEL` defined in config but logging is never used
- Filter column (`value`) is hardcoded in `main.py:7`
- `save_csv` silently no-ops if data is empty — no file written, no warning
- Output directory not created automatically before writing
- README references a `requirements.txt` that doesn't exist (only stdlib is used)

**Why:** Project appears to be a thesis experiment test repo (`git log` message: "Add realistic project code for thesis experiments").
**How to apply:** Treat this as a work-in-progress / experimental codebase; suggest fixes incrementally rather than full rewrites.

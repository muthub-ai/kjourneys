# Site builds

One folder per MI report, written as the last step of `scripts/refresh.sh` (`tools/store_site.py`). Rerunning for the same report replaces its folder; earlier reports' folders are kept as they were.

| MI report | Site | Also stored | Status |
|---|---|---|---|
| 2026-11-07-v2 | [index.html](2026-11-07-v2/index.html) | summary.md, coverage.json, kjourneys.json, facts.jsonl | current |

Open `index.html` in a browser: it is self-contained and works offline. `summary.md` is the data status; `kjourneys.json` is the full assembled dataset; `facts.jsonl` is the same as one fact per line; `coverage.json` is coverage by bank and rail.

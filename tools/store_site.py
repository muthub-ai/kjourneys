#!/usr/bin/env python3
"""Final step of scripts/refresh.sh: copy what the run built into docs/site/<MI report version>/.

  python3 tools/store_site.py

The version is the current MI report: the newest one that no other report's manifest supersedes. Running it again
for the same report replaces that folder; a new report gets a new folder and earlier folders are left as they were.
Copied from dist/: index.html (the site), summary.md, coverage.json, kjourneys.json, facts.jsonl. Not copied:
artifact.html (the same page without its outer document, only for publishing to claude.ai).
docs/site/README.md lists every stored version."""
import glob, json, os, shutil, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["index.html", "summary.md", "coverage.json", "kjourneys.json", "facts.jsonl"]
missing = [f for f in FILES if not os.path.exists(os.path.join(ROOT, "dist", f))]
if missing: sys.exit(f"store_site: dist/ is missing {', '.join(missing)}; run make check (or scripts/refresh.sh) first")
ms = [json.load(open(m)) for m in glob.glob(os.path.join(ROOT, "reports/*/manifest.json"))]
gone = {m.get("supersedes") for m in ms}
current = max(m["report_version"] for m in ms if m["report_version"] not in gone)
dest = os.path.join(ROOT, "docs/site", current)
if os.path.isdir(dest): shutil.rmtree(dest)
os.makedirs(dest)
for f in FILES: shutil.copy2(os.path.join(ROOT, "dist", f), os.path.join(dest, f))
vs = sorted((os.path.basename(d) for d in glob.glob(os.path.join(ROOT, "docs/site/*")) if os.path.isdir(d)), reverse=True)
open(os.path.join(ROOT, "docs/site/README.md"), "w").write(
    "# Site builds\n\nOne folder per MI report, written as the last step of `scripts/refresh.sh` (`tools/store_site.py`). "
    "Rerunning for the same report replaces its folder; earlier reports' folders are kept as they were.\n\n"
    "| MI report | Site | Also stored | Status |\n|---|---|---|---|\n" +
    "".join(f"| {v} | [index.html]({v}/index.html) | summary.md, coverage.json, kjourneys.json, facts.jsonl | "
            f"{'current' if v == current else 'superseded'} |\n" for v in vs) +
    "\nOpen `index.html` in a browser: it is self-contained and works offline. `summary.md` is the data status; "
    "`kjourneys.json` is the full assembled dataset; `facts.jsonl` is the same as one fact per line; `coverage.json` is coverage by bank and rail.\n")
size = sum(os.path.getsize(os.path.join(dest, f)) for f in FILES) // (1024 * 1024)
print(f"stored the site and outputs in docs/site/{current}/ ({size} MB)")

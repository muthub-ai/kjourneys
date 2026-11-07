# reports/

Market-intelligence (MI) reports, kept exactly as received, one folder per version. They are the evidence behind every competitor fact in `data/comparisons/`.

```
reports/
  ingest-log.json             every version ingested: when, how many runs, facts applied, banks touched
  2026-11-20-v1/              <delivery date>-v<n>
    manifest.json             version, product, producer, received_at, files + sha256
    report.pdf                the deliverable as received (any format)
    report.html  report.docx  data.xlsx    the deliverables as received, any formats
    extract/
      zelle/citi.json         structured facts for one product and bank (docs/mi-extraction.md)
      ach/citi.json
  2026-12-05-v1/              a later delivery; changed facts supersede earlier ones
```

## Rules

- **Immutable.** Once a version is ingested, its files never change. The validator re-checks every report's sha256 on every build. Corrections arrive as a new version.
- **One version, one commit.** Commit the report folder and the data it produces together (`scripts/refresh.sh <version> --commit`), so the evidence sits beside the change.
- **Rerun freely.** Ingesting a version again rolls back what it wrote and applies its extracts afresh, so you can fix an extract and rerun. Once a later version supersedes its facts, only the latest version can be rerun.
- **The report files themselves never change.** Only extracts can be fixed between runs.
- **Version names** are `YYYY-MM-DD-vN`: the delivery date, plus a counter for same-day deliveries.

## manifest.json

```json
{
  "report_version": "2026-11-20-v1",
  "products": ["zelle", "ach", "wire", "billpay", "instant"],
  "title": "Money-movement competitive scan — top 10 US banks",
  "produced_by": "process:mi-session",
  "received_at": "2026-11-20T17:30:00-06:00",
  "files": [
    { "path": "report.html", "sha256": "<sha256>", "kind": "report" },
    { "path": "report.docx", "sha256": "<sha256>", "kind": "report" },
    { "path": "data.xlsx",   "sha256": "<sha256>", "kind": "data" }
  ]
}
```

Get each hash with `shasum -a 256 <file>` (macOS) or `sha256sum <file>` (Linux). List the main report first; it becomes the source every ingested fact cites. Every listed file is checksum-pinned, so all three formats are preserved exactly. A report about one product may use `"product": "zelle"` instead of `products`, and may put extracts directly in `extract/<bank>.json`.

Each product needs its comparison questions before its first ingest: `python3 tools/new_comparison.py <product> <attributes.json>` creates them, with an awaiting slot for every bank.

## Ingest

```bash
scripts/refresh.sh reports/2026-11-20-v1            # rerun as often as needed
scripts/refresh.sh reports/2026-11-20-v1 --commit   # commit on the current branch when it passes
```

This applies the extracts, registers the report and every cited URL as sources, keeps history for changed facts, logs the version, validates, runs the tests, and rebuilds the site (`dist/index.html`) and exports.

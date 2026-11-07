# reports/

Market-intelligence (MI) reports, kept exactly as received, one folder per version. They are the evidence behind every competitor fact in `data/comparisons/`.

```
reports/
  ingest-log.json             every version ingested, when, and what it changed
  2026-11-20-v1/              <delivery date>-v<n>
    manifest.json             version, product, producer, received_at, files + sha256
    report.pdf                the deliverable as received (any format)
    extract/
      citi.json               structured facts for one bank (docs/mi-extraction.md)
      pnc.json
  2026-12-05-v1/              a later delivery; changed facts supersede earlier ones
```

## Rules

- **Immutable.** Once a version is ingested, its files never change. The validator re-checks every report's sha256 on every build. Corrections arrive as a new version.
- **One version, one pull request.** Commit the report folder and the data it produces together, so reviewers see the evidence beside the change.
- **No re-ingest.** `tools/ingest_mi.py` refuses a version already in `ingest-log.json`.
- **Version names** are `YYYY-MM-DD-vN`: the delivery date, plus a counter for same-day deliveries.

## manifest.json

```json
{
  "report_version": "2026-11-20-v1",
  "product": "zelle",
  "title": "Zelle competitive scan — top 10 US banks",
  "produced_by": "process:mi-session",
  "received_at": "2026-11-20T17:30:00-06:00",
  "files": [
    { "path": "report.pdf", "sha256": "<sha256 of the file>", "kind": "report" }
  ]
}
```

Get the hash with `shasum -a 256 report.pdf` (macOS) or `sha256sum report.pdf` (Linux). List the main report first; it becomes the source every ingested fact cites.

## Ingest

```bash
make ingest REPORT=reports/2026-11-20-v1
```

This applies the extracts, registers the report and every cited URL as sources, keeps history for changed facts, logs the version, and runs the full check.

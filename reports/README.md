# reports/

Market-intelligence (MI) reports, kept exactly as received, one folder per version. They are the evidence behind every MI journey, finding, score and comparison fact in `data/`.

```
reports/
  ingest-log.json             every version ingested: when, how many runs, facts applied, banks touched
  2026-11-06-v1/              <delivery date>-v<n>: the first money-movement delivery
    manifest.json             version, products, producer, received_at, workbook, files + sha256
    money-movement-intelligence.html             the report as read by people
    Money_Movement_CI_Dossier.docx               17 chapters
    Money_Movement_CI_Sources_and_Verification.docx
    Money_Movement_CI_Data.xlsx                  the workbook: the source the repo reads
    extract/
      zelle/citi.json         facts for one product and bank, generated from the workbook
      rtp/citi.json
  2026-12-05-v1/              a later delivery; changed facts supersede earlier ones
```

## Rules

- **Immutable.** Once a version is ingested, its files never change. The validator re-checks every report's sha256 on every build. Corrections arrive as a new version.
- **One version, one commit.** Commit the report folder and the data it produces together (`scripts/refresh.sh <version> --commit`), so the evidence sits beside the change.
- **Rerun freely.** Ingesting a version again rolls back what it wrote and applies its extracts afresh, so you can fix an extract and rerun. Once a later version supersedes its facts, only the latest version can be rerun.
- **The report files themselves never change.** Extracts generated from a workbook are rewritten on every run; hand-written extracts can be fixed between runs.
- **The workbook wins.** When a delivery has both a workbook and a report with embedded data, the workbook is canonical. In 2026-11-06-v1 it is newer than the HTML (Wells Fargo index 69.3 against 69.5; 8 more Wells Fargo findings).
- **Version names** are `YYYY-MM-DD-vN`: the delivery date, plus a counter for same-day deliveries.

## manifest.json

```json
{
  "report_version": "2026-11-20-v1",
  "products": ["zelle", "request-to-pay", "ach-external-transfer", "…"],
  "title": "Money-movement competitive scan — top 10 US banks",
  "produced_by": "process:mi-session",
  "received_at": "2026-11-20T17:30:00-06:00",
  "workbook": "data.xlsx",
  "files": [
    { "path": "report.html", "sha256": "<sha256>", "kind": "report" },
    { "path": "report.docx", "sha256": "<sha256>", "kind": "report" },
    { "path": "data.xlsx",   "sha256": "<sha256>", "kind": "data" }
  ]
}
```

Get each hash with `shasum -a 256 <file>` (macOS) or `sha256sum <file>` (Linux). List the canonical file first; it becomes the source every ingested fact cites. With a workbook, the importer lists the workbook first for you. Every listed file is checksum-pinned, so all three formats are preserved exactly. A report about one product may use `"product": "zelle"` instead of `products`, and may put extracts directly in `extract/<bank>.json`.

With a `workbook`, the importer writes each product's comparison questions (capability flags and stage scores) and every bank's slots. Without one, each product needs its questions before its first ingest: `python3 tools/new_comparison.py <product> <attributes.json>` creates them.

## Ingest

```bash
scripts/refresh.sh reports/2026-11-20-v1            # rerun as often as needed
scripts/refresh.sh reports/2026-11-20-v1 --commit   # commit on the current branch when it passes
```

This imports the workbook (journeys, findings, composites, scores, extracts), applies the extracts, registers the report and its sources, keeps history for changed facts, logs the version, validates, runs the tests, and rebuilds the site (`dist/index.html`) and exports.

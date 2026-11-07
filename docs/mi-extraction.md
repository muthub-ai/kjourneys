# From an MI report to facts: extraction

A market-intelligence report is prose. The comparison needs typed, sourced facts. Extraction turns one into the other, writing one `extract/<product>/<bank>.json` per bank beside the report. `tools/ingest_mi.py` then applies the extracts deterministically.

**When the delivery includes the MI workbook, you don't write extracts.** `tools/import_mi_workbook.py` generates them from the workbook (capability flags and stage scores), and `scripts/refresh.sh` runs it for you. This page is for reports that arrive without one, or for a hand correction between deliveries.

## Who extracts

1. **Preferred: the MI session itself.** Give it this document and [the data contract](market-intelligence-contract.md), and ask it to deliver the extract files with its report. It already holds the sources, so nothing is lost in translation.
2. **Otherwise: an extraction pass by Claude** over the finished report, using the prompt below, followed by a human check of the extract before ingest.

Either way, the commit holds the report, the extract and the resulting data change side by side, so anyone reviewing can compare all three.

## Extract file format

`reports/<version>/extract/<product>/<bank-id>.json` (or `extract/<bank-id>.json` when the report covers one product):

```json
{
  "bank": "citi",
  "product": "zelle",
  "facts": [
    {
      "attribute": "attr-cap-scam-warning-interstitial",
      "value": true,
      "display": "Yes — full-screen warning on first payment to a new recipient",
      "basis": "disclosed",
      "confidence": "medium",
      "observed_on": "2026-11-12",
      "sources": [
        { "title": "Citi — Zelle FAQ", "url": "https://…", "retrieved_at": "2026-11-12T10:05:00-06:00" }
      ],
      "evidence": { "quote": "Before you send …", "report_ref": "report.pdf p.14, §3.2", "mi_level": "CONFIRMED_BANK" }
    }
  ]
}
```

The values above are illustrative only.

| Field | Rule |
|---|---|
| `attribute` | An ID in `data/comparisons/<product>/comparison.json` (`attr-cap-<flag>`, `attr-score-<stage>`), at most once per file |
| `value` | Typed by the attribute: integer, boolean, money (a number, not "$2,500"), enum or enum_list (allowed values only, exact case), ISO 8601 duration (`PT5M`, `P1D`, `PT0.5H`, not "5 minutes"), or text. Use `null` plus `display` when only wording is known. |
| `basis` | `observed` (seen first-hand), `disclosed` (public source) or `inferred` (reasoned). Never `sample` or `internal`. |
| `confidence` | `high`, `medium` or `low`. Use `low` for anything inferred. |
| `observed_on` | Date the fact was seen or read, as YYYY-MM-DD |
| `sources` or `source_ids` | Observed and disclosed facts need one of: `sources` (the original page, each with a `url`; `title`, `kind` and `retrieved_at` optional), `source_ids` already in `registries/sources.json`, or `evidence.report_ref` citing the report. |
| `evidence` | Optional but recommended: the exact quote, where it sits in the report, and the MI evidence level (`mi_level`) |

Leave out any attribute the report doesn't answer. It stays `awaiting`; never guess to fill a cell.

## Extraction prompt

Use with the report attached, once per bank:

> You are extracting facts about **{bank name}**'s **{rail}** experience from the attached market-intelligence report into the JSON format in `docs/mi-extraction.md`.
> For each of these attributes, extract a fact only if the report states it with a source: {paste the attribute table from the MI contract}.
> Rules: use only the report and the sources it cites; copy the source URL the report cites, not the report itself. Set basis to disclosed for public pages, observed for first-hand walkthroughs, inferred only when the report reasons without a source (confidence low). Values must use the allowed values exactly. Put the supporting sentence in evidence.quote and its location in evidence.report_ref. Omit attributes the report doesn't cover. Output only the JSON.

## Then

```bash
python3 tools/ingest_mi.py reports/<version> --dry-run   # optional: check the extracts without writing anything
scripts/refresh.sh reports/<version>            # import (if a workbook), ingest, validate, test, rebuild site; rerun freely
scripts/refresh.sh reports/<version> --commit   # once it passes: commit on the current branch
```

Ingest validates the complete result before writing, so a bad extract leaves the repo untouched: fix it and rerun. If you edited data by hand and want to start over, run `git checkout -- data registries reports/ingest-log.json`.

Unknown fields (a typo like `valeu`) are refused rather than ignored.

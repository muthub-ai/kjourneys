# From an MI report to facts: extraction

A market-intelligence report is prose. The comparison needs typed, sourced facts. Extraction turns one into the other, writing one `extract/<bank>.json` per competitor beside the report. `tools/ingest_mi.py` then applies the extracts deterministically.

## Who extracts

1. **Preferred: the MI session itself.** Give it this document and [the data contract](market-intelligence-contract.md), and ask it to deliver the extract files with its report. It already holds the sources, so nothing is lost in translation.
2. **Otherwise: an extraction pass by Claude** over the finished report, using the prompt below, followed by a human check of the extract before ingest.

Either way, the pull request shows the report, the extract and the resulting data change side by side. Reviewers compare all three.

## Extract file format

`reports/<version>/extract/<bank-id>.json`:

```json
{
  "bank": "citi",
  "product": "zelle",
  "facts": [
    {
      "attribute": "attr-daily-limit",
      "value": 2500,
      "display": "$2,500 per day",
      "qualifier": "segment: standard consumer checking",
      "basis": "disclosed",
      "confidence": "medium",
      "observed_on": "2026-11-12",
      "sources": [
        { "title": "Citi — Zelle FAQ", "url": "https://…", "retrieved_at": "2026-11-12T10:05:00-06:00" }
      ],
      "evidence": { "quote": "Send up to …", "report_ref": "report.pdf p.14, §3.2" }
    }
  ]
}
```

The values above are illustrative only.

| Field | Rule |
|---|---|
| `attribute` | One of the 11 IDs in `data/comparisons/zelle/comparison.json`, at most once per file |
| `value` | Typed by the attribute: integer, boolean, money (number), enum or enum_list (allowed values only), ISO 8601 duration, or text. Use `null` plus `display` when only wording is known. |
| `basis` | `observed` (seen first-hand), `disclosed` (public source) or `inferred` (reasoned). Never `sample` or `internal`. |
| `confidence` | `high`, `medium` or `low`. Use `low` for anything inferred. |
| `observed_on` | Date the fact was seen or read, as YYYY-MM-DD |
| `sources` | Required for observed and disclosed facts: the original page, not the report |
| `evidence` | Optional but recommended: the exact quote and where it sits in the report |

Leave out any attribute the report doesn't answer. It stays `awaiting`; never guess to fill a cell.

## Extraction prompt

Use with the report attached, once per bank:

> You are extracting facts about **{bank name}**'s **Zelle** experience from the attached market-intelligence report into the JSON format in `docs/mi-extraction.md`.
> For each of these attributes, extract a fact only if the report states it with a source: {paste the attribute table from the MI contract}.
> Rules: use only the report and the sources it cites; copy the source URL the report cites, not the report itself. Set basis to disclosed for public pages, observed for first-hand walkthroughs, inferred only when the report reasons without a source (confidence low). Values must use the allowed values exactly. Put the supporting sentence in evidence.quote and its location in evidence.report_ref. Omit attributes the report doesn't cover. Output only the JSON.

## Then

```bash
make ingest REPORT=reports/<version>     # applies extracts, then runs the full check
```

Commit the report folder and the data changes together, then open a pull request.

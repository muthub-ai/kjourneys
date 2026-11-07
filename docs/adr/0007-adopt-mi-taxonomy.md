# ADR-0007: Adopt the market-intelligence study's taxonomy

- Status: Accepted
- Date: 2026-11-06

## Context

The first MI delivery (`reports/2026-11-06-v1/`) came with its own vocabulary: ten banks (Fifth Third rather than the Citizens placeholder), sixteen rails, nine stages (DISCOVER … SUPPORT), six evidence levels, sixteen capability flags and a 0–4 stage-score rubric. kjourneys had five products, six stages and eleven drafted Zelle questions with sample values. Mapping MI's richer model onto ours would have lost detail on every import and made each fact harder to trace back to the workbook.

## Decision

Adopt MI's taxonomy as the ontology's (kos-journey/0.7.0, `tools/migrate_0_6_to_0_7.py`):

- One product per rail, with a family for grouping. The nine MI stages become the stage codelist.
- Evidence levels map onto basis and confidence (CONFIRMED_BANK → disclosed/high, OBSERVED_SESSION → observed/high, THIRD_PARTY → disclosed/medium, COMMUNITY, INFERRED and UNKNOWN → inferred/low). The original level is kept on every record.
- Comparisons are generated from the workbook: a boolean per capability flag (Yes if any sub-product on the rail has it, No only if all lack it) and an integer per stage score. U stays awaiting and is never counted as 0.
- MI's analysis (findings, composites, observations, verifications, participation, ranking) becomes first-class, validated collections.
- The drafted Zelle questions are removed. The Wells Fargo sample blueprint stays, labeled sample, as the only journey with a backstage.
- The Excel workbook is canonical. It is newer than the HTML report's embedded data (WF index 69.3 against 69.5).

## Consequences

Imports are lossless and rerunnable, and every fact points to a workbook row and its sources. Backstage fields on moments become optional, because outside-in journeys cannot fill them honestly. A future MI delivery with a different layout needs an importer change, which is reviewed like code. Wells Fargo can now carry MI facts in comparisons, since the study scores it like every other bank.

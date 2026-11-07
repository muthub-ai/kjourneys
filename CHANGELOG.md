# Changelog

## 0.5.0 — 2026-11-06

- **Versioned MI reports:** `reports/<YYYY-MM-DD-vN>/` holds each report as received, its manifest (sha256-pinned) and per-bank extracts.
- **`tools/ingest_mi.py` (`make ingest REPORT=...`):**
  - Turns extracts into sourced facts and registers the report and every cited URL as sources.
  - Supersedes changed facts instead of overwriting them.
  - Refuses re-ingest, sample basis, and MI facts for Wells Fargo.
- **Validation:** fails if any ingested report is missing or edited.
- **`tests/test_ingest.py`:** 10 end-to-end checks of the ingest flow, run in CI.
- **Wording:** the "our bank" label is removed; Wells Fargo is the focus bank (`portfolio.focus_bank`, party role `focus`).

## 0.4.0 — 2026-11-06

First repository release.

- **Ontology kos-journey/0.4.0**
  - Assertion history with one current entry per slot.
  - Comparison has its own governance block.
  - Publish gates.
  - Principals, bank-scoped URNs, percent scale, enum allowed values and ISO 8601 durations.
- **Validator**
  - Uniqueness, URN kind and bank, variant order, value typing and temporal checks.
  - Competitor facts are restricted to observed, disclosed or inferred.
  - The validator refuses to run without the date-time format checker.
- **Negative tests:** 29 fixtures, each of which must fail.
- **Split sources:** registries, journeys, and comparisons split per bank, assembled in CI.
- **Output ports:** journey site, `kjourneys.json`, `facts.jsonl`, `coverage.json`, plus a CI job summary.
- **Docs:** data product descriptor, architecture, six ADRs and the market-intelligence data contract.

## 0.3.0

Global identity, catalogs, assertions, metric definitions, governance and JSON Schema.

## 0.2.0

Portfolio, hot spots, unhappy paths and competitor comparison.

## 0.1.0

The first Zelle service blueprint.

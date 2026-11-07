# Changelog

## 0.7.0 — 2026-11-06

- **First MI delivery landed** (`reports/2026-11-06-v1/`: HTML report, dossier, sources and verification, workbook), preserved byte for byte and sha256-pinned.
- **The MI taxonomy is the ontology's** ([ADR-0007](docs/adr/0007-adopt-mi-taxonomy.md)): ten banks, sixteen rails, nine stages, six evidence levels. `tools/migrate_0_6_to_0_7.py`.
- **`tools/import_mi_workbook.py`:** reads the workbook into 236 journeys (2,176 steps), 419 gaps and strengths, 17 composites, 595 observations, 206 verifications, 70 participation rows, the ranking, 1,156 sources and 16 product comparisons (16 capability flags, 0–4 stage scores on 12 scored rails). `scripts/refresh.sh` runs it when the manifest names a `workbook`.
- **Removed:** the drafted Zelle comparison (11 questions, sample values). The Wells Fargo sample blueprint stays, labeled sample.
- **Schema:** new collections (findings, composites, observations, verifications, participation, rankings); moment backstage fields optional; moments gain actor, decision, notification; journeys gain exceptions, notifications, status tracking and assessment.
- **Validator:** MI references resolve, STR/GAP IDs match their type, records cite a known report, MI journey IDs are unique per bank. The focus bank may now hold MI facts.
- **Site rebuilt for MI data:** overview (ranking, rail heat map, top Wells Fargo gaps), stage scores per bank with a gap-to-best mode, any journey as a blueprint with findings and sources, bank-by-bank compare per rail, filterable gaps and strengths, method (files, evidence levels, verification round). A compact view model keeps the page near 2.8 MB.
- **Journey and blueprint views carried over for every journey:**
  - Journey: a stacked graph of the bank's stage scores against the best bank and Wells Fargo, over its gaps by severity with strengths above the line; stage cards; ranked gaps.
  - Blueprint: lenses, highlights and jump-to for every journey. The sample keeps its experience curve, hot spots, unhappy paths, app tracing and systems table.
  - Present mode and the engineering sequence diagram are back. The story's numbers are computed from the MI data.
- **Exports:** facts.jsonl adds findings and rankings; summary adds the ranking.
- **Tests:** 40 negative fixtures (9 new for MI collections), now picking attributes by datatype; the ingest test uses its own TEST questions. `openpyxl` added to requirements.

## 0.6.0 — 2026-11-06

- **Several products:**
  - The assembled instance holds `comparisons[]`, one per product. The site's Compare view has a product switcher, and the coverage grid shows sourced competitor facts per product and bank.
  - `tools/new_comparison.py` scaffolds a product's questions with an awaiting slot for every bank. Rerunning it with new questions keeps existing facts.
- **Multi-product MI reports:**
  - The manifest takes `products: [...]`, and extracts live in `extract/<product>/<bank>.json`.
  - Any formats are preserved: html, docx, xlsx, all checksum-pinned.
- **Validation:** one comparison per product, and every comparison product must be in the portfolio. Two new negative fixtures (31 in total). The ingest test has 27 checks, including multi-product cases.
- **Migration:** `tools/migrate_0_5_to_0_6.py`.

## 0.5.0 — 2026-11-06

- **Versioned MI reports:** `reports/<YYYY-MM-DD-vN>/` holds each report as received, its manifest (sha256-pinned) and per-bank extracts.
- **`scripts/refresh.sh [reports/<version>] [--commit] [--push]`:** one rerunnable command on the current branch: ingest, validate, test, rebuild the site and exports, and optionally commit. CI now only re-validates on push and no longer builds the site; pull-request mode is gone.
- **`tools/ingest_mi.py`:**
  - Turns extracts into sourced facts and registers the report and every cited URL as sources.
  - Supersedes changed facts instead of overwriting them.
  - Rerunnable: re-ingesting a version rolls back what it wrote and applies it afresh. It refuses only when a later version builds on it.
  - Refuses sample basis, and MI facts for Wells Fargo.
- **Validation:** fails if any ingested report is missing or edited.
- **`tests/test_ingest.py`:** 22 end-to-end checks of the ingest, rerun and refusal flows, run in CI.
- **Independent review fixes:**
  - Ingest validates the complete result in a scratch copy before writing, then writes atomically, ingest log last. A bad extract leaves the repo untouched.
  - Ingest refuses unknown fields (typos), a null value without display wording, inferred facts that aren't low confidence, future `observed_on`, sources without `url`, impossible version dates and bad `received_at`.
  - Missing manifests or bank files give clear messages instead of tracebacks.
  - Tests are data-independent: fixtures pick awaiting slots at runtime, and the ingest test starts from placeholders. Real MI data no longer turns the build red.
  - The validator resolves report paths from the repo root, rejects duplicate list items, and accepts full ISO 8601 durations (W, fractions).
  - Site: Wells Fargo pinned first, competitor values shown as readable text, counts by evidence type, and no claim of legal review that isn't enforced.
  - `tools/migrate_0_4_to_0_5.py` for the breaking rename. Docs corrected for IDs, source fields, dry run, recovery, tags and fonts.
  - CI actions bumped to checkout@v5 and setup-python@v6.
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

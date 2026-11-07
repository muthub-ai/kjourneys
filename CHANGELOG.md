# Changelog

## 0.8.0 — 2026-11-07 · Wells Fargo map and bundles

- **Lines of business:** `registries/lines-of-business.json` records Wells Fargo's four reportable segments (Q3 2026 10-Q) and each marketed product's owning line of business, with the rule used; validated.
- **Wells Fargo-only export:** `tools/export_focus.py` writes `docs/bundles/_source/wells-fargo.json` with Wells Fargo records only; other banks named in Wells Fargo text become "a peer bank"; best practice is a number with no bank. It fails if any other bank is still named.
- **Bundles:** `tools/build_bundles.py` builds 15 product bundles and 4 line-of-business bundles in OKF v0.2 (manifest, index, insert-only log, knowledge-source, cited sections, script-built journey-graph, human-only knowledge-sources). `tools/validate_bundles.py` checks frontmatter, every citation and its record hash, manifests, indexes, and that no other bank is named. CI rebuilds and compares.
- **Site:** a "Wells Fargo map" tab with a network view (precomputed layout, pan, zoom, filters, search, details panel) and a flow view.

## 0.7.1 — 2026-11-07 · v0.1 release review

An independent review (a different model, given the code, not the conclusions) found these. Each was checked against the workbook before it was fixed.

- **Capability flags:** free text was read as Yes. They now follow MI's own counting (literal Yes only; "not evidenced" is No; other text is unknown, kept as detail). This changes flags such as step-up authentication, where MI counts 1 bank, not 9.
- **ScoreTotals:** MI's index and rail means do not match its own stage scores (all 10 banks; 35 rail means). The ranking now shows MI's index beside one recomputed from the scores (Wells Fargo 69.3 vs 61.8, #3 vs #4); the heat map and stage views use the scores. Raised with MI.
- **Customer-journey links:** MI's references now decide; otherwise rail and segment must match. The rail-only "closest match" is gone, so commercial and receive journeys are no longer forced onto consumer send journeys (178 of 236 linked).
- **Gap stages:** 63 gaps are filed under a best-practice stage that differs from the step they sit on; that step's stage is now kept as `step_stage`, and the validator checks it.
- **Report immutability is enforced:** the importer refuses a changed pinned file, every validation re-checks every file in every manifest, and CI runs `import_mi_workbook.py --check` so imported data cannot be hand-edited. The workbook is now the report source every MI record cites (the HTML is an earlier cut).
- **Safe imports:** the importer stages every write, validates in a scratch copy, then writes; unknown stages, observation types, severities, step numbering and out-of-range scores now stop it; a second report version needs `--replace`.
- **Validator:** finding ↔ journey bank, product, step and stage; composite steps; score 0–4; ranking ranges; rail-segment links on the same rail; competitor backstage only disclosed or inferred (ADR-0004, amended). `run_tests.sh` now requires each fixture to fail with its own message, and treats a crash as a failure (55 fixtures).
- **Ingest:** a fact counts as unchanged only if confidence, sources and evidence also match.
- **Site:** `dist/index.html` is a complete document (doctype, charset, viewport, lang); `dist/artifact.html` is the fragment for the artifact host. Links accept only http(s), observed-session sources are never linked, the drawer keeps keyboard focus, inline data cannot close its script. Wells Fargo's Zelle journeys show the sample backstage by stage, labeled sample.
- **Not changed, by decision:** the public repo and the observed-session detail (owner's call, deferred); a pull-request CI trigger (owner chose push-only); CODEOWNERS (owner's call), now documented as not enforced; MI sub-products whose rail is not in their product's rail list (33, mostly "Other"), which is how MI recorded them.

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
- **Customer journeys, bank journeys, products:**
  - The 17 MI composites are the customer journeys. Each bank journey links to the one it delivers; the link is derived and labeled (MI's own references, else rail and segment, else rail only as a closest match). 209 of 236 are linked; the rest are grouped by rail.
  - Each bank's catalog is imported: 143 products as marketed and 462 sub-products, with capability flags per sub-product. Journeys carry their product, sub-product, and limits, fees and cut-offs.
  - The Journey tab opens on a customer journey: best-practice steps with the bank steps they come from, then every bank's journeys with product › sub-product and stage scores. A new Products tab shows each catalog. The blueprint gains a best-practice row and a picker grouped by customer journey. Compare cells list the sub-products behind each Yes or No.
  - Workbook check: TD-J18 names product TD-P10, but its sub-product TD-P04-S05 belongs to TD-P04. The import uses TD-P04, keeps the original as x-mi_product_id, and records a warning in the manifest.
- **Exports:** facts.jsonl adds findings and rankings; summary adds the ranking.
- **Tests:** 55 negative fixtures (15 new for MI collections, catalog and journey links), now picking attributes by datatype; the ingest test uses its own TEST questions. `openpyxl` added to requirements.

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

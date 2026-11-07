# Changelog

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

# kjourneys

A git-native data product for customer journeys in banking. It holds Wells Fargo service blueprints and sourced, dated competitor facts on the same stages. Every change is validated, reviewed and versioned, and is published as an executive journey site plus machine-readable outputs.

First study: **money movement** across the ten largest US retail banks: 16 payment rails (Zelle, request to pay, ACH, wires, remittance, RTP, FedNow, push to card, bill pay, internal transfers, mobile deposit, cash, wallets), nine journey stages from Discover to Support. The first MI delivery (`reports/2026-11-06-v1/`) supplies 236 journeys, 2,176 steps, 419 gaps and strengths, 0–4 stage scores and 16 capability flags per rail, all traced to 1,156 sources.

> **Prototype.** The competitor data is public-source competitive intelligence, with CI legal review still pending, so share the site only after that review. The Wells Fargo backstage (processes, controls, app IDs) is sample data. Real bank internals belong in enterprise GitHub (see [architecture §6](docs/architecture.md#6-governance)).

## Quick start

```bash
pip install -r requirements.txt
scripts/refresh.sh                                   # validate, test, rebuild site + exports
scripts/refresh.sh reports/2026-11-06-v1             # import + ingest an MI report first (rerunnable)
scripts/refresh.sh reports/2026-11-06-v1 --commit    # commit on the current branch when it passes
open dist/index.html
```

Everything runs locally on your branch, and you can rerun it as often as you like. On every push, CI re-validates the data as a safety net; it does not build the site.

## How data gets in

| You are | You change | Reviewed by | Guide |
|---|---|---|---|
| Market-intelligence session | `reports/<version>/` (report files + the MI workbook), then `scripts/refresh.sh` | CI legal + study lead | [MI contract](docs/market-intelligence-contract.md) · [extraction](docs/mi-extraction.md) · [reports](reports/README.md) |
| Journey owner | `data/journeys/<bank>/<journey>.json` | Journey owners | [Ontology](schema/journey-ontology.yaml) |
| Data office | `registries/`, `schema/`, `tools/` | Data office | [Architecture](docs/architecture.md) |

## What comes out

| Port | File | For |
|---|---|---|
| Journey site | `dist/index.html` | Executives, product, engineering: ranking and rail heat map, stage scores, journey graphs, blueprints with lenses, bank-by-bank compare, gaps and strengths, method, present mode |
| Canonical instance | `dist/kjourneys.json` | KOS ingestion, tooling |
| Facts | `dist/facts.jsonl` | BI, agents, retrieval: one row per current fact (comparison cells, step evidence, findings, rankings) with basis and sources |
| Coverage | `dist/coverage.json` | Health: completeness by bank and basis, staleness, legal status |

## Wells Fargo bundles and map

`docs/bundles/` holds Wells Fargo product and line-of-business bundles (OKF v0.2), built from a Wells Fargo-only export that no other bank can leak into. The site's "Wells Fargo map" tab shows line of business → product → sub-product → journey → customer journey. See [docs/bundles/README.md](docs/bundles/README.md).

## Why trust it

- **Provenance on every fact:** basis (observed, disclosed, inferred, internal, sample, awaiting), the MI evidence level it came from, sources, who asserted it and when, and validity dates.
- **History is never lost:** facts are superseded, never overwritten, and git keeps every prior state. Tag the commit you present from.
- **Rules are code:** a schema, an integrity checker and publish gates enforce them, and 55 negative tests prove the rules hold.
- **The line of visibility is a provenance boundary:** competitors' backstage is never presented as fact.

## Repo map

```
manifest.json  dataproduct.yaml  Makefile  requirements.txt
schema/   registries/   data/   reports/   tools/   tests/   site/   docs/
```

Design and decisions: [docs/architecture.md](docs/architecture.md) · [docs/adr/](docs/adr/) · [dataproduct.yaml](dataproduct.yaml)

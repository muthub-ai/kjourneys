# kjourneys

A git-native data product for customer journeys in banking. It holds our own service blueprints and sourced, dated competitor facts on the same stages. Every change is validated, reviewed and versioned, and is published as an executive journey site plus machine-readable outputs.

First study: **money movement** (Zelle, ACH, wire, bill pay, instant payments) across the top 10 US banks.

> **Prototype.** This repo holds sample data only. Real bank internals and competitor research belong in enterprise GitHub (see [architecture §6](docs/architecture.md#6-governance)).

## Quick start

```bash
pip install -r requirements.txt
make check          # assemble → validate → negative tests → build site → export
open dist/index.html
```

`make check` must print `PASS` and no `HOLE` lines. CI runs the same pipeline on every pull request and posts a data-status summary.

## How data gets in

| You are | You change | Reviewed by | Guide |
|---|---|---|---|
| Market-intelligence session | `data/comparisons/<product>/values/<bank>.json` | CI legal + study lead | [MI data contract](docs/market-intelligence-contract.md) |
| Journey owner | `data/journeys/<bank>/<journey>.json` | Journey owners | [Ontology](schema/journey-ontology.yaml) |
| Data office | `registries/`, `schema/`, `tools/` | Data office | [Architecture](docs/architecture.md) |

## What comes out

| Port | File | For |
|---|---|---|
| Journey site | `dist/index.html` | Executives, product, engineering: portfolio, journey, blueprint, compare, method, present mode |
| Canonical instance | `dist/kjourneys.json` | KOS ingestion, tooling |
| Facts | `dist/facts.jsonl` | BI, agents, retrieval: one row per current fact with basis and sources |
| Coverage | `dist/coverage.json` | Health: completeness by bank and basis, staleness, legal status |

## Why trust it

- **Provenance on every fact:** basis (observed, disclosed, inferred, internal, sample, awaiting), sources, who asserted it and when, and validity dates.
- **History is never lost:** facts are superseded, never overwritten, and every readout cites a release tag.
- **Rules are code:** a schema, an integrity checker and publish gates enforce them, and 29 negative tests prove the rules hold.
- **The line of visibility is a provenance boundary:** competitors' backstage is never presented as fact.

## Repo map

```
manifest.json  dataproduct.yaml  Makefile  requirements.txt
schema/      registries/      data/      tools/      tests/      site/      docs/
```

Design and decisions: [docs/architecture.md](docs/architecture.md) · [docs/adr/](docs/adr/) · [dataproduct.yaml](dataproduct.yaml)

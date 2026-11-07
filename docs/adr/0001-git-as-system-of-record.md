# ADR-0001: Git is the system of record

- Status: Accepted
- Date: 2026-11-06

## Context

Journey and competitor data needs review, attribution, history and rollback. The team already runs KOS knowledge this way (kbundles: git, gates, human approval).

## Decision

Store all source data as JSON files in git. Changes arrive as commits on a branch, produced and checked by scripts/refresh.sh, which can be rerun on the same branch until it passes. CI re-validates every push. Outputs are derived artifacts, never edited.

## Consequences

Full audit trail and reproducibility by tag at no infrastructure cost. Simple to operate; pull-request review can be layered on later without changing the data. Queries need an export (facts.jsonl) rather than a database. If write volume ever outgrows this, put the KOS Knowledge Factory API in front, with git still as the record.

# ADR-0001: Git is the system of record

- Status: Accepted
- Date: 2026-11-06

## Context

Journey and competitor data needs review, attribution, history and rollback. The team already runs KOS knowledge this way (kbundles: git, pull requests, gates, human approval).

## Decision

Store all source data as JSON files in git. Changes arrive only by pull request. CI gates every change. Outputs are derived artifacts, never edited.

## Consequences

Full audit trail and reproducibility by tag at no infrastructure cost. Familiar review workflow. Queries need an export (facts.jsonl) rather than a database. If write volume ever exceeds what pull requests handle, put the KOS Knowledge Factory API in front, with git still as the record.

# ADR-0002: Split source files, assembled instance

- Status: Accepted
- Date: 2026-11-06

## Context

A single instance file would make ten concurrent market-intelligence updates conflict, and would prevent per-folder ownership.

## Decision

Split sources by owner and change rate: registries/, data/journeys/<bank>/, data/comparisons/<product>/values/<bank>.json. tools/assemble.py builds dist/kjourneys.json, which is what the validator and every output use. Assembly checks that file contents agree with their paths.

## Consequences

No merge conflicts between banks, and folder-level ownership stays possible (a CODEOWNERS template is included). One more build step. The assembled file is the only thing consumers see, so the split stays an internal detail.

# ADR-0003: Every fact is an assertion with history

- Status: Accepted
- Date: 2026-11-06

## Context

Competitor facts change (limits, policies) and executives must be able to reproduce what was shown on a given date. The data office requires per-fact provenance.

## Decision

Each comparison cell is an Assertion[] with exactly one current entry (valid_to null). An assertion carries basis, source_ids, asserted_by, asserted_at, observed_on, valid_from/valid_to, supersedes, verified_by and confidence. Changes close the old entry and append a new one.

## Consequences

Bitemporal history (business validity plus assertion time, plus git commit time). Slightly more verbose files. The validator enforces one current entry and supersedes resolution.

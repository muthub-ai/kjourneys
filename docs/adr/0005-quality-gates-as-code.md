# ADR-0005: Quality gates as code, with negative tests

- Status: Accepted
- Date: 2026-11-06

## Context

Round-2 data-office review showed a schema plus validator that accepted five deliberately broken files. A rule that isn't tested is not enforced.

## Decision

Encode every rule in tools/validate_journey.py (schema, integrity, typing, temporal, provenance, publish gates). Keep a negative fixture for each rule in tests/; CI fails if any fixture passes. The validator refuses to run without the date-time format checker.

## Consequences

Rules are executable and regression-proof. Each new rule ships with its fixture. Adding a rule is a code review, not a policy memo.

# ADR-0004: The line of visibility is a provenance boundary

- Status: Accepted
- Date: 2026-11-06

## Context

Service blueprints separate what the customer sees from the backstage. That is also exactly what market intelligence can and cannot observe about a competitor.

## Decision

Lanes above the line of visibility can hold observed or disclosed facts for any bank. Lanes below it hold internal facts for Wells Fargo (sourced from KOS bundles) and only inferred facts for competitors. Named competitors never take sample or internal facts; the validator enforces this.

## Consequences

Executives can always tell what we know from what we assume. Competitor blueprints stay honest about their backstage. Some lanes for competitors stay empty or inferred by design.

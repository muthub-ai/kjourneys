# ADR-0006: Static, self-contained outputs

- Status: Accepted
- Date: 2026-11-06

## Context

Audiences range from executives on a shared link to agents and BI tools. Running a server adds operations and security review for a read-mostly product.

## Decision

Publish four static output ports from CI: kjourneys.json (canonical), facts.jsonl (flat facts), coverage.json (health), and index.html (a journey site with all data inlined; only web fonts load from Google Fonts, with system fonts as the fallback offline). Any host can serve them: an artifact link, internal static hosting, or KOS ingestion.

## Consequences

Zero runtime infrastructure and trivially cacheable. Data is only as fresh as the last merge, which matches how facts arrive. Large data volumes would move the page to loading kjourneys.json beside it.

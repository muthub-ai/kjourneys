# Market-intelligence data contract

How the market-intelligence (MI) session delivers competitor facts into kjourneys. Follow it exactly and `scripts/refresh.sh` passes; skip a rule and it stops with the reason.

## What you write

One file per bank per product:

```
data/comparisons/zelle/values/<bank-id>.json
```

Bank IDs come from `registries/parties.json` (for example `jpmorgan-chase`, `bank-of-america`, `citi`). Every file already exists with each attribute set to `awaiting`. You replace those placeholders with facts; you never add or remove attributes.

Every source you cite goes in `registries/sources.json`.

## The questions (attributes)

Defined in `data/comparisons/zelle/comparison.json`. Each has a datatype, an optional unit, a normalization rule, and for enums the allowed values.

| Attribute | Datatype | Allowed values or format |
|---|---|---|
| `attr-enroll-where` | enum_list | `mobile-app`, `web`, `branch`, `standalone-app` |
| `attr-enroll-steps` | integer | count of screens from Zelle hub to first send |
| `attr-payee-name-shown` | boolean | `true` only if the registered name is shown before confirming |
| `attr-new-payee-warning` | enum | `none`, `first-payment`, `every-payment`, `risk-based` |
| `attr-daily-limit` | money (USD) | lowest published standard-tier limit; segment goes in `qualifier` |
| `attr-stepup-trigger` | text | the bank's own wording, paraphrased, with source |
| `attr-time-to-recipient` | duration | ISO 8601, e.g. `PT5M`; leave `value` null and use `display` if the bank only says "minutes" |
| `attr-notifications` | enum_list | `push`, `email`, `sms`, `in-app` |
| `attr-cancel-pending` | enum | `never`, `only-if-unclaimed`, `within-window`, `always` |
| `attr-report-channels` | enum_list | `mobile-app`, `web`, `chat`, `contact-center`, `branch` |
| `attr-scam-reimbursement` | text | the bank's public stance, with source |

## One fact (an assertion)

Replace the `awaiting` entry with a sourced assertion. Example: a disclosed daily limit for Chase.

```json
"attr-daily-limit": [
  {
    "id": "urn:kos:assertion:jpmorgan-chase:zelle:daily-limit:1",
    "value": 2000,
    "display": "$2,000 per day (standard checking)",
    "qualifier": "segment: standard consumer checking",
    "basis": "disclosed",
    "source_ids": ["src-chase-zelle-faq-2026-11"],
    "asserted_by": "process:mi-session",
    "asserted_at": "2026-11-10T14:00:00-06:00",
    "observed_on": "2026-11-10",
    "valid_from": "2026-11-10",
    "valid_to": null,
    "verified_by": null,
    "verified_at": null,
    "confidence": "medium"
  }
]
```

The number above is illustrative only. When you use `scripts/refresh.sh`, you don't write this by hand: ingest assigns the assertion ID (the next number after the `:1` placeholder, so the first real fact is `:2`), adds the report itself (`src-mi-<version>`) and each cited URL (`src-<title-slug>-<hash>`) to the sources, and fills in the asserter and dates. Its source entry in `registries/sources.json` looks like this:

```json
{ "id": "src-chase-zelle-faq-2026-11", "kind": "web-page", "title": "Chase — Zelle FAQs",
  "origin": "chase.com", "url": "https://…", "retrieved_at": "2026-11-10T13:55:00-06:00" }
```

## Rules CI enforces

1. **Basis.** Named competitors take `observed` (seen first-hand), `disclosed` (public source) or `inferred` (reasoned, and then `confidence` must be `low`). Never `sample` or `internal`.
2. **Sources.** Any non-awaiting fact needs at least one `source_ids` entry that exists in `registries/sources.json`, plus `asserted_by` and `asserted_at`.
3. **Types.** The `value` must match the attribute datatype and, for enums, the allowed values.
4. **Awaiting means empty.** An `awaiting` entry carries no `value` and no `valid_from`. A real fact with `value: null` must have `display` wording.
8. **No duplicates, no future dates.** List values don't repeat an item, and `observed_on` is never in the future.
5. **History, never overwrite.** When a fact changes, set `valid_to` on the old entry and append a new one with `"supersedes": "<old id>"` and the next sequence number in its ID. Exactly one entry per attribute has `valid_to: null`.
6. **Dates.** `valid_from` is on or before `valid_to`; timestamps are RFC 3339.
7. **Principals.** `asserted_by` and `verified_by` look like `process:mi-session` or `human:<id>`.

## How to submit

The preferred path is a versioned report, so every fact links back to the report it came from:

1. Add the report as received to `reports/<YYYY-MM-DD-vN>/`, with a `manifest.json` ([reports/README.md](../reports/README.md)).
2. Add one `extract/<bank>.json` per bank ([mi-extraction.md](mi-extraction.md)).
3. Run `scripts/refresh.sh reports/<version>`. It writes the facts and sources described above, keeps history, validates, runs the tests, and rebuilds the site and exports.
4. If it stops, fix the extract and run the same command again. Rerunning a version replaces what it wrote before.
5. When it passes, run it once more with `--commit` (and `--push` if you want) to commit the report folder and data changes together on the current branch.

For a single quick fix, you can still edit `values/<bank>.json` by hand using the rules above, then run `scripts/refresh.sh --commit`.

The rebuilt site is `dist/index.html`, and the Compare view shows a column for every bank that now has facts. Have legal review competitor facts before the site is shared.

## What not to collect

- Anything behind a login you are not entitled to, from a former employee, or under NDA.
- Personal information about bank customers or staff.
- Material non-public information of any kind.

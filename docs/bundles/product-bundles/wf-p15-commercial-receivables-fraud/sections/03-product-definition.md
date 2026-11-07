---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay): sub-products, capabilities per sub-product, notes, limits and fees",
 "sources": [
  {
   "id": "kj-wells-fargo",
   "path": "docs/bundles/_source/wells-fargo.json",
   "sha256": "749175201ed7a14af05937360afbf82f3ec2afe567c9152116002b2adbe035f9"
  },
  {
   "id": "mi-2026-11-06-v1",
   "report_version": "2026-11-06-v1",
   "path": "reports/2026-11-06-v1/Money_Movement_CI_Data.xlsx",
   "sha256": "b9a60999aa1273f195fc7d6d81ad81fea0e5e011c8863bd458c5f58c622c8e88"
  }
 ],
 "generated": {
  "by": "process:build-bundles",
  "at": "2026-11-06T23:59:00-06:00"
 },
 "verified": [],
 "x_kf": {
  "schema": "kf-product-bundle/0.1",
  "bundle_id": "wf-p15-commercial-receivables-fraud",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P15",
  "line_of_business": "wf-cb",
  "content_sha256": "ecc3a6b5dfa3fc73fd4e9dbe2493201541848e92b1c4ca94738da713e48ffb85",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — product definition

Where it sits in the bank's app and site: Vantage/CEO services; Fraud Manager in Vantage[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P15-S01` Bill Manager (e-invoice + ACH debit collection) | ACH origination (business) | commercial, small-business | Send electronic invoices and reminders; collect via ACH; sync with accounting software.[^2] |
| `WF-P15-S02` Perfect Receivables® (proxy account numbers for ACH/wire receipts) | Other money movement | commercial | Unique proxy account numbers per payer to route and identify incoming ACH and wires.[^3] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P15-S01 | WF-P15-S02 | Detail |
|---|---|---|---|
| Cancel before it is sent | ✗ | ✗ | [^2][^3] |
| Pay from phone contacts | ✗ | ✗ | [^2][^3] |
| Dual approval (business) | ✗ | ✗ | [^2][^3] |
| Email or text notifications | ✓ | ✗ | [^2][^3] |
| Instant delivery | ✗ | ✗ | [^2][^3] |
| International | ✗ | ✗ | [^2][^3] |
| Push notifications | ✗ | ✗ | [^2][^3] |
| QR code | ✗ | ✗ | [^2][^3] |
| Recurring payments | ✓ | ✗ | [^2][^3] |
| Request money | ✓ | ✗ | [^2][^3] |
| Same-day delivery | ✗ | ✗ | [^2][^3] |
| Scam warning before sending | ✗ | ✗ | [^2][^3] |
| Schedule for a future date | ✗ | ✗ | [^2][^3] |
| Split a payment | ✗ | ✗ | [^2][^3] |
| Status tracking | ✓ | ✓ | [^2][^3] |

## Notes from the study

- `WF-P15-S01`: Segment overlap unclear (marketed on commercial TM page).[^2]

## Limits, fees and timing (captured incidentally)

- `WF-J24` — limits: Wire limits at company/account/user level[^4]

[^1]: kj · product/WF-P15 · 1b70c83e2760
[^2]: kj · sub-product/WF-P15-S01 · 8329a58bb402
[^3]: kj · sub-product/WF-P15-S02 · 9ea8fd1b8b2b
[^4]: kj · journey/WF-J24 · 72f66a396d8c

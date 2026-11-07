---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Mobile Deposit (Wells Fargo Mobile® Deposit): sub-products, capabilities per sub-product, notes, limits and fees",
 "sources": [
  {
   "id": "kj-wells-fargo",
   "path": "docs/bundles/_source/wells-fargo.json",
   "sha256": "053f4c412d7d3780c7d905451ccabb460abdf36275b1bf937a9a115910add0cb"
  },
  {
   "id": "mi-2026-11-07-v2",
   "report_version": "2026-11-07-v2",
   "path": "reports/2026-11-07-v2/Money_Movement_CI_Data.xlsx",
   "sha256": "cf986dd85a0b1c9d6476009cd08a98a3a1d2a3057d66999907c8b8b93ed9e6aa"
  }
 ],
 "generated": {
  "by": "process:build-bundles",
  "at": "2026-11-07T23:59:00-06:00"
 },
 "verified": [],
 "x_kf": {
  "schema": "kf-product-bundle/0.1",
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "8022e85ba7654ea7c852e091cb4992e8db4cb58ae2d2ef79f9a971a5ebdb9e54",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Mobile Deposit (Wells Fargo Mobile® Deposit) — product definition

Where it sits in the bank's app and site: Mobile: 'Deposit' in bottom bar, or long-press app icon > 'Deposit Checks'; screens 'Deposit to'/'To', 'Enter Amount', photo capture, 'Deposit' button.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P06-S01` Deposit a check by photo | Mobile check deposit | consumer, small-business | Endorse with 'For Mobile Deposit at Wells Fargo Only' (or check the mobile-deposit box), capture front/back, confirm, submit; first $400 generally same-day.[^2] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P06-S01 | Detail |
|---|---|---|
| Cancel before it is sent | ✗ | [^2] |
| Pay from phone contacts | ✗ | [^2] |
| Dual approval (business) | ✗ | [^2] |
| Email or text notifications | ✓ | [^2] |
| Instant delivery | ✗ | [^2] |
| International | ✗ | [^2] |
| Push notifications | ✓ | [^2] |
| QR code | ✗ | [^2] |
| Recurring payments | ✗ | [^2] |
| Request money | ✗ | [^2] |
| Same-day delivery | ✓ | [^2] |
| Scam warning before sending | ✗ | [^2] |
| Schedule for a future date | ✗ | [^2] |
| Split a payment | ✗ | [^2] |
| Status tracking | ✓ | [^2] |

## Limits, fees and timing (captured incidentally)

- `WF-J13` — cutoffs: 9 pm PT; fees: None (analyzed business may be charged); limits: Shown on screen; vary by account[^3]
- `WF-J19` — cutoffs: 9 pm PT; fees: Possible for analyzed accounts[^4]

[^1]: kj · product/WF-P06 · 7447c97a0fac
[^2]: kj · sub-product/WF-P06-S01 · adf0bd6e0f63
[^3]: kj · journey/WF-J13 · 0dcdd11b8e8d
[^4]: kj · journey/WF-J19 · 2d1ad618854b

---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Direct Pay for Business: sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "32dae7169dd362592a85bc70159332a7960ed302df5175c503f851e2015bd64d",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — product definition

Where it sits in the bank's app and site: Business Online: 'Transfer & Pay' (page also says 'Transfers & Payments') > 'Direct Pay for Business'; tabs 'Payees', 'Payments' > 'Create Payment'; pay groups 'Individual Master List' / 'Business Master List'; 'Enroll Another TIN' under General.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P08-S01` Pay employees/contractors (direct deposit) | ACH origination (business) | small-business | Individual Master List payees; net pay, bonuses, reimbursements; optional notification emails to payee.[^2] |
| `WF-P08-S02` Pay vendors / other businesses | ACH origination (business) | small-business | Business Master List payees; optional remittance information; $3 per payment to business accounts.[^3] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P08-S01 | WF-P08-S02 | Detail |
|---|---|---|---|
| Cancel before it is sent | ✓ | ✓ | [^2][^3] |
| Pay from phone contacts | ✗ | ✗ | [^2][^3] |
| Dual approval (business) | ✓ | ✓ | [^2][^3] |
| Email or text notifications | ✓ | ✓ | [^2][^3] |
| Instant delivery | ✗ | ✗ | [^2][^3] |
| International | ✗ | ✗ | [^2][^3] |
| Push notifications | ✗ | ✗ | [^2][^3] |
| QR code | ✗ | ✗ | [^2][^3] |
| Recurring payments | ✓ | ✓ | [^2][^3] |
| Request money | ✗ | ✗ | [^2][^3] |
| Same-day delivery | ✗ | ✗ | [^2][^3] |
| Scam warning before sending | ✗ | ✗ | [^2][^3] |
| Schedule for a future date | ✓ | ✓ | [^2][^3] |
| Split a payment | ✗ | ✗ | [^2][^3] |
| Status tracking | ✓ | ✓ | [^2][^3] |
| Step-up authentication | — | — | WF-P08-S01: RSA SecurID or Advanced Access 6-digit code at enrollment/sensitive actions; WF-P08-S02: RSA SecurID / Advanced Access[^2][^3] |

## Notes from the study

- `WF-P08-S01`: Direct Pay FAQ (browser): enroll via Business Online 'Transfer and Pay' > 'Direct Pay for Business'; 'Enroll Another TIN' on the Direct Pay Main Page; $10/month per enrolled business, $0 to Wells Fargo personal accounts, $0.50 to non-WF personal accounts, $3 to business accounts; cutoff 3:00 pm PT; funds debited 3:00 pm PT on Send On Date; payee validation 2 business days (WF accounts) / up to 3 (other banks); edits to payee routing/account re-trigger validation; schedule up to 13 months ahead; access levels Input/Release/Control, Input/Release, Input Only, No Access. FAQ remains silent on cancel/edit of scheduled payments, returns and Same Day ACH.[^2]

## Limits, fees and timing (captured incidentally)

- `WF-J16` — cutoffs: 3:00 pm PT; next business day; fees: $10/month; $0/$0.50/$3 per payment; SecurID free for Direct Pay customers; limits: Higher/Lower tiers as above[^4]

[^1]: kj · product/WF-P08 · 53a0b5f81ba1
[^2]: kj · sub-product/WF-P08-S01 · 49d1af9a29ac
[^3]: kj · sub-product/WF-P08-S02 · 76fa6c9a0dcb
[^4]: kj · journey/WF-J16 · 38a8b7c0348a

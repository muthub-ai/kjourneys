---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Direct Pay for Business delivers",
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
  "content_sha256": "71b527f60ad30a1ab1c0af09ee113dc312dc8e35fd2eeda74f3643a15bf1b085",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — customers and channels

Segments: small-business. Channels: web.[^1]

Network or vendor: Wells Fargo as ODFI (Nacha ACH).[^1]

## Customer journeys this product delivers

- **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** (small_business, send) — 10 best-practice steps[^2]

## Who the journeys are for

- `WF-J16` Small business enrolls in Direct Pay, adds payees and runs an ACH payroll/vendor payment with dual control — persona: Owner + bookkeeper at a 10-employee firm; goal: “Pay employees and vendors electronically next business day with separation of duties”[^3]

[^1]: kj · product/WF-P08 · 53a0b5f81ba1
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11
[^3]: kj · journey/WF-J16 · 38a8b7c0348a

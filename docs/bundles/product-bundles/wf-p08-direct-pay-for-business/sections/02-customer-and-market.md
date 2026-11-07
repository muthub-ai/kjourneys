---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Direct Pay for Business delivers",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "37ca0c976d5d147989ad75497f3e69163dd07db8233d663426527cc100314330",
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

[^1]: kj · product/WF-P08 · 3868912428e5
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · 18172095afc9
[^3]: kj · journey/WF-J16 · 67eed586f4fc

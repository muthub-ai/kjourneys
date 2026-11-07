---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Mobile Deposit (Wells Fargo Mobile® Deposit) delivers",
 "sources": [
  {
   "id": "kj-wells-fargo",
   "path": "docs/bundles/_source/wells-fargo.json",
   "sha256": "7320ba3f33f2f88d6c7aa278ce5e73815a221e37edfb352b6b11bcd36c0aedb7"
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "248020f44669efee8f89dacbc80d80ecccf9ae67f0ed2f5032a074e1c66cb5a3",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Mobile Deposit (Wells Fargo Mobile® Deposit) — customers and channels

Segments: consumer, small-business. Channels: mobile-app.[^1]

Network or vendor: Wells Fargo (vendor not disclosed).[^1]

## Customer journeys this product delivers

- **Consumer deposits a check with the mobile app** (consumer, deposit) — 9 best-practice steps[^2]

## Who the journeys are for

- `WF-J13` Consumer deposits a check with Mobile Deposit — persona: Consumer depositing a paycheck; goal: “Deposit a check without visiting a branch”[^3]
- `WF-J19` Small business deposits checks via mobile and manages delegate access — persona: Retail store owner with a bookkeeper; goal: “Deposit customer checks and let staff view/transact safely”[^4]

[^1]: kj · product/WF-P06 · aa0e6fda3732
[^2]: kj · customer-journey/CJ-MOBILE-DEPOSIT · 6dd6d232e8bd
[^3]: kj · journey/WF-J13 · e4ae53b47a45
[^4]: kj · journey/WF-J19 · 2f91942d8e13

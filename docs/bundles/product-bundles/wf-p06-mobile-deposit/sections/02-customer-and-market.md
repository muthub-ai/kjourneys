---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Mobile Deposit (Wells Fargo Mobile® Deposit) delivers",
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
  "content_sha256": "0eb8c6e4cf7efcc1dd200ca5c2a94b973612806abe14d1034510db1dbaddd623",
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

[^1]: kj · product/WF-P06 · 7447c97a0fac
[^2]: kj · customer-journey/CJ-MOBILE-DEPOSIT · c134e8cc0f1e
[^3]: kj · journey/WF-J13 · 0dcdd11b8e8d
[^4]: kj · journey/WF-J19 · 2d1ad618854b

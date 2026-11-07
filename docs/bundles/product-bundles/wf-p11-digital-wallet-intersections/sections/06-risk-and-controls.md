---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p11-digital-wallet-intersections",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P11",
  "line_of_business": "wf-cbl",
  "content_sha256": "9832139dfcd7e9486c04f1ec117e947a60a344c7f394a40cfe5c6637a701421f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM) — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

None recorded in this study.[^1]

## Exception paths

- `WF-J27` · Merchant not participating: Paze unavailable → [^2]

[^1]: kj · product/WF-P11 · 18c5f5e9f2bf
[^2]: kj · journey/WF-J27 · 49e51d4414ad

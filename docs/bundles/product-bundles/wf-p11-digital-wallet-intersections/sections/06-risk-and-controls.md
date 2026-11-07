---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p11-digital-wallet-intersections",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P11",
  "line_of_business": "wf-cbl",
  "content_sha256": "608a7b567bee45b7624719e119d756e9c05b53d85a462aee0b21788d8c63564f",
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

[^1]: kj · product/WF-P11 · df9119f7188e
[^2]: kj · journey/WF-J27 · 25ca42f849dc

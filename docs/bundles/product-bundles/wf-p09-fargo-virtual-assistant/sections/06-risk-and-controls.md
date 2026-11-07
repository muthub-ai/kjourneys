---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Fargo® virtual assistant: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "5bbfc651c95a96da345503889277f26684d8e08e2cd093057db79407ee55fd7a",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

None recorded in this study.[^1]

## Exception paths

- `WF-J04` · Fargo misunderstands request: Fargo asks again or routes to Customer Service → [^2]
- `WF-J04` · Community: AI assistant 'unhelpful' complaints in Google Play reviews: Frustration → [^2]

[^1]: kj · product/WF-P09 · d4d1ce4a76b1
[^2]: kj · journey/WF-J04 · 292f135b2287

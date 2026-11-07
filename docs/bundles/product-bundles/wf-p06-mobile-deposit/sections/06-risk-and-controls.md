---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Mobile Deposit (Wells Fargo Mobile® Deposit): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "37a908556b761550d71caf2dd7a1b0206e60f714803cb66699420af74df3ae43",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Mobile Deposit (Wells Fargo Mobile® Deposit) — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

None recorded in this study.[^1]

## Exception paths

- `WF-J13` · Ineligible check (international, money order, duplicate, illegible MICR): Rejected at capture/processing → Deposit at branch/ATM[^2]
- `WF-J13` · Hold: Notification with release date → [^2]
- `WF-J13` · Returned check: Written notice by mail; funds reversed → [^2]
- `WF-J13` · Community: capture failures/crashes reported in app reviews: Retry; reinstall → [^2]
- `WF-J19` · Returned check: Mail notice; view returned checks online → [^3]

[^1]: kj · product/WF-P06 · aa0e6fda3732
[^2]: kj · journey/WF-J13 · e4ae53b47a45
[^3]: kj · journey/WF-J19 · 2f91942d8e13

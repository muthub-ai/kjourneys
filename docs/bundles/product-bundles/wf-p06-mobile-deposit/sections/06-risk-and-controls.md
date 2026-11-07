---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Mobile Deposit (Wells Fargo Mobile® Deposit): security and exception gaps, fail points, exception paths and controls",
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
  "content_sha256": "406bc391120b9d5b4a90a4f813e005226d8f7250f5e30aaa1420856105ec5ae1",
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

[^1]: kj · product/WF-P06 · 7447c97a0fac
[^2]: kj · journey/WF-J13 · 0dcdd11b8e8d
[^3]: kj · journey/WF-J19 · 2d1ad618854b

---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Direct Pay for Business: security and exception gaps, fail points, exception paths and controls",
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
  "content_sha256": "26bfa85626250f4f5dd95c4192e32d9a34d4300bf237df1c749c0067a55d2e97",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — risk and controls

## Security, trust and exception gaps

- **medium** · Returned ACH, failed validation and NSF handling are not published (UNKNOWN).[^1]

## Fail points along the journeys

- `WF-J16` M10 · Cancel/edit rules for scheduled Direct Pay payments not documented[^2]

## Exception paths

- `WF-J16` · Payee validation fails / wrong routing: Payee not active; FAQ warns check routing numbers may not support ACH → Correct and re-validate[^3]
- `WF-J16` · Returned ACH credit: UNKNOWN — not published → [^3]
- `WF-J16` · Unauthorized payment on business account: Call 1-866-867-5568; non-Reg E → [^3]

[^1]: kj · finding/GAP-WF-0029 · c7d7360df8f3
[^2]: kj · step/WF-J16#M10 · 333fd6d5dbcc
[^3]: kj · journey/WF-J16 · 67eed586f4fc

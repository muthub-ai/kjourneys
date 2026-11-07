---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "ExpressSend®: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "16d32bcaa6e602f81ed942e6f0d05fce6518d63cb3cccf1480e00a7a6f970727",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ExpressSend® — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

- `WF-J12` M02 · The web hub item routes to the app; no web-initiated flow was offered.[^2]
- `WF-J12` M09 · Two parallel service tracks with different channels and labels[^3]

## Exception paths

- `WF-J12` · Cash pickup unavailable (disaster, currency, security): Delay; call 1-800-556-0605 → [^4]
- `WF-J12` · Not picked up in 15 days: Auto-canceled; refund incl. fees → [^4]
- `WF-J12` · Cancel within 30 min: Full refund in 3 business days → [^4]
- `WF-J12` · Error/dispute: 180-day notice; 90-day investigation → [^4]

[^1]: kj · product/WF-P05 · 4247b60967aa
[^2]: kj · step/WF-J12#M02 · 9d6bbabdc09e
[^3]: kj · step/WF-J12#M09 · 9ce0d2fd3d00
[^4]: kj · journey/WF-J12 · 94fc27116502

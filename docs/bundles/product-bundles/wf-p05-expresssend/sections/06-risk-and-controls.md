---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "ExpressSend®: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "34b520cefe6f47a0b6a6c44fbdb61957a4221414c74ac2fda849835c8b7cd3b3",
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

[^1]: kj · product/WF-P05 · 0e61b73c4811
[^2]: kj · step/WF-J12#M02 · a7d5a7ed6de3
[^3]: kj · step/WF-J12#M09 · 9907c40cd56c
[^4]: kj · journey/WF-J12 · 98b1c3096cb7

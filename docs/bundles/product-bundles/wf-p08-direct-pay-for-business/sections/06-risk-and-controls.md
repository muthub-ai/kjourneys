---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Direct Pay for Business: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "2dd77f5c25ab2d631fa0e96055c46c5cf81af0e735b74ab85d76e5ef517b1568",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — risk and controls

## Security, trust and exception gaps

- **medium** · Returned ACH credits from the payee's bank and Same Day ACH are not published; second-wave evidence closes only part of the gap — insufficient funds ('we may either decline the transfer' or complete it and overdraw), payment by account number only with no name check, and rejection notices are now published in the Direct Pay Agreement (S970).[^1]

## Fail points along the journeys

- `WF-J16` M10 · Cancel/edit rules for scheduled Direct Pay payments not documented[^2]

## Exception paths

- `WF-J16` · Payee validation fails / wrong routing: Payee not active; FAQ warns check routing numbers may not support ACH → Correct and re-validate[^3]
- `WF-J16` · Returned ACH credit: UNKNOWN — not published → [^3]
- `WF-J16` · Unauthorized payment on business account: Call 1-866-867-5568; non-Reg E → [^3]
- `WF-J16` · Insufficient available funds in the Direct Pay Funding Account on the Send On Date: Payment may be declined, or completed and the account overdrawn → Fund the account and resubmit; WF 'will attempt to notify you of any rejected payment on or before the Pay By Date'[^3]

[^1]: kj · finding/GAP-WF-0028 · 631690a78ab9
[^2]: kj · step/WF-J16#M10 · cceea2e0b8f5
[^3]: kj · journey/WF-J16 · 38a8b7c0348a

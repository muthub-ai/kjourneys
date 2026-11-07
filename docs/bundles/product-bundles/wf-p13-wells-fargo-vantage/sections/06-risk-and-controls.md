---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "7ed92c2a21aed765f57caf0af4479be2f02fbc0f53351831a64c8e69583e1d95",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — risk and controls

## Security, trust and exception gaps

- **low** · Fallback when a receiver is unreachable on both rails is undocumented.[^1]

## Fail points along the journeys

- `WF-J22` M01 · Requires developer integration (mutual TLS, OAuth2 key rotation every 24 hours)[^2]

## Exception paths

- `WF-J20` · Unauthorized ACH debit: Alert; pay/return decision → [^3]
- `WF-J21` · BEC / changed instructions: Call 800-289-3557; holds/flags → [^4]
- `WF-J22` · Receiver not reachable on either rail: Fallback rail/ACH UNKNOWN → [^5]
- `WF-J22` · Creditor routing number not instant-payments enabled, participant unavailable, or rail INACTIVE: Verify-routing-number call returns instant_payments_enabled=NO / participant_available=NO / payment_rail=INACTIVE; client should not submit the credit transfer → Re-check later or use another rail[^5]
- `WF-J22` · Credit transfer REJECTED by network or receiving bank: status REJECTED with code IN01/IN02/MM20/MM21 or NARR (free-form text from the receiving bank) → Contact Gateway Customer Support; retry only after guidance[^5]
- `WF-J23` · File rejects: UNKNOWN → [^6]
- `WF-J25` · Capture failures (community reviews): Retry → [^7]

[^1]: kj · finding/GAP-WF-0034 · 11d66ca955c7
[^2]: kj · step/WF-J22#M01 · 6d15965dc645
[^3]: kj · journey/WF-J20 · aed31b6fcb25
[^4]: kj · journey/WF-J21 · f36035bd9611
[^5]: kj · journey/WF-J22 · 1ca66149586f
[^6]: kj · journey/WF-J23 · d8e43801cb3c
[^7]: kj · journey/WF-J25 · 4d80482f689e

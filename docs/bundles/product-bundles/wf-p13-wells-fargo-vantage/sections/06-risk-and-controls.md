---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "31c8a088402a53a411eae2cbe6f3cc9a80e82af91704e51010de7f50c9f4e4d5",
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

[^1]: kj · finding/GAP-WF-0035 · 0a84506564fc
[^2]: kj · step/WF-J22#M01 · fd9fa0deae21
[^3]: kj · journey/WF-J20 · a09dfa7d417c
[^4]: kj · journey/WF-J21 · a9e16e59c03f
[^5]: kj · journey/WF-J22 · 30a8718f1eaf
[^6]: kj · journey/WF-J23 · 194624059efa
[^7]: kj · journey/WF-J25 · 982023d3f4b5

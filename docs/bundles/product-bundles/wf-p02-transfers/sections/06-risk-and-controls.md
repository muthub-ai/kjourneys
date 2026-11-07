---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Transfers (Transfer Money): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "362c44e4f71fb78ccd9469838d9720cfa49453cc63542ace2036ab3f384bd3f6",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — risk and controls

## Security, trust and exception gaps

- **low** · Same-day internal transfers cannot be cancelled; a wrong-account transfer must be reversed manually.[^1]
- **low** · Observed: 'Set up for transfers' on an already-verified payments-only external account completed with one click and no confirmation step, immediately enabling outbound transfers to that account.[^2]

## Fail points along the journeys

- `WF-J06` M03 · No aggregator / credential-login option is offered; routing and account numbers must be keyed.[^3]
- `WF-J06` M05 · Only micro-deposit/proof-of-ownership verification (1–3 business days); no instant (aggregator/credential-based) verification is offered on any public page. Meanwhile the unverified external account 'may be able to' be used to pay Wells Fargo credit accounts.[^4]
- `WF-J06` M06 · A single click changes the account's capability with no confirmation step — convenient, but easy to trigger unintentionally.[^5]

## Exception paths

- `WF-J05` · Insufficient funds: WF decides at its discretion to pay (overdraft), or decline → [^6]
- `WF-J05` · Wrong account chosen on immediate transfer: Cannot cancel; must reverse manually → Customer makes offsetting transfer[^6]
- `WF-J06` · External account verification fails: Cannot transfer; can still pay WF credit accounts from it → Customer retries/provides proof[^7]
- `WF-J06` · ACH return (NSF/closed account at other bank): Transfer fails; funds not credited → [^7]
- `WF-J06` · Suspicious/irregular transfer: Extended hold → [^7]
- `WF-J06` · Customer wants faster than standard delivery or instant external-account verification: No instant verification option; verification 1–3 business days; 'Depending on your history of transfer activity, expedited transfer options may be available to you' (not user-selectable up front) → Wait for standard verification/delivery or use Zelle/wire[^7]

[^1]: kj · finding/GAP-WF-0033 · deb4b6489d31
[^2]: kj · finding/GAP-WF-0037 · 966f77825654
[^3]: kj · step/WF-J06#M03 · 17cb738f04bf
[^4]: kj · step/WF-J06#M05 · e75982fd09d5
[^5]: kj · step/WF-J06#M06 · 0e78091bd7f6
[^6]: kj · journey/WF-J05 · 961155a3b7eb
[^7]: kj · journey/WF-J06 · ee855eb97a21

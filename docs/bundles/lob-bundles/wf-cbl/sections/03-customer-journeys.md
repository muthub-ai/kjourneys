---
{
 "type": "lob-bundle/section",
 "title": "Customer journeys",
 "description": "Customer journeys delivered by Consumer Banking and Lending's products",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cbl",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cbl",
  "content_sha256": "0a3e34a2c97f76b0b9cea41faae6d3102777f78a843f7b4ccd91f481431f650b",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Consumer Banking and Lending — customer journeys

- **Consumer links an external account and pushes money out** — delivered by `WF-J06`[^1][^2]
- **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** — delivered by `WF-J16`, `WF-J17`, `WF-J18`[^3][^4][^5][^6]
- **Consumer activates eBills and manages autopay** — delivered by `WF-J08`[^7][^8]
- **Consumer adds a payee and pays a bill** — delivered by `WF-J07`[^9][^10]
- **Consumer receives an instant credit and pays a biller Request for Payment (payer side)** — delivered by `WF-J09`, `WF-J15`[^11][^12][^13]
- **Consumer moves money between own accounts** — delivered by `WF-J05`[^14][^15]
- **Consumer deposits a check with the mobile app** — delivered by `WF-J13`[^16][^17]
- **Consumer sends a cross-border remittance (account credit or cash pickup)** — delivered by `WF-J12`[^18][^19]
- **Consumer sends a domestic wire to a new recipient** — delivered by `WF-J10`[^20][^21]
- **Consumer sends an international wire in foreign currency** — delivered by `WF-J11`[^22][^23]
- **Consumer sends money to a new recipient with Zelle (mobile-first)** — delivered by `WF-J01`, `WF-J04`, `WF-J28`, `WF-J29`[^24][^25][^26][^27][^28]
- **Consumer requests money or splits a bill with Zelle** — delivered by `WF-J02`[^29][^30]
- **Small business gets paid with a Zelle tag/QR and pays vendors under controls** — delivered by `WF-J03`[^31][^32]

[^1]: kj · customer-journey/CJ-ACH-EXT-SEND · 74e77a0ea302
[^2]: kj · journey/WF-J06 · ee855eb97a21
[^3]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · e1251bb592b3
[^4]: kj · journey/WF-J17 · adbdce251781
[^5]: kj · journey/WF-J18 · 7f1916a52a55
[^6]: kj · journey/WF-J16 · 67eed586f4fc
[^7]: kj · customer-journey/CJ-BILLPAY-EBILL-MANAGE · 10f51b6b94d0
[^8]: kj · journey/WF-J08 · 3a462c0bcc44
[^9]: kj · customer-journey/CJ-BILLPAY-SEND · 2108d8b1b57d
[^10]: kj · journey/WF-J07 · add9e5f0ca96
[^11]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · faad41fab3cd
[^12]: kj · journey/WF-J09 · 92c2140a6c2a
[^13]: kj · journey/WF-J15 · e61f32bb5fb1
[^14]: kj · customer-journey/CJ-INTERNAL-TRANSFER · 2d8719aff17e
[^15]: kj · journey/WF-J05 · 961155a3b7eb
[^16]: kj · customer-journey/CJ-MOBILE-DEPOSIT · 6dd6d232e8bd
[^17]: kj · journey/WF-J13 · e4ae53b47a45
[^18]: kj · customer-journey/CJ-REMITTANCE-SEND · e13395512089
[^19]: kj · journey/WF-J12 · 94fc27116502
[^20]: kj · customer-journey/CJ-WIRE-DOM-CONSUMER-SEND · 5229e78a1d68
[^21]: kj · journey/WF-J10 · 47452d55448b
[^22]: kj · customer-journey/CJ-WIRE-INTL-CONSUMER-SEND · eee82a62d089
[^23]: kj · journey/WF-J11 · e4ed66bc72f0
[^24]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 54cdbe9360ea
[^25]: kj · journey/WF-J01 · 5459e5785f84
[^26]: kj · journey/WF-J28 · b20fda0a115f
[^27]: kj · journey/WF-J29 · d718f795aee2
[^28]: kj · journey/WF-J04 · 292f135b2287
[^29]: kj · customer-journey/CJ-ZELLE-REQUEST · ff349a4a3d24
[^30]: kj · journey/WF-J02 · 14bc08a80f04
[^31]: kj · customer-journey/CJ-ZELLE-SMB-RECEIVE · 1a1ab5a1e86e
[^32]: kj · journey/WF-J03 · b89c841e1309

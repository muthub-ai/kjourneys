---
{
 "type": "lob-bundle/section",
 "title": "Customer journeys",
 "description": "Customer journeys delivered by Consumer Banking and Lending's products",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cbl",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cbl",
  "content_sha256": "af517867b1c0e88ae8c9e3834bdaa2e8aa4763e756133b0bc408e9cbd47ada77",
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

[^1]: kj · customer-journey/CJ-ACH-EXT-SEND · 2ec667c942b3
[^2]: kj · journey/WF-J06 · 5ac14c85b11a
[^3]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11
[^4]: kj · journey/WF-J17 · 161d120bfa87
[^5]: kj · journey/WF-J18 · da9c57fe16e4
[^6]: kj · journey/WF-J16 · 38a8b7c0348a
[^7]: kj · customer-journey/CJ-BILLPAY-EBILL-MANAGE · 24c5b603c3ec
[^8]: kj · journey/WF-J08 · 43861b5c7ba6
[^9]: kj · customer-journey/CJ-BILLPAY-SEND · ebd10948d1ce
[^10]: kj · journey/WF-J07 · 8270f6fa66c5
[^11]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · f0a2b8d96952
[^12]: kj · journey/WF-J09 · 57b4cafbf531
[^13]: kj · journey/WF-J15 · c6f5929e58f1
[^14]: kj · customer-journey/CJ-INTERNAL-TRANSFER · edfddfd7c154
[^15]: kj · journey/WF-J05 · 8cc99d20c29f
[^16]: kj · customer-journey/CJ-MOBILE-DEPOSIT · c134e8cc0f1e
[^17]: kj · journey/WF-J13 · 0dcdd11b8e8d
[^18]: kj · customer-journey/CJ-REMITTANCE-SEND · c2ae3445c9e7
[^19]: kj · journey/WF-J12 · 98b1c3096cb7
[^20]: kj · customer-journey/CJ-WIRE-DOM-CONSUMER-SEND · ba0b56b8b7ed
[^21]: kj · journey/WF-J10 · ca29755fbe66
[^22]: kj · customer-journey/CJ-WIRE-INTL-CONSUMER-SEND · 556725478191
[^23]: kj · journey/WF-J11 · 5759e78f0c18
[^24]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 1f6b6a0e7521
[^25]: kj · journey/WF-J01 · c3b8e132fd5c
[^26]: kj · journey/WF-J28 · cf400c417393
[^27]: kj · journey/WF-J29 · f76130105e87
[^28]: kj · journey/WF-J04 · 2e981edf18c3
[^29]: kj · customer-journey/CJ-ZELLE-REQUEST · cda300f4d27d
[^30]: kj · journey/WF-J02 · 2eca5861046f
[^31]: kj · customer-journey/CJ-ZELLE-SMB-RECEIVE · dd3d94ee596e
[^32]: kj · journey/WF-J03 · 558dd3d0215c

---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Digital Wires (Wire Money) delivers",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "a2574a63516a3d97a1fdd6e4c998f2d089e4050e0ad361260fab4e853caa9551",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital Wires (Wire Money) — customers and channels

Segments: consumer, small-business. Channels: mobile-app, web, branch.[^1]

Network or vendor: Fedwire / SWIFT (WFBIUS6S).[^1]

## Customer journeys this product delivers

- **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** (small_business, send) — 10 best-practice steps[^2]
- **Consumer sends a domestic wire to a new recipient** (consumer, send) — 9 best-practice steps[^3]
- **Consumer sends an international wire in foreign currency** (consumer, send) — 9 best-practice steps[^4]

## Who the journeys are for

- `WF-J10` Consumer sends a domestic wire online (Digital Wires) — persona: Consumer closing on a home / paying a contractor; goal: “Send a large same-day payment to a specific bank account”[^5]
- `WF-J11` Consumer sends an international wire in foreign currency — persona: Consumer paying overseas tuition; goal: “Send money abroad with a locked FX rate and known delivery amount”[^6]
- `WF-J18` Small business sends a foreign-currency wire from Business Online — persona: Importer paying an overseas supplier; goal: “Pay a supplier in their currency with a locked rate”[^7]

[^1]: kj · product/WF-P04 · 728ab1540360
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11
[^3]: kj · customer-journey/CJ-WIRE-DOM-CONSUMER-SEND · ba0b56b8b7ed
[^4]: kj · customer-journey/CJ-WIRE-INTL-CONSUMER-SEND · 556725478191
[^5]: kj · journey/WF-J10 · ca29755fbe66
[^6]: kj · journey/WF-J11 · 5759e78f0c18
[^7]: kj · journey/WF-J18 · da9c57fe16e4

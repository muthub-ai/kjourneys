---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Bill Pay (Online Bill Pay / Business Bill Pay) delivers",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "8b890a6a9f354bc360148f88cad86686e611c1b8fcda2f132bfc3711659e5094",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Bill Pay (Online Bill Pay / Business Bill Pay) — customers and channels

Segments: consumer, small-business. Channels: mobile-app, web, voice-chat-assistant.[^1]

Network or vendor: Wells Fargo (processor not disclosed); RTP network (The Clearing House) for instant payments.[^1]

## Customer journeys this product delivers

- **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** (small_business, send) — 10 best-practice steps[^2]
- **Consumer activates eBills and manages autopay** (consumer, send) — 9 best-practice steps[^3]
- **Consumer adds a payee and pays a bill** (consumer, send) — 9 best-practice steps[^4]
- **Consumer receives an instant credit and pays a biller Request for Payment (payer side)** (consumer, receive) — 9 best-practice steps[^5]

## Who the journeys are for

- `WF-J07` Consumer adds a payee and pays a bill (electronic or check) — persona: Consumer paying a utility; goal: “Pay a bill without writing a check and know it will arrive on time”[^6]
- `WF-J08` Consumer activates eBills and sets auto pay — persona: Consumer automating card/utility bills; goal: “Never miss a due date; pay the exact statement amount automatically”[^7]
- `WF-J09` Consumer pays a Request for Payment instantly in Bill Pay (RTP instant payment, mobile) — persona: Consumer paying a participating biller (e.g., utility, loan servicer) on the due date; goal: “Pay a bill right now and have the biller see it within seconds”[^8]
- `WF-J17` Small business pays an invoice with Business Bill Pay funded by a business credit card — persona: Small business owner managing cash flow; goal: “Pay a supplier while extending float on a business card”[^9]

[^1]: kj · product/WF-P03 · 0c4750f70904
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11
[^3]: kj · customer-journey/CJ-BILLPAY-EBILL-MANAGE · 24c5b603c3ec
[^4]: kj · customer-journey/CJ-BILLPAY-SEND · ebd10948d1ce
[^5]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · f0a2b8d96952
[^6]: kj · journey/WF-J07 · 8270f6fa66c5
[^7]: kj · journey/WF-J08 · 43861b5c7ba6
[^8]: kj · journey/WF-J09 · 57b4cafbf531
[^9]: kj · journey/WF-J17 · 161d120bfa87

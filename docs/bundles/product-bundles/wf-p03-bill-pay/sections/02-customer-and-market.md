---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Bill Pay (Online Bill Pay / Business Bill Pay) delivers",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "9236637587c7cca04833559a33305c873932fe0897a18237c384d5b85e44e382",
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

[^1]: kj · product/WF-P03 · b839aacb8026
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · 18172095afc9
[^3]: kj · customer-journey/CJ-BILLPAY-EBILL-MANAGE · 10f51b6b94d0
[^4]: kj · customer-journey/CJ-BILLPAY-SEND · 2108d8b1b57d
[^5]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · faad41fab3cd
[^6]: kj · journey/WF-J07 · add9e5f0ca96
[^7]: kj · journey/WF-J08 · 3a462c0bcc44
[^8]: kj · journey/WF-J09 · 92c2140a6c2a
[^9]: kj · journey/WF-J17 · adbdce251781

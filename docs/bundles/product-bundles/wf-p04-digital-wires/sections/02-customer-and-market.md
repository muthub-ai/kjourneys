---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Digital Wires (Wire Money) delivers",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "ec9c77c27c72a53ef8c62596c4795ab545ae6b9ef215eb9bc571f783b8272dee",
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

[^1]: kj · product/WF-P04 · 7ae69c334eed
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · 18172095afc9
[^3]: kj · customer-journey/CJ-WIRE-DOM-CONSUMER-SEND · 5229e78a1d68
[^4]: kj · customer-journey/CJ-WIRE-INTL-CONSUMER-SEND · eee82a62d089
[^5]: kj · journey/WF-J10 · 47452d55448b
[^6]: kj · journey/WF-J11 · e4ed66bc72f0
[^7]: kj · journey/WF-J18 · 7f1916a52a55

---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Transfers (Transfer Money) delivers",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "1ef6277323245397d461fab790ee4201d1bdd9cf9a1791baf6972b1baad06f9c",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — customers and channels

Segments: consumer, small-business. Channels: mobile-app, web, voice-chat-assistant, atm, phone.[^1]

Network or vendor: Wells Fargo (ACH via Nacha for external).[^1]

## Customer journeys this product delivers

- **Consumer links an external account and pushes money out** (consumer, send) — 9 best-practice steps[^2]
- **Consumer moves money between own accounts** (consumer, send) — 9 best-practice steps[^3]

## Who the journeys are for

- `WF-J05` Consumer transfers between own Wells Fargo accounts (mobile), one-time and recurring — persona: Consumer topping up checking from savings; goal: “Move money instantly to cover a purchase or automate savings”[^4]
- `WF-J06` Consumer links an external bank account and transfers money ('Bank-to-bank transfers') — persona: Consumer moving savings from an online bank; goal: “Pull/push money between my Wells Fargo and another bank's account”[^5]

[^1]: kj · product/WF-P02 · 9eb25008fe7d
[^2]: kj · customer-journey/CJ-ACH-EXT-SEND · 74e77a0ea302
[^3]: kj · customer-journey/CJ-INTERNAL-TRANSFER · 2d8719aff17e
[^4]: kj · journey/WF-J05 · 961155a3b7eb
[^5]: kj · journey/WF-J06 · ee855eb97a21

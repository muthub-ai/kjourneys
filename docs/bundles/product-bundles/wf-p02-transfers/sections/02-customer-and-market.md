---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Transfers (Transfer Money) delivers",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "6515f06131b5376f7d56765de900857b08056e30446b94b920bf7eb810e900be",
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

[^1]: kj · product/WF-P02 · 0b29dca0b27f
[^2]: kj · customer-journey/CJ-ACH-EXT-SEND · 2ec667c942b3
[^3]: kj · customer-journey/CJ-INTERNAL-TRANSFER · edfddfd7c154
[^4]: kj · journey/WF-J05 · 8cc99d20c29f
[^5]: kj · journey/WF-J06 · 5ac14c85b11a

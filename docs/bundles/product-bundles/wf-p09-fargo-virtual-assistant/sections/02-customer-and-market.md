---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Fargo® virtual assistant delivers",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "d681fa2244671ea0b41396e167e8a458f65093ee77da5bf7905ad7a84c05988f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — customers and channels

Segments: consumer. Channels: voice-chat-assistant.[^1]

Network or vendor: Wells Fargo (Google Cloud Dialogflow/Gemini per press — not fetched; UNKNOWN here).[^1]

## Customer journeys this product delivers

- **Consumer sends money to a new recipient with Zelle (mobile-first)** (consumer, send) — 11 best-practice steps[^2]

## Who the journeys are for

- `WF-J04` Consumer sends Zelle® money by voice/chat with Fargo® — persona: Busy consumer using voice in the app; goal: “Pay a stored contact hands-free”[^3]

[^1]: kj · product/WF-P09 · 87601a523c62
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 54cdbe9360ea
[^3]: kj · journey/WF-J04 · 292f135b2287

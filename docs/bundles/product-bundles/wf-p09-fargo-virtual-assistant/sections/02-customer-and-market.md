---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Fargo® virtual assistant delivers",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "3b789f0b29643ba0db6e3a3419c633349af35795272a30d184fe9f4c8a3dc323",
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

[^1]: kj · product/WF-P09 · d4d1ce4a76b1
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 54cdbe9360ea
[^3]: kj · journey/WF-J04 · 292f135b2287

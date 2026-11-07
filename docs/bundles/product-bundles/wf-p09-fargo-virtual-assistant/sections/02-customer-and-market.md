---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Fargo® virtual assistant delivers",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "85017001605120eae8fe9706f16435f23bb031351ac24e0e2819d38488dbc71d",
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

[^1]: kj · product/WF-P09 · 4787881df475
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 1f6b6a0e7521
[^3]: kj · journey/WF-J04 · 2e981edf18c3

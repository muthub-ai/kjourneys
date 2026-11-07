---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) delivers",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "67068440375e202c00a7e7932ddd54bd267b74f6fcaffb8ac851856a5c2a42ea",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — customers and channels

Segments: consumer. Channels: mobile-app, web.[^1]

Network or vendor: Nacha ACH; RTP (TCH); FedNow (Federal Reserve).[^1]

## Customer journeys this product delivers

- **Consumer receives an instant credit and pays a biller Request for Payment (payer side)** (consumer, receive) — 9 best-practice steps[^2]

## Who the journeys are for

- `WF-J15` Consumer receives an RTP®/FedNow® instant payment or early ACH direct deposit — persona: Gig worker paid by instant payout; salaried employee; goal: “Get paid instantly / early and know when funds land”[^3]

[^1]: kj · product/WF-P12 · d73da35d0cb8
[^2]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · faad41fab3cd
[^3]: kj · journey/WF-J15 · e61f32bb5fb1

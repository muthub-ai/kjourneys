---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) delivers",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "8d56e781a1414f1fc3bf0c6430454e5737e96c02a44d34558d6b105925c9d00a",
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

[^1]: kj · product/WF-P12 · 932e654a57de
[^2]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · f0a2b8d96952
[^3]: kj · journey/WF-J15 · c6f5929e58f1

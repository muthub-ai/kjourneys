---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) journey: steps, stages, channels and MI's assessment",
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
  "content_sha256": "7f8e28df74ac7f14a47a79b103f769a19ac71b8e6eaab8c191ea8cdf899735fd",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — journeys and experience

## `WF-J15` Consumer receives an RTP®/FedNow® instant payment or early ACH direct deposit

10 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web. Status tracking: Account Activity / Available Balance.[^1]

Delivers the customer journey **Consumer receives an instant credit and pays a biller Request for Payment (payer side)** (linked by mi reference).[^1][^2]

MI assessment: Receive-side instant rails are live but invisible in marketing; Early Pay Day is competitive with peers.[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J15 · c6f5929e58f1
[^2]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · f0a2b8d96952

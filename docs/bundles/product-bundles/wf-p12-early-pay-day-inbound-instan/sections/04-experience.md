---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "2bfc17955ae01126b8a49ce764ee04cde1c5cd83d3898c9469a0e5c52a2d7c9d",
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

[^1]: kj · journey/WF-J15 · e61f32bb5fb1
[^2]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · faad41fab3cd

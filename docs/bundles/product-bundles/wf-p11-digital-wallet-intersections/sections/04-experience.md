---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p11-digital-wallet-intersections",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P11",
  "line_of_business": "wf-cbl",
  "content_sha256": "f5831a87c786dbbe759e25065930f93a743950bca058dea5e057f679ce64efbc",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM) — journeys and experience

## `WF-J27` Consumer activates Paze and links a card to PayPal from the Wells Fargo app (wallet intersections)

10 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web. Status tracking: Card Settings > Digital Wallet.[^1]

MI assessment: WF is a Paze founding-tier participant; no published guidance on funding Venmo/Apple Cash from WF accounts (gap vs. peers' help centers).[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J27 · 25ca42f849dc

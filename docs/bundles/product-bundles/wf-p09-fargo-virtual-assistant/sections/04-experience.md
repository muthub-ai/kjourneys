---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Fargo® virtual assistant journey: steps, stages, channels and MI's assessment",
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
  "content_sha256": "e1c415e1761d1054bc75ae469c13a11515248ae15081c662b7f08a369dd5ff7b",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — journeys and experience

## `WF-J04` Consumer sends Zelle® money by voice/chat with Fargo®

9 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: voice-chat-assistant, mobile-app. Status tracking: 'Zelle® Activity' (24 months, sorted Completed vs Pending) and 'Scheduled' tab; 'Account Activity' (18 months searchable); Fargo 'View Zelle transactions'.[^1]

Delivers the customer journey **Consumer sends money to a new recipient with Zelle (mobile-first)** (linked by mi reference).[^1][^2]

MI assessment: Unique among top-4: an assistant that initiates Zelle sends. Exact confirmation UX unpublished (INFERRED).[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J04 · 292f135b2287
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 54cdbe9360ea

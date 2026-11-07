---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Fargo® virtual assistant journey: steps, stages, channels and MI's assessment",
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
  "content_sha256": "6dc420e643ef1a25ecc1c45e4fdb231d053b8b0c298cf2f5ec942c6f7744266d",
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

[^1]: kj · journey/WF-J04 · 2e981edf18c3
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 1f6b6a0e7521

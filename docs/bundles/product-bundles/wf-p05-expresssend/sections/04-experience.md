---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each ExpressSend® journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "f7f322c4839a076803fb83e449317b4f76144c602ae14e198256a4e8021dd67e",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ExpressSend® — journeys and experience

## `WF-J12` Consumer sends an ExpressSend® remittance for cash pickup or account credit (mobile)

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app. Status tracking: Pay & Transfer > Transfer Internationally > Activity.[^1]

Delivers the customer journey **Consumer sends a cross-border remittance (account credit or cash pickup)** (linked by mi reference).[^1][^2]

MI assessment: Only top-4 bank with a proprietary cash-pickup remittance product; recently moved to app-only (Jul 2026 release notes), with no recurring or branch support — a trade-off for the core Hispanic customer base.[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J12 · 94fc27116502
[^2]: kj · customer-journey/CJ-REMITTANCE-SEND · e13395512089

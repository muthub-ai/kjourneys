---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each ExpressSend® journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "3b7ebbf278da92863e2d44eb53f2de3502f7cc4c76479dbb62d19e9039e7f719",
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

[^1]: kj · journey/WF-J12 · 98b1c3096cb7
[^2]: kj · customer-journey/CJ-REMITTANCE-SEND · c2ae3445c9e7

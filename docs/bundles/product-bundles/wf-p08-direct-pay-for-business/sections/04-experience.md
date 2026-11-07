---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Direct Pay for Business journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "a571cd771981329a02a4ebc404b37a1bd73056977c76b6820907e330ef544655",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — journeys and experience

## `WF-J16` Small business enrolls in Direct Pay, adds payees and runs an ACH payroll/vendor payment with dual control

13 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web. Status tracking: Direct Pay Payments list / Business Online activity.[^1]

Delivers the customer journey **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** (linked by mi reference).[^1][^2]

MI assessment: Genuine SMB ACH origination with four-tier access model (dual control) inside Business Online — stronger than most peers' SMB offerings; weaknesses: desktop-only, next-day only (no Same Day ACH option documented), monthly fee, no published exception handling.[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J16 · 67eed586f4fc
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · 18172095afc9

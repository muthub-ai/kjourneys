---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Direct Pay for Business journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "66e75ad787947d14ccf656ab4dca771e6b70860c2a9d29e26fd7c39b651d7cdb",
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
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · e1251bb592b3

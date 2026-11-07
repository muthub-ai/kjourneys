---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Direct Pay for Business journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "955168872e46b47ffd822f676b84ecc64e6b34ea4969e48b752a97d24fe53dd4",
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

[^1]: kj · journey/WF-J16 · 38a8b7c0348a
[^2]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11

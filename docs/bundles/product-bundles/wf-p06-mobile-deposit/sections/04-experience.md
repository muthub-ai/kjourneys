---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Mobile Deposit (Wells Fargo Mobile® Deposit) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "f23fc31004c87bcff9564ccfbac79e82ed7be7d7b43210e20b94b819a7d48621",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Mobile Deposit (Wells Fargo Mobile® Deposit) — journeys and experience

## `WF-J13` Consumer deposits a check with Mobile Deposit

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, atm, branch. Status tracking: Account Activity; confirmation screen/email show deposit credit date.[^1]

Delivers the customer journey **Consumer deposits a check with the mobile app** (linked by mi reference).[^1][^2]

MI assessment: Complete, well-documented flow with explicit limit visibility and three-channel confirmation.[^1]

## `WF-J19` Small business deposits checks via mobile and manages delegate access

10 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web, atm. Status tracking: Account activity / deposit details.[^3]

MI assessment: Delegate model is simple (two levels) — adequate for micro-business, light for growing SMBs.[^3]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1][^3]

[^1]: kj · journey/WF-J13 · 0dcdd11b8e8d
[^2]: kj · customer-journey/CJ-MOBILE-DEPOSIT · c134e8cc0f1e
[^3]: kj · journey/WF-J19 · 2d1ad618854b

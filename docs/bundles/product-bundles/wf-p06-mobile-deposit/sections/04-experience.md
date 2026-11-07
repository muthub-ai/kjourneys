---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Mobile Deposit (Wells Fargo Mobile® Deposit) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "f4990005c072adee1ea9bba3e0f4114e82fcb6c1763ad4d4981a85c8bc7f68f7",
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

[^1]: kj · journey/WF-J13 · e4ae53b47a45
[^2]: kj · customer-journey/CJ-MOBILE-DEPOSIT · 6dd6d232e8bd
[^3]: kj · journey/WF-J19 · 2f91942d8e13

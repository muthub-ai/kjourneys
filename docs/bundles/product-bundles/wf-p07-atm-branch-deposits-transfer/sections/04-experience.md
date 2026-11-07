---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each ATM & branch deposits/transfers journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p07-atm-branch-deposits-transfer",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P07",
  "line_of_business": "wf-cbl",
  "content_sha256": "62afbdfd10b8104f7b13166eef162cf20e6760821ead14fb12de1df6f5eb8511",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ATM & branch deposits/transfers — journeys and experience

## `WF-J14` Consumer deposits cash/check and transfers at a Wells Fargo ATM (incl. card-free wallet access)

9 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: atm, branch. Status tracking: Receipt; Account Activity.[^1]

MI assessment: Envelope-free, wallet tap access and e-receipts are table stakes delivered well.[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J14 · d4a1b057205c

---
{
 "type": "product-bundle/section",
 "title": "Operating model",
 "description": "ATM & branch deposits/transfers: owning line of business, supporting applications and ownership to assign",
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
  "bundle_id": "wf-p07-atm-branch-deposits-transfer",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P07",
  "line_of_business": "wf-cbl",
  "content_sha256": "fe285bf992850bee4c68d84fbb2b8e60303a73f7a75f7fbeb0e3576a4f0d5fe0",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ATM & branch deposits/transfers — operating model

Owning line of business: **Consumer Banking and Lending**, Consumer, Small and Business Banking.[^1][^2]

No application IDs are mapped to this product's journeys yet; they come from the application bundles of the systems that run it.[^3]

*Assessment:* Product owner, steward and approver are not assigned; set them in knowledge-source.json before this bundle is submitted for review.

[^1]: kj · assignment/WF-P07 · a7162a28f27a
[^2]: kj · lob/wf-cbl · 949b2dbdb1b9
[^3]: kj · product/WF-P07 · 60c66e3aae03

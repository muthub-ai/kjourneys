---
{
 "type": "product-bundle/section",
 "title": "Operating model",
 "description": "Direct Pay for Business: owning line of business, supporting applications and ownership to assign",
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
  "content_sha256": "ac712c23aa6dd9909064385cad125440aafacb072151e24f87817fb398659a4f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — operating model

Owning line of business: **Consumer Banking and Lending**, Consumer, Small and Business Banking.[^1][^2]

No application IDs are mapped to this product's journeys yet; they come from the application bundles of the systems that run it.[^3]

*Assessment:* Product owner, steward and approver are not assigned; set them in knowledge-source.json before this bundle is submitted for review.

[^1]: kj · assignment/WF-P08 · 59a2dcfc7280
[^2]: kj · lob/wf-cbl · 9bd65bef07df
[^3]: kj · product/WF-P08 · 3868912428e5

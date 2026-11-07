---
{
 "type": "lob-bundle/section",
 "title": "Operating model",
 "description": "Corporate and Investment Banking: assignments to confirm and ownership to assign",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cib",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cib",
  "content_sha256": "c7be23f27ad21c819cea9e8310ad903707bbbfc79785b4afc44d52d6d0f50039",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Corporate and Investment Banking — operating model

- Confirm: `WF-P13` Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — MI tags this product commercial. Wells Fargo reports treasury management and payments revenue in both Commercial Banking and Corporate and Investment Banking, so which one owns the product is a judgment, not a disclosure; Commercial Banking is assumed; small-business use (one sub-product) adds Consumer Banking and Lending. Confirm.[^1]
- Confirm: `WF-P14` Wells Fargo Gateway® APIs (developer portal) — MI tags this product commercial. Wells Fargo reports treasury management and payments revenue in both Commercial Banking and Corporate and Investment Banking, so which one owns the product is a judgment, not a disclosure; Commercial Banking is assumed. Confirm.[^2]
- Confirm: `WF-P15` Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — MI tags this product commercial. Wells Fargo reports treasury management and payments revenue in both Commercial Banking and Corporate and Investment Banking, so which one owns the product is a judgment, not a disclosure; Commercial Banking is assumed. Confirm.[^3]

*Assessment:* Line-of-business owner, steward and approver are not assigned; set them in knowledge-source.json.

[^1]: kj · assignment/WF-P13 · c64f59363a8c
[^2]: kj · assignment/WF-P14 · 3a904d805836
[^3]: kj · assignment/WF-P15 · 0dd0a5a36565

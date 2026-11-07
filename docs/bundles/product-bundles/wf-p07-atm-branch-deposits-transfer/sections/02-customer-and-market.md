---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys ATM & branch deposits/transfers delivers",
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
  "content_sha256": "b9e7e6ae5ef7f3b0a5ffc18fc523da53985e4c229b73fa881058f20121e00c6e",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ATM & branch deposits/transfers — customers and channels

Segments: consumer, small-business. Channels: atm, branch.[^1]

Network or vendor: Wells Fargo (~11,000–12,700 ATMs, ~4,600–4,800 branches).[^1]

## Customer journeys this product delivers

None recorded in this study.[^1]

## Who the journeys are for

- `WF-J14` Consumer deposits cash/check and transfers at a Wells Fargo ATM (incl. card-free wallet access) — persona: Consumer depositing cash tips; goal: “Deposit cash and move money without a branch visit”[^2]

[^1]: kj · product/WF-P07 · 60c66e3aae03
[^2]: kj · journey/WF-J14 · d4a1b057205c

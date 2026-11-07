---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p10-card-settings",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P10",
  "line_of_business": "wf-cbl",
  "content_sha256": "0f6d78fb2eb82d7b12ac5702bc896ec180ab80358412eb3f18f622eef8c5cf77",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

- `WF-J26` M07 · Card-off does not block recurring charges; no in-app 'cancel subscription' action evidenced[^2]

## Exception paths

- `WF-J26` · Recurring charge continues after card off: Charge posts → Contact merchant / dispute[^3]

[^1]: kj · product/WF-P10 · ae4ea79539a2
[^2]: kj · step/WF-J26#M07 · 2d88ebbb9775
[^3]: kj · journey/WF-J26 · 63eb2e769619

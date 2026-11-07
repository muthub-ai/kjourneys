---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p10-card-settings",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P10",
  "line_of_business": "wf-cbl",
  "content_sha256": "51dd0db624c3d1d5144539ff7a875e7535fdf408c13ab63e7360a0d54b6b6fe2",
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
- `WF-J26` M09 · Turning a card off does not stop previously authorized recurring payments (per Debit card FAQs), so 'card off' is not a subscription-cancel tool — customers must cancel with the merchant.[^3]

## Exception paths

- `WF-J26` · Recurring charge continues after card off: Charge posts → Contact merchant / dispute[^4]

[^1]: kj · product/WF-P10 · 5dc2c6e95e66
[^2]: kj · step/WF-J26#M07 · 597230b0233c
[^3]: kj · step/WF-J26#M09 · 246cfffacddb
[^4]: kj · journey/WF-J26 · 1e8e3f066822

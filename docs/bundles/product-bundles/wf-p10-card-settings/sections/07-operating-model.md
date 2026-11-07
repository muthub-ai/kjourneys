---
{
 "type": "product-bundle/section",
 "title": "Operating model",
 "description": "Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠: owning line of business, supporting applications and ownership to assign",
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
  "content_sha256": "6e584d2053141943780be428005c4b0a4747bf83e53ebd6a91b273b1e2bb8097",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ — operating model

Owning line of business: **Consumer Banking and Lending**, Consumer, Small and Business Banking.[^1][^2]

No application IDs are mapped to this product's journeys yet; they come from the application bundles of the systems that run it.[^3]

*Assessment:* Product owner, steward and approver are not assigned; set them in knowledge-source.json before this bundle is submitted for review.

[^1]: kj · assignment/WF-P10 · 61f49f4b4a83
[^2]: kj · lob/wf-cbl · 9bd65bef07df
[^3]: kj · product/WF-P10 · 5dc2c6e95e66

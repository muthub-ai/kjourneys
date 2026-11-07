---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys ATM & branch deposits/transfers delivers",
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
  "bundle_id": "wf-p07-atm-branch-deposits-transfer",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P07",
  "line_of_business": "wf-cbl",
  "content_sha256": "285669f47187a230dc5bc32416dac258b0d4f5702e5945f0f2a15ca0dba9f66e",
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

[^1]: kj · product/WF-P07 · 4fe5c088f5d6
[^2]: kj · journey/WF-J14 · 5120bc547ac2

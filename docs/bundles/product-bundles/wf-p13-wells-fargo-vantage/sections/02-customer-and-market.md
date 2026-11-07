---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) delivers",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "76f80eb08ba63cc7925902ff468a580635fecb83167312c091dd56414649ec9f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — customers and channels

Segments: commercial, small-business. Channels: api-treasury-portal, mobile-app.[^1]

Network or vendor: Wells Fargo.[^1]

## Customer journeys this product delivers

- **Commercial instant payments (RTP/FedNow) via API or treasury portal — sketch** (commercial, send) — 7 best-practice steps[^2]

## Who the journeys are for

- `WF-J20` Commercial ACH origination with dual custody and ACH Fraud Filter (Vantage/CEO) — persona: Treasury analyst/approver at a middle-market company; goal: “Commercial ACH origination with dual custody and ACH Fraud Filter (Vantage/CEO)”[^3]
- `WF-J21` Commercial wire (domestic/international/FX) creation, approval and status search — persona: Treasury analyst/approver at a middle-market company; goal: “Commercial wire (domestic/international/FX) creation, approval and status search”[^4]
- `WF-J22` Commercial instant payment (RTP®/FedNow®) via Gateway API with rail routing — persona: Treasury analyst/approver at a middle-market company; goal: “Commercial instant payment (RTP®/FedNow®) via Gateway API with rail routing”[^5]
- `WF-J23` Commercial consolidated payables file (ACH, wire, card, check) with online approval — persona: Treasury analyst/approver at a middle-market company; goal: “Commercial consolidated payables file (ACH, wire, card, check) with online approval”[^6]
- `WF-J25` Commercial mobile multi-check deposit with deposit approval (Vantage app) — persona: Treasury analyst/approver at a middle-market company; goal: “Commercial mobile multi-check deposit with deposit approval (Vantage app)”[^7]

[^1]: kj · product/WF-P13 · b3c19188f55a
[^2]: kj · customer-journey/CJ-COMMERCIAL-INSTANT · 39b78e3dcf64
[^3]: kj · journey/WF-J20 · aed31b6fcb25
[^4]: kj · journey/WF-J21 · f36035bd9611
[^5]: kj · journey/WF-J22 · 1ca66149586f
[^6]: kj · journey/WF-J23 · d8e43801cb3c
[^7]: kj · journey/WF-J25 · 4d80482f689e

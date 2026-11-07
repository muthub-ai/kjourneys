---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) delivers",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "81bab6934436294b17af086940d2a46ee4c30445feeb8866a5c7e735dc32236a",
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

[^1]: kj · product/WF-P13 · 8d686fdb6385
[^2]: kj · customer-journey/CJ-COMMERCIAL-INSTANT · a7aa87a86868
[^3]: kj · journey/WF-J20 · a09dfa7d417c
[^4]: kj · journey/WF-J21 · a9e16e59c03f
[^5]: kj · journey/WF-J22 · 30a8718f1eaf
[^6]: kj · journey/WF-J23 · 194624059efa
[^7]: kj · journey/WF-J25 · 982023d3f4b5

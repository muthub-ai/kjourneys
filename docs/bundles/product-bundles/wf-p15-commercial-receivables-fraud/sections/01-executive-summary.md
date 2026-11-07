---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p15-commercial-receivables-fraud",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P15",
  "line_of_business": "wf-cb",
  "content_sha256": "f606a62b4f0ebccd4534b05cf1e7c9ec79205b390b4579b2633ffe02b25483c0",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — executive summary

**Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay)** (`WF-P15`) is a Wells Fargo product. Inbound money-movement products: Perfect Receivables proxy account numbers for ACH/wire; Bill Manager e-invoicing with ACH collections; Integrated Receivables cash application; Lockbox; Global invoice payments (pay in local currency); fraud controls (ACH Fraud Filter Stop/Review, Positive Pay, Payee Validation, Reverse Positive Pay, Payment Authorization, Account validation).[^1]

It is owned by **Commercial Banking** (Treasury management and payments); it also serves Corporate and Investment Banking. Basis: inferred — Commercial product: treasury management and payments is reported in Commercial Banking and in Corporate and Investment Banking (Q3 2026 10-Q).[^2][^3]

It has 2 sub-products, 1 of them with a mapped journey, across the ACH origination (business), Other money movement, Domestic wire rail(s).[^1][^4][^5]

MI documented 1 journey(s) for it, delivering 0 customer journey(s); they carry 0 gap(s) () and 0 strength(s).[^6]

[^1]: kj · product/WF-P15 · 1b70c83e2760
[^2]: kj · assignment/WF-P15 · c990e0f81a08
[^3]: kj · lob/wf-cb · 81d8b2643976
[^4]: kj · sub-product/WF-P15-S01 · 8329a58bb402
[^5]: kj · sub-product/WF-P15-S02 · 9ea8fd1b8b2b
[^6]: kj · journey/WF-J24 · 72f66a396d8c

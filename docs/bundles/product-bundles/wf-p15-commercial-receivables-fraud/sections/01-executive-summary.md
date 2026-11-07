---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p15-commercial-receivables-fraud",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P15",
  "line_of_business": "wf-cb",
  "content_sha256": "3f0f2bf94c50d24ad5053ff5f327de446ab9ea118c05597daa38e57161f3e5d2",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — executive summary

**Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay)** (`WF-P15`) is a Wells Fargo product. Inbound money-movement products: Perfect Receivables proxy account numbers for ACH/wire; Bill Manager e-invoicing with ACH collections; Integrated Receivables cash application; Lockbox; Global invoice payments (pay in local currency); fraud controls (ACH Fraud Filter Stop/Review, Positive Pay, Payee Validation, Reverse Positive Pay, Payment Authorization, Account validation).[^1]

It is owned by **Commercial Banking** (Treasury management and payments); it also serves Corporate and Investment Banking. Basis: inferred — MI tags this product commercial. Wells Fargo reports treasury management and payments revenue in both Commercial Banking and Corporate and Investment Banking, so which one owns the product is a judgment, not a disclosure; Commercial Banking is assumed. Confirm..[^2][^3]

It has 2 sub-products, 1 of them with a mapped journey, across the ACH origination (business), Other money movement, Domestic wire rail(s).[^1][^4][^5]

MI documented 1 journey(s) for it, delivering 0 customer journey(s); they carry 0 gap(s) () and 0 strength(s).[^6]

[^1]: kj · product/WF-P15 · 8d59fa7b533b
[^2]: kj · assignment/WF-P15 · 0dd0a5a36565
[^3]: kj · lob/wf-cb · 56d63ed70382
[^4]: kj · sub-product/WF-P15-S01 · 13ddd347e96a
[^5]: kj · sub-product/WF-P15-S02 · 87362be9aaea
[^6]: kj · journey/WF-J24 · e6ceb8fc7dba

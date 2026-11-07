---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Wells Fargo Gateway® APIs (developer portal): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p14-wells-fargo-gateway-apis",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P14",
  "line_of_business": "wf-cb",
  "content_sha256": "395906afa3f5829dad71c599eab6d18d5e420e7c8d038ede1105a7ec0c5277d6",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Gateway® APIs (developer portal) — executive summary

**Wells Fargo Gateway® APIs (developer portal)** (`WF-P14`) is a Wells Fargo product. Wells Fargo Gateway® developer portal (developer.wellsfargo.com) with product catalog, API references, guides and sandbox. Commercial products: Account Balance; Account Validation (Full Response / Logic Box — 'status and ownership information from over 750 million accounts'); ACH Payments (v2, no batch requirement, ACH Exception Reporting webhooks); Bank Lookup; Commercial User Administration; Dodd-Frank Payment Fees; Foreign Exchange (v3) and FX Banknotes; Image Retrieval; Instant Payments (v1); Investment Positions and Activity; Distribution Finance (Dealer/Manufacturer); Money Market Funds Trading; Positive Pay; Push to Card (v2); Transaction Detail (v3); Virtual Card Payments; Wire Payments (v1 — freeform/templated wires, straight-through vs secondary-approval, status); unified Payments API (v1); UK Open Banking (Account & Transaction Information, Confirmation of Funds, Payment Initiation); plus consumer data-sharing APIs (Consumer Access/Consent Management, Consumer Financial Data v6.5, Consumer Information, Consumer Tax Documents, Recipient Registration) and consumer products (Account Aggregation, Account Statements, Prescreened Offers, Private Label Credit Cards). Mutual TLS in Validation/Production; OAuth2 client-credentials keys regenerated every 24 hours.[^1]

It is owned by **Commercial Banking** (Treasury management and payments); it also serves Corporate and Investment Banking. Basis: inferred — MI tags this product commercial. Wells Fargo reports treasury management and payments revenue in both Commercial Banking and Corporate and Investment Banking, so which one owns the product is a judgment, not a disclosure; Commercial Banking is assumed. Confirm..[^2][^3]

It has 3 sub-products, 0 of them with a mapped journey, across the ACH origination (business), FedNow, Other money movement, Push to card, RTP (The Clearing House), Domestic wire, International wire rail(s).[^1][^4][^5][^6]

MI documented no journey for this product yet; its sub-products are listed in the product definition.[^1]

[^1]: kj · product/WF-P14 · 93004be7802c
[^2]: kj · assignment/WF-P14 · 3a904d805836
[^3]: kj · lob/wf-cb · 56d63ed70382
[^4]: kj · sub-product/WF-P14-S01 · bb13747b48ec
[^5]: kj · sub-product/WF-P14-S02 · 2f2a1f64cc97
[^6]: kj · sub-product/WF-P14-S03 · 828a6dc2853b

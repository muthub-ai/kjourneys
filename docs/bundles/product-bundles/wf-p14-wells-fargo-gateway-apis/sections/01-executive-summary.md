---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Wells Fargo Gateway® APIs (developer portal): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p14-wells-fargo-gateway-apis",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P14",
  "line_of_business": "wf-cb",
  "content_sha256": "9978bfed02fb26c46bd6cba013e5fefa31e5c285051a8a309d8198fd3bc88e2c",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Gateway® APIs (developer portal) — executive summary

**Wells Fargo Gateway® APIs (developer portal)** (`WF-P14`) is a Wells Fargo product. Wells Fargo Gateway® developer portal (developer.wellsfargo.com) with product catalog, API references, guides and sandbox. Commercial products: Account Balance; Account Validation (Full Response / Logic Box — 'status and ownership information from over 750 million accounts'); ACH Payments (v2, no batch requirement, ACH Exception Reporting webhooks); Bank Lookup; Commercial User Administration; Dodd-Frank Payment Fees; Foreign Exchange (v3) and FX Banknotes; Image Retrieval; Instant Payments (v1); Investment Positions and Activity; Distribution Finance (Dealer/Manufacturer); Money Market Funds Trading; Positive Pay; Push to Card (v2); Transaction Detail (v3); Virtual Card Payments; Wire Payments (v1 — freeform/templated wires, straight-through vs secondary-approval, status); unified Payments API (v1); UK Open Banking (Account & Transaction Information, Confirmation of Funds, Payment Initiation); plus consumer data-sharing APIs (Consumer Access/Consent Management, Consumer Financial Data v6.5, Consumer Information, Consumer Tax Documents, Recipient Registration) and consumer products (Account Aggregation, Account Statements, Prescreened Offers, Private Label Credit Cards). Mutual TLS in Validation/Production; OAuth2 client-credentials keys regenerated every 24 hours.[^1]

It is owned by **Commercial Banking** (Treasury management and payments); it also serves Corporate and Investment Banking. Basis: inferred — Commercial product: treasury management and payments is reported in Commercial Banking and in Corporate and Investment Banking (Q3 2026 10-Q).[^2][^3]

It has 3 sub-products, 0 of them with a mapped journey, across the ACH origination (business), FedNow, Other money movement, Push to card, RTP (The Clearing House), Domestic wire, International wire rail(s).[^1][^4][^5][^6]

MI documented no journey for this product yet; its sub-products are listed in the product definition.[^1]

[^1]: kj · product/WF-P14 · 716df6a9b366
[^2]: kj · assignment/WF-P14 · fda8c386281c
[^3]: kj · lob/wf-cb · 81d8b2643976
[^4]: kj · sub-product/WF-P14-S01 · 7e7c82510c8d
[^5]: kj · sub-product/WF-P14-S02 · 36981c1c1087
[^6]: kj · sub-product/WF-P14-S03 · 63a19ef5a505

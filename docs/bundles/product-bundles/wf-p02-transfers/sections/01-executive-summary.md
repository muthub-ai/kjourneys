---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Transfers (Transfer Money): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "11bdf94a6cbbf7b6b58cc67be42a0e972ba1a92268613ab67ed3c3a11a60410b",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — executive summary

**Transfers (Transfer Money)** (`WF-P02`) is a Wells Fargo product. Move money between Wells Fargo accounts (immediate), to/from accounts at other U.S. financial institutions ('Bank-to-bank transfers' / 'Add Non-Wells Fargo Accounts'), pay Wells Fargo credit/loan accounts, automatic savings transfers, brokerage transfers.[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer, small-business customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 6 sub-products, 2 of them with a mapped journey, across the ACH external transfer, Internal transfer, Other money movement rail(s).[^1][^4][^5][^6][^7][^8][^9]

MI documented 2 journey(s) for it, delivering 2 customer journey(s); they carry 7 gap(s) (4 medium, 3 low) and 1 strength(s).[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19]

## Most severe gaps

- **medium** · Set up · External-account linking is micro-deposit/proof-of-ownership only — verification 1-3 business days per the public FAQ; no instant credential/aggregator verification (peer banks offer it). Corroborated on the web (Nov 2026, S990): the 'Add Non-Wells Fargo Account' form takes keyed routing and account numbers with an ownership attestation and an account-use choice ('Payments only' vs 'Transfers and payments'); enabling transfers is quoted as 'additional security measures (may take 2-3 business days)'; no aggregator option is offered.[^12]
- **medium** · Initiate · Outbound external transfers default to 2-3 business days; next-day is discretionary and there is no same-day or instant option, although WF already sends RTP/FedNow via its Instant Payments API (a peer bank offers free instant with auto rail selection).[^13]
- **medium** · Exception · Returned/failed external transfers lead to suspension and reinstatement at lower limits with no published plain-language reason codes; ACH return handling is INFERRED.[^14]

[^1]: kj · product/WF-P02 · 9eb25008fe7d
[^2]: kj · assignment/WF-P02 · 8fdf77850db2
[^3]: kj · lob/wf-cbl · 949b2dbdb1b9
[^4]: kj · sub-product/WF-P02-S01 · 9d6d0e037925
[^5]: kj · sub-product/WF-P02-S02 · 341dc9701a79
[^6]: kj · sub-product/WF-P02-S03 · 3e7dc4b77244
[^7]: kj · sub-product/WF-P02-S04 · be32b5135cc9
[^8]: kj · sub-product/WF-P02-S05 · bd7ce3138d2d
[^9]: kj · sub-product/WF-P02-S06 · 74d7e77234fa
[^10]: kj · journey/WF-J05 · 961155a3b7eb
[^11]: kj · journey/WF-J06 · ee855eb97a21
[^12]: kj · finding/GAP-WF-0009 · ba68193d896f
[^13]: kj · finding/GAP-WF-0010 · 6c91b1c549a1
[^14]: kj · finding/GAP-WF-0011 · 907c3416ca30
[^15]: kj · finding/GAP-WF-0013 · 73fe0c3986d5
[^16]: kj · finding/GAP-WF-0012 · 4d065129c300
[^17]: kj · finding/GAP-WF-0033 · deb4b6489d31
[^18]: kj · finding/GAP-WF-0037 · 966f77825654
[^19]: kj · finding/STR-WF-0014 · 3d1262fa3bd4

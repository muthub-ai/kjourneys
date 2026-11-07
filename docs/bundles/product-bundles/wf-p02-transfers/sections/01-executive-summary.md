---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Transfers (Transfer Money): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "10bffc33949f22c58dd49ccf150baafe704c0b658c3a99e1020e5730ba815e28",
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

- **medium** · Set up · External-account linking is micro-deposit/proof-of-ownership only — verification 1-3 business days per the public FAQ; no instant credential/aggregator verification. Corroborated on the web (Nov 2026, S990): the 'Add Non-Wells Fargo Account' form takes keyed routing and account numbers with an ownership attestation and an account-use choice ('Payments only' vs 'Transfers and payments'); enabling transfers is quoted as 'additional security measures (may take 2-3 business days)'; no aggregator option is offered.[^12]
- **medium** · Initiate · Outbound external transfers default to 2-3 business days; next-day is discretionary and there is no same-day or instant option, although WF already sends RTP/FedNow via its Instant Payments API.[^13]
- **medium** · Exception · Returned/failed external transfers lead to suspension and reinstatement at lower limits with no published plain-language reason codes; ACH return handling is INFERRED.[^14]

[^1]: kj · product/WF-P02 · 0b29dca0b27f
[^2]: kj · assignment/WF-P02 · 8fdf77850db2
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P02-S01 · 38cc9de650d6
[^5]: kj · sub-product/WF-P02-S02 · 66f02e827ee4
[^6]: kj · sub-product/WF-P02-S03 · 1b4d45d19976
[^7]: kj · sub-product/WF-P02-S04 · 881dbd9b1863
[^8]: kj · sub-product/WF-P02-S05 · 9bd759243dd7
[^9]: kj · sub-product/WF-P02-S06 · 29d5a0af6c15
[^10]: kj · journey/WF-J05 · 8cc99d20c29f
[^11]: kj · journey/WF-J06 · 5ac14c85b11a
[^12]: kj · finding/GAP-WF-0009 · e2a53e131f01
[^13]: kj · finding/GAP-WF-0010 · a8ddf215d92c
[^14]: kj · finding/GAP-WF-0011 · 2a4a77043815
[^15]: kj · finding/GAP-WF-0013 · e429c2ad51cd
[^16]: kj · finding/GAP-WF-0012 · 2d644efd9069
[^17]: kj · finding/GAP-WF-0032 · 277f2a8e776e
[^18]: kj · finding/GAP-WF-0036 · 8d671b1b3d0a
[^19]: kj · finding/STR-WF-0015 · 708faa6b9cdd

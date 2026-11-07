---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Digital Wires (Wire Money): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "4e52630407913247274b778013a3b7931e3f0872c98c217dbcd09fe73f1495c8",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital Wires (Wire Money) — executive summary

**Digital Wires (Wire Money)** (`WF-P04`) is a Wells Fargo product. Send domestic and international wires in USD or 30 foreign currencies to 200+ countries from Wells Fargo Online, Business Online or mobile; branch wires for amounts above digital limits.[^1]

Former names: Online Wires[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer, small-business customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 3 sub-products, 2 of them with a mapped journey, across the Domestic wire, International wire rail(s).[^1][^4][^5][^6]

MI documented 3 journey(s) for it, delivering 3 customer journey(s); they carry 5 gap(s) (1 high, 3 medium, 1 low) and 5 strength(s).[^7][^8][^9][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19]

## Most severe gaps

- **high** · Review & authorize · SMB wires from Business Online have no dual approval (INFERRED, WF-C003); a single delegate can release a foreign-currency wire.[^10]
- **medium** · Initiate · Digital wire fee messaging conflicts ($30 flat on product page vs '$0-$30' in FAQ) and limits are opaque until entry.[^11]
- **medium** · Exception · Cancellation is possible only while 'Scheduled'; once Pending, recall requires a call to 877-499-6920 and there is no in-app recall request.[^12]

[^1]: kj · product/WF-P04 · 728ab1540360
[^2]: kj · assignment/WF-P04 · 70de3dac3dfc
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P04-S01 · 6f24fe64a471
[^5]: kj · sub-product/WF-P04-S02 · e70a46bc9ff4
[^6]: kj · sub-product/WF-P04-S03 · 4d2ac294b702
[^7]: kj · journey/WF-J10 · ca29755fbe66
[^8]: kj · journey/WF-J11 · 5759e78f0c18
[^9]: kj · journey/WF-J18 · da9c57fe16e4
[^10]: kj · finding/GAP-WF-0029 · a87fe000d932
[^11]: kj · finding/GAP-WF-0014 · 1b33694647db
[^12]: kj · finding/GAP-WF-0016 · 3613671e20fa
[^13]: kj · finding/GAP-WF-0017 · cb93b1938aa9
[^14]: kj · finding/GAP-WF-0015 · 38cf398e4fca
[^15]: kj · finding/STR-WF-0006 · 122172aba700
[^16]: kj · finding/STR-WF-0008 · 94263ca0c11c
[^17]: kj · finding/STR-WF-0007 · c982fc56f2d8
[^18]: kj · finding/STR-WF-0023 · 5f1179bd2b02
[^19]: kj · finding/STR-WF-0024 · ce7383770d37

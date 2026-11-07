---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Digital Wires (Wire Money): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "c83ab9a394e26b0a5d51382f678f8f01a4ecc58ecc07e3337c3c16804a629759",
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

[^1]: kj · product/WF-P04 · 7ae69c334eed
[^2]: kj · assignment/WF-P04 · 70de3dac3dfc
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P04-S01 · 3c9c3eb660ba
[^5]: kj · sub-product/WF-P04-S02 · 474bb477f97e
[^6]: kj · sub-product/WF-P04-S03 · 7ef4ebeda48b
[^7]: kj · journey/WF-J10 · 47452d55448b
[^8]: kj · journey/WF-J11 · e4ed66bc72f0
[^9]: kj · journey/WF-J18 · 7f1916a52a55
[^10]: kj · finding/GAP-WF-0030 · f8866096040e
[^11]: kj · finding/GAP-WF-0014 · d0dbb9e7f48b
[^12]: kj · finding/GAP-WF-0016 · a80da4c53fb1
[^13]: kj · finding/GAP-WF-0017 · 04e895889ce3
[^14]: kj · finding/GAP-WF-0015 · 8ef1e8b3b41e
[^15]: kj · finding/STR-WF-0005 · 11afe95e45b8
[^16]: kj · finding/STR-WF-0007 · f309c9fffd63
[^17]: kj · finding/STR-WF-0006 · b5476d0aaece
[^18]: kj · finding/STR-WF-0022 · 7cf8dedc0711
[^19]: kj · finding/STR-WF-0023 · 4867db231dfa

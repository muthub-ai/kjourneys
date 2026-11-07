---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Zelle®: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "2693ca28ab3ff9596899518a4aa10caffd9a64b39fc856b6ce4124ca0705a845",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — executive summary

**Zelle®** (`WF-P01`) is a Wells Fargo product. Bank-embedded P2P send/request/split via email, U.S. mobile number or (business-only) Zelle tag; QR code pay; recurring and future-dated; Fargo assistant can send to stored contacts. No standalone app since April 2025.[^1]

Former names: SurePay (Wells Fargo's pre-2017 P2P brand on clearXchange; still present in site meta keywords); clearXchange (network predecessor co-founded by Wells Fargo, 2011)[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer, small-business customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 5 sub-products, 3 of them with a mapped journey, across the Request to pay, Zelle rail(s).[^1][^4][^5][^6][^7][^8]

MI documented 5 journey(s) for it (plus the hand-built sample blueprint), delivering 3 customer journey(s); they carry 8 gap(s) (3 high, 3 medium, 2 low) and 6 strength(s).[^9][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28]

## Most severe gaps

- **high** · Review & authorize · Review screen carries only static 'only send to people you know and trust' copy; no risk-tiered interstitial, payment-purpose or contact-origin question is documented, and the Zelle-specific scam page now 404s. Observed on the web (Nov 2026): the only scam messaging before the amount screen is a static banner shown on every Zelle visit; the review screen itself was not reached.[^15]
- **high** · Exception · Unauthorized and scam claims start by phone (1-800-956-4442 / 1-866-867-5568) or by mail to a P.O. box; no in-app 'report a problem' on the Zelle transaction and no in-app claim status tracker for Zelle. Corroborated on the web (Nov 2026, S990): a completed Zelle payment's detail screen offers only 'Block'; on the observed profile the 'Track Claims > Dispute a charge' picker listed only debit-card purchases (whether non-card items are excluded is unconfirmed); 'Report Phish & Email Scams' leaves the secure session for a public education page.[^16]
- **high** · Review & authorize · Business Zelle sends in Business Online can be executed by a single 'View and Transact' delegate; no secondary approval (INFERRED from OAA per WF-C003; the second-wave check of the Zelle for Your Business FAQ confirms the review screen, recipient-name display and first-time access code but says nothing about dual approval, S956). Dual custody exists only for Vantage Treasury Management enrollees.[^17]

[^1]: kj · product/WF-P01 · f217122e121a
[^2]: kj · assignment/WF-P01 · daf9fc88d74e
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P01-S01 · fd892338eb7b
[^5]: kj · sub-product/WF-P01-S02 · 88b81a74ed86
[^6]: kj · sub-product/WF-P01-S03 · 459b1ae65d26
[^7]: kj · sub-product/WF-P01-S04 · d167429d7fc3
[^8]: kj · sub-product/WF-P01-S05 · 9d7ee732e4a6
[^9]: kj · journey/WF-J01 · c3b8e132fd5c
[^10]: kj · journey/WF-J02 · 2eca5861046f
[^11]: kj · journey/WF-J03 · 558dd3d0215c
[^12]: kj · journey/WF-J28 · cf400c417393
[^13]: kj · journey/WF-J29 · f76130105e87
[^14]: kj · journey/sample · e85b2befb3b0
[^15]: kj · finding/GAP-WF-0001 · 1e4eff85a315
[^16]: kj · finding/GAP-WF-0002 · 5f257a86aa4a
[^17]: kj · finding/GAP-WF-0008 · 2074ba55f5b7
[^18]: kj · finding/GAP-WF-0003 · d7739d2d4711
[^19]: kj · finding/GAP-WF-0004 · 2b1a133e331a
[^20]: kj · finding/GAP-WF-0006 · d4cf77ecd112
[^21]: kj · finding/GAP-WF-0007 · 521fc1be3252
[^22]: kj · finding/GAP-WF-0035 · 0713fae04ce2
[^23]: kj · finding/STR-WF-0002 · 5debf3f862e8
[^24]: kj · finding/STR-WF-0003 · fb1b6dc2f235
[^25]: kj · finding/STR-WF-0004 · 0a23a8ab1ce7
[^26]: kj · finding/STR-WF-0005 · 9050d412286d
[^27]: kj · finding/STR-WF-0022 · e07b4ec8bedd
[^28]: kj · finding/STR-WF-0021 · 2fcca8416a99

---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Zelle®: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "cc5439fc788a7d61c640d0fe6abf1b388333165639367c09f30c51cb0579c5cf",
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
- **high** · Review & authorize · Business Zelle sends in Business Online can be executed by a single 'View and Transact' delegate; no secondary approval (INFERRED from OAA per WF-C003). Dual custody exists only for Vantage Treasury Management enrollees.[^17]

[^1]: kj · product/WF-P01 · 7db18a666d60
[^2]: kj · assignment/WF-P01 · daf9fc88d74e
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P01-S01 · dac14fe19dea
[^5]: kj · sub-product/WF-P01-S02 · 22b37fa1ea11
[^6]: kj · sub-product/WF-P01-S03 · 677aab3d9fbb
[^7]: kj · sub-product/WF-P01-S04 · 05811c9bbdb1
[^8]: kj · sub-product/WF-P01-S05 · 8377db259ff9
[^9]: kj · journey/WF-J01 · 251e989b61ea
[^10]: kj · journey/WF-J02 · 14bc08a80f04
[^11]: kj · journey/WF-J03 · b89c841e1309
[^12]: kj · journey/WF-J28 · b20fda0a115f
[^13]: kj · journey/WF-J29 · d718f795aee2
[^14]: kj · journey/sample · e85b2befb3b0
[^15]: kj · finding/GAP-WF-0001 · 38c101614c6a
[^16]: kj · finding/GAP-WF-0002 · 4e09e7353ec2
[^17]: kj · finding/GAP-WF-0008 · 35e06b5dbd70
[^18]: kj · finding/GAP-WF-0003 · a9b601e4c21e
[^19]: kj · finding/GAP-WF-0004 · 069260253e2f
[^20]: kj · finding/GAP-WF-0006 · 3782e8a4f392
[^21]: kj · finding/GAP-WF-0007 · 8cfc91935657
[^22]: kj · finding/GAP-WF-0036 · 100d7a3aaf40
[^23]: kj · finding/STR-WF-0001 · bb3dd7fabeb8
[^24]: kj · finding/STR-WF-0002 · 63a6e9b96a41
[^25]: kj · finding/STR-WF-0003 · db967ece611f
[^26]: kj · finding/STR-WF-0004 · f24f20dbe1a5
[^27]: kj · finding/STR-WF-0021 · 1fa52835558b
[^28]: kj · finding/STR-WF-0020 · 9d37e3577ce0

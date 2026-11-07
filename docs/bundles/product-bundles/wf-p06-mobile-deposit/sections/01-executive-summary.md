---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Mobile Deposit (Wells Fargo Mobile® Deposit): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "ec4dee60ba47e01589583b9fe6cef5c5efc7df40b7227a0297051c7b2b45dfe5",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Mobile Deposit (Wells Fargo Mobile® Deposit) — executive summary

**Mobile Deposit (Wells Fargo Mobile® Deposit)** (`WF-P06`) is a Wells Fargo product. Camera check deposit in the Wells Fargo Mobile app with guided capture, on-screen limits, email + Message Center confirmation, 9 pm PT cutoff.[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer, small-business customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 1 sub-products, 1 of them with a mapped journey, across the Mobile check deposit rail(s).[^1][^4]

MI documented 2 journey(s) for it, delivering 1 customer journey(s); they carry 1 gap(s) (1 low) and 2 strength(s).[^5][^6][^7][^8][^9]

## Most severe gaps

- **low** · Exception · Returned-check notice is a written letter; no digital return notification documented.[^7]

[^1]: kj · product/WF-P06 · aa0e6fda3732
[^2]: kj · assignment/WF-P06 · 14c5b738cdf5
[^3]: kj · lob/wf-cbl · 949b2dbdb1b9
[^4]: kj · sub-product/WF-P06-S01 · 91e8f2a090b8
[^5]: kj · journey/WF-J13 · e4ae53b47a45
[^6]: kj · journey/WF-J19 · 2f91942d8e13
[^7]: kj · finding/GAP-WF-0032 · aaf39ff632ca
[^8]: kj · finding/STR-WF-0012 · 3dff85a0574b
[^9]: kj · finding/STR-WF-0013 · ff17d44548b8

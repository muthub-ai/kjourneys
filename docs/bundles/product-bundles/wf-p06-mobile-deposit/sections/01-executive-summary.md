---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Mobile Deposit (Wells Fargo Mobile® Deposit): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "9895d4fce9cd80c4932f3398086634769464f66bf5b41f37272ef5382fd5dcbe",
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

[^1]: kj · product/WF-P06 · 7447c97a0fac
[^2]: kj · assignment/WF-P06 · 14c5b738cdf5
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P06-S01 · adf0bd6e0f63
[^5]: kj · journey/WF-J13 · 0dcdd11b8e8d
[^6]: kj · journey/WF-J19 · 2d1ad618854b
[^7]: kj · finding/GAP-WF-0031 · ca82807356e3
[^8]: kj · finding/STR-WF-0013 · e5a788c526fb
[^9]: kj · finding/STR-WF-0014 · a216597059a7

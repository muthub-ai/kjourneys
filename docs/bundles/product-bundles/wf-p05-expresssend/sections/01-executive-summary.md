---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "ExpressSend®: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "f7a71e1b6a6e7db82db316fbbd69402c2a710802148bee333e3007393b06ef70",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ExpressSend® — executive summary

**ExpressSend®** (`WF-P05`) is a Wells Fargo product. Consumer person-to-person remittance to 12 countries (Mexico, Dominican Republic, El Salvador, Guatemala, Honduras, Nicaragua, Colombia, Ecuador, Peru, India, Philippines, Vietnam) with account credit or cash pickup through named Remittance Network Members. Two tracks coexist: (1) legacy ExpressSend service agreements — first remittance in person at a branch (or by Phone Bank for existing customers), later remittances at a branch, by Phone Bank, or through Wells Fargo Online on a desktop/laptop ('Transfer and Pay' > 'Send to Another Country'); (2) ExpressSend Mobile — nationwide launch announced Sep 14 2026 (in app release notes from v26.06.00, Jun 29 2026), first mobile transfer fee waived, up to 10 recipients, real-time tracking and alerts; once a customer accepts the mobile terms the service becomes app-only ('You'll no longer be able to use it in a web browser, at a branch, or by phone'). No recurring or future-dated transfers on either track.[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 2 sub-products, 1 of them with a mapped journey, across the Remittance rail(s).[^1][^4][^5]

MI documented 1 journey(s) for it, delivering 1 customer journey(s); they carry 2 gap(s) (2 medium) and 2 strength(s).[^6][^7][^8][^9][^10]

## Most severe gaps

- **medium** · Manage · ExpressSend supports neither recurring nor future-dated transfers on either service track.[^7]
- **medium** · Discover · ExpressSend is migrating to app-only: accepting mobile terms removes branch, web and phone access, leaving two parallel service tracks with different labels. Corroborated on the web (Nov 2026, S990): the logged-in hub item 'Send with ExpressSend®' routes to a public page ('Send it in the app').[^8]

[^1]: kj · product/WF-P05 · 0e61b73c4811
[^2]: kj · assignment/WF-P05 · 607b1c155d64
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P05-S01 · f975b8e7294f
[^5]: kj · sub-product/WF-P05-S02 · 79d38fd49e62
[^6]: kj · journey/WF-J12 · 98b1c3096cb7
[^7]: kj · finding/GAP-WF-0018 · e188881f4b71
[^8]: kj · finding/GAP-WF-0019 · 3cbbaf201625
[^9]: kj · finding/STR-WF-0009 · 681c2f8bbf3d
[^10]: kj · finding/STR-WF-0010 · 8f532125f072

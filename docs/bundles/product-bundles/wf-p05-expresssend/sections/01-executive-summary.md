---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "ExpressSend®: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "0cbd2fbadf89aa7d799f18349b0cdac028f78b03538c203593a7adf20fef9da7",
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

[^1]: kj · product/WF-P05 · 4247b60967aa
[^2]: kj · assignment/WF-P05 · 607b1c155d64
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P05-S01 · 9697c6c44150
[^5]: kj · sub-product/WF-P05-S02 · dfcb6ac16268
[^6]: kj · journey/WF-J12 · 94fc27116502
[^7]: kj · finding/GAP-WF-0018 · 59b1c988973b
[^8]: kj · finding/GAP-WF-0019 · e5190615f7b0
[^9]: kj · finding/STR-WF-0008 · a381b8d38fc5
[^10]: kj · finding/STR-WF-0009 · 376b9cc3c369

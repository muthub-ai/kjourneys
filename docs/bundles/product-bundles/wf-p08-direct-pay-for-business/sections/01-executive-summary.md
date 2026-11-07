---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Direct Pay for Business: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "78a6ba92ef13afc6d13410c90cda3d9243ace35c70ee2e9c67b7e333ecba0e54",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — executive summary

**Direct Pay for Business** (`WF-P08`) is a Wells Fargo product. Business Online ACH credit origination to employees, contractors, sales agents and vendors (U.S., Guam, PR, USVI); payee validation; one-time or recurring; next-business-day delivery; four user access levels giving input/approve/release separation; $10/month plus per-payment fees.[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves small-business customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 2 sub-products, 1 of them with a mapped journey, across the ACH origination (business) rail(s).[^1][^4][^5]

MI documented 1 journey(s) for it, delivering 1 customer journey(s); they carry 4 gap(s) (1 high, 3 medium) and 2 strength(s).[^6][^7][^8][^9][^10][^11][^12]

## Most severe gaps

- **high** · Discover · Direct Pay is desktop-browser only: SMB owners cannot initiate or approve ACH on mobile unless they enrol in Vantage Treasury Management.[^7]
- **medium** · Initiate · Direct Pay is next-business-day only; no Same Day ACH option documented after a search of the Direct Pay FAQ (S931).[^8]
- **medium** · Manage · Edit/cancel rules for scheduled Direct Pay payments are not documented.[^9]

[^1]: kj · product/WF-P08 · 3868912428e5
[^2]: kj · assignment/WF-P08 · 59a2dcfc7280
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P08-S01 · db68e67b33e1
[^5]: kj · sub-product/WF-P08-S02 · 70fa5adeaa25
[^6]: kj · journey/WF-J16 · 67eed586f4fc
[^7]: kj · finding/GAP-WF-0026 · 98f60378df46
[^8]: kj · finding/GAP-WF-0027 · 3f10807fa15d
[^9]: kj · finding/GAP-WF-0028 · fa0fe1897d28
[^10]: kj · finding/GAP-WF-0029 · c7d7360df8f3
[^11]: kj · finding/STR-WF-0017 · ebeb4dc413cc
[^12]: kj · finding/STR-WF-0018 · 64c7f9a8f46b

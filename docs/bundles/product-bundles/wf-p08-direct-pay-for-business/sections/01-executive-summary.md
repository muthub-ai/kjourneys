---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Direct Pay for Business: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "d06e1df29d29168126391d12fce1b558417b7eaeb8ef01e4c12d5ce7d3c7c993",
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

MI documented 1 journey(s) for it, delivering 1 customer journey(s); they carry 4 gap(s) (1 high, 2 medium, 1 low) and 2 strength(s).[^6][^7][^8][^9][^10][^11][^12]

## Most severe gaps

- **high** · Discover · Direct Pay is desktop-browser only: SMB owners cannot initiate or approve ACH on mobile unless they enrol in Vantage Treasury Management.[^7]
- **medium** · Initiate · Direct Pay is next-business-day only; no Same Day ACH option documented after a search of the Direct Pay FAQ (S931).[^8]
- **medium** · Exception · Returned ACH credits from the payee's bank and Same Day ACH are not published; second-wave evidence closes only part of the gap — insufficient funds ('we may either decline the transfer' or complete it and overdraw), payment by account number only with no name check, and rejection notices are now published in the Direct Pay Agreement (S970).[^9]

[^1]: kj · product/WF-P08 · 53a0b5f81ba1
[^2]: kj · assignment/WF-P08 · 59a2dcfc7280
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P08-S01 · 49d1af9a29ac
[^5]: kj · sub-product/WF-P08-S02 · 76fa6c9a0dcb
[^6]: kj · journey/WF-J16 · 38a8b7c0348a
[^7]: kj · finding/GAP-WF-0025 · c507ffb51a47
[^8]: kj · finding/GAP-WF-0026 · 78c5f344fbea
[^9]: kj · finding/GAP-WF-0028 · 631690a78ab9
[^10]: kj · finding/GAP-WF-0027 · cb8e2556a07e
[^11]: kj · finding/STR-WF-0018 · fc01adb0b7c4
[^12]: kj · finding/STR-WF-0019 · a3bb48aa2a09

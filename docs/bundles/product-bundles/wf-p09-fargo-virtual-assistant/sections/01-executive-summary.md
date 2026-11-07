---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Fargo® virtual assistant: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "926f2204987754d9efd73972a437a3bbea0ea1ca3c2654f4433000cf65fc075d",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — executive summary

**Fargo® virtual assistant** (`WF-P09`) is a Wells Fargo product. AI-powered virtual assistant in the Wells Fargo Mobile app (smartphone only, consumer accounts only, English/Spanish). Published capabilities: 'Transferring between accounts and sending money with Zelle®', 'Updating account and card settings', bills-due view, 'Make a payment or transfer', 'View Zelle® transactions', 'Find my routing number', 'I need to turn my card off', balance/activity forecasts, spending and subscription insights. Zelle initiation is peer parity; scale is the differentiator (>1B interactions, >3M Spanish-speaking users).[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 1 sub-products, 1 of them with a mapped journey, across the Bill pay, Internal transfer, Other money movement, Zelle rail(s).[^1][^4]

MI documented 1 journey(s) for it, delivering 1 customer journey(s); they carry 1 gap(s) (1 low) and 0 strength(s).[^5][^6]

## Most severe gaps

- **low** · Support · Fargo can initiate a Zelle send, but its confirmation UX is unpublished (INFERRED hand-off to the standard review screen).[^6]

[^1]: kj · product/WF-P09 · 4787881df475
[^2]: kj · assignment/WF-P09 · 335f6c8682e1
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P09-S01 · a2a787230b72
[^5]: kj · journey/WF-J04 · 2e981edf18c3
[^6]: kj · finding/GAP-WF-0005 · 23ad46977fbc

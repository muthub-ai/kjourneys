---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "ATM & branch deposits/transfers: ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p07-atm-branch-deposits-transfer",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P07",
  "line_of_business": "wf-cbl",
  "content_sha256": "c750d2ecf96ff62df0ec7af99a9abc1f6901815ee17d534bfa3dc3b7b336f394",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ATM & branch deposits/transfers — executive summary

**ATM & branch deposits/transfers** (`WF-P07`) is a Wells Fargo product. Envelope-free ATM cash/check deposits (ATM scans checks, counts bills), ATM transfers between accounts and WF credit card payments, digital-wallet/contactless card-free ATM access, e-receipts; branch wires ($40) and deposits; Bank by Mail.[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer, small-business customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 4 sub-products, 1 of them with a mapped journey, across the Cash, ATM and branch, Other money movement rail(s).[^1][^4][^5][^6][^7]

MI documented 1 journey(s) for it, delivering 0 customer journey(s); they carry 0 gap(s) () and 0 strength(s).[^8]

[^1]: kj · product/WF-P07 · 60c66e3aae03
[^2]: kj · assignment/WF-P07 · a7162a28f27a
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P07-S01 · aa32b478be83
[^5]: kj · sub-product/WF-P07-S02 · 99c24b809b94
[^6]: kj · sub-product/WF-P07-S03 · 679662e56f3c
[^7]: kj · sub-product/WF-P07-S04 · 23f5e215875f
[^8]: kj · journey/WF-J14 · d4a1b057205c

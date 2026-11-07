---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "8f00f29564c12e3692529924ead0df3cbe17a4059086544f4bfcb851b5c3cea7",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — executive summary

**Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®)** (`WF-P13`) is a Wells Fargo product. Next-generation commercial digital banking platform (microfrontends, APIs, AI/ML, GraphQL) with persona-driven dashboard, Tasks hub, Message Center alerts, dual custody, RSA mobile token, biometrics, Secure Validation (SMS/voice codes) and Token Validation (PIN + RSA SecurID). Published workflows: 'Review and approve payments, Process exceptions, Manage company users, Sign documents, View balances, Paydown loans, View transaction detail, Transfer money, Create wires, Create FX payments'. CEO being phased out with both available during migration (2026). Vantage mobile 2026 cadence (App Store): Tasks hub for ACH Fraud Filter/Positive Pay (Feb 17), domestic wire approvals (Mar 17), all wire approvals (Jul 21), Positive Pay decisions in Fraud Manager + Wires Status Search (Sep 10), approvals for wires/federal tax payments/book transfers/drawdowns + Cash Accounts history (Oct 13), payments tasks on home screen + 3 months card history + iPad (Nov 5). Tokenized deposits (on-chain, 24/7/365 settlement, smart-contract programmability) announced Aug 4 2026 for select corporate/commercial clients (USD→GBP pilot fall 2026; broader 2027 rollout), integrated into existing offering with automatic routing.[^1]

Former names: Commercial Electronic Office (CEO) portal; CEO Mobile (app renamed Wells Fargo Vantage)[^1]

It is owned by **Commercial Banking** (Treasury management and payments); it also serves Corporate and Investment Banking, Consumer Banking and Lending. Basis: inferred — Commercial product: treasury management and payments is reported in Commercial Banking and in Corporate and Investment Banking (Q3 2026 10-Q); also used by small businesses.[^2][^3]

It has 8 sub-products, 5 of them with a mapped journey, across the ACH origination (business), Mobile check deposit, FedNow, Internal transfer, Other money movement, RTP (The Clearing House), Domestic wire, International wire rail(s).[^1][^4][^5][^6][^7][^8][^9][^10][^11]

MI documented 5 journey(s) for it, delivering 1 customer journey(s); they carry 3 gap(s) (1 medium, 2 low) and 1 strength(s).[^12][^13][^14][^15][^16][^17][^18][^19][^20]

## Most severe gaps

- **medium** · Initiate · Commercial Request for Payment is absent from the public Instant Payments API v1 (credit transfers only); dedicated treasury instant-payment pages 404.[^17]
- **low** · Set up · The routing-number reachability check (RTP | FEDNOW) exists only in the API; no consumer/SMB surface shows instant eligibility.[^18]
- **low** · Exception · Fallback when a receiver is unreachable on both rails is undocumented.[^19]

[^1]: kj · product/WF-P13 · 8d686fdb6385
[^2]: kj · assignment/WF-P13 · 8799b4a3e937
[^3]: kj · lob/wf-cb · 81d8b2643976
[^4]: kj · sub-product/WF-P13-S01 · d47d872c35b3
[^5]: kj · sub-product/WF-P13-S02 · fcdcd0d9bd23
[^6]: kj · sub-product/WF-P13-S03 · 09da1d723a6a
[^7]: kj · sub-product/WF-P13-S04 · b1d1dec413e7
[^8]: kj · sub-product/WF-P13-S05 · f44e78fc1421
[^9]: kj · sub-product/WF-P13-S06 · d87de4a70317
[^10]: kj · sub-product/WF-P13-S07 · f793bcdc6041
[^11]: kj · sub-product/WF-P13-S08 · c4c278b878d7
[^12]: kj · journey/WF-J20 · a09dfa7d417c
[^13]: kj · journey/WF-J21 · a9e16e59c03f
[^14]: kj · journey/WF-J22 · 30a8718f1eaf
[^15]: kj · journey/WF-J23 · 194624059efa
[^16]: kj · journey/WF-J25 · 982023d3f4b5
[^17]: kj · finding/GAP-WF-0034 · 6985b24955d0
[^18]: kj · finding/GAP-WF-0022 · 5bf6f52632fa
[^19]: kj · finding/GAP-WF-0035 · 0a84506564fc
[^20]: kj · finding/STR-WF-0019 · c2bf4588e07b

---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "5163b320d00b58e3210cf9ff398eb261b1ee43842da278139d59e8ca348d5133",
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

It is owned by **Commercial Banking** (Treasury management and payments); it also serves Corporate and Investment Banking, Consumer Banking and Lending. Basis: inferred — MI tags this product commercial. Wells Fargo reports treasury management and payments revenue in both Commercial Banking and Corporate and Investment Banking, so which one owns the product is a judgment, not a disclosure; Commercial Banking is assumed; small-business use (one sub-product) adds Consumer Banking and Lending. Confirm..[^2][^3]

It has 8 sub-products, 5 of them with a mapped journey, across the ACH origination (business), Mobile check deposit, FedNow, Internal transfer, Other money movement, RTP (The Clearing House), Domestic wire, International wire rail(s).[^1][^4][^5][^6][^7][^8][^9][^10][^11]

MI documented 5 journey(s) for it, delivering 1 customer journey(s); they carry 3 gap(s) (1 medium, 2 low) and 1 strength(s).[^12][^13][^14][^15][^16][^17][^18][^19][^20]

## Most severe gaps

- **medium** · Initiate · Commercial Request for Payment is absent from the public Instant Payments API v1 (credit transfers only); dedicated treasury instant-payment pages 404.[^17]
- **low** · Set up · The routing-number reachability check (RTP | FEDNOW) exists only in the API; no consumer/SMB surface shows instant eligibility.[^18]
- **low** · Exception · Fallback when a receiver is unreachable on both rails is undocumented.[^19]

[^1]: kj · product/WF-P13 · b3c19188f55a
[^2]: kj · assignment/WF-P13 · c64f59363a8c
[^3]: kj · lob/wf-cb · 56d63ed70382
[^4]: kj · sub-product/WF-P13-S01 · ded60df73563
[^5]: kj · sub-product/WF-P13-S02 · 05565cc0302e
[^6]: kj · sub-product/WF-P13-S03 · 4c6b4d5ffa9a
[^7]: kj · sub-product/WF-P13-S04 · 018bb34f5188
[^8]: kj · sub-product/WF-P13-S05 · 0e0fdb067b70
[^9]: kj · sub-product/WF-P13-S06 · d815ddabce53
[^10]: kj · sub-product/WF-P13-S07 · 282f71a0fbdc
[^11]: kj · sub-product/WF-P13-S08 · 7b6897ce2e68
[^12]: kj · journey/WF-J20 · aed31b6fcb25
[^13]: kj · journey/WF-J21 · f36035bd9611
[^14]: kj · journey/WF-J22 · 1ca66149586f
[^15]: kj · journey/WF-J23 · d8e43801cb3c
[^16]: kj · journey/WF-J25 · 4d80482f689e
[^17]: kj · finding/GAP-WF-0033 · 73eff2ab59a7
[^18]: kj · finding/GAP-WF-0022 · b4cf64e39188
[^19]: kj · finding/GAP-WF-0034 · 11d66ca955c7
[^20]: kj · finding/STR-WF-0020 · 2e5d23c39cf2

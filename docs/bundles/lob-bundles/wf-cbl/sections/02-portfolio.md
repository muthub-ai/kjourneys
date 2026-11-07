---
{
 "type": "lob-bundle/section",
 "title": "Product portfolio",
 "description": "Consumer Banking and Lending: products owned and served, with links to their bundles",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cbl",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cbl",
  "content_sha256": "be178d022443425ec577b103c70dcb11389270d152e3b4cf153746991288972d",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Consumer Banking and Lending — product portfolio

## Products it owns

| Product | Component | Sub-products | Journeys | Gaps | Bundle |
|---|---|---|---|---|---|
| `WF-P01` Zelle® | Consumer, Small and Business Banking | 5 | 5 | 8 | [wf-p01-zelle](../../product-bundles/wf-p01-zelle/index.md)[^1][^2] |
| `WF-P02` Transfers (Transfer Money) | Consumer, Small and Business Banking | 6 | 2 | 7 | [wf-p02-transfers](../../product-bundles/wf-p02-transfers/index.md)[^3][^4] |
| `WF-P03` Bill Pay (Online Bill Pay / Business Bill Pay) | Consumer, Small and Business Banking | 4 | 4 | 4 | [wf-p03-bill-pay](../../product-bundles/wf-p03-bill-pay/index.md)[^5][^6] |
| `WF-P04` Digital Wires (Wire Money) | Consumer, Small and Business Banking | 3 | 3 | 5 | [wf-p04-digital-wires](../../product-bundles/wf-p04-digital-wires/index.md)[^7][^8] |
| `WF-P05` ExpressSend® | Consumer, Small and Business Banking | 2 | 1 | 2 | [wf-p05-expresssend](../../product-bundles/wf-p05-expresssend/index.md)[^9][^10] |
| `WF-P06` Mobile Deposit (Wells Fargo Mobile® Deposit) | Consumer, Small and Business Banking | 1 | 2 | 1 | [wf-p06-mobile-deposit](../../product-bundles/wf-p06-mobile-deposit/index.md)[^11][^12] |
| `WF-P07` ATM & branch deposits/transfers | Consumer, Small and Business Banking | 4 | 1 | 0 | [wf-p07-atm-branch-deposits-transfer](../../product-bundles/wf-p07-atm-branch-deposits-transfer/index.md)[^13][^14] |
| `WF-P08` Direct Pay for Business | Consumer, Small and Business Banking | 2 | 1 | 4 | [wf-p08-direct-pay-for-business](../../product-bundles/wf-p08-direct-pay-for-business/index.md)[^15][^16] |
| `WF-P09` Fargo® virtual assistant | Consumer, Small and Business Banking | 1 | 1 | 1 | [wf-p09-fargo-virtual-assistant](../../product-bundles/wf-p09-fargo-virtual-assistant/index.md)[^17][^18] |
| `WF-P10` Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ | Consumer, Small and Business Banking | 1 | 1 | 0 | [wf-p10-card-settings](../../product-bundles/wf-p10-card-settings/index.md)[^19][^20] |
| `WF-P11` Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM) | Consumer, Small and Business Banking | 2 | 1 | 0 | [wf-p11-digital-wallet-intersections](../../product-bundles/wf-p11-digital-wallet-intersections/index.md)[^21][^22] |
| `WF-P12` Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) | Consumer, Small and Business Banking | 3 | 1 | 3 | [wf-p12-early-pay-day-inbound-instan](../../product-bundles/wf-p12-early-pay-day-inbound-instan/index.md)[^23][^24] |

## Products it also serves

| Product | Owned by | Bundle |
|---|---|---|
| `WF-P13` Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) | Commercial Banking | [wf-p13-wells-fargo-vantage](../../product-bundles/wf-p13-wells-fargo-vantage/index.md)[^25] |

[^1]: kj · product/WF-P01 · 7db18a666d60
[^2]: kj · assignment/WF-P01 · daf9fc88d74e
[^3]: kj · product/WF-P02 · 9eb25008fe7d
[^4]: kj · assignment/WF-P02 · 8fdf77850db2
[^5]: kj · product/WF-P03 · b839aacb8026
[^6]: kj · assignment/WF-P03 · e2aaf98a158a
[^7]: kj · product/WF-P04 · 7ae69c334eed
[^8]: kj · assignment/WF-P04 · 70de3dac3dfc
[^9]: kj · product/WF-P05 · 4247b60967aa
[^10]: kj · assignment/WF-P05 · 607b1c155d64
[^11]: kj · product/WF-P06 · aa0e6fda3732
[^12]: kj · assignment/WF-P06 · 14c5b738cdf5
[^13]: kj · product/WF-P07 · 60c66e3aae03
[^14]: kj · assignment/WF-P07 · a7162a28f27a
[^15]: kj · product/WF-P08 · 3868912428e5
[^16]: kj · assignment/WF-P08 · 59a2dcfc7280
[^17]: kj · product/WF-P09 · d4d1ce4a76b1
[^18]: kj · assignment/WF-P09 · 335f6c8682e1
[^19]: kj · product/WF-P10 · ae4ea79539a2
[^20]: kj · assignment/WF-P10 · 61f49f4b4a83
[^21]: kj · product/WF-P11 · df9119f7188e
[^22]: kj · assignment/WF-P11 · eccf60df1390
[^23]: kj · product/WF-P12 · d73da35d0cb8
[^24]: kj · assignment/WF-P12 · 64f7eaee3789
[^25]: kj · assignment/WF-P13 · c64f59363a8c

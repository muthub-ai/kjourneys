---
{
 "type": "lob-bundle/section",
 "title": "Product portfolio",
 "description": "Consumer Banking and Lending: products owned and served, with links to their bundles",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cbl",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cbl",
  "content_sha256": "0182982bf83c886d26da1b38b3b9bd9d2a8b924932e2f7a617c5d05bb6d73da4",
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
| `WF-P12` Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) | Consumer, Small and Business Banking | 3 | 1 | 2 | [wf-p12-early-pay-day-inbound-instan](../../product-bundles/wf-p12-early-pay-day-inbound-instan/index.md)[^23][^24] |

## Products it also serves

| Product | Owned by | Bundle |
|---|---|---|
| `WF-P13` Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) | Commercial Banking | [wf-p13-wells-fargo-vantage](../../product-bundles/wf-p13-wells-fargo-vantage/index.md)[^25] |

[^1]: kj · product/WF-P01 · f217122e121a
[^2]: kj · assignment/WF-P01 · daf9fc88d74e
[^3]: kj · product/WF-P02 · 0b29dca0b27f
[^4]: kj · assignment/WF-P02 · 8fdf77850db2
[^5]: kj · product/WF-P03 · 0c4750f70904
[^6]: kj · assignment/WF-P03 · e2aaf98a158a
[^7]: kj · product/WF-P04 · 728ab1540360
[^8]: kj · assignment/WF-P04 · 70de3dac3dfc
[^9]: kj · product/WF-P05 · 0e61b73c4811
[^10]: kj · assignment/WF-P05 · 607b1c155d64
[^11]: kj · product/WF-P06 · 7447c97a0fac
[^12]: kj · assignment/WF-P06 · 14c5b738cdf5
[^13]: kj · product/WF-P07 · 4fe5c088f5d6
[^14]: kj · assignment/WF-P07 · a7162a28f27a
[^15]: kj · product/WF-P08 · 53a0b5f81ba1
[^16]: kj · assignment/WF-P08 · 59a2dcfc7280
[^17]: kj · product/WF-P09 · 4787881df475
[^18]: kj · assignment/WF-P09 · 335f6c8682e1
[^19]: kj · product/WF-P10 · 5dc2c6e95e66
[^20]: kj · assignment/WF-P10 · 61f49f4b4a83
[^21]: kj · product/WF-P11 · 18c5f5e9f2bf
[^22]: kj · assignment/WF-P11 · eccf60df1390
[^23]: kj · product/WF-P12 · 932e654a57de
[^24]: kj · assignment/WF-P12 · 64f7eaee3789
[^25]: kj · assignment/WF-P13 · c64f59363a8c

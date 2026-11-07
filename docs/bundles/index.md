# Wells Fargo bundles

Line-of-business and product bundles in OKF v0.2, built by `tools/build_bundles.py` from the Wells Fargo-only export `_source/wells-fargo.json` (`7320ba3f33f2`, MI report 2026-11-06-v1).

## Lines of business

- [Consumer Banking and Lending](lob-bundles/wf-cbl/index.md) — owns 12 product(s), also serves 1
- [Commercial Banking](lob-bundles/wf-cb/index.md) — owns 3 product(s), also serves 0
- [Corporate and Investment Banking](lob-bundles/wf-cib/index.md) — owns 0 product(s), also serves 3
- [Wealth and Investment Management](lob-bundles/wf-wim/index.md) — owns 0 product(s), also serves 0

## Products

| Bundle | Product | Owned by | Sub-products | Journeys | Gaps |
|---|---|---|---|---|---|
| [wf-p01-zelle](product-bundles/wf-p01-zelle/index.md) | Zelle® | Consumer Banking and Lending | 5 | 6 | 8 |
| [wf-p02-transfers](product-bundles/wf-p02-transfers/index.md) | Transfers (Transfer Money) | Consumer Banking and Lending | 6 | 2 | 7 |
| [wf-p03-bill-pay](product-bundles/wf-p03-bill-pay/index.md) | Bill Pay (Online Bill Pay / Business Bill Pay) | Consumer Banking and Lending | 4 | 4 | 4 |
| [wf-p04-digital-wires](product-bundles/wf-p04-digital-wires/index.md) | Digital Wires (Wire Money) | Consumer Banking and Lending | 3 | 3 | 5 |
| [wf-p05-expresssend](product-bundles/wf-p05-expresssend/index.md) | ExpressSend® | Consumer Banking and Lending | 2 | 1 | 2 |
| [wf-p06-mobile-deposit](product-bundles/wf-p06-mobile-deposit/index.md) | Mobile Deposit (Wells Fargo Mobile® Deposit) | Consumer Banking and Lending | 1 | 2 | 1 |
| [wf-p07-atm-branch-deposits-transfer](product-bundles/wf-p07-atm-branch-deposits-transfer/index.md) | ATM & branch deposits/transfers | Consumer Banking and Lending | 4 | 1 | 0 |
| [wf-p08-direct-pay-for-business](product-bundles/wf-p08-direct-pay-for-business/index.md) | Direct Pay for Business | Consumer Banking and Lending | 2 | 1 | 4 |
| [wf-p09-fargo-virtual-assistant](product-bundles/wf-p09-fargo-virtual-assistant/index.md) | Fargo® virtual assistant | Consumer Banking and Lending | 1 | 1 | 1 |
| [wf-p10-card-settings](product-bundles/wf-p10-card-settings/index.md) | Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ | Consumer Banking and Lending | 1 | 1 | 0 |
| [wf-p11-digital-wallet-intersections](product-bundles/wf-p11-digital-wallet-intersections/index.md) | Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM) | Consumer Banking and Lending | 2 | 1 | 0 |
| [wf-p12-early-pay-day-inbound-instan](product-bundles/wf-p12-early-pay-day-inbound-instan/index.md) | Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) | Consumer Banking and Lending | 3 | 1 | 3 |
| [wf-p13-wells-fargo-vantage](product-bundles/wf-p13-wells-fargo-vantage/index.md) | Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) | Commercial Banking | 8 | 5 | 3 |
| [wf-p14-wells-fargo-gateway-apis](product-bundles/wf-p14-wells-fargo-gateway-apis/index.md) | Wells Fargo Gateway® APIs (developer portal) | Commercial Banking | 3 | 0 | 0 |
| [wf-p15-commercial-receivables-fraud](product-bundles/wf-p15-commercial-receivables-fraud/index.md) | Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) | Commercial Banking | 2 | 1 | 0 |

See [README.md](README.md) for the layout, citation rules and how to rebuild.

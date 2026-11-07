---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Wells Fargo Gateway® APIs (developer portal): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p14-wells-fargo-gateway-apis",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P14",
  "line_of_business": "wf-cb",
  "content_sha256": "cee24c4daa0f9ff85081905dfc55aa7421f38f5370acb62ef6566e19663d3e81",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Gateway® APIs (developer portal) — product definition

Where it sits in the bank's app and site: developer.wellsfargo.com[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P14-S01` Payments & data APIs | RTP (The Clearing House) | commercial | Instant payments API with rail routing; data & reporting APIs; account validation services.[^2] |
| `WF-P14-S02` Push to Card API (near-real-time disbursement to U.S. debit / GPR prepaid cards) | Push to card | commercial | 'Send payments in near real time to U.S. customer debit cards and general purpose reloadable prepaid cards'; tokenized payment capability to minimize PCI DSS scope; positioned for insurance claims, government tax refunds, and paying 'consumer and small business vendors in near real time'; can be combined with Account Balance API. Listed alongside FedNow, RTP and Zelle as an 'Instant payment method' in commercial marketing.[^3] |
| `WF-P14-S03` Account Validation API (Full Response / Logic Box) and Bank Lookup | Other money movement | commercial | Pre-payment account verification: 'Receive detailed responses to help boost payment accuracy and possibly reduce the cost of returns by accessing status and ownership information from over 750 million accounts' (Full Response) or simplified pass/fail responses (Logic Box); Bank Lookup 'Instantly validate bank routing numbers and retrieve bank information for supported payment types'. Marketed in the commercial hub as 'Account validation services — Reduce transaction fraud with real-time account ownership and account status screening'.[^4] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P14-S01 | WF-P14-S02 | WF-P14-S03 | Detail |
|---|---|---|---|---|
| Cancel before it is sent | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Pay from phone contacts | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Dual approval (business) | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Email or text notifications | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Instant delivery | ✓ | ✓ | ✓ | [^2][^3][^4] |
| International | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Push notifications | ✗ | ✗ | ✗ | [^2][^3][^4] |
| QR code | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Recurring payments | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Request money | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Same-day delivery | ✗ | ✓ | ✓ | [^2][^3][^4] |
| Scam warning before sending | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Schedule for a future date | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Split a payment | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Status tracking | ✓ | ✓ | ✗ | [^2][^3][^4] |
| Step-up authentication | — | — | — | WF-P14-S02: API entitlements; mutual TLS; OAuth2; WF-P14-S03: API entitlements; mutual TLS; OAuth2[^2][^3][^4] |

## Notes from the study

- `WF-P14-S01`: Catalog verified in browser: ACH Payments API v2, Wire Payments API v1 ('Originate freeform or templated wires and check wire status... Straight-through and secondary approval wires are all verified against account entitlements'), Instant Payments API v1, Push to Card API v2, Virtual Card Payments v1, unified Payments API v1 ('Initiate and search for transactions'), Bank Lookup v1, Account Balance v2, Transaction Detail v3, Account Validation (Full Response / Logic Box), Positive Pay v1, Foreign Exchange v3, Commercial User Administration, Dodd-Frank Payment Fees, Image Retrieval v2, UK Open Banking APIs.[^2]
- `WF-P14-S02`: Corrects rail_participation.push_to_card (previously false/INFERRED): Wells Fargo offers push-to-card as a commercial API disbursement product; no consumer-facing push-to-card product found.[^3]
- `WF-P14-S03`: SET_UP/REVIEW-stage fraud control for commercial payment origination; not evidenced for consumer/SMB external-account linking.[^4]

[^1]: kj · product/WF-P14 · 716df6a9b366
[^2]: kj · sub-product/WF-P14-S01 · 7e7c82510c8d
[^3]: kj · sub-product/WF-P14-S02 · 36981c1c1087
[^4]: kj · sub-product/WF-P14-S03 · 63a19ef5a505

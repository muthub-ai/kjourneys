---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Wells Fargo Gateway® APIs (developer portal): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p14-wells-fargo-gateway-apis",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P14",
  "line_of_business": "wf-cb",
  "content_sha256": "3d4882037a43667df6fb6b03a254184cf636b910565e257a0b3f81b4d28ee626",
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

[^1]: kj · product/WF-P14 · 93004be7802c
[^2]: kj · sub-product/WF-P14-S01 · bb13747b48ec
[^3]: kj · sub-product/WF-P14-S02 · 2f2a1f64cc97
[^4]: kj · sub-product/WF-P14-S03 · 828a6dc2853b

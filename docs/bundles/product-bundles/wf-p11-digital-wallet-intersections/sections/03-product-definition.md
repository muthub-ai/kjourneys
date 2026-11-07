---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p11-digital-wallet-intersections",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P11",
  "line_of_business": "wf-cbl",
  "content_sha256": "a1ffc39092f03b1e9d4a6c175e4efbae4d5636503e9d5c874410ae08391b9b24",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital wallet intersections (Paze, PayPal, Apple/Google/Samsung Pay, card-free ATM) — product definition

Where it sits in the bank's app and site: Mobile: Menu > Card Settings > Digital Wallet.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P11-S01` Paze enrollment/activation | Digital wallets | consumer | Consumer debit/credit cards (not business) available in Paze; one-time activation in app or at checkout via email/OTP.[^2] |
| `WF-P11-S02` Add WF card to PayPal / wallets from WF app | Digital wallets | consumer, small-business | Add a Wells Fargo card to digital wallets. Observed (web 'Add Cards to Digital Wallets'): 'Available wallets' offers PayPal push-provisioning directly from the web; Apple Pay / Google Pay are added from the phone via an on-page QR code ('Scan to add cards to digital wallets'); Paze® mark present. Mobile app: Card Settings > Digital Wallet.[^3] |

## Capabilities by sub-product

✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).[^2][^3]

| Capability | WF-P11-S01 | WF-P11-S02 | Detail |
|---|---|---|---|
| Cancel before it is sent | ✗ | ✗ | [^2][^3] |
| Pay from phone contacts | ✗ | ✗ | [^2][^3] |
| Dual approval (business) | ✗ | ✗ | [^2][^3] |
| Email or text notifications | ✗ | ✗ | [^2][^3] |
| Instant delivery | ✗ | ✗ | [^2][^3] |
| International | ✗ | ✗ | [^2][^3] |
| Push notifications | ✗ | ✗ | [^2][^3] |
| QR code | ✗ | ✗ | [^2][^3] |
| Recurring payments | ✗ | ✗ | [^2][^3] |
| Request money | ✗ | ✗ | [^2][^3] |
| Same-day delivery | ✗ | ✗ | [^2][^3] |
| Scam warning before sending | ✗ | ✗ | [^2][^3] |
| Schedule for a future date | ✗ | ✗ | [^2][^3] |
| Split a payment | ✗ | ✗ | [^2][^3] |
| Status tracking | ✗ | ✗ | [^2][^3] |
| Step-up authentication | — | — | WF-P11-S01: OTP to mobile/email at activation; WF-P11-S02: additional verification may be requested[^2][^3] |

## Limits, fees and timing (captured incidentally)

- `WF-J27` — fees: None from WF[^4]

[^1]: kj · product/WF-P11 · df9119f7188e
[^2]: kj · sub-product/WF-P11-S01 · bccee3eda68f
[^3]: kj · sub-product/WF-P11-S02 · 0e74f1f42074
[^4]: kj · journey/WF-J27 · 25ca42f849dc

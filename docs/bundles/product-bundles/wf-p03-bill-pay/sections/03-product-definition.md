---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Bill Pay (Online Bill Pay / Business Bill Pay): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "d07a6b3e93ec7a41407bebc5440aeb5c62e656d44e8d17edaa8f6ed9fad6d36e",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Bill Pay (Online Bill Pay / Business Bill Pay) — product definition

Where it sits in the bank's app and site: Web: 'Transfer and Pay' > Bill Pay ('Add Payee', 'Manage Payee', 'Payment History'). Mobile: Bill Pay in Transfer & Pay. Fargo: 'Which bills are due?'[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P03-S01` Add payee & pay a bill (one-time / scheduled) | Bill pay | consumer, small-business | Add payee manually, browse list or search; schedule up to 1 year ahead; electronic or paper check delivery; 'Send On' date and 'Deliver by' date.[^2] |
| `WF-P03-S02` Auto pay (automatic recurring payments) | Bill pay | consumer, small-business | Set timing and amount rules; service pays recurring bills automatically, including variable-amount eBills.[^3] |
| `WF-P03-S03` eBills | Bill pay | consumer, small-business | Electronic versions of bills viewable/payable/printable in Bill Pay; reminders; activation from Bill Pay home, 'Manage Payee', or new payee setup; WF loan eBills.[^4] |
| `WF-P03-S04` Bill Pay instant payments (RTP, in response to Request for Payment) | RTP (The Clearing House) | consumer, small-business | For participating payees only, in the Wells Fargo Mobile app: pay a payee's Request for Payment instantly; the service 'may use the RTP® network ... or another third party network'; funds typically available within seconds 24/7; cannot be canceled or amended; $50,000 per payment; not excluded from the Bill Pay Payment Guarantee (explicit RfP carve-out).[^5] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P03-S01 | WF-P03-S02 | WF-P03-S03 | WF-P03-S04 | Detail |
|---|---|---|---|---|---|
| Cancel before it is sent | ✓ | ✓ | ✗ | ✗ | [^2][^3][^4][^5] |
| Pay from phone contacts | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Dual approval (business) | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Email or text notifications | ✓ | ✓ | ✓ | ✗ | [^2][^3][^4][^5] |
| Instant delivery | ✗ | ✗ | ✗ | ✓ | [^2][^3][^4][^5] |
| International | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Push notifications | ✓ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| QR code | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Recurring payments | ✓ | ✓ | ✓ | ✗ | [^2][^3][^4][^5] |
| Request money | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Same-day delivery | ✗ | ✗ | ✗ | ✓ | [^2][^3][^4][^5] |
| Scam warning before sending | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Schedule for a future date | ✓ | ✓ | ✗ | ✗ | [^2][^3][^4][^5] |
| Split a payment | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5] |
| Status tracking | ✓ | ✓ | ✓ | ✓ | [^2][^3][^4][^5] |

## Notes from the study

- `WF-P03-S02`: Marketed lowercase 'auto pay'; OAA calls it 'automatic (recurring)' payments.[^3]
- `WF-P03-S04`: Only documented in Online Access Agreement §6(i) and Payment Guarantee exclusions; no marketing page found. Confirms WF consumer RTP send (credit-push) capability.[^5]

## Limits, fees and timing (captured incidentally)

- `WF-J07` — cutoffs: 7 pm PT; funds withdrawn biz day after Send On; 2–5 biz days delivery; fees: None for Bill Pay; a $30 stop-payment fee may apply to stopping a mailed check (general check stop-payment fee); limits: $50,000 per payment (checking); $10,000 business credit card[^6]
- `WF-J08` — cutoffs: Biller approval ≤10 business days; fees: None[^7]
- `WF-J09` — cutoffs: 24/7/365, seconds; fees: Not stated (none documented); limits: $50,000 per payment[^8]
- `WF-J17` — cutoffs: 7 pm PT; fees: None; limits: $10,000 per payment/day on business credit card[^9]

[^1]: kj · product/WF-P03 · b839aacb8026
[^2]: kj · sub-product/WF-P03-S01 · f5bd218ab193
[^3]: kj · sub-product/WF-P03-S02 · 41e23afe6f1e
[^4]: kj · sub-product/WF-P03-S03 · 4de9c1aaf8f5
[^5]: kj · sub-product/WF-P03-S04 · e6c346f56e63
[^6]: kj · journey/WF-J07 · add9e5f0ca96
[^7]: kj · journey/WF-J08 · 3a462c0bcc44
[^8]: kj · journey/WF-J09 · 92c2140a6c2a
[^9]: kj · journey/WF-J17 · adbdce251781

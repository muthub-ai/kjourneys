---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Transfers (Transfer Money): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "d49f084e200e121c7b225416f8ccd6e4a670d174da932799aae8903de82b6191",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — product definition

Where it sits in the bank's app and site: Mobile: 'Transfer' in bottom bar; 'Scheduled Transfers & Payments'. Web: 'Transfer and Pay' > 'Transfer Money' screen ('Add Non-Wells Fargo Accounts' button); 'Transfer and payment Activity' with View/Edit, View/Delete. Fargo: 'Make a payment or transfer'.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P02-S01` Between your accounts (internal transfer) | Internal transfer | consumer, small-business | Same-day immediate transfer between Wells Fargo deposit/credit accounts; future-dated and recurring with Frequency and Memo.[^2] |
| `WF-P02-S02` Bank-to-bank transfers (external, 'Transfer between banks') | ACH external transfer | consumer, small-business | Link an external (non-Wells Fargo) account by routing and account number with an ownership attestation, then transfer to/from it. Observed (web): two account-use tiers — 'Payments only' (pay WF credit accounts from it) vs 'Transfers and payments' (outbound/inbound transfers); upgrading requires 'additional security measures (may take 2-3 business days)'; 'Set up for transfers' on an already-verified payments-only account completed instantly with no review step. No aggregator/credential-login option on the add-account form; 'To transfer money to another person, use Zelle®.'[^3] |
| `WF-P02-S03` Wells Fargo payments (pay WF credit card/loan from WF or external account) | Internal transfer | consumer, small-business | Pay a Wells Fargo credit card or loan from a WF deposit account or a linked external account. Observed (web): 'Pay My Wells Fargo Accounts' is the same single form as Transfer Money (From / To / Frequency / Amount → Continue), with 'Credit card Autopay terms' and a 'Transfer & payment activity' rail listing scheduled items (View / Edit → 'Autopay Details' with the fields From / To / Frequency / Next payment / Ending / Amount option / Status and the actions Delete Autopay / Edit Autopay / One-time payment).[^4] |
| `WF-P02-S04` Saving made easy (automatic recurring savings transfer) | Internal transfer | consumer | Automatic recurring transfers into a WF savings account.[^5] |
| `WF-P02-S05` Brokerage transfers (WellsTrade / Wells Fargo Advisors) | Internal transfer | consumer | Transfers to/from linked brokerage accounts, 1–3 business days; phone 1-800-TRADERS.[^6] |
| `WF-P02-S06` Stop future payments (online ACH debit stop) and Stop a check | Other money movement | consumer | Accounts menu 'Stop Future Payments': select account → Continue → stop a merchant's future ACH debits online. In-page help scopes the online stop to ACH payments: a single check is stopped on the 'Stop a Check' page; a range of checks, a recurring debit-card payment, or a credit-card transaction require a phone call (1-800-869-3557 / number on the card); Bill Pay payments are cancelled on the Bill Pay page.[^7] |

## Capabilities by sub-product

✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).[^2][^3][^4][^5][^6][^7]

| Capability | WF-P02-S01 | WF-P02-S02 | WF-P02-S03 | WF-P02-S04 | WF-P02-S05 | WF-P02-S06 | Detail |
|---|---|---|---|---|---|---|---|
| Cancel before it is sent | ✓ | ✓ | ✓ | ✓ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Pay from phone contacts | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Dual approval (business) | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Email or text notifications | ✓ | ✓ | ✓ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Instant delivery | ✓ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| International | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Push notifications | ✓ | ✓ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| QR code | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Recurring payments | ✓ | ✓ | ✓ | ✓ | ✓ | — | [^2][^3][^4][^5][^6][^7] |
| Request money | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Same-day delivery | ✓ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Scam warning before sending | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Schedule for a future date | ✓ | ✓ | ✓ | ✓ | ✓ | — | [^2][^3][^4][^5][^6][^7] |
| Split a payment | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7] |
| Status tracking | ✓ | ✓ | ✓ | ✗ | ✓ | — | [^2][^3][^4][^5][^6][^7] |
| Step-up authentication | ✗ | — | — | — | — | — | WF-P02-S02: Advanced Access code when receiving from a new non-WF account; additional security measures at add-account[^2][^3][^4][^5][^6][^7] |

## Notes from the study

- `WF-P02-S02`: Transfers FAQ (browser): 'click Add Non-Wells Fargo Accounts to get started... additional security measures are required. Verification may take 1-3 business days'; no instant/aggregator verification offered. Initial delivery speed 2 business days outbound / 3 inbound; 'Depending on your history of transfer activity, expedited transfer options may be available.' Mobile edit/delete: 'select Transfer in the bottom bar, tap on each transfer listed under Scheduled Transfers & Payments, and select Edit Transfer or Delete Transfer'; cutoff 11:59 pm PT the day before. Same-day transfers to Wells Fargo accounts cannot be canceled once submitted.[^3]
- `WF-P02-S06`: Adjacent capability (stop payments), not a transfer rail; observed on web.[^7]

## Limits, fees and timing (captured incidentally)

- `WF-J05` — cutoffs: 8 pm PT availability cutoff; edit until 11:59 pm PT day before; fees: None[^8]
- `WF-J06` — cutoffs: WF→ext 2 biz days; ext→WF 3 biz days; expedited may be offered; fees: None from WF; limits: Not published; higher-limit service discretionary[^9]

[^1]: kj · product/WF-P02 · 9eb25008fe7d
[^2]: kj · sub-product/WF-P02-S01 · 9d6d0e037925
[^3]: kj · sub-product/WF-P02-S02 · 341dc9701a79
[^4]: kj · sub-product/WF-P02-S03 · 3e7dc4b77244
[^5]: kj · sub-product/WF-P02-S04 · be32b5135cc9
[^6]: kj · sub-product/WF-P02-S05 · bd7ce3138d2d
[^7]: kj · sub-product/WF-P02-S06 · 74d7e77234fa
[^8]: kj · journey/WF-J05 · 961155a3b7eb
[^9]: kj · journey/WF-J06 · ee855eb97a21

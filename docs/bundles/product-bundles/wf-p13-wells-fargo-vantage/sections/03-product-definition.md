---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "content_sha256": "f3d0a10b0afcafdab8978918420d937d0a4dcb00f62f13eccc12830674119c3a",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — product definition

Where it sits in the bank's app and site: Sign-on wellsoffice.ceo.wellsfargo.com; Vantage mobile app (iOS/Android, formerly CEO Mobile); Tasks hub; User Profile > App Settings > Mobile token.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P13-S01` ACH origination (payroll, vendor, collections) with ACH Fraud Filter | ACH origination (business) | commercial | ACH payments/collections initiated in Vantage/CEO with dual custody; ACH Fraud Filter Stop/Review decisions in Tasks hub (mobile multi-item pay/return since Nov 2025).[^2] |
| `WF-P13-S02` Wires (domestic, international, FX) with approvals and Wires Status Search | Domestic wire | commercial | Create wires and FX payments in Vantage; Vantage iOS app: approve/reject domestic pending wires (Mar 2026), all pending wires (Jul 2026), wires/federal tax payments/book transfers/drawdowns (Oct 2026); 'Wires Status Search' lifecycle tracking (Sep 2026); wire limits at company/account/user level. Android dates not verified.[^3] |
| `WF-P13-S03` Transfers (book transfers) and drawdowns | Internal transfer | commercial | Create/view/edit/cancel transfers in Vantage mobile (Jul 2025); approve book transfers and drawdowns.[^4] |
| `WF-P13-S04` Instant payments (RTP® / FedNow®) via API with smart rail routing | RTP (The Clearing House) | commercial | 24/7/365 instant payments offered 'through an API channel that routes each payment over the most suitable rail' (RTP or FedNow). Portal-initiated instant payment UI and Request for Payment send not confirmed.[^5] |
| `WF-P13-S05` Consolidated payables (Integrated Payables) | ACH origination (business) | commercial | One file with multiple payment types and remittance detail from ERP/AP with approval in online banking; commercial/virtual card payables.[^6] |
| `WF-P13-S06` Mobile deposit (multi-check) and deposit approvals | Mobile check deposit | commercial | Vantage app: deposit multiple checks, review/approve pending deposits, PDF confirmations.[^7] |
| `WF-P13-S07` Tokenized deposits (on-chain 24/7/365 settlement; USD→GBP pilot) | Other money movement | commercial | 'A blockchain-based representation of commercial bank money that when fully deployed will enable Wells Fargo's corporate and commercial clients to move, program, and settle funds 24/7/365 — without leaving the regulated, insured banking system.' Rolls out fall 2026 for select clients with USD→GBP exchange; expands through 2027 to more clients, countries and currencies. Integrated into the existing offering: payments are automatically routed through tokenized deposits 'when they can improve speed, timing, and flexibility'. Future: always-on settlement between accounts/subsidiaries/counterparties, smart-contract conditional payments, same deposit-insurance eligibility.[^8] |
| `WF-P13-S08` Treasury Management Services for Business Banking (via Vantage) | ACH origination (business) | small-business | Small businesses can enroll in Treasury Management Services delivered through Wells Fargo Vantage and the Vantage app: same-day or future-dated domestic/cross-border wires with approve/reject on smartphone; ACH payments (prepaid credit) for payroll, tax and vendor payments; Desktop Deposit® (scanner) and Vantage mobile deposit; ACH fraud filter pay/return decisions; dual custody, user transaction limits and online user administration; ACH NOC/returns report.[^9] |

## Capabilities by sub-product

✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).[^2][^3][^4][^5][^6][^7][^8][^9]

| Capability | WF-P13-S01 | WF-P13-S02 | WF-P13-S03 | WF-P13-S04 | WF-P13-S05 | WF-P13-S06 | WF-P13-S07 | WF-P13-S08 | Detail |
|---|---|---|---|---|---|---|---|---|---|
| Cancel before it is sent | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Pay from phone contacts | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Dual approval (business) | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Email or text notifications | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Instant delivery | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ | ✗ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| International | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Push notifications | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| QR code | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Recurring payments | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Request money | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Same-day delivery | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Scam warning before sending | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Schedule for a future date | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Split a payment | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Status tracking | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | [^2][^3][^4][^5][^6][^7][^8][^9] |
| Step-up authentication | — | — | — | — | — | — | — | — | WF-P13-S01: RSA SecurID hard token or Vantage mobile token; dual custody; WF-P13-S02: token + dual custody; WF-P13-S08: Vantage credentials + token validation[^2][^3][^4][^5][^6][^7][^8][^9] |

## Notes from the study

- `WF-P13-S04`: Confirmed by the public Instant Payments API v1 reference: 'Send a payment from your Wells Fargo account to another U.S. based bank account via Instant Payments'; GET /instant-payments/v1/routing-numbers/verify/{rtn}?amount= returns instant_payments_enabled, participant_available, payment_rail (RTP | FEDNOW | RTP_and_FEDNOW | INACTIVE), participant_name, supported_messages (CRDT Credit Transfer); POST /credit-transfers (end_to_end_id visible to recipient, duplicate_check lookback days, debtor/creditor/ultimate_debtor, USD only, 18-second timeout); GET /credit-transfers/{uetr} and POST /search return status RECEIVED | PROCESSING | COMPLETED | REJECTED with reason codes IN01, IN02, MM20, MM21, NARR (free text from receiving bank). Commercial hub: 'Our API channel offers intelligent routing — once the payment is initiated, it is sent through the most appropriate rail — RTP® and FedNow®.' No Request for Payment resource in the public v1 reference.[^5]
- `WF-P13-S07`: Announcement-level evidence only; client UI/entitlement flow not published.[^8]
- `WF-P13-S08`: Corrects the chapter view that Vantage/approval workflows are unavailable to small business.[^9]

## Limits, fees and timing (captured incidentally)

- `WF-J20` — limits: Wire limits at company/account/user level[^10]
- `WF-J21` — limits: Wire limits at company/account/user level[^11]
- `WF-J22` — limits: Wire limits at company/account/user level[^12]
- `WF-J23` — limits: Wire limits at company/account/user level[^13]
- `WF-J25` — limits: Wire limits at company/account/user level[^14]

[^1]: kj · product/WF-P13 · 8d686fdb6385
[^2]: kj · sub-product/WF-P13-S01 · d47d872c35b3
[^3]: kj · sub-product/WF-P13-S02 · fcdcd0d9bd23
[^4]: kj · sub-product/WF-P13-S03 · 09da1d723a6a
[^5]: kj · sub-product/WF-P13-S04 · b1d1dec413e7
[^6]: kj · sub-product/WF-P13-S05 · f44e78fc1421
[^7]: kj · sub-product/WF-P13-S06 · d87de4a70317
[^8]: kj · sub-product/WF-P13-S07 · f793bcdc6041
[^9]: kj · sub-product/WF-P13-S08 · c4c278b878d7
[^10]: kj · journey/WF-J20 · a09dfa7d417c
[^11]: kj · journey/WF-J21 · a9e16e59c03f
[^12]: kj · journey/WF-J22 · 30a8718f1eaf
[^13]: kj · journey/WF-J23 · 194624059efa
[^14]: kj · journey/WF-J25 · 982023d3f4b5

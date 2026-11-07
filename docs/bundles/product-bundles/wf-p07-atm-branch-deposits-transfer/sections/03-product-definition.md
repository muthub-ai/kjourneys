---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "ATM & branch deposits/transfers: sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p07-atm-branch-deposits-transfer",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P07",
  "line_of_business": "wf-cbl",
  "content_sha256": "849580f04edb2952bf609fd54b0bd851b1ac7663c44cb3570532862c0075a4ba",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ATM & branch deposits/transfers — product definition

Where it sits in the bank's app and site: ATM menu (transfers, credit card payment, deposits); Contactless Symbol for wallet/contactless card access.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P07-S01` ATM deposit (cash/check) and ATM transfer/payment | Cash, ATM and branch | consumer, small-business | Scan checks and count bills at ATM; transfer between personal or business accounts; pay WF credit card; 9 pm local cutoff; receipts by text/email/secure inbox.[^2] |
| `WF-P07-S02` Branch wire / branch deposit | Cash, ATM and branch | consumer, small-business | Branch-initiated wires for amounts above digital limits or when digital wire cannot be completed; $40 branch wire fee.[^3] |
| `WF-P07-S03` Cashier's checks (online order) and money orders (branch) | Other money movement | consumer, small-business | Cashier's check ordered online ('Order a cashier's check': payable to ≤87 characters, amount, account to charge, terms checkbox → Submit; request 'reviewed and approved', then shipped by express delivery with signature required; U.S. addresses only, no PO Boxes; $2,000 per check and $6,000 per month per customer — observed) or at a branch; money orders at branch only.[^4] |
| `WF-P07-S04` Foreign currency cash order (online; branch pickup required over $3,000) | Cash, ATM and branch | consumer | Accounts menu 'Foreign Currency' → 'Order Foreign Currency Cash': Check Rates; choose currency and amount (in USD or the foreign currency) → Calculate → order basket of up to 5 currencies. Minimum order $200; orders over $3,000 USD must be picked up at a branch; branches no longer sell foreign currency cash over the counter for same-day purchase; business accounts must order in a branch.[^5] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P07-S01 | WF-P07-S02 | WF-P07-S03 | WF-P07-S04 | Detail |
|---|---|---|---|---|---|
| Cancel before it is sent | ✗ | ✗ | — | — | [^2][^3][^4][^5] |
| Pay from phone contacts | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Dual approval (business) | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Email or text notifications | ✓ | ✗ | — | — | [^2][^3][^4][^5] |
| Instant delivery | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| International | ✗ | ✓ | ✗ | ✓ | [^2][^3][^4][^5] |
| Push notifications | ✗ | ✗ | — | — | [^2][^3][^4][^5] |
| QR code | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Recurring payments | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Request money | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Same-day delivery | ✓ | ✓ | ✗ | — | [^2][^3][^4][^5] |
| Scam warning before sending | ✗ | ✗ | — | — | [^2][^3][^4][^5] |
| Schedule for a future date | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Split a payment | ✗ | ✗ | ✗ | — | [^2][^3][^4][^5] |
| Status tracking | ✓ | ✗ | — | — | [^2][^3][^4][^5] |

## Notes from the study

- `WF-P07-S03`: Online-services fee schedule (verification pass).[^4]

## Limits, fees and timing (captured incidentally)

- `WF-J14` — cutoffs: 9 pm local; fees: None[^6]

[^1]: kj · product/WF-P07 · 4fe5c088f5d6
[^2]: kj · sub-product/WF-P07-S01 · 8a11b3f23726
[^3]: kj · sub-product/WF-P07-S02 · 08f430a9459d
[^4]: kj · sub-product/WF-P07-S03 · f542571f980a
[^5]: kj · sub-product/WF-P07-S04 · c012027ab795
[^6]: kj · journey/WF-J14 · 5120bc547ac2

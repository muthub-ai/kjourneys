---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Digital Wires (Wire Money): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "fca5490f3ebddfa6d0731b03e5a17206cd86f3f48d1c93e265f789f90e5548b3",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital Wires (Wire Money) — product definition

Where it sits in the bank's app and site: Web/mobile: 'Transfer & Pay' > 'Wire Money'; sub-pages 'Recipients', 'Recipient's bank info', wire 'Activity', 'Wire details'. Enrollment deep link serviceType=digitalwires.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P04-S01` Domestic wire (USD) | Domestic wire | consumer, small-business | Same-business-day if by 3:00 pm PT; recipient saved for reuse; statuses Scheduled/Pending/Completed/Failed/Canceled/Returned/Under review.[^2] |
| `WF-P04-S02` International wire (USD or foreign currency) | International wire | consumer, small-business | SWIFT/BIC + IBAN/country codes (BSB, CLABE, IFSC, Sort Code, etc.); foreign-currency option locks rate; consumer FX wires $0 fee; 30-minute cancellation right for consumer international wires (Reg E remittance).[^3] |
| `WF-P04-S03` Receive incoming wire | Domestic wire | consumer, small-business | Domestic ABA 121000248; SWIFT WFBIUS6S; incoming FX converted to USD without notice; no incoming fee for consumer/non-analyzed business, $15 analyzed.[^4] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P04-S01 | WF-P04-S02 | WF-P04-S03 | Detail |
|---|---|---|---|---|
| Cancel before it is sent | ✓ | ✓ | ✗ | [^2][^3][^4] |
| Pay from phone contacts | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Dual approval (business) | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Email or text notifications | ✓ | ✓ | ✗ | [^2][^3][^4] |
| Instant delivery | ✗ | ✗ | ✗ | [^2][^3][^4] |
| International | ✗ | ✓ | ✓ | [^2][^3][^4] |
| Push notifications | ✓ | ✗ | ✗ | [^2][^3][^4] |
| QR code | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Recurring payments | ✓ | ✓ | ✗ | [^2][^3][^4] |
| Request money | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Same-day delivery | ✓ | ✗ | ✗ | [^2][^3][^4] |
| Scam warning before sending | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Schedule for a future date | ✓ | ✓ | ✗ | [^2][^3][^4] |
| Split a payment | ✗ | ✗ | ✗ | [^2][^3][^4] |
| Status tracking | ✓ | ✓ | ✓ | [^2][^3][^4] |
| Step-up authentication | — | — | — | WF-P04-S01: Required: valid U.S. mobile number (text code) or RSA SecurID device; WF-P04-S02: U.S. mobile text code or RSA SecurID[^2][^3][^4] |

## Notes from the study

- `WF-P04-S01`: Recurring and future-dated wires (Preauthorized Orders) per OAA §8(h).[^2]

## Limits, fees and timing (captured incidentally)

- `WF-J10` — cutoffs: 3:00 pm PT domestic; 4:30 pm PT WF-to-WF; fees: $30 digital (waivable), $40 branch; incoming $0 consumer; limits: Daily and rolling 30-day, recipient-specific, undisclosed[^5]
- `WF-J11` — cutoffs: 2:20 pm PT international; fees: $30 USD international; $0 foreign-currency (consumer); FX markup; limits: Undisclosed[^6]
- `WF-J18` — cutoffs: 2:20 pm PT; fees: $30 USD; $0 FX (non-analyzed); $25 analyzed; limits: Daily/30-day undisclosed[^7]

[^1]: kj · product/WF-P04 · 7ae69c334eed
[^2]: kj · sub-product/WF-P04-S01 · 3c9c3eb660ba
[^3]: kj · sub-product/WF-P04-S02 · 474bb477f97e
[^4]: kj · sub-product/WF-P04-S03 · 7ef4ebeda48b
[^5]: kj · journey/WF-J10 · 47452d55448b
[^6]: kj · journey/WF-J11 · e4ed66bc72f0
[^7]: kj · journey/WF-J18 · 7f1916a52a55

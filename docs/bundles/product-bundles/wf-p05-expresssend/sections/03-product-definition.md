---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "ExpressSend®: sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "798e9833f261a090d32c7ec099cf8ef220f35073ce9e429b17784364b54a56a8",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ExpressSend® — product definition

Where it sits in the bank's app and site: Mobile: 'Pay & Transfer' (a.k.a. Transfer & Pay) > 'Transfer Internationally' (ExpressSend) > 'Who are you sending to?' / 'How much are you sending?' / 'Activity'. Enrollment deep link serviceType=ExpressSendNative.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P05-S01` Send to bank account abroad | Remittance | consumer | Credit to recipient's qualifying account (CLABE for Mexico, IFSC for India); paid in local currency for MX/DO/GT/HN/CO/IN/PH and USD for EC/SV/NI/PE/VN.[^2] |
| `WF-P05-S02` Send for cash pickup | Remittance | consumer | Recipient collects cash at supported location with government ID matching name exactly (fingerprint/photo may be required); 15 days to collect, else auto-cancel and refund.[^3] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P05-S01 | WF-P05-S02 | Detail |
|---|---|---|---|
| Cancel before it is sent | ✓ | ✓ | [^2][^3] |
| Pay from phone contacts | ✗ | ✗ | [^2][^3] |
| Dual approval (business) | ✗ | ✗ | [^2][^3] |
| Email or text notifications | ✓ | ✗ | [^2][^3] |
| Instant delivery | ✗ | ✗ | [^2][^3] |
| International | ✓ | ✓ | [^2][^3] |
| Push notifications | ✗ | ✗ | [^2][^3] |
| QR code | ✗ | ✗ | [^2][^3] |
| Recurring payments | ✗ | ✗ | [^2][^3] |
| Request money | ✗ | ✗ | [^2][^3] |
| Same-day delivery | ✓ | ✓ | [^2][^3] |
| Scam warning before sending | ✗ | ✗ | [^2][^3] |
| Schedule for a future date | ✗ | ✗ | [^2][^3] |
| Split a payment | ✗ | ✗ | [^2][^3] |
| Status tracking | ✓ | ✓ | [^2][^3] |

## Notes from the study

- `WF-P05-S01`: Account-credit Remittance Network Members by country captured (see product network_or_vendor); beneficiary account must be denominated in the receiving currency (local currency for Mexico, DR, Guatemala, Honduras, Colombia, India, Philippines; USD for Ecuador, El Salvador, Nicaragua, Peru, Vietnam). Estimator data shows per-member daily/30-day limits (e.g., Colombia $1,500/day; Ecuador $1,000/day; minimum $25). Up to 10 recipients in mobile. Legacy web cancel path: 'Transfer and Pay' > 'Send to Another Country' > 'History' > select remittance.[^2]
- `WF-P05-S02`: Cash-pickup Remittance Network Members by country captured (retail chains such as Soriana, Walmart, Bodega Aurrera, Farmacias Guadalajara, Grupo Éxito, M. Lhuillier, Cebuana Lhuillier are cash-pickup only). Recipient name must exactly match government ID; 'Any cash pick-up transfer not picked up by the recipient within 15 days will be canceled without notice' and refunded to the funding account (check mailed if account closed). Cash pickup issues: 1-800-556-0605.[^3]

## Limits, fees and timing (captured incidentally)

- `WF-J12` — cutoffs: Same business day for many locations; fees: Per-country $3–$12; first mobile transfer free; limits: $25 min; $5,000/day; $12,500/30 days; 10 recipients[^4]

[^1]: kj · product/WF-P05 · 4247b60967aa
[^2]: kj · sub-product/WF-P05-S01 · 9697c6c44150
[^3]: kj · sub-product/WF-P05-S02 · dfcb6ac16268
[^4]: kj · journey/WF-J12 · 94fc27116502

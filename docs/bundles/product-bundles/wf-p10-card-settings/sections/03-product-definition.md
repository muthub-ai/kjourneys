---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠: sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p10-card-settings",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P10",
  "line_of_business": "wf-cbl",
  "content_sha256": "6ccee7c1b0b640d1068f6e98fd382f5cf7a9e9eea9cc6361e793a3e7c4f1ce82",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ — product definition

Where it sits in the bank's app and site: Mobile: Menu > Card Settings — 'Easily activate or turn cards on or off, add cards to digital wallets, view recurring payments, and manage account access with Card Settings' (App Store description). Fargo prompt 'I need to turn my card off.' Business mobile: 'Card Controls'. The 'Control Tower' label no longer appears on any public page (all landing/FAQ URLs 404; site search empty).[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P10-S01` View recurring payments & subscriptions on card; card on/off | Other money movement | consumer, small-business | Card Controls (web 'Turn Card On or Off'; app 'Card Settings', formerly Control Tower): per card — Card details · Card On or Off · International usage on/off · Digital wallets panel (wallets the card is provisioned to) · Recurring payments & subscriptions panel (merchants on file). Disclosure: turning a card off is not a replacement for reporting it lost or stolen. (Observed on web.)[^2] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P10-S01 | Detail |
|---|---|---|
| Cancel before it is sent | ✗ | [^2] |
| Pay from phone contacts | ✗ | [^2] |
| Dual approval (business) | ✗ | [^2] |
| Email or text notifications | ✗ | [^2] |
| Instant delivery | ✗ | [^2] |
| International | ✗ | [^2] |
| Push notifications | ✓ | [^2] |
| QR code | ✗ | [^2] |
| Recurring payments | ✗ | [^2] |
| Request money | ✗ | [^2] |
| Same-day delivery | ✗ | [^2] |
| Scam warning before sending | ✗ | [^2] |
| Schedule for a future date | ✗ | [^2] |
| Split a payment | ✗ | [^2] |
| Status tracking | ✓ | [^2] |

[^1]: kj · product/WF-P10 · ae4ea79539a2
[^2]: kj · sub-product/WF-P10-S01 · 4dcbb04ef48b

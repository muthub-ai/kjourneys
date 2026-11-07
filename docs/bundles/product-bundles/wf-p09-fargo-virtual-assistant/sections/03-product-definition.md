---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Fargo® virtual assistant: sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "7ef0c16d2fdf7b9cb2a45b8f5630fd209a44754a6fc39f4fae6c795023566ad4",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — product definition

Where it sits in the bank's app and site: Mobile: purple Fargo icon in the search bar; type or tap microphone.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P09-S01` Fargo-initiated Zelle send / transfer / bill view | Zelle | consumer | Conversational initiation of a Zelle payment to a stored contact or an account transfer; confirms in the standard flow.[^2] |

## Capabilities by sub-product

✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).[^2]

| Capability | WF-P09-S01 | Detail |
|---|---|---|
| Cancel before it is sent | ✗ | [^2] |
| Pay from phone contacts | ✓ | [^2] |
| Dual approval (business) | ✗ | [^2] |
| Email or text notifications | ✗ | [^2] |
| Instant delivery | ✓ | [^2] |
| International | ✗ | [^2] |
| Push notifications | ✗ | [^2] |
| QR code | ✗ | [^2] |
| Recurring payments | ✗ | [^2] |
| Request money | ✗ | [^2] |
| Same-day delivery | ✗ | [^2] |
| Scam warning before sending | ✗ | [^2] |
| Schedule for a future date | ✗ | [^2] |
| Split a payment | ✗ | [^2] |
| Status tracking | ✓ | [^2] |

## Notes from the study

- `WF-P09-S01`: Fargo page video transcripts cover balance forecast, spending summary and bills ('Here's what I found. Which would you like to pay?'); no transcript or FAQ describes the confirmation screen for a Fargo-initiated Zelle send. Mar 2026 press release confirms Fargo is used for 'sending money with Zelle®, paying bills, locating routing numbers'. Confirmation UX remains INFERRED (standard Zelle review + first-time-recipient access code).[^2]

[^1]: kj · product/WF-P09 · 87601a523c62
[^2]: kj · sub-product/WF-P09-S01 · c81b73e86911

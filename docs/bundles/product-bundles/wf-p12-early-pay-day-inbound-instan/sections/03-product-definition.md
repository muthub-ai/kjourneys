---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): sub-products, capabilities per sub-product, notes, limits and fees",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "7910bc017082b440459b1b6959cd330113dd1e79f983999e2f86a7ee22b54e61",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — product definition

Where it sits in the bank's app and site: Automatic; deposit alerts via 'Manage Alerts'.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P12-S01` Receive RTP / FedNow instant credit | RTP (The Clearing House) | consumer, small-business | Inbound instant payments post to WF accounts (evidenced only by Early Pay Day exclusion list and TCH participant list); customer-facing status/labels UNKNOWN.[^2] |
| `WF-P12-S02` Early Pay Day (ACH direct deposit early availability) | Other money movement | consumer | Up to 2 business days early, timing varies with payor file receipt; alerts optional.[^3] |
| `WF-P12-S03` Set up direct deposit (prefilled form generator) | Other money movement | consumer | Accounts menu 'Set Up Direct Deposit' → 'Prefill your direct deposit form': 3 steps (select up to 3 accounts → allocate deposits across them → verify) → 'Create Form' produces a prefilled PDF to 'provide … to the company or agency that pays you'; 'Or download a blank form'. With one account the allocation step is skipped. No embedded payroll-provider switch (no employer search / credential-based switch).[^4] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P12-S01 | WF-P12-S02 | WF-P12-S03 | Detail |
|---|---|---|---|---|
| Cancel before it is sent | ✗ | ✗ | — | [^2][^3][^4] |
| Pay from phone contacts | ✗ | ✗ | — | [^2][^3][^4] |
| Dual approval (business) | ✗ | ✗ | — | [^2][^3][^4] |
| Email or text notifications | ✓ | ✓ | — | [^2][^3][^4] |
| Instant delivery | ✓ | ✗ | — | [^2][^3][^4] |
| International | ✗ | ✗ | — | [^2][^3][^4] |
| Push notifications | ✓ | ✓ | — | [^2][^3][^4] |
| QR code | ✗ | ✗ | — | [^2][^3][^4] |
| Recurring payments | ✗ | ✗ | — | [^2][^3][^4] |
| Request money | ✗ | ✗ | — | [^2][^3][^4] |
| Same-day delivery | ✗ | ✗ | — | [^2][^3][^4] |
| Scam warning before sending | ✗ | ✗ | — | [^2][^3][^4] |
| Schedule for a future date | ✗ | ✗ | — | [^2][^3][^4] |
| Split a payment | ✗ | ✗ | — | [^2][^3][^4] |
| Status tracking | ✓ | ✓ | — | [^2][^3][^4] |

## Notes from the study

- `WF-P12-S01`: Receive capability confirmed; Early Pay Day footnote: 'instant payments processed through the RTP® network or FedNow℠ service... are not eligible for Early Pay Day' (they post as ordinary credits). How they are labeled in Account Activity still not published.[^2]
- `WF-P12-S03`: Mobile path published as 'create Direct Deposit form in app' (S025); web observed.[^4]

## Limits, fees and timing (captured incidentally)

- `WF-J15` — cutoffs: ACH up to 2 business days early; fees: None[^5]

[^1]: kj · product/WF-P12 · d73da35d0cb8
[^2]: kj · sub-product/WF-P12-S01 · cdbc7b849c06
[^3]: kj · sub-product/WF-P12-S02 · df182af38e17
[^4]: kj · sub-product/WF-P12-S03 · 9a2db967acf9
[^5]: kj · journey/WF-J15 · e61f32bb5fb1

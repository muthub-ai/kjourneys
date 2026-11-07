---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "ExpressSend®: stage scores against best practice, gaps and strengths",
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
  "content_sha256": "8b865aaa249e59cf07ba21f21e7aa2fdb179d74d63ac2ca1c2f35ec40406de33",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ExpressSend® — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Remittance | Discover | 2 | 4 | −2[^1] |
| Remittance | Set up | 4 | 4 | at best practice[^2] |
| Remittance | Initiate | 3 | 4 | −1[^3] |
| Remittance | Review & authorize | 3 | 3 | at best practice[^4] |
| Remittance | Execute & track | 4 | 4 | at best practice[^5] |
| Remittance | Confirm & complete | 3 | 3 | at best practice[^6] |
| Remittance | Manage | 2 | 3 | −1[^7] |
| Remittance | Exception | 3 | 3 | at best practice[^8] |
| Remittance | Support | 3 | 3 | at best practice[^9] |

## Gaps

- **medium** · Manage · missing capability · ExpressSend supports neither recurring nor future-dated transfers on either service track.[^10]
- **medium** · Discover · channel gap · ExpressSend is migrating to app-only: accepting mobile terms removes branch, web and phone access, leaving two parallel service tracks with different labels. Corroborated on the web (Nov 2026, S990): the logged-in hub item 'Send with ExpressSend®' routes to a public page ('Send it in the app').[^11]

## Strengths

- Set up · ExpressSend offers cash pickup at named retail partners in 12 countries, the only proprietary cash-pickup remittance among the ten.[^12]
- Execute & track · ExpressSend Mobile (nationwide Sep 2026): real-time tracking and alerts, upfront fee/FX display, first-transfer fee waiver.[^13]

[^1]: kj · score/remittance/discover · 17a0bd5ea943
[^2]: kj · score/remittance/set-up · 49ae40d3e583
[^3]: kj · score/remittance/initiate · b5762c609a52
[^4]: kj · score/remittance/review-authorize · 1e5fe25e9536
[^5]: kj · score/remittance/execute-track · f45bd4e64a0d
[^6]: kj · score/remittance/confirm-complete · 1e5fe25e9536
[^7]: kj · score/remittance/manage · 716e589ec4d5
[^8]: kj · score/remittance/exception · 1e5fe25e9536
[^9]: kj · score/remittance/support · 1e5fe25e9536
[^10]: kj · finding/GAP-WF-0018 · 59b1c988973b
[^11]: kj · finding/GAP-WF-0019 · e5190615f7b0
[^12]: kj · finding/STR-WF-0008 · a381b8d38fc5
[^13]: kj · finding/STR-WF-0009 · 376b9cc3c369

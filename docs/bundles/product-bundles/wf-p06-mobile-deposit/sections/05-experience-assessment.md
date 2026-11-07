---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Mobile Deposit (Wells Fargo Mobile® Deposit): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p06-mobile-deposit",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P06",
  "line_of_business": "wf-cbl",
  "content_sha256": "ab9754a6bbb2dd2c80df11ef940170a713053b7eddfbdf66f29c25c9e618956f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Mobile Deposit (Wells Fargo Mobile® Deposit) — experience assessment

Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.[^1]

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Mobile check deposit | Discover | 4 | 4 | at best practice[^1] |
| Mobile check deposit | Set up | 3 | 3 | at best practice[^2] |
| Mobile check deposit | Initiate | 3 | 3 | at best practice[^3] |
| Mobile check deposit | Review & authorize | 3 | 4 | −1[^4] |
| Mobile check deposit | Execute & track | 3 | 4 | −1[^5] |
| Mobile check deposit | Confirm & complete | 4 | 4 | at best practice[^6] |
| Mobile check deposit | Manage | 3 | 3 | at best practice[^7] |
| Mobile check deposit | Exception | 3 | 4 | −1[^8] |
| Mobile check deposit | Support | 3 | 3 | at best practice[^9] |

## Gaps

- **low** · Exception · transparency · Returned-check notice is a written letter; no digital return notification documented.[^10]

## Strengths

- Discover · Mobile Deposit shows remaining daily and 30-day limits on screen before capture.[^11]
- Confirm & complete · Three-channel deposit confirmation: screen, email and Message Center.[^12]

[^1]: kj · score/check-deposit-mobile/discover · 62fc95092d77
[^2]: kj · score/check-deposit-mobile/set-up · 2f2b9ba349d5
[^3]: kj · score/check-deposit-mobile/initiate · 2f2b9ba349d5
[^4]: kj · score/check-deposit-mobile/review-authorize · c9bee44ca271
[^5]: kj · score/check-deposit-mobile/execute-track · c9bee44ca271
[^6]: kj · score/check-deposit-mobile/confirm-complete · a70b283d9e5e
[^7]: kj · score/check-deposit-mobile/manage · 2f2b9ba349d5
[^8]: kj · score/check-deposit-mobile/exception · b562608e90bd
[^9]: kj · score/check-deposit-mobile/support · 2f2b9ba349d5
[^10]: kj · finding/GAP-WF-0032 · aaf39ff632ca
[^11]: kj · finding/STR-WF-0012 · 3dff85a0574b
[^12]: kj · finding/STR-WF-0013 · ff17d44548b8

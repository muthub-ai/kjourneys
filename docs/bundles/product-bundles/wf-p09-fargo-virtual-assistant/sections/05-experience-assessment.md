---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Fargo® virtual assistant: stage scores against best practice, gaps and strengths",
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
  "content_sha256": "f1c548cc554bd7a3295744b6271f2cf4f69f067c08b4c8bd85d0a06e1ae7a75e",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — experience assessment

Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.[^1]

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Bill pay | Discover | 3 | 3 | at best practice[^1] |
| Bill pay | Set up | 3 | 3 | at best practice[^2] |
| Bill pay | Initiate | 3 | 4 | −1[^3] |
| Bill pay | Review & authorize | 3 | 3 | at best practice[^4] |
| Bill pay | Execute & track | 3 | 3 | at best practice[^5] |
| Bill pay | Confirm & complete | 3 | 3 | at best practice[^6] |
| Bill pay | Manage | 3 | 3 | at best practice[^7] |
| Bill pay | Exception | 3 | 3 | at best practice[^8] |
| Bill pay | Support | 3 | 3 | at best practice[^9] |
| Internal transfer | Discover | 3 | 4 | −1[^10] |
| Internal transfer | Set up | 3 | 3 | at best practice[^11] |
| Internal transfer | Initiate | 3 | 4 | −1[^12] |
| Internal transfer | Review & authorize | 3 | 3 | at best practice[^13] |
| Internal transfer | Execute & track | 3 | 3 | at best practice[^14] |
| Internal transfer | Confirm & complete | 3 | 3 | at best practice[^15] |
| Internal transfer | Manage | 3 | 3 | at best practice[^16] |
| Internal transfer | Exception | 3 | 3 | at best practice[^17] |
| Internal transfer | Support | 3 | 4 | −1[^18] |
| Zelle | Discover | 3 | 3 | at best practice[^19] |
| Zelle | Set up | 3 | 3 | at best practice[^20] |
| Zelle | Initiate | 3 | 3 | at best practice[^21] |
| Zelle | Review & authorize | 1 | 3 | −2[^22] |
| Zelle | Execute & track | 3 | 3 | at best practice[^23] |
| Zelle | Confirm & complete | 3 | 3 | at best practice[^24] |
| Zelle | Manage | 3 | 3 | at best practice[^25] |
| Zelle | Exception | 2 | 2 | at best practice[^26] |
| Zelle | Support | 2 | 3 | −1[^27] |

## Gaps

- **low** · Support · transparency · Fargo can initiate a Zelle send, but its confirmation UX is unpublished (INFERRED hand-off to the standard review screen).[^28]

## Strengths

None recorded in this study.[^29]

[^1]: kj · score/bill-pay/discover · 992518b75df6
[^2]: kj · score/bill-pay/set-up · 992518b75df6
[^3]: kj · score/bill-pay/initiate · 1c0b06399f9f
[^4]: kj · score/bill-pay/review-authorize · 992518b75df6
[^5]: kj · score/bill-pay/execute-track · 992518b75df6
[^6]: kj · score/bill-pay/confirm-complete · 992518b75df6
[^7]: kj · score/bill-pay/manage · 53ac3b61085d
[^8]: kj · score/bill-pay/exception · 5a0578a2664c
[^9]: kj · score/bill-pay/support · 992518b75df6
[^10]: kj · score/internal-transfer/discover · 5e0adabac2df
[^11]: kj · score/internal-transfer/set-up · ad9fea561b11
[^12]: kj · score/internal-transfer/initiate · b6f4a071e141
[^13]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^14]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^15]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^16]: kj · score/internal-transfer/manage · fdb4992e1029
[^17]: kj · score/internal-transfer/exception · 6e98a0705895
[^18]: kj · score/internal-transfer/support · b6f4a071e141
[^19]: kj · score/zelle/discover · 2bd0b74d37f1
[^20]: kj · score/zelle/set-up · f3093057d59e
[^21]: kj · score/zelle/initiate · 673a47124b13
[^22]: kj · score/zelle/review-authorize · c20c7f17c2eb
[^23]: kj · score/zelle/execute-track · 02cb1535a9b8
[^24]: kj · score/zelle/confirm-complete · 02cb1535a9b8
[^25]: kj · score/zelle/manage · 8d99b809a6a4
[^26]: kj · score/zelle/exception · 5cd8d0e17f2b
[^27]: kj · score/zelle/support · 850a938312d2
[^28]: kj · finding/GAP-WF-0005 · aed989733509
[^29]: kj · product/WF-P09 · 87601a523c62

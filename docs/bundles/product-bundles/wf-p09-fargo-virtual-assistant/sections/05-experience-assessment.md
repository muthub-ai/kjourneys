---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Fargo® virtual assistant: stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p09-fargo-virtual-assistant",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P09",
  "line_of_business": "wf-cbl",
  "content_sha256": "9cd85e75640baa8bd0cdc0e153c494ea4021dd0b8f62d5ac40d1a32329e6bd16",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Fargo® virtual assistant — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. From report v2, each score is the mean across MI's customer journeys, so half points occur. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Bill pay | Discover | 3 | 3.5 | −0.5[^1] |
| Bill pay | Set up | 3 | 3 | at best practice[^2] |
| Bill pay | Initiate | 3 | 4 | −1[^3] |
| Bill pay | Review & authorize | 3 | 3 | at best practice[^4] |
| Bill pay | Execute & track | 3 | 3 | at best practice[^5] |
| Bill pay | Confirm & complete | 3 | 3 | at best practice[^6] |
| Bill pay | Manage | 3 | 3 | at best practice[^7] |
| Bill pay | Exception | 3.5 | 3.5 | at best practice[^8] |
| Bill pay | Support | 3 | 3.5 | −0.5[^9] |
| Internal transfer | Discover | 3 | 4 | −1[^10] |
| Internal transfer | Set up | 3 | 3 | at best practice[^11] |
| Internal transfer | Initiate | 3 | 4 | −1[^12] |
| Internal transfer | Review & authorize | 3 | 3 | at best practice[^13] |
| Internal transfer | Execute & track | 3 | 3 | at best practice[^14] |
| Internal transfer | Confirm & complete | 3 | 3 | at best practice[^15] |
| Internal transfer | Manage | 3 | 3 | at best practice[^16] |
| Internal transfer | Exception | 3 | 3 | at best practice[^17] |
| Internal transfer | Support | 3 | 4 | −1[^18] |
| Zelle | Discover | 3.5 | 3.5 | at best practice[^19] |
| Zelle | Set up | 3.5 | 3.5 | at best practice[^20] |
| Zelle | Initiate | 3 | 3 | at best practice[^21] |
| Zelle | Review & authorize | 1 | 3.5 | −2.5[^22] |
| Zelle | Execute & track | 3 | 3 | at best practice[^23] |
| Zelle | Confirm & complete | 3 | 3 | at best practice[^24] |
| Zelle | Manage | 3.5 | 3.5 | at best practice[^25] |
| Zelle | Exception | 2 | 2 | at best practice[^26] |
| Zelle | Support | 2.5 | 3.5 | −1.0[^27] |

## Gaps

- **low** · Support · transparency · Fargo can initiate a Zelle send, but its confirmation UX is unpublished (INFERRED hand-off to the standard review screen).[^28]

## Strengths

None recorded in this study.[^29]

[^1]: kj · score/bill-pay/discover · 8e100b7ea6ea
[^2]: kj · score/bill-pay/set-up · 992518b75df6
[^3]: kj · score/bill-pay/initiate · 29efc9575cbb
[^4]: kj · score/bill-pay/review-authorize · 992518b75df6
[^5]: kj · score/bill-pay/execute-track · 992518b75df6
[^6]: kj · score/bill-pay/confirm-complete · 992518b75df6
[^7]: kj · score/bill-pay/manage · 53ac3b61085d
[^8]: kj · score/bill-pay/exception · c5079ab325b6
[^9]: kj · score/bill-pay/support · 8e100b7ea6ea
[^10]: kj · score/internal-transfer/discover · 6bf8de0e67f3
[^11]: kj · score/internal-transfer/set-up · ad9fea561b11
[^12]: kj · score/internal-transfer/initiate · b6f4a071e141
[^13]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^14]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^15]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^16]: kj · score/internal-transfer/manage · fdb4992e1029
[^17]: kj · score/internal-transfer/exception · c5eb205122b4
[^18]: kj · score/internal-transfer/support · b6f4a071e141
[^19]: kj · score/zelle/discover · 2e480e051cdf
[^20]: kj · score/zelle/set-up · da3bfa89785c
[^21]: kj · score/zelle/initiate · b619e43b371b
[^22]: kj · score/zelle/review-authorize · 7f32aa3fe19c
[^23]: kj · score/zelle/execute-track · 02cb1535a9b8
[^24]: kj · score/zelle/confirm-complete · 02cb1535a9b8
[^25]: kj · score/zelle/manage · aef7039d70a0
[^26]: kj · score/zelle/exception · 89e1f8bb4e9d
[^27]: kj · score/zelle/support · 0f0e3acf9195
[^28]: kj · finding/GAP-WF-0005 · 23ad46977fbc
[^29]: kj · product/WF-P09 · 4787881df475

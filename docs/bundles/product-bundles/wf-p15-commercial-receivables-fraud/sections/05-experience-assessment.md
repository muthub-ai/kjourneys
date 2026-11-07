---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p15-commercial-receivables-fraud",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P15",
  "line_of_business": "wf-cb",
  "content_sha256": "f4cd779724757836b774847d187a99ce5a69613a1b73c68cef13c47e5ee0903d",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — experience assessment

Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.[^1]

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| ACH origination (business) | Discover | 1 | 3 | −2[^1] |
| ACH origination (business) | Set up | 4 | 4 | at best practice[^2] |
| ACH origination (business) | Initiate | 2 | 4 | −2[^3] |
| ACH origination (business) | Review & authorize | 1 | 4 | −3[^4] |
| ACH origination (business) | Execute & track | 3 | 4 | −1[^5] |
| ACH origination (business) | Confirm & complete | 3 | 3 | at best practice[^6] |
| ACH origination (business) | Manage | 2 | 3 | −1[^7] |
| ACH origination (business) | Exception | 2 | 4 | −2[^8] |
| ACH origination (business) | Support | 3 | 3 | at best practice[^9] |
| Domestic wire | Discover | 3 | 3 | at best practice[^10] |
| Domestic wire | Set up | 3 | 4 | −1[^11] |
| Domestic wire | Initiate | 2 | 3 | −1[^12] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^13] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^14] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^15] |
| Domestic wire | Manage | 3 | 3 | at best practice[^16] |
| Domestic wire | Exception | 2 | 3 | −1[^17] |
| Domestic wire | Support | 3 | 3 | at best practice[^18] |

## Gaps

None recorded in this study.[^19]

## Strengths

None recorded in this study.[^19]

[^1]: kj · score/ach-origination/discover · a46a68a0fbe7
[^2]: kj · score/ach-origination/set-up · 82fdfd419043
[^3]: kj · score/ach-origination/initiate · 7fb1c066e3db
[^4]: kj · score/ach-origination/review-authorize · 94adcfb43be7
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · a9bd48eaecb0
[^8]: kj · score/ach-origination/exception · 136525b3eddb
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · score/wire-domestic/discover · a7eda35b2559
[^11]: kj · score/wire-domestic/set-up · ca81496610da
[^12]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^13]: kj · score/wire-domestic/review-authorize · 5ada8599fcd1
[^14]: kj · score/wire-domestic/execute-track · 12930d4bae3c
[^15]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^16]: kj · score/wire-domestic/manage · 2814a728a910
[^17]: kj · score/wire-domestic/exception · ec3f316bff3e
[^18]: kj · score/wire-domestic/support · 2814a728a910
[^19]: kj · product/WF-P15 · 1b70c83e2760

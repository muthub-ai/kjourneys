---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Direct Pay for Business: stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "e3c6b0dc9f3d892b587d98f543c17b51b5daf9451e6d0928a499882ef318213b",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — experience assessment

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

## Gaps

- **high** · Discover · channel gap · Direct Pay is desktop-browser only: SMB owners cannot initiate or approve ACH on mobile unless they enrol in Vantage Treasury Management.[^10]
- **medium** · Initiate · missing capability · Direct Pay is next-business-day only; no Same Day ACH option documented after a search of the Direct Pay FAQ (S931).[^11]
- **medium** · Manage · transparency · Edit/cancel rules for scheduled Direct Pay payments are not documented.[^12]
- **medium** · Exception · exception handling · Returned ACH, failed validation and NSF handling are not published (UNKNOWN).[^13]

## Strengths

- Set up · Direct Pay four-level access model (Input Only, Input/Release, Input/Release/Control, No Access) enforces dual control for SMB ACH.[^14]
- Set up · Payee pre-validation with re-validation on bank-detail change; 13-month scheduling.[^15]

[^1]: kj · score/ach-origination/discover · a46a68a0fbe7
[^2]: kj · score/ach-origination/set-up · 82fdfd419043
[^3]: kj · score/ach-origination/initiate · 7fb1c066e3db
[^4]: kj · score/ach-origination/review-authorize · 94adcfb43be7
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · a9bd48eaecb0
[^8]: kj · score/ach-origination/exception · 136525b3eddb
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · finding/GAP-WF-0026 · 98f60378df46
[^11]: kj · finding/GAP-WF-0027 · 3f10807fa15d
[^12]: kj · finding/GAP-WF-0028 · fa0fe1897d28
[^13]: kj · finding/GAP-WF-0029 · c7d7360df8f3
[^14]: kj · finding/STR-WF-0017 · ebeb4dc413cc
[^15]: kj · finding/STR-WF-0018 · 64c7f9a8f46b

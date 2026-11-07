---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Direct Pay for Business: stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p08-direct-pay-for-business",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P08",
  "line_of_business": "wf-cbl",
  "content_sha256": "4bf5d209c98a881f445590a5b675ef359839a2a4ee0951423e8d4221805171bd",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Direct Pay for Business — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. From report v2, each score is the mean across MI's customer journeys, so half points occur. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| ACH origination (business) | Discover | 1 | 3 | −2[^1] |
| ACH origination (business) | Set up | 4 | 4 | at best practice[^2] |
| ACH origination (business) | Initiate | 2 | 4 | −2[^3] |
| ACH origination (business) | Review & authorize | 1 | 4 | −3[^4] |
| ACH origination (business) | Execute & track | 3 | 4 | −1[^5] |
| ACH origination (business) | Confirm & complete | 3 | 3 | at best practice[^6] |
| ACH origination (business) | Manage | 3 | 3 | at best practice[^7] |
| ACH origination (business) | Exception | 2 | 4 | −2[^8] |
| ACH origination (business) | Support | 3 | 3 | at best practice[^9] |

## Gaps

- **high** · Discover · channel gap · Direct Pay is desktop-browser only: SMB owners cannot initiate or approve ACH on mobile unless they enrol in Vantage Treasury Management.[^10]
- **medium** · Initiate · missing capability · Direct Pay is next-business-day only; no Same Day ACH option documented after a search of the Direct Pay FAQ (S931).[^11]
- **medium** · Exception · exception handling · Returned ACH credits from the payee's bank and Same Day ACH are not published; second-wave evidence closes only part of the gap — insufficient funds ('we may either decline the transfer' or complete it and overdraw), payment by account number only with no name check, and rejection notices are now published in the Direct Pay Agreement (S970).[^12]
- **low** · Manage · transparency · Second-wave evidence: the Direct Pay Agreement publishes the cancel/change cutoff (before 3 p.m. Pacific on the Send On Date; payments in process cannot be cancelled or changed) and the rejection notice ('on or before the Pay By Date'), closing most of the first-wave transparency gap; the FAQ and Quick Start Guide still do not surface these rules in the flow.[^13]

## Strengths

- Set up · Direct Pay four-level access model (Input Only, Input/Release, Input/Release/Control, No Access) enforces dual control for SMB ACH.[^14]
- Set up · Payee pre-validation with re-validation on bank-detail change; 13-month scheduling.[^15]

[^1]: kj · score/ach-origination/discover · e7868e030a7b
[^2]: kj · score/ach-origination/set-up · 9cd5f2dd79c9
[^3]: kj · score/ach-origination/initiate · c946a97de3a8
[^4]: kj · score/ach-origination/review-authorize · 43ac935a9848
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · 77661bdd40e1
[^8]: kj · score/ach-origination/exception · 6a30cf3346db
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · finding/GAP-WF-0025 · c507ffb51a47
[^11]: kj · finding/GAP-WF-0026 · 78c5f344fbea
[^12]: kj · finding/GAP-WF-0028 · 631690a78ab9
[^13]: kj · finding/GAP-WF-0027 · cb8e2556a07e
[^14]: kj · finding/STR-WF-0018 · fc01adb0b7c4
[^15]: kj · finding/STR-WF-0019 · a3bb48aa2a09

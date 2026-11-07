---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Transfers (Transfer Money): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "eab1c9b9706ef9e5f566dae657007d668d8d127b96c248c8379f40492cf701f2",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| ACH external transfer | Discover | 3 | 3 | at best practice[^1] |
| ACH external transfer | Set up | 2 | 3 | −1[^2] |
| ACH external transfer | Initiate | 2 | 4 | −2[^3] |
| ACH external transfer | Review & authorize | 3 | 3 | at best practice[^4] |
| ACH external transfer | Execute & track | 3 | 3 | at best practice[^5] |
| ACH external transfer | Confirm & complete | 3 | 3 | at best practice[^6] |
| ACH external transfer | Manage | 3 | 3 | at best practice[^7] |
| ACH external transfer | Exception | 2 | 3 | −1[^8] |
| ACH external transfer | Support | 3 | 3 | at best practice[^9] |
| Internal transfer | Discover | 3 | 4 | −1[^10] |
| Internal transfer | Set up | 3 | 3 | at best practice[^11] |
| Internal transfer | Initiate | 3 | 4 | −1[^12] |
| Internal transfer | Review & authorize | 3 | 3 | at best practice[^13] |
| Internal transfer | Execute & track | 3 | 3 | at best practice[^14] |
| Internal transfer | Confirm & complete | 3 | 3 | at best practice[^15] |
| Internal transfer | Manage | 3 | 3 | at best practice[^16] |
| Internal transfer | Exception | 3 | 3 | at best practice[^17] |
| Internal transfer | Support | 3 | 4 | −1[^18] |

## Gaps

- **medium** · Set up · missing capability · External-account linking is micro-deposit/proof-of-ownership only — verification 1-3 business days per the public FAQ; no instant credential/aggregator verification. Corroborated on the web (Nov 2026, S990): the 'Add Non-Wells Fargo Account' form takes keyed routing and account numbers with an ownership attestation and an account-use choice ('Payments only' vs 'Transfers and payments'); enabling transfers is quoted as 'additional security measures (may take 2-3 business days)'; no aggregator option is offered.[^19]
- **medium** · Initiate · missing capability · Outbound external transfers default to 2-3 business days; next-day is discretionary and there is no same-day or instant option, although WF already sends RTP/FedNow via its Instant Payments API.[^20]
- **medium** · Exception · transparency · Returned/failed external transfers lead to suspension and reinstatement at lower limits with no published plain-language reason codes; ACH return handling is INFERRED.[^21]
- **medium** · Initiate · missing capability · Inbound pulls are standard ACH only; no free next-day or RfP-based instant pull.[^22]
- **low** · Discover · friction · Linking entry ('Add Non-Wells Fargo Accounts') is documented for web; the mobile linking path is not published.[^23]
- **low** · Exception · exception handling · Same-day internal transfers cannot be cancelled; a wrong-account transfer must be reversed manually.[^24]
- **low** · Set up · security trust · Observed: 'Set up for transfers' on an already-verified payments-only external account completed with one click and no confirmation step, immediately enabling outbound transfers to that account.[^25]

## Strengths

- Discover · Transfer on the bottom bar, via Fargo and at ATMs.[^26]

[^1]: kj · score/ach-external-transfer/discover · 516e0c8f9b3a
[^2]: kj · score/ach-external-transfer/set-up · 583615d6bc29
[^3]: kj · score/ach-external-transfer/initiate · 485f4a13f91d
[^4]: kj · score/ach-external-transfer/review-authorize · ee3085b5cb36
[^5]: kj · score/ach-external-transfer/execute-track · ee3085b5cb36
[^6]: kj · score/ach-external-transfer/confirm-complete · 40b39d959133
[^7]: kj · score/ach-external-transfer/manage · ee3085b5cb36
[^8]: kj · score/ach-external-transfer/exception · 8b72238450b6
[^9]: kj · score/ach-external-transfer/support · ee3085b5cb36
[^10]: kj · score/internal-transfer/discover · 5e0adabac2df
[^11]: kj · score/internal-transfer/set-up · ad9fea561b11
[^12]: kj · score/internal-transfer/initiate · b6f4a071e141
[^13]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^14]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^15]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^16]: kj · score/internal-transfer/manage · fdb4992e1029
[^17]: kj · score/internal-transfer/exception · 6e98a0705895
[^18]: kj · score/internal-transfer/support · b6f4a071e141
[^19]: kj · finding/GAP-WF-0009 · 0194eced10a6
[^20]: kj · finding/GAP-WF-0010 · ce6ee0b68b21
[^21]: kj · finding/GAP-WF-0011 · 907c3416ca30
[^22]: kj · finding/GAP-WF-0013 · 82e2204f8b74
[^23]: kj · finding/GAP-WF-0012 · 4d065129c300
[^24]: kj · finding/GAP-WF-0033 · deb4b6489d31
[^25]: kj · finding/GAP-WF-0037 · 966f77825654
[^26]: kj · finding/STR-WF-0014 · 3d1262fa3bd4

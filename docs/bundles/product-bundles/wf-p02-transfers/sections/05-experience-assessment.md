---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Transfers (Transfer Money): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "1864ac6eb073a255ec85ade035fcab9e5e4bb973145a715a59d47cbed72faf3f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. From report v2, each score is the mean across MI's customer journeys, so half points occur. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| ACH external transfer | Discover | 3 | 3 | at best practice[^1] |
| ACH external transfer | Set up | 2 | 3.5 | −1.5[^2] |
| ACH external transfer | Initiate | 2 | 4 | −2[^3] |
| ACH external transfer | Review & authorize | 3 | 3 | at best practice[^4] |
| ACH external transfer | Execute & track | 3 | 3 | at best practice[^5] |
| ACH external transfer | Confirm & complete | 3 | 3 | at best practice[^6] |
| ACH external transfer | Manage | 3 | 3.5 | −0.5[^7] |
| ACH external transfer | Exception | 2.5 | 3 | −0.5[^8] |
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
[^2]: kj · score/ach-external-transfer/set-up · 15d596cfb20c
[^3]: kj · score/ach-external-transfer/initiate · 485f4a13f91d
[^4]: kj · score/ach-external-transfer/review-authorize · ee3085b5cb36
[^5]: kj · score/ach-external-transfer/execute-track · ee3085b5cb36
[^6]: kj · score/ach-external-transfer/confirm-complete · 31a7c40a8502
[^7]: kj · score/ach-external-transfer/manage · fd772c289e01
[^8]: kj · score/ach-external-transfer/exception · 8e804d0d24df
[^9]: kj · score/ach-external-transfer/support · ee3085b5cb36
[^10]: kj · score/internal-transfer/discover · 6bf8de0e67f3
[^11]: kj · score/internal-transfer/set-up · ad9fea561b11
[^12]: kj · score/internal-transfer/initiate · b6f4a071e141
[^13]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^14]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^15]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^16]: kj · score/internal-transfer/manage · fdb4992e1029
[^17]: kj · score/internal-transfer/exception · c5eb205122b4
[^18]: kj · score/internal-transfer/support · b6f4a071e141
[^19]: kj · finding/GAP-WF-0009 · e2a53e131f01
[^20]: kj · finding/GAP-WF-0010 · a8ddf215d92c
[^21]: kj · finding/GAP-WF-0011 · 2a4a77043815
[^22]: kj · finding/GAP-WF-0013 · e429c2ad51cd
[^23]: kj · finding/GAP-WF-0012 · 2d644efd9069
[^24]: kj · finding/GAP-WF-0032 · 277f2a8e776e
[^25]: kj · finding/GAP-WF-0036 · 8d671b1b3d0a
[^26]: kj · finding/STR-WF-0015 · 708faa6b9cdd

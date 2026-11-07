---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "98521b9d10c12fa837f6dd5d275dd2999eb43e896dfaeb5cbe0e7c0ac9ff108b",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — experience assessment

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
| Mobile check deposit | Discover | 4 | 4 | at best practice[^10] |
| Mobile check deposit | Set up | 3 | 3 | at best practice[^11] |
| Mobile check deposit | Initiate | 3 | 3 | at best practice[^12] |
| Mobile check deposit | Review & authorize | 3 | 4 | −1[^13] |
| Mobile check deposit | Execute & track | 3 | 4 | −1[^14] |
| Mobile check deposit | Confirm & complete | 4 | 4 | at best practice[^15] |
| Mobile check deposit | Manage | 3 | 3 | at best practice[^16] |
| Mobile check deposit | Exception | 3 | 4 | −1[^17] |
| Mobile check deposit | Support | 3 | 3 | at best practice[^18] |
| Internal transfer | Discover | 3 | 4 | −1[^19] |
| Internal transfer | Set up | 3 | 3 | at best practice[^20] |
| Internal transfer | Initiate | 3 | 4 | −1[^21] |
| Internal transfer | Review & authorize | 3 | 3 | at best practice[^22] |
| Internal transfer | Execute & track | 3 | 3 | at best practice[^23] |
| Internal transfer | Confirm & complete | 3 | 3 | at best practice[^24] |
| Internal transfer | Manage | 3 | 3 | at best practice[^25] |
| Internal transfer | Exception | 3 | 3 | at best practice[^26] |
| Internal transfer | Support | 3 | 4 | −1[^27] |
| RTP (The Clearing House) | Discover | 1.5 | 3.5 | −2.0[^28] |
| RTP (The Clearing House) | Set up | 1.5 | 3 | −1.5[^29] |
| RTP (The Clearing House) | Initiate | 1.5 | 3 | −1.5[^30] |
| RTP (The Clearing House) | Review & authorize | 1.5 | 3.5 | −2.0[^31] |
| RTP (The Clearing House) | Execute & track | 1.5 | 3 | −1.5[^32] |
| RTP (The Clearing House) | Confirm & complete | 1.5 | 3.5 | −2.0[^33] |
| RTP (The Clearing House) | Manage | 1.5 | 3 | −1.5[^34] |
| RTP (The Clearing House) | Exception | 1.5 | 3 | −1.5[^35] |
| RTP (The Clearing House) | Support | 1.5 | 3 | −1.5[^36] |
| Domestic wire | Discover | 3 | 3 | at best practice[^37] |
| Domestic wire | Set up | 3 | 4 | −1[^38] |
| Domestic wire | Initiate | 2 | 3 | −1[^39] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^40] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^41] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^42] |
| Domestic wire | Manage | 3 | 3 | at best practice[^43] |
| Domestic wire | Exception | 2 | 3 | −1[^44] |
| Domestic wire | Support | 3 | 3 | at best practice[^45] |
| International wire | Discover | 3 | 3 | at best practice[^46] |
| International wire | Set up | 3 | 3 | at best practice[^47] |
| International wire | Initiate | 4 | 4 | at best practice[^48] |
| International wire | Review & authorize | 3 | 4 | −1[^49] |
| International wire | Execute & track | 2 | 2 | at best practice[^50] |
| International wire | Confirm & complete | 3 | 3 | at best practice[^51] |
| International wire | Manage | 3 | 4 | −1[^52] |
| International wire | Exception | 3 | 3 | at best practice[^53] |
| International wire | Support | 3 | 3 | at best practice[^54] |

## Gaps

- **medium** · Initiate · missing capability · Commercial Request for Payment is absent from the public Instant Payments API v1 (credit transfers only); dedicated treasury instant-payment pages 404.[^55]
- **low** · Set up · transparency · The routing-number reachability check (RTP | FEDNOW) exists only in the API; no consumer/SMB surface shows instant eligibility.[^56]
- **low** · Exception · exception handling · Fallback when a receiver is unreachable on both rails is undocumented.[^57]

## Strengths

- Set up · Public Instant Payments API returns the reachable rail (RTP | FEDNOW | both) before send and exposes UETR-based statuses with reason codes.[^58]

[^1]: kj · score/ach-origination/discover · e7868e030a7b
[^2]: kj · score/ach-origination/set-up · 9cd5f2dd79c9
[^3]: kj · score/ach-origination/initiate · c946a97de3a8
[^4]: kj · score/ach-origination/review-authorize · 43ac935a9848
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · 77661bdd40e1
[^8]: kj · score/ach-origination/exception · 6a30cf3346db
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · score/check-deposit-mobile/discover · e82d47009a33
[^11]: kj · score/check-deposit-mobile/set-up · 2f2b9ba349d5
[^12]: kj · score/check-deposit-mobile/initiate · 2f2b9ba349d5
[^13]: kj · score/check-deposit-mobile/review-authorize · c9bee44ca271
[^14]: kj · score/check-deposit-mobile/execute-track · c9bee44ca271
[^15]: kj · score/check-deposit-mobile/confirm-complete · bf401bcea1b1
[^16]: kj · score/check-deposit-mobile/manage · 2f2b9ba349d5
[^17]: kj · score/check-deposit-mobile/exception · a343ff2e0ff0
[^18]: kj · score/check-deposit-mobile/support · 2f2b9ba349d5
[^19]: kj · score/internal-transfer/discover · 6bf8de0e67f3
[^20]: kj · score/internal-transfer/set-up · ad9fea561b11
[^21]: kj · score/internal-transfer/initiate · b6f4a071e141
[^22]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^23]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^24]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^25]: kj · score/internal-transfer/manage · fdb4992e1029
[^26]: kj · score/internal-transfer/exception · c5eb205122b4
[^27]: kj · score/internal-transfer/support · b6f4a071e141
[^28]: kj · score/rtp/discover · 48ea2f9e1d21
[^29]: kj · score/rtp/set-up · 77bc42247c8b
[^30]: kj · score/rtp/initiate · f0d83abc5932
[^31]: kj · score/rtp/review-authorize · b368661dc399
[^32]: kj · score/rtp/execute-track · 77bc42247c8b
[^33]: kj · score/rtp/confirm-complete · eeb6592c861a
[^34]: kj · score/rtp/manage · 77bc42247c8b
[^35]: kj · score/rtp/exception · 77bc42247c8b
[^36]: kj · score/rtp/support · 77bc42247c8b
[^37]: kj · score/wire-domestic/discover · a7eda35b2559
[^38]: kj · score/wire-domestic/set-up · b1ac6d947794
[^39]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^40]: kj · score/wire-domestic/review-authorize · ede3c9a5d788
[^41]: kj · score/wire-domestic/execute-track · 7ce523a435ef
[^42]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^43]: kj · score/wire-domestic/manage · 2814a728a910
[^44]: kj · score/wire-domestic/exception · ec3f316bff3e
[^45]: kj · score/wire-domestic/support · 2814a728a910
[^46]: kj · score/wire-international/discover · 6260b23c8d9a
[^47]: kj · score/wire-international/set-up · 6260b23c8d9a
[^48]: kj · score/wire-international/initiate · adc77a4c5488
[^49]: kj · score/wire-international/review-authorize · 25add189f337
[^50]: kj · score/wire-international/execute-track · e924cf09b15f
[^51]: kj · score/wire-international/confirm-complete · 6260b23c8d9a
[^52]: kj · score/wire-international/manage · 25add189f337
[^53]: kj · score/wire-international/exception · 6260b23c8d9a
[^54]: kj · score/wire-international/support · 6260b23c8d9a
[^55]: kj · finding/GAP-WF-0033 · 73eff2ab59a7
[^56]: kj · finding/GAP-WF-0022 · b4cf64e39188
[^57]: kj · finding/GAP-WF-0034 · 11d66ca955c7
[^58]: kj · finding/STR-WF-0020 · 2e5d23c39cf2

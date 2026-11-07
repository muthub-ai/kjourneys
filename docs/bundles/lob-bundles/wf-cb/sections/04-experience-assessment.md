---
{
 "type": "lob-bundle/section",
 "title": "Experience assessment",
 "description": "Commercial Banking: stage scores for its rails and its most severe gaps",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cb",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cb",
  "content_sha256": "46d87155bded650e374a6a7303c29c7701f8b7fdd9b9bfc94bf7393449021695",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial Banking — experience assessment

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
| Push to card | Discover | 0 | 0 | at best practice[^28] |
| Push to card | Set up | 0 | 0 | at best practice[^29] |
| Push to card | Initiate | 0 | 0 | at best practice[^30] |
| Push to card | Review & authorize | 0 | 0 | at best practice[^31] |
| Push to card | Execute & track | 0 | 0 | at best practice[^32] |
| Push to card | Confirm & complete | 0 | 0 | at best practice[^33] |
| Push to card | Manage | 0 | 0 | at best practice[^34] |
| Push to card | Exception | 0 | 0 | at best practice[^35] |
| Push to card | Support | 0 | 0 | at best practice[^36] |
| RTP (The Clearing House) | Discover | 1 | 3 | −2[^37] |
| RTP (The Clearing House) | Set up | 1 | 3 | −2[^38] |
| RTP (The Clearing House) | Initiate | 1 | 3 | −2[^39] |
| RTP (The Clearing House) | Review & authorize | 1 | 3 | −2[^40] |
| RTP (The Clearing House) | Execute & track | 1 | 3 | −2[^41] |
| RTP (The Clearing House) | Confirm & complete | 1 | 3 | −2[^42] |
| RTP (The Clearing House) | Manage | 1 | 3 | −2[^43] |
| RTP (The Clearing House) | Exception | 1 | 3 | −2[^44] |
| RTP (The Clearing House) | Support | 1 | 3 | −2[^45] |
| Domestic wire | Discover | 3 | 3 | at best practice[^46] |
| Domestic wire | Set up | 3 | 4 | −1[^47] |
| Domestic wire | Initiate | 2 | 3 | −1[^48] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^49] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^50] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^51] |
| Domestic wire | Manage | 3 | 3 | at best practice[^52] |
| Domestic wire | Exception | 2 | 3 | −1[^53] |
| Domestic wire | Support | 3 | 3 | at best practice[^54] |
| International wire | Discover | 3 | 3 | at best practice[^55] |
| International wire | Set up | 3 | 3 | at best practice[^56] |
| International wire | Initiate | 4 | 4 | at best practice[^57] |
| International wire | Review & authorize | 3 | 4 | −1[^58] |
| International wire | Execute & track | 2 | 2 | at best practice[^59] |
| International wire | Confirm & complete | 3 | 3 | at best practice[^60] |
| International wire | Manage | 3 | 4 | −1[^61] |
| International wire | Exception | 3 | 3 | at best practice[^62] |
| International wire | Support | 3 | 3 | at best practice[^63] |

## Most severe gaps across its products

- **medium** · Commercial Request for Payment is absent from the public Instant Payments API v1 (credit transfers only); dedicated treasury instant-payment pages 404.[^64]
- **low** · The routing-number reachability check (RTP | FEDNOW) exists only in the API; no consumer/SMB surface shows instant eligibility.[^65]
- **low** · Fallback when a receiver is unreachable on both rails is undocumented.[^66]

[^1]: kj · score/ach-origination/discover · a46a68a0fbe7
[^2]: kj · score/ach-origination/set-up · 82fdfd419043
[^3]: kj · score/ach-origination/initiate · 7fb1c066e3db
[^4]: kj · score/ach-origination/review-authorize · 94adcfb43be7
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · a9bd48eaecb0
[^8]: kj · score/ach-origination/exception · 136525b3eddb
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · score/check-deposit-mobile/discover · 62fc95092d77
[^11]: kj · score/check-deposit-mobile/set-up · 2f2b9ba349d5
[^12]: kj · score/check-deposit-mobile/initiate · 2f2b9ba349d5
[^13]: kj · score/check-deposit-mobile/review-authorize · c9bee44ca271
[^14]: kj · score/check-deposit-mobile/execute-track · c9bee44ca271
[^15]: kj · score/check-deposit-mobile/confirm-complete · a70b283d9e5e
[^16]: kj · score/check-deposit-mobile/manage · 2f2b9ba349d5
[^17]: kj · score/check-deposit-mobile/exception · b562608e90bd
[^18]: kj · score/check-deposit-mobile/support · 2f2b9ba349d5
[^19]: kj · score/internal-transfer/discover · 5e0adabac2df
[^20]: kj · score/internal-transfer/set-up · ad9fea561b11
[^21]: kj · score/internal-transfer/initiate · b6f4a071e141
[^22]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^23]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^24]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^25]: kj · score/internal-transfer/manage · fdb4992e1029
[^26]: kj · score/internal-transfer/exception · 6e98a0705895
[^27]: kj · score/internal-transfer/support · b6f4a071e141
[^28]: kj · score/push-to-card/discover · fccdb7e4e1b7
[^29]: kj · score/push-to-card/set-up · fccdb7e4e1b7
[^30]: kj · score/push-to-card/initiate · fccdb7e4e1b7
[^31]: kj · score/push-to-card/review-authorize · fccdb7e4e1b7
[^32]: kj · score/push-to-card/execute-track · fccdb7e4e1b7
[^33]: kj · score/push-to-card/confirm-complete · fccdb7e4e1b7
[^34]: kj · score/push-to-card/manage · fccdb7e4e1b7
[^35]: kj · score/push-to-card/exception · fccdb7e4e1b7
[^36]: kj · score/push-to-card/support · fccdb7e4e1b7
[^37]: kj · score/rtp/discover · 946ae7ab398c
[^38]: kj · score/rtp/set-up · 4b62946fe364
[^39]: kj · score/rtp/initiate · f4120de6c42a
[^40]: kj · score/rtp/review-authorize · 2758a9be323a
[^41]: kj · score/rtp/execute-track · 4b62946fe364
[^42]: kj · score/rtp/confirm-complete · 4b62946fe364
[^43]: kj · score/rtp/manage · 4b62946fe364
[^44]: kj · score/rtp/exception · 4b62946fe364
[^45]: kj · score/rtp/support · 4b62946fe364
[^46]: kj · score/wire-domestic/discover · a7eda35b2559
[^47]: kj · score/wire-domestic/set-up · ca81496610da
[^48]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^49]: kj · score/wire-domestic/review-authorize · 5ada8599fcd1
[^50]: kj · score/wire-domestic/execute-track · 12930d4bae3c
[^51]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^52]: kj · score/wire-domestic/manage · 2814a728a910
[^53]: kj · score/wire-domestic/exception · ec3f316bff3e
[^54]: kj · score/wire-domestic/support · 2814a728a910
[^55]: kj · score/wire-international/discover · 6260b23c8d9a
[^56]: kj · score/wire-international/set-up · 6260b23c8d9a
[^57]: kj · score/wire-international/initiate · 7a3db9e89d6a
[^58]: kj · score/wire-international/review-authorize · 25add189f337
[^59]: kj · score/wire-international/execute-track · e924cf09b15f
[^60]: kj · score/wire-international/confirm-complete · 6260b23c8d9a
[^61]: kj · score/wire-international/manage · 25add189f337
[^62]: kj · score/wire-international/exception · 6260b23c8d9a
[^63]: kj · score/wire-international/support · 6260b23c8d9a
[^64]: kj · finding/GAP-WF-0034 · 6985b24955d0
[^65]: kj · finding/GAP-WF-0022 · 5bf6f52632fa
[^66]: kj · finding/GAP-WF-0035 · 0a84506564fc

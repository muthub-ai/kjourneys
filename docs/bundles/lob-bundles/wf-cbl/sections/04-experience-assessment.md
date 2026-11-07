---
{
 "type": "lob-bundle/section",
 "title": "Experience assessment",
 "description": "Consumer Banking and Lending: stage scores for its rails and its most severe gaps",
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
  "bundle_id": "wf-cbl",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cbl",
  "content_sha256": "d4ce74989dd1aeafebe4c0ceb29706cf89b3ab6cac5d64aa27055ade15af8707",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Consumer Banking and Lending — experience assessment

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
| ACH origination (business) | Discover | 1 | 3 | −2[^10] |
| ACH origination (business) | Set up | 4 | 4 | at best practice[^11] |
| ACH origination (business) | Initiate | 2 | 4 | −2[^12] |
| ACH origination (business) | Review & authorize | 1 | 4 | −3[^13] |
| ACH origination (business) | Execute & track | 3 | 4 | −1[^14] |
| ACH origination (business) | Confirm & complete | 3 | 3 | at best practice[^15] |
| ACH origination (business) | Manage | 2 | 3 | −1[^16] |
| ACH origination (business) | Exception | 2 | 4 | −2[^17] |
| ACH origination (business) | Support | 3 | 3 | at best practice[^18] |
| Bill pay | Discover | 3 | 3 | at best practice[^19] |
| Bill pay | Set up | 3 | 3 | at best practice[^20] |
| Bill pay | Initiate | 3 | 4 | −1[^21] |
| Bill pay | Review & authorize | 3 | 3 | at best practice[^22] |
| Bill pay | Execute & track | 3 | 3 | at best practice[^23] |
| Bill pay | Confirm & complete | 3 | 3 | at best practice[^24] |
| Bill pay | Manage | 3 | 3 | at best practice[^25] |
| Bill pay | Exception | 3 | 3 | at best practice[^26] |
| Bill pay | Support | 3 | 3 | at best practice[^27] |
| Mobile check deposit | Discover | 4 | 4 | at best practice[^28] |
| Mobile check deposit | Set up | 3 | 3 | at best practice[^29] |
| Mobile check deposit | Initiate | 3 | 3 | at best practice[^30] |
| Mobile check deposit | Review & authorize | 3 | 4 | −1[^31] |
| Mobile check deposit | Execute & track | 3 | 4 | −1[^32] |
| Mobile check deposit | Confirm & complete | 4 | 4 | at best practice[^33] |
| Mobile check deposit | Manage | 3 | 3 | at best practice[^34] |
| Mobile check deposit | Exception | 3 | 4 | −1[^35] |
| Mobile check deposit | Support | 3 | 3 | at best practice[^36] |
| Internal transfer | Discover | 3 | 4 | −1[^37] |
| Internal transfer | Set up | 3 | 3 | at best practice[^38] |
| Internal transfer | Initiate | 3 | 4 | −1[^39] |
| Internal transfer | Review & authorize | 3 | 3 | at best practice[^40] |
| Internal transfer | Execute & track | 3 | 3 | at best practice[^41] |
| Internal transfer | Confirm & complete | 3 | 3 | at best practice[^42] |
| Internal transfer | Manage | 3 | 3 | at best practice[^43] |
| Internal transfer | Exception | 3 | 3 | at best practice[^44] |
| Internal transfer | Support | 3 | 4 | −1[^45] |
| Remittance | Discover | 2 | 4 | −2[^46] |
| Remittance | Set up | 4 | 4 | at best practice[^47] |
| Remittance | Initiate | 3 | 4 | −1[^48] |
| Remittance | Review & authorize | 3 | 3 | at best practice[^49] |
| Remittance | Execute & track | 4 | 4 | at best practice[^50] |
| Remittance | Confirm & complete | 3 | 3 | at best practice[^51] |
| Remittance | Manage | 2 | 3 | −1[^52] |
| Remittance | Exception | 3 | 3 | at best practice[^53] |
| Remittance | Support | 3 | 3 | at best practice[^54] |
| Request to pay | Discover | 3 | 4 | −1[^55] |
| Request to pay | Set up | 3 | 3 | at best practice[^56] |
| Request to pay | Initiate | 2 | 4 | −2[^57] |
| Request to pay | Review & authorize | 3 | 3 | at best practice[^58] |
| Request to pay | Execute & track | 3 | 3 | at best practice[^59] |
| Request to pay | Confirm & complete | 3 | 3 | at best practice[^60] |
| Request to pay | Manage | 3 | 3 | at best practice[^61] |
| Request to pay | Exception | 3 | 3 | at best practice[^62] |
| Request to pay | Support | 3 | 3 | at best practice[^63] |
| RTP (The Clearing House) | Discover | 1 | 3 | −2[^64] |
| RTP (The Clearing House) | Set up | 1 | 3 | −2[^65] |
| RTP (The Clearing House) | Initiate | 1 | 3 | −2[^66] |
| RTP (The Clearing House) | Review & authorize | 1 | 3 | −2[^67] |
| RTP (The Clearing House) | Execute & track | 1 | 3 | −2[^68] |
| RTP (The Clearing House) | Confirm & complete | 1 | 3 | −2[^69] |
| RTP (The Clearing House) | Manage | 1 | 3 | −2[^70] |
| RTP (The Clearing House) | Exception | 1 | 3 | −2[^71] |
| RTP (The Clearing House) | Support | 1 | 3 | −2[^72] |
| Domestic wire | Discover | 3 | 3 | at best practice[^73] |
| Domestic wire | Set up | 3 | 4 | −1[^74] |
| Domestic wire | Initiate | 2 | 3 | −1[^75] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^76] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^77] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^78] |
| Domestic wire | Manage | 3 | 3 | at best practice[^79] |
| Domestic wire | Exception | 2 | 3 | −1[^80] |
| Domestic wire | Support | 3 | 3 | at best practice[^81] |
| International wire | Discover | 3 | 3 | at best practice[^82] |
| International wire | Set up | 3 | 3 | at best practice[^83] |
| International wire | Initiate | 4 | 4 | at best practice[^84] |
| International wire | Review & authorize | 3 | 4 | −1[^85] |
| International wire | Execute & track | 2 | 2 | at best practice[^86] |
| International wire | Confirm & complete | 3 | 3 | at best practice[^87] |
| International wire | Manage | 3 | 4 | −1[^88] |
| International wire | Exception | 3 | 3 | at best practice[^89] |
| International wire | Support | 3 | 3 | at best practice[^90] |
| Zelle | Discover | 3 | 3 | at best practice[^91] |
| Zelle | Set up | 3 | 3 | at best practice[^92] |
| Zelle | Initiate | 3 | 3 | at best practice[^93] |
| Zelle | Review & authorize | 1 | 3 | −2[^94] |
| Zelle | Execute & track | 3 | 3 | at best practice[^95] |
| Zelle | Confirm & complete | 3 | 3 | at best practice[^96] |
| Zelle | Manage | 3 | 3 | at best practice[^97] |
| Zelle | Exception | 2 | 2 | at best practice[^98] |
| Zelle | Support | 2 | 3 | −1[^99] |

## Most severe gaps across its products

- **high** · Review screen carries only static 'only send to people you know and trust' copy; no risk-tiered interstitial, payment-purpose or contact-origin question is documented, and the Zelle-specific scam page now 404s. Observed on the web (Nov 2026): the only scam messaging before the amount screen is a static banner shown on every Zelle visit; the review screen itself was not reached.[^100]
- **high** · Unauthorized and scam claims start by phone (1-800-956-4442 / 1-866-867-5568) or by mail to a P.O. box; no in-app 'report a problem' on the Zelle transaction and no in-app claim status tracker for Zelle. Corroborated on the web (Nov 2026, S990): a completed Zelle payment's detail screen offers only 'Block'; on the observed profile the 'Track Claims > Dispute a charge' picker listed only debit-card purchases (whether non-card items are excluded is unconfirmed); 'Report Phish & Email Scams' leaves the secure session for a public education page.[^101]
- **high** · Business Zelle sends in Business Online can be executed by a single 'View and Transact' delegate; no secondary approval (INFERRED from OAA per WF-C003). Dual custody exists only for Vantage Treasury Management enrollees.[^102]
- **high** · No consumer- or SMB-initiated RTP/FedNow send exists outside RfP-driven Bill Pay, and instant rails are not marketed at all, despite WF being a dual-rail sender via API (CONFIRMED_BANK S916).[^103]
- **high** · Direct Pay is desktop-browser only: SMB owners cannot initiate or approve ACH on mobile unless they enrol in Vantage Treasury Management.[^104]
- **high** · SMB wires from Business Online have no dual approval (INFERRED, WF-C003); a single delegate can release a foreign-currency wire.[^105]
- **medium** · Scam-reimbursement stance is the network minimum ('qualifying imposter scams'); eligibility criteria and decision timeline for authorized-scam claims are not published.[^106]
- **medium** · Fraud and scam support is split across at least four phone numbers with different scopes (1-800-869-3557, 1-800-956-4442, 1-866-867-5568, 1-800-225-5935).[^107]
- **medium** · 'Split' is marketed but implemented as separate single requests; no multi-payer split screen with per-person amounts.[^108]
- **medium** · External-account linking is micro-deposit/proof-of-ownership only — verification 1-3 business days per the public FAQ; no instant credential/aggregator verification. Corroborated on the web (Nov 2026, S990): the 'Add Non-Wells Fargo Account' form takes keyed routing and account numbers with an ownership attestation and an account-use choice ('Payments only' vs 'Transfers and payments'); enabling transfers is quoted as 'additional security measures (may take 2-3 business days)'; no aggregator option is offered.[^109]

[^1]: kj · score/ach-external-transfer/discover · 516e0c8f9b3a
[^2]: kj · score/ach-external-transfer/set-up · 583615d6bc29
[^3]: kj · score/ach-external-transfer/initiate · 485f4a13f91d
[^4]: kj · score/ach-external-transfer/review-authorize · ee3085b5cb36
[^5]: kj · score/ach-external-transfer/execute-track · ee3085b5cb36
[^6]: kj · score/ach-external-transfer/confirm-complete · 40b39d959133
[^7]: kj · score/ach-external-transfer/manage · ee3085b5cb36
[^8]: kj · score/ach-external-transfer/exception · 8b72238450b6
[^9]: kj · score/ach-external-transfer/support · ee3085b5cb36
[^10]: kj · score/ach-origination/discover · a46a68a0fbe7
[^11]: kj · score/ach-origination/set-up · 82fdfd419043
[^12]: kj · score/ach-origination/initiate · 7fb1c066e3db
[^13]: kj · score/ach-origination/review-authorize · 94adcfb43be7
[^14]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^15]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^16]: kj · score/ach-origination/manage · a9bd48eaecb0
[^17]: kj · score/ach-origination/exception · 136525b3eddb
[^18]: kj · score/ach-origination/support · f4048a16db48
[^19]: kj · score/bill-pay/discover · 992518b75df6
[^20]: kj · score/bill-pay/set-up · 992518b75df6
[^21]: kj · score/bill-pay/initiate · 1c0b06399f9f
[^22]: kj · score/bill-pay/review-authorize · 992518b75df6
[^23]: kj · score/bill-pay/execute-track · 992518b75df6
[^24]: kj · score/bill-pay/confirm-complete · 992518b75df6
[^25]: kj · score/bill-pay/manage · 53ac3b61085d
[^26]: kj · score/bill-pay/exception · 5a0578a2664c
[^27]: kj · score/bill-pay/support · 992518b75df6
[^28]: kj · score/check-deposit-mobile/discover · 62fc95092d77
[^29]: kj · score/check-deposit-mobile/set-up · 2f2b9ba349d5
[^30]: kj · score/check-deposit-mobile/initiate · 2f2b9ba349d5
[^31]: kj · score/check-deposit-mobile/review-authorize · c9bee44ca271
[^32]: kj · score/check-deposit-mobile/execute-track · c9bee44ca271
[^33]: kj · score/check-deposit-mobile/confirm-complete · a70b283d9e5e
[^34]: kj · score/check-deposit-mobile/manage · 2f2b9ba349d5
[^35]: kj · score/check-deposit-mobile/exception · b562608e90bd
[^36]: kj · score/check-deposit-mobile/support · 2f2b9ba349d5
[^37]: kj · score/internal-transfer/discover · 5e0adabac2df
[^38]: kj · score/internal-transfer/set-up · ad9fea561b11
[^39]: kj · score/internal-transfer/initiate · b6f4a071e141
[^40]: kj · score/internal-transfer/review-authorize · fdb4992e1029
[^41]: kj · score/internal-transfer/execute-track · ad9fea561b11
[^42]: kj · score/internal-transfer/confirm-complete · ad9fea561b11
[^43]: kj · score/internal-transfer/manage · fdb4992e1029
[^44]: kj · score/internal-transfer/exception · 6e98a0705895
[^45]: kj · score/internal-transfer/support · b6f4a071e141
[^46]: kj · score/remittance/discover · 17a0bd5ea943
[^47]: kj · score/remittance/set-up · 49ae40d3e583
[^48]: kj · score/remittance/initiate · b5762c609a52
[^49]: kj · score/remittance/review-authorize · 1e5fe25e9536
[^50]: kj · score/remittance/execute-track · f45bd4e64a0d
[^51]: kj · score/remittance/confirm-complete · 1e5fe25e9536
[^52]: kj · score/remittance/manage · 716e589ec4d5
[^53]: kj · score/remittance/exception · 1e5fe25e9536
[^54]: kj · score/remittance/support · 1e5fe25e9536
[^55]: kj · score/request-to-pay/discover · 8aaf5ddcb63e
[^56]: kj · score/request-to-pay/set-up · 64a250a3c380
[^57]: kj · score/request-to-pay/initiate · 72fbb231701c
[^58]: kj · score/request-to-pay/review-authorize · 64a250a3c380
[^59]: kj · score/request-to-pay/execute-track · 64a250a3c380
[^60]: kj · score/request-to-pay/confirm-complete · 64a250a3c380
[^61]: kj · score/request-to-pay/manage · a1ae3362759e
[^62]: kj · score/request-to-pay/exception · 64a250a3c380
[^63]: kj · score/request-to-pay/support · 64a250a3c380
[^64]: kj · score/rtp/discover · 946ae7ab398c
[^65]: kj · score/rtp/set-up · 4b62946fe364
[^66]: kj · score/rtp/initiate · f4120de6c42a
[^67]: kj · score/rtp/review-authorize · 2758a9be323a
[^68]: kj · score/rtp/execute-track · 4b62946fe364
[^69]: kj · score/rtp/confirm-complete · 4b62946fe364
[^70]: kj · score/rtp/manage · 4b62946fe364
[^71]: kj · score/rtp/exception · 4b62946fe364
[^72]: kj · score/rtp/support · 4b62946fe364
[^73]: kj · score/wire-domestic/discover · a7eda35b2559
[^74]: kj · score/wire-domestic/set-up · ca81496610da
[^75]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^76]: kj · score/wire-domestic/review-authorize · 5ada8599fcd1
[^77]: kj · score/wire-domestic/execute-track · 12930d4bae3c
[^78]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^79]: kj · score/wire-domestic/manage · 2814a728a910
[^80]: kj · score/wire-domestic/exception · ec3f316bff3e
[^81]: kj · score/wire-domestic/support · 2814a728a910
[^82]: kj · score/wire-international/discover · 6260b23c8d9a
[^83]: kj · score/wire-international/set-up · 6260b23c8d9a
[^84]: kj · score/wire-international/initiate · 7a3db9e89d6a
[^85]: kj · score/wire-international/review-authorize · 25add189f337
[^86]: kj · score/wire-international/execute-track · e924cf09b15f
[^87]: kj · score/wire-international/confirm-complete · 6260b23c8d9a
[^88]: kj · score/wire-international/manage · 25add189f337
[^89]: kj · score/wire-international/exception · 6260b23c8d9a
[^90]: kj · score/wire-international/support · 6260b23c8d9a
[^91]: kj · score/zelle/discover · 2bd0b74d37f1
[^92]: kj · score/zelle/set-up · f3093057d59e
[^93]: kj · score/zelle/initiate · 673a47124b13
[^94]: kj · score/zelle/review-authorize · a3f06b174bf4
[^95]: kj · score/zelle/execute-track · 02cb1535a9b8
[^96]: kj · score/zelle/confirm-complete · 02cb1535a9b8
[^97]: kj · score/zelle/manage · 8d99b809a6a4
[^98]: kj · score/zelle/exception · 89e1f8bb4e9d
[^99]: kj · score/zelle/support · 850a938312d2
[^100]: kj · finding/GAP-WF-0001 · 38c101614c6a
[^101]: kj · finding/GAP-WF-0002 · 4e09e7353ec2
[^102]: kj · finding/GAP-WF-0008 · 35e06b5dbd70
[^103]: kj · finding/GAP-WF-0021 · 6a96d04bb8de
[^104]: kj · finding/GAP-WF-0026 · 98f60378df46
[^105]: kj · finding/GAP-WF-0030 · f8866096040e
[^106]: kj · finding/GAP-WF-0003 · a9b601e4c21e
[^107]: kj · finding/GAP-WF-0004 · 069260253e2f
[^108]: kj · finding/GAP-WF-0006 · 3782e8a4f392
[^109]: kj · finding/GAP-WF-0009 · 0194eced10a6

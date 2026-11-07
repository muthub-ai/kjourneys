---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Wells Fargo Gateway® APIs (developer portal): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p14-wells-fargo-gateway-apis",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P14",
  "line_of_business": "wf-cb",
  "content_sha256": "b2265868f1d4bdf09b4d43edcab358f2ae62255460139f9010dd9e72c069e3fe",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Gateway® APIs (developer portal) — experience assessment

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
| Push to card | Discover | 0 | 0 | at best practice[^10] |
| Push to card | Set up | 0 | 0 | at best practice[^11] |
| Push to card | Initiate | 0 | 0 | at best practice[^12] |
| Push to card | Review & authorize | 0 | 0 | at best practice[^13] |
| Push to card | Execute & track | 0 | 0 | at best practice[^14] |
| Push to card | Confirm & complete | 0 | 0 | at best practice[^15] |
| Push to card | Manage | 0 | 0 | at best practice[^16] |
| Push to card | Exception | 0 | 0 | at best practice[^17] |
| Push to card | Support | 0 | 0 | at best practice[^18] |
| RTP (The Clearing House) | Discover | 1.5 | 3.5 | −2.0[^19] |
| RTP (The Clearing House) | Set up | 1.5 | 3 | −1.5[^20] |
| RTP (The Clearing House) | Initiate | 1.5 | 3 | −1.5[^21] |
| RTP (The Clearing House) | Review & authorize | 1.5 | 3.5 | −2.0[^22] |
| RTP (The Clearing House) | Execute & track | 1.5 | 3 | −1.5[^23] |
| RTP (The Clearing House) | Confirm & complete | 1.5 | 3.5 | −2.0[^24] |
| RTP (The Clearing House) | Manage | 1.5 | 3 | −1.5[^25] |
| RTP (The Clearing House) | Exception | 1.5 | 3 | −1.5[^26] |
| RTP (The Clearing House) | Support | 1.5 | 3 | −1.5[^27] |
| Domestic wire | Discover | 3 | 3 | at best practice[^28] |
| Domestic wire | Set up | 3 | 4 | −1[^29] |
| Domestic wire | Initiate | 2 | 3 | −1[^30] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^31] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^32] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^33] |
| Domestic wire | Manage | 3 | 3 | at best practice[^34] |
| Domestic wire | Exception | 2 | 3 | −1[^35] |
| Domestic wire | Support | 3 | 3 | at best practice[^36] |
| International wire | Discover | 3 | 3 | at best practice[^37] |
| International wire | Set up | 3 | 3 | at best practice[^38] |
| International wire | Initiate | 4 | 4 | at best practice[^39] |
| International wire | Review & authorize | 3 | 4 | −1[^40] |
| International wire | Execute & track | 2 | 2 | at best practice[^41] |
| International wire | Confirm & complete | 3 | 3 | at best practice[^42] |
| International wire | Manage | 3 | 4 | −1[^43] |
| International wire | Exception | 3 | 3 | at best practice[^44] |
| International wire | Support | 3 | 3 | at best practice[^45] |

## Gaps

None recorded in this study.[^46]

## Strengths

None recorded in this study.[^46]

[^1]: kj · score/ach-origination/discover · e7868e030a7b
[^2]: kj · score/ach-origination/set-up · 9cd5f2dd79c9
[^3]: kj · score/ach-origination/initiate · c946a97de3a8
[^4]: kj · score/ach-origination/review-authorize · 43ac935a9848
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · 77661bdd40e1
[^8]: kj · score/ach-origination/exception · 6a30cf3346db
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · score/push-to-card/discover · fccdb7e4e1b7
[^11]: kj · score/push-to-card/set-up · fccdb7e4e1b7
[^12]: kj · score/push-to-card/initiate · fccdb7e4e1b7
[^13]: kj · score/push-to-card/review-authorize · fccdb7e4e1b7
[^14]: kj · score/push-to-card/execute-track · fccdb7e4e1b7
[^15]: kj · score/push-to-card/confirm-complete · fccdb7e4e1b7
[^16]: kj · score/push-to-card/manage · fccdb7e4e1b7
[^17]: kj · score/push-to-card/exception · fccdb7e4e1b7
[^18]: kj · score/push-to-card/support · fccdb7e4e1b7
[^19]: kj · score/rtp/discover · 48ea2f9e1d21
[^20]: kj · score/rtp/set-up · 77bc42247c8b
[^21]: kj · score/rtp/initiate · f0d83abc5932
[^22]: kj · score/rtp/review-authorize · b368661dc399
[^23]: kj · score/rtp/execute-track · 77bc42247c8b
[^24]: kj · score/rtp/confirm-complete · eeb6592c861a
[^25]: kj · score/rtp/manage · 77bc42247c8b
[^26]: kj · score/rtp/exception · 77bc42247c8b
[^27]: kj · score/rtp/support · 77bc42247c8b
[^28]: kj · score/wire-domestic/discover · a7eda35b2559
[^29]: kj · score/wire-domestic/set-up · b1ac6d947794
[^30]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^31]: kj · score/wire-domestic/review-authorize · ede3c9a5d788
[^32]: kj · score/wire-domestic/execute-track · 7ce523a435ef
[^33]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^34]: kj · score/wire-domestic/manage · 2814a728a910
[^35]: kj · score/wire-domestic/exception · ec3f316bff3e
[^36]: kj · score/wire-domestic/support · 2814a728a910
[^37]: kj · score/wire-international/discover · 6260b23c8d9a
[^38]: kj · score/wire-international/set-up · 6260b23c8d9a
[^39]: kj · score/wire-international/initiate · adc77a4c5488
[^40]: kj · score/wire-international/review-authorize · 25add189f337
[^41]: kj · score/wire-international/execute-track · e924cf09b15f
[^42]: kj · score/wire-international/confirm-complete · 6260b23c8d9a
[^43]: kj · score/wire-international/manage · 25add189f337
[^44]: kj · score/wire-international/exception · 6260b23c8d9a
[^45]: kj · score/wire-international/support · 6260b23c8d9a
[^46]: kj · product/WF-P14 · 93004be7802c

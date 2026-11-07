---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Bill Pay (Online Bill Pay / Business Bill Pay): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "dbf41e00179d044ab867b274a436754376e7e42bbcee06453e9bed23be1c74c2",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Bill Pay (Online Bill Pay / Business Bill Pay) — experience assessment

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
| RTP (The Clearing House) | Discover | 1.5 | 3.5 | −2.0[^10] |
| RTP (The Clearing House) | Set up | 1.5 | 3 | −1.5[^11] |
| RTP (The Clearing House) | Initiate | 1.5 | 3 | −1.5[^12] |
| RTP (The Clearing House) | Review & authorize | 1.5 | 3.5 | −2.0[^13] |
| RTP (The Clearing House) | Execute & track | 1.5 | 3 | −1.5[^14] |
| RTP (The Clearing House) | Confirm & complete | 1.5 | 3.5 | −2.0[^15] |
| RTP (The Clearing House) | Manage | 1.5 | 3 | −1.5[^16] |
| RTP (The Clearing House) | Exception | 1.5 | 3 | −1.5[^17] |
| RTP (The Clearing House) | Support | 1.5 | 3 | −1.5[^18] |

## Gaps

- **high** · Discover · missing capability · No consumer- or SMB-initiated RTP/FedNow send exists outside RfP-driven Bill Pay, and instant rails are not marketed at all, despite WF being a dual-rail sender via API (CONFIRMED_BANK S916).[^19]
- **medium** · Review & authorize · security trust · Business Bill Pay has no dual control; any 'View and Transact' delegate can pay.[^20]
- **low** · Manage · transparency · Public Bill Pay FAQs omit edit/cancel and return handling (deferred to post-sign-on Help).[^21]
- **low** · Discover · transparency · RfP instant pay is not marketed; discoverability depends entirely on biller participation. Observed on the web (Nov 2026, S990): the pre-enrollment Bill Pay welcome page does not mention instant payments or Request for Payment.[^22]

## Strengths

- Exception · Bill Pay Payment Guarantee covers late fees and explicitly includes RfP instant payments.[^23]
- Review & authorize · Consumers can pay a biller Request for Payment instantly in mobile Bill Pay (RTP or another instant network, up to $50k).[^24]
- Initiate · Autopay rules cover full statement, minimum or fixed amount.[^25]

[^1]: kj · score/bill-pay/discover · 8e100b7ea6ea
[^2]: kj · score/bill-pay/set-up · 992518b75df6
[^3]: kj · score/bill-pay/initiate · 29efc9575cbb
[^4]: kj · score/bill-pay/review-authorize · 992518b75df6
[^5]: kj · score/bill-pay/execute-track · 992518b75df6
[^6]: kj · score/bill-pay/confirm-complete · 992518b75df6
[^7]: kj · score/bill-pay/manage · 53ac3b61085d
[^8]: kj · score/bill-pay/exception · c5079ab325b6
[^9]: kj · score/bill-pay/support · 8e100b7ea6ea
[^10]: kj · score/rtp/discover · 48ea2f9e1d21
[^11]: kj · score/rtp/set-up · 77bc42247c8b
[^12]: kj · score/rtp/initiate · f0d83abc5932
[^13]: kj · score/rtp/review-authorize · b368661dc399
[^14]: kj · score/rtp/execute-track · 77bc42247c8b
[^15]: kj · score/rtp/confirm-complete · eeb6592c861a
[^16]: kj · score/rtp/manage · 77bc42247c8b
[^17]: kj · score/rtp/exception · 77bc42247c8b
[^18]: kj · score/rtp/support · 77bc42247c8b
[^19]: kj · finding/GAP-WF-0021 · 5e5beba3e875
[^20]: kj · finding/GAP-WF-0030 · 7bc98ff7c9c1
[^21]: kj · finding/GAP-WF-0020 · 47488cd765b0
[^22]: kj · finding/GAP-WF-0023 · bb31f6be7f9e
[^23]: kj · finding/STR-WF-0011 · 783b030bc6fa
[^24]: kj · finding/STR-WF-0012 · fe40b315e4b6
[^25]: kj · finding/STR-WF-0017 · caf214179018

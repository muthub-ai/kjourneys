---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Bill Pay (Online Bill Pay / Business Bill Pay): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "503f89691f0a9c96bd113929b1ebc5650dd84b67f55235addddaf9eb97647986",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Bill Pay (Online Bill Pay / Business Bill Pay) — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Bill pay | Discover | 3 | 3 | at best practice[^1] |
| Bill pay | Set up | 3 | 3 | at best practice[^2] |
| Bill pay | Initiate | 3 | 4 | −1[^3] |
| Bill pay | Review & authorize | 3 | 3 | at best practice[^4] |
| Bill pay | Execute & track | 3 | 3 | at best practice[^5] |
| Bill pay | Confirm & complete | 3 | 3 | at best practice[^6] |
| Bill pay | Manage | 3 | 3 | at best practice[^7] |
| Bill pay | Exception | 3 | 3 | at best practice[^8] |
| Bill pay | Support | 3 | 3 | at best practice[^9] |
| RTP (The Clearing House) | Discover | 1 | 3 | −2[^10] |
| RTP (The Clearing House) | Set up | 1 | 3 | −2[^11] |
| RTP (The Clearing House) | Initiate | 1 | 3 | −2[^12] |
| RTP (The Clearing House) | Review & authorize | 1 | 3 | −2[^13] |
| RTP (The Clearing House) | Execute & track | 1 | 3 | −2[^14] |
| RTP (The Clearing House) | Confirm & complete | 1 | 3 | −2[^15] |
| RTP (The Clearing House) | Manage | 1 | 3 | −2[^16] |
| RTP (The Clearing House) | Exception | 1 | 3 | −2[^17] |
| RTP (The Clearing House) | Support | 1 | 3 | −2[^18] |

## Gaps

- **high** · Discover · missing capability · No consumer- or SMB-initiated RTP/FedNow send exists outside RfP-driven Bill Pay, and instant rails are not marketed at all, despite WF being a dual-rail sender via API (CONFIRMED_BANK S916).[^19]
- **medium** · Review & authorize · security trust · Business Bill Pay has no dual control; any 'View and Transact' delegate can pay.[^20]
- **low** · Manage · transparency · Public Bill Pay FAQs omit edit/cancel and return handling (deferred to post-sign-on Help).[^21]
- **low** · Discover · transparency · RfP instant pay is not marketed; discoverability depends entirely on biller participation. Observed on the web (Nov 2026, S990): the pre-enrollment Bill Pay welcome page does not mention instant payments or Request for Payment.[^22]

## Strengths

- Exception · Bill Pay Payment Guarantee covers late fees and explicitly includes RfP instant payments.[^23]
- Review & authorize · Consumers can pay a biller Request for Payment instantly in mobile Bill Pay (RTP or another instant network, up to $50k).[^24]
- Initiate · Autopay rules cover full statement, minimum or fixed amount.[^25]

[^1]: kj · score/bill-pay/discover · 992518b75df6
[^2]: kj · score/bill-pay/set-up · 992518b75df6
[^3]: kj · score/bill-pay/initiate · 1c0b06399f9f
[^4]: kj · score/bill-pay/review-authorize · 992518b75df6
[^5]: kj · score/bill-pay/execute-track · 992518b75df6
[^6]: kj · score/bill-pay/confirm-complete · 992518b75df6
[^7]: kj · score/bill-pay/manage · 53ac3b61085d
[^8]: kj · score/bill-pay/exception · 5a0578a2664c
[^9]: kj · score/bill-pay/support · 992518b75df6
[^10]: kj · score/rtp/discover · 946ae7ab398c
[^11]: kj · score/rtp/set-up · 4b62946fe364
[^12]: kj · score/rtp/initiate · f4120de6c42a
[^13]: kj · score/rtp/review-authorize · 2758a9be323a
[^14]: kj · score/rtp/execute-track · 4b62946fe364
[^15]: kj · score/rtp/confirm-complete · 4b62946fe364
[^16]: kj · score/rtp/manage · 4b62946fe364
[^17]: kj · score/rtp/exception · 4b62946fe364
[^18]: kj · score/rtp/support · 4b62946fe364
[^19]: kj · finding/GAP-WF-0021 · 6a96d04bb8de
[^20]: kj · finding/GAP-WF-0031 · 2c6179b4c9e0
[^21]: kj · finding/GAP-WF-0020 · 7a3608b53b50
[^22]: kj · finding/GAP-WF-0024 · acf7de526324
[^23]: kj · finding/STR-WF-0010 · e804199b7d4b
[^24]: kj · finding/STR-WF-0011 · cdaca39c7bba
[^25]: kj · finding/STR-WF-0016 · 0796d10725fb

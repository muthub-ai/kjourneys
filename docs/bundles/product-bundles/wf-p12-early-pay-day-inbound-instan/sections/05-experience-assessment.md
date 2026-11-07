---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "68a658e1777d1f73648087a1d9e29010e7f786f79f3fcb0413f63efb5ffd81b0",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| RTP (The Clearing House) | Discover | 1 | 3 | −2[^1] |
| RTP (The Clearing House) | Set up | 1 | 3 | −2[^2] |
| RTP (The Clearing House) | Initiate | 1 | 3 | −2[^3] |
| RTP (The Clearing House) | Review & authorize | 1 | 3 | −2[^4] |
| RTP (The Clearing House) | Execute & track | 1 | 3 | −2[^5] |
| RTP (The Clearing House) | Confirm & complete | 1 | 3 | −2[^6] |
| RTP (The Clearing House) | Manage | 1 | 3 | −2[^7] |
| RTP (The Clearing House) | Exception | 1 | 3 | −2[^8] |
| RTP (The Clearing House) | Support | 1 | 3 | −2[^9] |

## Gaps

- **medium** · Initiate · transparency · How inbound RTP/FedNow credits are labelled and alerted is unpublished.[^10]
- **medium** · Set up · missing capability · Observed: direct-deposit setup is a prefilled PDF ('Prefill your direct deposit form' → 'Create Form' → hand to the employer).[^11]
- **low** · Confirm & complete · transparency · Observed: the web 'Manage Alerts' page offers checking accounts only balance (zero/low/high), Direct Deposit and Returned Deposited Item alerts — no transfer-sent, transfer-received or Zelle alert options on the web (app alert catalogue not observed).[^12]

## Strengths

- Initiate · Early Pay Day applies automatically with no enrollment.[^13]

[^1]: kj · score/rtp/discover · 946ae7ab398c
[^2]: kj · score/rtp/set-up · 4b62946fe364
[^3]: kj · score/rtp/initiate · f4120de6c42a
[^4]: kj · score/rtp/review-authorize · 2758a9be323a
[^5]: kj · score/rtp/execute-track · 4b62946fe364
[^6]: kj · score/rtp/confirm-complete · 4b62946fe364
[^7]: kj · score/rtp/manage · 4b62946fe364
[^8]: kj · score/rtp/exception · 4b62946fe364
[^9]: kj · score/rtp/support · 4b62946fe364
[^10]: kj · finding/GAP-WF-0023 · bbb6b037be46
[^11]: kj · finding/GAP-WF-0038 · afdbdd7ae471
[^12]: kj · finding/GAP-WF-0039 · d396e36594a3
[^13]: kj · finding/STR-WF-0015 · 2a19538886f3

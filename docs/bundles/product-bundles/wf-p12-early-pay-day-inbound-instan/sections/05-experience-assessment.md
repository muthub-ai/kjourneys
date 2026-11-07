---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "4dae99c16e2da966a77faaa716b73023ee75803691922481d1f5b5e1bb8934f0",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. From report v2, each score is the mean across MI's customer journeys, so half points occur. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| RTP (The Clearing House) | Discover | 1.5 | 3.5 | −2.0[^1] |
| RTP (The Clearing House) | Set up | 1.5 | 3 | −1.5[^2] |
| RTP (The Clearing House) | Initiate | 1.5 | 3 | −1.5[^3] |
| RTP (The Clearing House) | Review & authorize | 1.5 | 3.5 | −2.0[^4] |
| RTP (The Clearing House) | Execute & track | 1.5 | 3 | −1.5[^5] |
| RTP (The Clearing House) | Confirm & complete | 1.5 | 3.5 | −2.0[^6] |
| RTP (The Clearing House) | Manage | 1.5 | 3 | −1.5[^7] |
| RTP (The Clearing House) | Exception | 1.5 | 3 | −1.5[^8] |
| RTP (The Clearing House) | Support | 1.5 | 3 | −1.5[^9] |

## Gaps

- **medium** · Set up · missing capability · Observed: direct-deposit setup is a prefilled PDF ('Prefill your direct deposit form' → 'Create Form' → hand to the employer).[^10]
- **low** · Confirm & complete · transparency · Observed: the web 'Manage Alerts' page offers checking accounts only balance (zero/low/high), Direct Deposit and Returned Deposited Item alerts — no transfer-sent, transfer-received or Zelle alert options on the web (app alert catalogue not observed).[^11]

## Strengths

- Initiate · Second-wave evidence: inbound RTP/FedNow credits display as 'Instant Pmt' with the sender's name and post to the available balance within seconds, 24/7 (instant payments FAQ, S971); alert configuration for instant credits is still not described.[^12]
- Initiate · Early Pay Day applies automatically with no enrollment.[^13]

[^1]: kj · score/rtp/discover · 48ea2f9e1d21
[^2]: kj · score/rtp/set-up · 77bc42247c8b
[^3]: kj · score/rtp/initiate · f0d83abc5932
[^4]: kj · score/rtp/review-authorize · b368661dc399
[^5]: kj · score/rtp/execute-track · 77bc42247c8b
[^6]: kj · score/rtp/confirm-complete · eeb6592c861a
[^7]: kj · score/rtp/manage · 77bc42247c8b
[^8]: kj · score/rtp/exception · 77bc42247c8b
[^9]: kj · score/rtp/support · 77bc42247c8b
[^10]: kj · finding/GAP-WF-0037 · fdd4036ab323
[^11]: kj · finding/GAP-WF-0038 · c93bd0348369
[^12]: kj · finding/STR-WF-0001 · 4ca71ea482b2
[^13]: kj · finding/STR-WF-0016 · b860c5256638

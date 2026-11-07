---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p15-commercial-receivables-fraud",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P15",
  "line_of_business": "wf-cb",
  "content_sha256": "7d05b587f2428d5d91bbaa6bf7375b596225b585f6f2db40cdaddde39b101569",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — experience assessment

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
| Domestic wire | Discover | 3 | 3 | at best practice[^10] |
| Domestic wire | Set up | 3 | 4 | −1[^11] |
| Domestic wire | Initiate | 2 | 3 | −1[^12] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^13] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^14] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^15] |
| Domestic wire | Manage | 3 | 3 | at best practice[^16] |
| Domestic wire | Exception | 2 | 3 | −1[^17] |
| Domestic wire | Support | 3 | 3 | at best practice[^18] |

## Gaps

None recorded in this study.[^19]

## Strengths

None recorded in this study.[^19]

[^1]: kj · score/ach-origination/discover · e7868e030a7b
[^2]: kj · score/ach-origination/set-up · 9cd5f2dd79c9
[^3]: kj · score/ach-origination/initiate · c946a97de3a8
[^4]: kj · score/ach-origination/review-authorize · 43ac935a9848
[^5]: kj · score/ach-origination/execute-track · 90a35a4bb765
[^6]: kj · score/ach-origination/confirm-complete · f4048a16db48
[^7]: kj · score/ach-origination/manage · 77661bdd40e1
[^8]: kj · score/ach-origination/exception · 6a30cf3346db
[^9]: kj · score/ach-origination/support · f4048a16db48
[^10]: kj · score/wire-domestic/discover · a7eda35b2559
[^11]: kj · score/wire-domestic/set-up · b1ac6d947794
[^12]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^13]: kj · score/wire-domestic/review-authorize · ede3c9a5d788
[^14]: kj · score/wire-domestic/execute-track · 7ce523a435ef
[^15]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^16]: kj · score/wire-domestic/manage · 2814a728a910
[^17]: kj · score/wire-domestic/exception · ec3f316bff3e
[^18]: kj · score/wire-domestic/support · 2814a728a910
[^19]: kj · product/WF-P15 · 8d59fa7b533b

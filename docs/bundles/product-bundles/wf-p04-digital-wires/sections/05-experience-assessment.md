---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Digital Wires (Wire Money): stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "f8e2aac04e1b0ea7a9c897386c07d24947f80e4cb6c93a9a658f6e2f3b82f5fa",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital Wires (Wire Money) — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. From report v2, each score is the mean across MI's customer journeys, so half points occur. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Domestic wire | Discover | 3 | 3 | at best practice[^1] |
| Domestic wire | Set up | 3 | 4 | −1[^2] |
| Domestic wire | Initiate | 2 | 3 | −1[^3] |
| Domestic wire | Review & authorize | 4 | 4 | at best practice[^4] |
| Domestic wire | Execute & track | 4 | 4 | at best practice[^5] |
| Domestic wire | Confirm & complete | 3 | 3 | at best practice[^6] |
| Domestic wire | Manage | 3 | 3 | at best practice[^7] |
| Domestic wire | Exception | 2 | 3 | −1[^8] |
| Domestic wire | Support | 3 | 3 | at best practice[^9] |
| International wire | Discover | 3 | 3 | at best practice[^10] |
| International wire | Set up | 3 | 3 | at best practice[^11] |
| International wire | Initiate | 4 | 4 | at best practice[^12] |
| International wire | Review & authorize | 3 | 4 | −1[^13] |
| International wire | Execute & track | 2 | 2 | at best practice[^14] |
| International wire | Confirm & complete | 3 | 3 | at best practice[^15] |
| International wire | Manage | 3 | 4 | −1[^16] |
| International wire | Exception | 3 | 3 | at best practice[^17] |
| International wire | Support | 3 | 3 | at best practice[^18] |

## Gaps

- **high** · Review & authorize · security trust · SMB wires from Business Online have no dual approval (INFERRED, WF-C003); a single delegate can release a foreign-currency wire.[^19]
- **medium** · Initiate · transparency · Digital wire fee messaging conflicts ($30 flat on product page vs '$0-$30' in FAQ) and limits are opaque until entry.[^20]
- **medium** · Exception · exception handling · Cancellation is possible only while 'Scheduled'; once Pending, recall requires a call to 877-499-6920 and there is no in-app recall request.[^21]
- **medium** · Execute & track · transparency · International wires show only Scheduled/Pending/Completed for 1-5 business days; no gpi-style correspondent tracking or ETA.[^22]
- **low** · Discover · channel gap · Published Digital Wires steps cover Wells Fargo Online only; the mobile-app flow (offered per the comparison chart) is undocumented.[^23]

## Strengths

- Execute & track · Richest public wire status vocabulary of the peer set (Scheduled, Pending, Completed, Failed, Canceled, Returned, Under review).[^24]
- Initiate · Foreign-currency rate lock with markup disclosed and a $0 consumer FX wire fee across 200+ countries / 30 currencies.[^25]
- Review & authorize · Mandatory OTP or RSA SecurID on every digital wire, plus wire-scam guidance on review.[^26]
- Discover · Observed: Wire Money opens with a rail-specific wire-scam banner and a 'Compare options' explainer (Zelle vs Wires; ExpressSend vs Wires) tabulating fees, delivery speed, cash-to-person, enrollment channel and locations — the in-hub rail guidance the composite calls for.[^27]
- Set up · Observed: the add-recipient wizard (3 steps) offers an in-flow 'Find an ABA/RTN' lookup and a Wells Fargo routing hint on the recipient's bank-info step.[^28]

[^1]: kj · score/wire-domestic/discover · a7eda35b2559
[^2]: kj · score/wire-domestic/set-up · b1ac6d947794
[^3]: kj · score/wire-domestic/initiate · 2df0c37cba04
[^4]: kj · score/wire-domestic/review-authorize · ede3c9a5d788
[^5]: kj · score/wire-domestic/execute-track · 7ce523a435ef
[^6]: kj · score/wire-domestic/confirm-complete · 2814a728a910
[^7]: kj · score/wire-domestic/manage · 2814a728a910
[^8]: kj · score/wire-domestic/exception · ec3f316bff3e
[^9]: kj · score/wire-domestic/support · 2814a728a910
[^10]: kj · score/wire-international/discover · 6260b23c8d9a
[^11]: kj · score/wire-international/set-up · 6260b23c8d9a
[^12]: kj · score/wire-international/initiate · adc77a4c5488
[^13]: kj · score/wire-international/review-authorize · 25add189f337
[^14]: kj · score/wire-international/execute-track · e924cf09b15f
[^15]: kj · score/wire-international/confirm-complete · 6260b23c8d9a
[^16]: kj · score/wire-international/manage · 25add189f337
[^17]: kj · score/wire-international/exception · 6260b23c8d9a
[^18]: kj · score/wire-international/support · 6260b23c8d9a
[^19]: kj · finding/GAP-WF-0029 · a87fe000d932
[^20]: kj · finding/GAP-WF-0014 · 1b33694647db
[^21]: kj · finding/GAP-WF-0016 · 3613671e20fa
[^22]: kj · finding/GAP-WF-0017 · cb93b1938aa9
[^23]: kj · finding/GAP-WF-0015 · 38cf398e4fca
[^24]: kj · finding/STR-WF-0006 · 122172aba700
[^25]: kj · finding/STR-WF-0008 · 94263ca0c11c
[^26]: kj · finding/STR-WF-0007 · c982fc56f2d8
[^27]: kj · finding/STR-WF-0023 · 5f1179bd2b02
[^28]: kj · finding/STR-WF-0024 · ce7383770d37

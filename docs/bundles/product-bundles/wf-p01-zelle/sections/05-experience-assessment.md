---
{
 "type": "product-bundle/section",
 "title": "Experience assessment",
 "description": "Zelle®: stage scores against best practice, gaps and strengths",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "503db6862507532045dd5ce36f1af03fd350252de65a378669e1962d4d3c599c",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — experience assessment

*Method:* Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.

| Rail | Stage | Wells Fargo | Best practice | Gap |
|---|---|---|---|---|
| Request to pay | Discover | 3 | 4 | −1[^1] |
| Request to pay | Set up | 3 | 3 | at best practice[^2] |
| Request to pay | Initiate | 2 | 4 | −2[^3] |
| Request to pay | Review & authorize | 3 | 3 | at best practice[^4] |
| Request to pay | Execute & track | 3 | 3 | at best practice[^5] |
| Request to pay | Confirm & complete | 3 | 3 | at best practice[^6] |
| Request to pay | Manage | 3 | 3 | at best practice[^7] |
| Request to pay | Exception | 3 | 3 | at best practice[^8] |
| Request to pay | Support | 3 | 3 | at best practice[^9] |
| Zelle | Discover | 3 | 3 | at best practice[^10] |
| Zelle | Set up | 3 | 3 | at best practice[^11] |
| Zelle | Initiate | 3 | 3 | at best practice[^12] |
| Zelle | Review & authorize | 1 | 3 | −2[^13] |
| Zelle | Execute & track | 3 | 3 | at best practice[^14] |
| Zelle | Confirm & complete | 3 | 3 | at best practice[^15] |
| Zelle | Manage | 3 | 3 | at best practice[^16] |
| Zelle | Exception | 2 | 2 | at best practice[^17] |
| Zelle | Support | 2 | 3 | −1[^18] |

## Gaps

- **high** · Review & authorize · security trust · Review screen carries only static 'only send to people you know and trust' copy; no risk-tiered interstitial, payment-purpose or contact-origin question is documented, and the Zelle-specific scam page now 404s. Observed on the web (Nov 2026): the only scam messaging before the amount screen is a static banner shown on every Zelle visit; the review screen itself was not reached.[^19]
- **high** · Exception · exception handling · Unauthorized and scam claims start by phone (1-800-956-4442 / 1-866-867-5568) or by mail to a P.O. box; no in-app 'report a problem' on the Zelle transaction and no in-app claim status tracker for Zelle. Corroborated on the web (Nov 2026, S990): a completed Zelle payment's detail screen offers only 'Block'; on the observed profile the 'Track Claims > Dispute a charge' picker listed only debit-card purchases (whether non-card items are excluded is unconfirmed); 'Report Phish & Email Scams' leaves the secure session for a public education page.[^20]
- **high** · Review & authorize · security trust · Business Zelle sends in Business Online can be executed by a single 'View and Transact' delegate; no secondary approval (INFERRED from OAA per WF-C003). Dual custody exists only for Vantage Treasury Management enrollees.[^21]
- **medium** · Exception · transparency · Scam-reimbursement stance is the network minimum ('qualifying imposter scams'); eligibility criteria and decision timeline for authorized-scam claims are not published.[^22]
- **medium** · Support · friction · Fraud and scam support is split across at least four phone numbers with different scopes (1-800-869-3557, 1-800-956-4442, 1-866-867-5568, 1-800-225-5935).[^23]
- **medium** · Initiate · friction · 'Split' is marketed but implemented as separate single requests; no multi-payer split screen with per-person amounts.[^24]
- **low** · Manage · friction · No request reminders; a payer who refuses cannot be re-requested.[^25]
- **low** · Discover · friction · Observed: on the web, Zelle is the fourth item of the 'Move Money & Pay Bills' panel and the hub offers no guidance on when to use Zelle versus a transfer or wire; the rail comparison lives inside Wire Money.[^26]

## Strengths

- Discover · Zelle has its own bottom-nav tab and can be initiated by Fargo, the deepest navigation placement among the ten.[^27]
- Review & authorize · Step-up access code (text or RSA SecurID) on first payment to a new recipient.[^28]
- Manage · Skip-one or cancel-series for scheduled Zelle until 11:30 PM PT the day before; 24-month activity and 2-year visibility of cancelled items.[^29]
- Set up · Business Zelle tag plus QR code displaying the business name.[^30]
- Manage · Observed: Zelle 'Family controls' lets a parent enable or disable Zelle for a teen account holder — a control no public Wells Fargo page describes and that appears in no peer inventory built from public sources.[^31]
- Initiate · Observed: the web amount screen shows the recipient's Zelle-registered name ('Enrolled as …'), the daily and 30-day limits inline (whether remaining or total amounts was not recorded), a required 'Pay from' selector and the 'Repeat payment' toggle on one screen.[^32]

[^1]: kj · score/request-to-pay/discover · 8aaf5ddcb63e
[^2]: kj · score/request-to-pay/set-up · 64a250a3c380
[^3]: kj · score/request-to-pay/initiate · 72fbb231701c
[^4]: kj · score/request-to-pay/review-authorize · 64a250a3c380
[^5]: kj · score/request-to-pay/execute-track · 64a250a3c380
[^6]: kj · score/request-to-pay/confirm-complete · 64a250a3c380
[^7]: kj · score/request-to-pay/manage · a1ae3362759e
[^8]: kj · score/request-to-pay/exception · 64a250a3c380
[^9]: kj · score/request-to-pay/support · 64a250a3c380
[^10]: kj · score/zelle/discover · 2bd0b74d37f1
[^11]: kj · score/zelle/set-up · f3093057d59e
[^12]: kj · score/zelle/initiate · 673a47124b13
[^13]: kj · score/zelle/review-authorize · a3f06b174bf4
[^14]: kj · score/zelle/execute-track · 02cb1535a9b8
[^15]: kj · score/zelle/confirm-complete · 02cb1535a9b8
[^16]: kj · score/zelle/manage · 8d99b809a6a4
[^17]: kj · score/zelle/exception · 89e1f8bb4e9d
[^18]: kj · score/zelle/support · 850a938312d2
[^19]: kj · finding/GAP-WF-0001 · 38c101614c6a
[^20]: kj · finding/GAP-WF-0002 · 4e09e7353ec2
[^21]: kj · finding/GAP-WF-0008 · 35e06b5dbd70
[^22]: kj · finding/GAP-WF-0003 · a9b601e4c21e
[^23]: kj · finding/GAP-WF-0004 · 069260253e2f
[^24]: kj · finding/GAP-WF-0006 · 3782e8a4f392
[^25]: kj · finding/GAP-WF-0007 · 8cfc91935657
[^26]: kj · finding/GAP-WF-0036 · 100d7a3aaf40
[^27]: kj · finding/STR-WF-0001 · bb3dd7fabeb8
[^28]: kj · finding/STR-WF-0002 · 63a6e9b96a41
[^29]: kj · finding/STR-WF-0003 · db967ece611f
[^30]: kj · finding/STR-WF-0004 · f24f20dbe1a5
[^31]: kj · finding/STR-WF-0021 · 1fa52835558b
[^32]: kj · finding/STR-WF-0020 · 9d37e3577ce0

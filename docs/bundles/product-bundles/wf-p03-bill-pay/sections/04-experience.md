---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Bill Pay (Online Bill Pay / Business Bill Pay) journey: steps, stages, channels and MI's assessment",
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
  "content_sha256": "13ca77317a6a05d127bee46ee435a341b47154d71b35c66953abc4ba2b432f89",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Bill Pay (Online Bill Pay / Business Bill Pay) — journeys and experience

## `WF-J07` Consumer adds a payee and pays a bill (electronic or check)

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app, voice-chat-assistant. Status tracking: Bill Pay 'Payment History' (incl. check cashed dates); 'Transfer and payment Activity'; Fargo 'Which bills are due?'.[^1]

Delivers the customer journey **Consumer adds a payee and pays a bill** (linked by mi reference).[^1][^2]

MI assessment: Mature bill pay with explicit guarantee and check-cashed visibility; no in-flow eligible 'instant' option except RfP-driven instant payments (J09).[^1]

## `WF-J08` Consumer activates eBills and sets auto pay

11 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app. Status tracking: Bill Pay 'Payment History' (incl. check cashed dates); 'Transfer and payment Activity'; Fargo 'Which bills are due?'.[^3]

Delivers the customer journey **Consumer activates eBills and manages autopay** (linked by mi reference).[^3][^4]

MI assessment: Standard eBill/autopay; WF loan eBills integrated.[^3]

## `WF-J09` Consumer pays a Request for Payment instantly in Bill Pay (RTP instant payment, mobile)

11 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app. Status tracking: Bill Pay in mobile app (Payment History).[^5]

Delivers the customer journey **Consumer receives an instant credit and pays a biller Request for Payment (payer side)** (linked by mi reference).[^5][^6]

MI assessment: Important hidden capability: WF consumers can SEND RTP credit-push payments, but only in response to a biller RfP inside Bill Pay, mobile-only — a 'request-to-pay' (inbound RfP) consumer experience that few peers have. Zero marketing presence; terms-only evidence.[^5]

## `WF-J17` Small business pays an invoice with Business Bill Pay funded by a business credit card

10 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app. Status tracking: Payment History.[^7]

Delivers the customer journey **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** (linked by mi reference).[^7][^8]

MI assessment: Card-funded bill pay is a differentiator for SMB cash flow.[^7]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1][^3][^5][^7]

[^1]: kj · journey/WF-J07 · 8270f6fa66c5
[^2]: kj · customer-journey/CJ-BILLPAY-SEND · ebd10948d1ce
[^3]: kj · journey/WF-J08 · 43861b5c7ba6
[^4]: kj · customer-journey/CJ-BILLPAY-EBILL-MANAGE · 24c5b603c3ec
[^5]: kj · journey/WF-J09 · 57b4cafbf531
[^6]: kj · customer-journey/CJ-INSTANT-RECEIVE-RFP · f0a2b8d96952
[^7]: kj · journey/WF-J17 · 161d120bfa87
[^8]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11

---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Digital Wires (Wire Money) journey: steps, stages, channels and MI's assessment",
 "sources": [
  {
   "id": "kj-wells-fargo",
   "path": "docs/bundles/_source/wells-fargo.json",
   "sha256": "7320ba3f33f2f88d6c7aa278ce5e73815a221e37edfb352b6b11bcd36c0aedb7"
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "2dbfc41a018e7cffa55d954e9e0e3afea83be6cfe3a42087bf4339c32281d9e2",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital Wires (Wire Money) — journeys and experience

## `WF-J10` Consumer sends a domestic wire online (Digital Wires)

15 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app, branch. Status tracking: Wire money home 'Activity', 'Wire details' page, Confirmation page.[^1]

Delivers the customer journey **Consumer sends a domestic wire to a new recipient** (linked by mi reference).[^1][^2]

MI assessment: Strong status vocabulary (7 states incl. Under review/Returned) and mandatory OTP/SecurID; weakness: no mobile-specific documentation, limits opaque, 'Scheduled'-only cancel window.[^1]

## `WF-J11` Consumer sends an international wire in foreign currency

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app, branch. Status tracking: Wire money home 'Activity', 'Wire details' page, Confirmation page.[^3]

Delivers the customer journey **Consumer sends an international wire in foreign currency** (linked by mi reference).[^3][^4]

MI assessment: Foreign-currency rate lock with $0 fee is a competitive hook; Reg E 30-minute cancel is well documented.[^3]

## `WF-J18` Small business sends a foreign-currency wire from Business Online

9 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app, branch. Status tracking: Wire Activity.[^5]

Delivers the customer journey **Small business pays payroll/vendors by ACH (standard, same-day, real-time) with approvals** (linked by mi reference).[^5][^6]

MI assessment: Same engine as consumer; FX rate lock and receive-in-27-currencies are strong; lacks SMB dual approval.[^5]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1][^3][^5]

[^1]: kj · journey/WF-J10 · 47452d55448b
[^2]: kj · customer-journey/CJ-WIRE-DOM-CONSUMER-SEND · 5229e78a1d68
[^3]: kj · journey/WF-J11 · e4ed66bc72f0
[^4]: kj · customer-journey/CJ-WIRE-INTL-CONSUMER-SEND · eee82a62d089
[^5]: kj · journey/WF-J18 · 7f1916a52a55
[^6]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · e1251bb592b3

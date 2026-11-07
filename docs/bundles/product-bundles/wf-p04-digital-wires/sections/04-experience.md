---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Digital Wires (Wire Money) journey: steps, stages, channels and MI's assessment",
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
  "content_sha256": "852af532b473d3ecddd1016f841a32bd2f96893fa0837e960db14ca27e360c62",
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

[^1]: kj · journey/WF-J10 · ca29755fbe66
[^2]: kj · customer-journey/CJ-WIRE-DOM-CONSUMER-SEND · ba0b56b8b7ed
[^3]: kj · journey/WF-J11 · 5759e78f0c18
[^4]: kj · customer-journey/CJ-WIRE-INTL-CONSUMER-SEND · 556725478191
[^5]: kj · journey/WF-J18 · da9c57fe16e4
[^6]: kj · customer-journey/CJ-ACH-ORIG-SMB-SEND · cfd851265b11

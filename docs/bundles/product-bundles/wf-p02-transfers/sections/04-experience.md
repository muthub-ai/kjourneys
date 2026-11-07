---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Transfers (Transfer Money) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "96d5ac9531ccf8e5341a9ed6f0a5e2531bb2e33a0a4c94ba4931d01ac74eaeba",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Transfers (Transfer Money) — journeys and experience

## `WF-J05` Consumer transfers between own Wells Fargo accounts (mobile), one-time and recurring

16 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web, voice-chat-assistant, atm. Status tracking: Web 'Transfer and payment Activity' (View/Edit, View/Delete); mobile 'Transfer' tab > 'Scheduled Transfers & Payments'; Account Activity shows 'pending' after 8 pm PT.[^1]

Delivers the customer journey **Consumer moves money between own accounts** (linked by mi reference).[^1][^2]

MI assessment: Clean, no-friction; memo field and ATM transfers are nice touches.[^1]

## `WF-J06` Consumer links an external bank account and transfers money ('Bank-to-bank transfers')

17 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app. Status tracking: Web 'Transfer & Payment Activity' table (Send on | From | To | Amount | Status | Action View / Edit) — observed; mobile 'Transfer' tab > 'Scheduled Transfers & Payments'; Account Activity shows 'pending' after 8 pm PT.[^3]

Delivers the customer journey **Consumer links an external account and pushes money out** (linked by mi reference).[^3][^4]

MI assessment: Standard ACH link-and-transfer; slower than peers that offer instant account verification and same/next-day by default. Expedited 'next day' only discretionary.[^3]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1][^3]

[^1]: kj · journey/WF-J05 · 8cc99d20c29f
[^2]: kj · customer-journey/CJ-INTERNAL-TRANSFER · edfddfd7c154
[^3]: kj · journey/WF-J06 · 5ac14c85b11a
[^4]: kj · customer-journey/CJ-ACH-EXT-SEND · 2ec667c942b3

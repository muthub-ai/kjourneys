---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Transfers (Transfer Money) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p02-transfers",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P02",
  "line_of_business": "wf-cbl",
  "content_sha256": "b2493201e48985976e4f910ad06923e558c7dec9983079fb66625fa46ec9b649",
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

[^1]: kj · journey/WF-J05 · 961155a3b7eb
[^2]: kj · customer-journey/CJ-INTERNAL-TRANSFER · 2d8719aff17e
[^3]: kj · journey/WF-J06 · ee855eb97a21
[^4]: kj · customer-journey/CJ-ACH-EXT-SEND · 74e77a0ea302

---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Zelle® journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "d0cb04b2fcde2c72b9b4245e9fd2c4f60fa6cadcace39758e42534139b8d1634",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — journeys and experience

## `WF-J01` Consumer sends money to a new recipient with Zelle® (mobile)

19 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web, voice-chat-assistant. Status tracking: 'Zelle® Activity' (24 months, sorted Completed vs Pending) and 'Scheduled' tab; 'Account Activity' (18 months searchable); Fargo 'View Zelle transactions'.[^1]

Delivers the customer journey **Consumer sends money to a new recipient with Zelle (mobile-first)** (linked by mi reference).[^1][^2]

MI assessment: Strength: deep native integration (bottom-nav tab, Fargo voice send, QR, repeat toggle, 24-month activity). Friction: step-up code on first-time recipient (good control, adds friction); only generic trust warnings — no published evidence of dynamic scam interstitials or payment-purpose prompts, which peers now show; reimbursement limited to 'qualifying imposter scams'.[^1]

## `WF-J02` Consumer requests money / splits a cost with Zelle®

11 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web. Status tracking: 'Zelle® Activity' (24 months, sorted Completed vs Pending) and 'Scheduled' tab; 'Account Activity' (18 months searchable); Fargo 'View Zelle transactions'.[^3]

Delivers the customer journey **Consumer requests money or splits a bill with Zelle** (linked by mi reference).[^3][^4]

MI assessment: Split is marketed but implemented as individual requests; no evidence of a dedicated 'split' multi-payer screen like Zelle app's former split feature.[^3]

## `WF-J03` Small business gets paid with a Zelle® tag / QR code and pays a vendor

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web. Status tracking: 'Zelle® Activity' (24 months, sorted Completed vs Pending) and 'Scheduled' tab; 'Account Activity' (18 months searchable); Fargo 'View Zelle transactions'.[^5]

Delivers the customer journey **Small business gets paid with a Zelle tag/QR and pays vendors under controls** (linked by mi reference).[^5][^6]

MI assessment: Tag + QR receive is a clear SMB differentiator; absence of SMB dual approval on Zelle is a control gap relative to Direct Pay.[^5]

## `WF-J28` Consumer reports an unauthorized Zelle/online transfer or an imposter scam and seeks reimbursement

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: phone, mobile-app, web, branch. Status tracking: Claim status by phone (debit 1-800-548-9554); Message Center; web Security & Support > Track Claims > 'My claims' (Open / Closed) — observed, scope of claim types shown not confirmed.[^7]

Delivers the customer journey **Consumer sends money to a new recipient with Zelle (mobile-first)** (linked by mi reference).[^7][^2]

MI assessment: Clear Reg E articulation in the Addendum; scam stance is the network minimum ('qualifying imposter scams'); no public WF-specific scam-reimbursement commitments beyond that, and the fraud phone tree is fragmented (four numbers).[^7]

## `WF-J29` Consumer sends, requests and manages Zelle® payments on the web (observed logged-in session)

15 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: web, mobile-app, voice-chat-assistant. Status tracking: Zelle > Activity (Sent | Received | Requests tabs; 'View more details' → confirmation number).[^8]

Delivers the customer journey **Consumer sends money to a new recipient with Zelle (mobile-first)** (linked by mi reference).[^8][^2]

MI assessment: Observed first-hand on the web (review and confirmation screens not reached). The send flow is compact (recipient → amount with inline limits and a repeat toggle → review) and shows the recipient's registered name before the amount, but the only scam messaging seen is a static banner on every visit. 'Family controls' for teen access is a control no public page describes; 'Blocked contacts' and 'Manage payment profiles' give publicly documented capabilities a management surface. The weak point is exception handling: a completed payment offers only 'Block', no Zelle item was offered in the online dispute picker on this profile, and scam intake is a phone number.[^8]

## `sample` Send money with Zelle

11 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception. Channels: not stated.[^9]

Delivers the customer journey **Consumer sends money to a new recipient with Zelle (mobile-first)** (linked by rail segment).[^9][^2]

*Assessment:* This is the hand-built sample blueprint; its emotions, hot spots, process, controls and app IDs are placeholders for design review.

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1][^3][^5][^7][^8][^9]

[^1]: kj · journey/WF-J01 · c3b8e132fd5c
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 1f6b6a0e7521
[^3]: kj · journey/WF-J02 · 2eca5861046f
[^4]: kj · customer-journey/CJ-ZELLE-REQUEST · cda300f4d27d
[^5]: kj · journey/WF-J03 · 558dd3d0215c
[^6]: kj · customer-journey/CJ-ZELLE-SMB-RECEIVE · dd3d94ee596e
[^7]: kj · journey/WF-J28 · cf400c417393
[^8]: kj · journey/WF-J29 · f76130105e87
[^9]: kj · journey/sample · e85b2befb3b0

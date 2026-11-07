---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Zelle® journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "3278caf2dc01f2eac50938519a0a0e8e2c00b729fd7e0b2b1d574a8afd1fbdce",
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

MI assessment: Strength: deep native integration (bottom-nav tab, Fargo voice send, QR, repeat toggle, 24-month activity). Friction: step-up code on first-time recipient (good control, adds friction); only generic trust warnings — no published evidence of dynamic scam interstitials or payment-purpose prompts, which peers (e.g., peer banks) now show; reimbursement limited to 'qualifying imposter scams'.[^1]

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

[^1]: kj · journey/WF-J01 · 5459e5785f84
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 54cdbe9360ea
[^3]: kj · journey/WF-J02 · 14bc08a80f04
[^4]: kj · customer-journey/CJ-ZELLE-REQUEST · ff349a4a3d24
[^5]: kj · journey/WF-J03 · b89c841e1309
[^6]: kj · customer-journey/CJ-ZELLE-SMB-RECEIVE · 1a1ab5a1e86e
[^7]: kj · journey/WF-J28 · b20fda0a115f
[^8]: kj · journey/WF-J29 · d718f795aee2
[^9]: kj · journey/sample · e85b2befb3b0

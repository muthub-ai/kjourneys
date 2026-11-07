---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "69d9a1db204d22d29749925ae5a8026012e1e3acd3bdc6f603511e36a43bf3d6",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — journeys and experience

## `WF-J20` Commercial ACH origination with dual custody and ACH Fraud Filter (Vantage/CEO)

6 steps across Initiate, Review & authorize, Execute & track, Manage, Exception, Support. Channels: api-treasury-portal, mobile-app. Status tracking: Vantage dashboard / Tasks.[^1]

MI assessment: Mature controls; Same Day ACH availability not confirmed from public pages.[^1]

## `WF-J21` Commercial wire (domestic/international/FX) creation, approval and status search

6 steps across Initiate, Review & authorize, Execute & track, Manage, Exception, Support. Channels: api-treasury-portal, mobile-app. Status tracking: Wires Status Search (Vantage); for international wires, Wells Fargo Payment Tracker (SWIFT gpi-based, 'near real-time status' up to the final beneficiary, incl. date, currency and amount credited and gpi duration; launched Oct 2020, 'Access the tool from any device').[^2]

MI assessment: Mobile wire approval and status search shipped in 2025; clear momentum on Vantage mobile.[^2]

## `WF-J22` Commercial instant payment (RTP®/FedNow®) via Gateway API with rail routing

7 steps across Set up, Initiate, Review & authorize, Execute & track, Manage, Exception, Support. Channels: api-treasury-portal, mobile-app. Status tracking: API / Vantage.[^3]

Delivers the customer journey **Commercial instant payments (RTP/FedNow) via API or treasury portal — sketch** (linked by mi reference).[^3][^4]

MI assessment: Bank page explicitly claims instant send over both RTP and FedNow via API; portal UI for instant payments and commercial RfP not evidenced (dedicated pages blocked).[^3]

## `WF-J23` Commercial consolidated payables file (ACH, wire, card, check) with online approval

6 steps across Initiate, Review & authorize, Execute & track, Manage, Exception, Support. Channels: api-treasury-portal, mobile-app. Status tracking: Vantage reporting.[^5]

MI assessment: Standard integrated payables; instant rail inclusion in payables file not stated.[^5]

## `WF-J25` Commercial mobile multi-check deposit with deposit approval (Vantage app)

6 steps across Initiate, Review & authorize, Execute & track, Manage, Exception, Support. Channels: api-treasury-portal, mobile-app. Status tracking: Vantage app deposit history.[^6]

MI assessment: Deposit approval workflow is a differentiator vs. SMB app.[^6]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1][^2][^3][^5][^6]

[^1]: kj · journey/WF-J20 · aed31b6fcb25
[^2]: kj · journey/WF-J21 · f36035bd9611
[^3]: kj · journey/WF-J22 · 1ca66149586f
[^4]: kj · customer-journey/CJ-COMMERCIAL-INSTANT · 39b78e3dcf64
[^5]: kj · journey/WF-J23 · d8e43801cb3c
[^6]: kj · journey/WF-J25 · 4d80482f689e

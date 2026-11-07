---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p13-wells-fargo-vantage",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P13",
  "line_of_business": "wf-cb",
  "content_sha256": "0936c5246ce11fb7ba4727f869b99c21e5c402a67a628ebd8e1e29a4f791f765",
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

6 steps across Initiate, Review & authorize, Execute & track, Manage, Exception, Support. Channels: api-treasury-portal, mobile-app. Status tracking: Wires Status Search.[^2]

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

[^1]: kj · journey/WF-J20 · a09dfa7d417c
[^2]: kj · journey/WF-J21 · a9e16e59c03f
[^3]: kj · journey/WF-J22 · 30a8718f1eaf
[^4]: kj · customer-journey/CJ-COMMERCIAL-INSTANT · a7aa87a86868
[^5]: kj · journey/WF-J23 · 194624059efa
[^6]: kj · journey/WF-J25 · 982023d3f4b5

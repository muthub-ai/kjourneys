---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p10-card-settings",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P10",
  "line_of_business": "wf-cbl",
  "content_sha256": "dca81bb4a45e89de6782a5df7cdd5335cf65ab68b6a962894b78270acfef3715",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ — journeys and experience

## `WF-J26` Consumer reviews recurring payments/subscriptions and turns a card off (Control Tower / Card Settings)

12 steps across Discover, Set up, Initiate, Review & authorize, Execute & track, Confirm & complete, Manage, Exception, Support. Channels: mobile-app, web, voice-chat-assistant. Status tracking: Card Settings.[^1]

MI assessment: Control Tower was an industry first (2018) but Wells Fargo's public pages no longer brand it; the landing/FAQ pages were unreachable (blocked). Capability persists as 'view recurring payments' in Card Settings per app-store listing.[^1]

Every journey opens as a blueprint in the kjourneys site ([Journey](../../../../dist/index.html#journeys) and [Blueprint](../../../../dist/index.html#blueprint) views).[^1]

[^1]: kj · journey/WF-J26 · 1e8e3f066822

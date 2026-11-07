---
{
 "type": "product-bundle/section",
 "title": "Journeys and experience",
 "description": "Each Card Settings (card on/off, view recurring payments, digital wallets, account access) — formerly Control Tower℠ journey: steps, stages, channels and MI's assessment",
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
  "bundle_id": "wf-p10-card-settings",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P10",
  "line_of_business": "wf-cbl",
  "content_sha256": "13f0be7bf90de1204f128a59cfaa42e099abb982d546c8f6bfce4f27c3e86a3a",
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

[^1]: kj · journey/WF-J26 · 63eb2e769619

---
{
 "type": "product-bundle/section",
 "title": "Operating model",
 "description": "Zelle®: owning line of business, supporting applications and ownership to assign",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "04f953076600ed94e7516cecafd9655a6ba3178491f167cad30ab27f4853b016",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — operating model

Owning line of business: **Consumer Banking and Lending**, Consumer, Small and Business Banking.[^1][^2]

## Applications behind it (sample)

| App ID | Name | Owner team | Application bundle |
|---|---|---|---|
| `agent` | Contact Center Workbench | Contact Center Technology | application-bundles/agent/[^3] |
| `amlmn` | AML Transaction Monitoring | Financial Crimes Technology | application-bundles/amlmn/[^4] |
| `authn` | Identity & Authentication | Identity Platform | application-bundles/authn/[^5] |
| `cstmr` | Customer Profile | Customer Data | application-bundles/cstmr/[^6] |
| `dspte` | Disputes & Claims | Claims Operations | application-bundles/dspte/[^7] |
| `evtbs` | Payments Event Bus | Integration Platform | application-bundles/evtbs/[^8] |
| `ext-zelle` | Zelle Network (Early Warning Services) | Third party — managed by Payments Partnerships | third party[^9] |
| `frdsc` | Real-time Fraud Scoring | Fraud Strategy & Engineering | application-bundles/frdsc/[^10] |
| `ledgr` | Deposit Ledger (DDA core) | Core Banking | application-bundles/ledgr/[^11] |
| `limit` | Limits & Entitlements | Payments Risk Platform | application-bundles/limit/[^12] |
| `mobil` | Mobile Banking App | Digital Channels | application-bundles/mobil/[^13] |
| `notif` | Notification Service | Customer Communications | application-bundles/notif/[^14] |
| `p2phb` | P2P Payments Hub | Digital Payments Engineering | application-bundles/p2phb/[^15] |
| `sttle` | Settlement & Reconciliation | Payments Operations | application-bundles/sttle/[^16] |
| `tokdr` | Token Directory Adapter | Digital Payments Engineering | application-bundles/tokdr/[^17] |

*Assessment:* Product owner, steward and approver are not assigned; set them in knowledge-source.json before this bundle is submitted for review.

[^1]: kj · assignment/WF-P01 · daf9fc88d74e
[^2]: kj · lob/wf-cbl · 9bd65bef07df
[^3]: kj · app/agent · 400d264333ad
[^4]: kj · app/amlmn · 137f74a3a1df
[^5]: kj · app/authn · 2df3575c89c2
[^6]: kj · app/cstmr · 4c1fc7efa157
[^7]: kj · app/dspte · 407377a9f770
[^8]: kj · app/evtbs · a48e2daf1a0e
[^9]: kj · app/ext-zelle · 8ba0169535a6
[^10]: kj · app/frdsc · 0c676b209010
[^11]: kj · app/ledgr · 8315e56a5ad9
[^12]: kj · app/limit · 73270a838258
[^13]: kj · app/mobil · 9078805cb86f
[^14]: kj · app/notif · 34d4ff8e74c2
[^15]: kj · app/p2phb · ff80fb7d1f82
[^16]: kj · app/sttle · 954c191939d5
[^17]: kj · app/tokdr · 4036afdd71c4

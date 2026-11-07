---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "6a1d03fe64dafafa494d0449c98e0a97dfe4ddfcaa915ed9423e078fe4015a40",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — executive summary

**Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits)** (`WF-P12`) is a Wells Fargo product. Early Pay Day posts eligible ACH direct deposits up to two business days early (no enrollment, no fee). The product page explicitly lists RTP® and FedNow® credits as ineligible — confirming WF receives both instant rails into consumer accounts.[^1]

It is owned by **Consumer Banking and Lending** (Consumer, Small and Business Banking). Basis: inferred — Serves consumer customers, which the 10-Q places in Consumer Banking and Lending.[^2][^3]

It has 3 sub-products, 1 of them with a mapped journey, across the FedNow, Other money movement, RTP (The Clearing House) rail(s).[^1][^4][^5][^6]

MI documented 1 journey(s) for it, delivering 1 customer journey(s); they carry 3 gap(s) (2 medium, 1 low) and 1 strength(s).[^7][^8][^9][^10][^11]

## Most severe gaps

- **medium** · Initiate · How inbound RTP/FedNow credits are labelled and alerted is unpublished.[^8]
- **medium** · Set up · Observed: direct-deposit setup is a prefilled PDF ('Prefill your direct deposit form' → 'Create Form' → hand to the employer).[^9]
- **low** · Confirm & complete · Observed: the web 'Manage Alerts' page offers checking accounts only balance (zero/low/high), Direct Deposit and Returned Deposited Item alerts — no transfer-sent, transfer-received or Zelle alert options on the web (app alert catalogue not observed).[^10]

[^1]: kj · product/WF-P12 · d73da35d0cb8
[^2]: kj · assignment/WF-P12 · 64f7eaee3789
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P12-S01 · cdbc7b849c06
[^5]: kj · sub-product/WF-P12-S02 · df182af38e17
[^6]: kj · sub-product/WF-P12-S03 · 9a2db967acf9
[^7]: kj · journey/WF-J15 · e61f32bb5fb1
[^8]: kj · finding/GAP-WF-0023 · bbb6b037be46
[^9]: kj · finding/GAP-WF-0038 · afdbdd7ae471
[^10]: kj · finding/GAP-WF-0039 · d396e36594a3
[^11]: kj · finding/STR-WF-0015 · 2a19538886f3

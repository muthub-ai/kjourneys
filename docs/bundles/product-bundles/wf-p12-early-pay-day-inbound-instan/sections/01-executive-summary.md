---
{
 "type": "product-bundle/section",
 "title": "Executive summary",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): ownership, scope, journeys and its most severe gaps",
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
  "bundle_id": "wf-p12-early-pay-day-inbound-instan",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P12",
  "line_of_business": "wf-cbl",
  "content_sha256": "5ec357b3a7c4df6e984d59acde354b049f246587f4894083f4f9d907b3dcc75c",
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

MI documented 1 journey(s) for it, delivering 1 customer journey(s); they carry 2 gap(s) (1 medium, 1 low) and 2 strength(s).[^7][^8][^9][^10][^11]

## Most severe gaps

- **medium** · Set up · Observed: direct-deposit setup is a prefilled PDF ('Prefill your direct deposit form' → 'Create Form' → hand to the employer).[^8]
- **low** · Confirm & complete · Observed: the web 'Manage Alerts' page offers checking accounts only balance (zero/low/high), Direct Deposit and Returned Deposited Item alerts — no transfer-sent, transfer-received or Zelle alert options on the web (app alert catalogue not observed).[^9]

[^1]: kj · product/WF-P12 · 932e654a57de
[^2]: kj · assignment/WF-P12 · 64f7eaee3789
[^3]: kj · lob/wf-cbl · 9bd65bef07df
[^4]: kj · sub-product/WF-P12-S01 · c723b9c2703e
[^5]: kj · sub-product/WF-P12-S02 · 3ac178eec85d
[^6]: kj · sub-product/WF-P12-S03 · 67cfc08066bd
[^7]: kj · journey/WF-J15 · c6f5929e58f1
[^8]: kj · finding/GAP-WF-0037 · fdd4036ab323
[^9]: kj · finding/GAP-WF-0038 · c93bd0348369
[^10]: kj · finding/STR-WF-0001 · 4ca71ea482b2
[^11]: kj · finding/STR-WF-0016 · b860c5256638

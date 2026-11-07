---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): security and exception gaps, fail points, exception paths and controls",
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
  "content_sha256": "312cc7e1de5bd1055fd3f18317cf34ce64b3568142bba1e11b1a6f2eb52c3daf",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits) — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

- `WF-J15` M03 · No embedded payroll-login direct-deposit switch; the customer carries a PDF to the employer. The web alert catalogue for money movement is thin (no transfer-sent/received or Zelle alert options on the web page; app catalogue not observed).[^2]
- `WF-J15` M06 · No published description of how RTP/FedNow credits are labeled[^3]

## Exception paths

- `WF-J15` · Early Pay Day not applied: Deposit posts on pay date → [^4]

[^1]: kj · product/WF-P12 · 932e654a57de
[^2]: kj · step/WF-J15#M03 · 54949347c136
[^3]: kj · step/WF-J15#M06 · 0dfba3f6cbe0
[^4]: kj · journey/WF-J15 · c6f5929e58f1

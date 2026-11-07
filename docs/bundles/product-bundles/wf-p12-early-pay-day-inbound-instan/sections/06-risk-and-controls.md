---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Early Pay Day & inbound instant receive (RTP/FedNow/Zelle credits): security and exception gaps, fail points, exception paths and controls",
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
  "content_sha256": "f536ad984cba502180663d06ff81fe1249a4abc66ccb4f01e054fdd1f53b839a",
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

[^1]: kj · product/WF-P12 · d73da35d0cb8
[^2]: kj · step/WF-J15#M03 · 2812f9fd2463
[^3]: kj · step/WF-J15#M06 · d4854912c7bd
[^4]: kj · journey/WF-J15 · e61f32bb5fb1

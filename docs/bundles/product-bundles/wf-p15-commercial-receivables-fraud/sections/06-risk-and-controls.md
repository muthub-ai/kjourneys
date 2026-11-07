---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p15-commercial-receivables-fraud",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P15",
  "line_of_business": "wf-cb",
  "content_sha256": "983f9d54d671fd03b86dab5381b6d7225abb0463ded713a95d50b269725c486f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — risk and controls

## Security, trust and exception gaps

None recorded in this study.[^1]

## Fail points along the journeys

None recorded in this study.[^1]

## Exception paths

- `WF-J24` · Unmatched remittance: Exception queue in Integrated Receivables → [^2]

[^1]: kj · product/WF-P15 · 1b70c83e2760
[^2]: kj · journey/WF-J24 · 72f66a396d8c

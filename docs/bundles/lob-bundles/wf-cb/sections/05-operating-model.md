---
{
 "type": "lob-bundle/section",
 "title": "Operating model",
 "description": "Commercial Banking: assignments to confirm and ownership to assign",
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
  "schema": "kf-lob-bundle/0.1",
  "bundle_id": "wf-cb",
  "bank": "wells-fargo",
  "kind": "lob-bundle",
  "line_of_business": "wf-cb",
  "content_sha256": "eee38a6ad1b7860b7647338f0dfad70dc2aca3b5945744b95e044d554bba3ace",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Commercial Banking — operating model

- Confirm: `WF-P13` Wells Fargo Vantage® (replacing Commercial Electronic Office® / CEO®) — Commercial product: treasury management and payments is reported in Commercial Banking and in Corporate and Investment Banking (Q3 2026 10-Q); also used by small businesses[^1]
- Confirm: `WF-P14` Wells Fargo Gateway® APIs (developer portal) — Commercial product: treasury management and payments is reported in Commercial Banking and in Corporate and Investment Banking (Q3 2026 10-Q)[^2]
- Confirm: `WF-P15` Commercial receivables & fraud controls (Perfect Receivables®, Bill Manager, Integrated Receivables, Lockbox, ACH Fraud Filter, Positive Pay) — Commercial product: treasury management and payments is reported in Commercial Banking and in Corporate and Investment Banking (Q3 2026 10-Q)[^3]

*Assessment:* Line-of-business owner, steward and approver are not assigned; set them in knowledge-source.json.

[^1]: kj · assignment/WF-P13 · 8799b4a3e937
[^2]: kj · assignment/WF-P14 · fda8c386281c
[^3]: kj · assignment/WF-P15 · c990e0f81a08

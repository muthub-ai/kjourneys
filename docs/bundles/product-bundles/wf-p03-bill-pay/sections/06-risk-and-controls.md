---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Bill Pay (Online Bill Pay / Business Bill Pay): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "237bbe74ff552f24e9afc1c78586bcca0e03ab63b56d8c6f2f81f0c421234e23",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Bill Pay (Online Bill Pay / Business Bill Pay) — risk and controls

## Security, trust and exception gaps

- **medium** · Business Bill Pay has no dual control; any 'View and Transact' delegate can pay.[^1]

## Fail points along the journeys

- `WF-J07` M02 · The pre-enrollment welcome page does not mention instant payments or Request for Payment.[^2]
- `WF-J09` M01 · Not marketed on any product page; discoverability depends on biller participation[^3]
- `WF-J17` M04 · No dual control for Business Bill Pay[^4]

## Exception paths

- `WF-J07` · Insufficient funds on Send On date: Payment may use Overdraft Protection (no fee; cash advance APR if credit); otherwise canceled after two unsuccessful attempts → Customer reschedules[^5]
- `WF-J07` · Payment late due to WF error: Customer contacts Customer Service → Reimbursed[^5]
- `WF-J07` · Paper check not cashed in 90 days: Funds returned → [^5]
- `WF-J07` · Unauthorized Bill Pay payment: Call 1-866-867-5568 → [^5]
- `WF-J08` · eBill activation failure: WF notification of problem → Contact payee[^6]
- `WF-J08` · Biller late delivering eBill: WF not responsible → [^6]
- `WF-J09` · Payee rejects or network unavailable: Payment fails → Customer pays via standard Bill Pay[^7]
- `WF-J09` · Customer paid wrong amount: Cannot amend; request return from payee → [^7]
- `WF-J17` · Insufficient credit: Canceled → [^8]

[^1]: kj · finding/GAP-WF-0031 · 2c6179b4c9e0
[^2]: kj · step/WF-J07#M02 · ef8faecfb2f2
[^3]: kj · step/WF-J09#M01 · 14b3309c41ed
[^4]: kj · step/WF-J17#M04 · 5b820f701b14
[^5]: kj · journey/WF-J07 · add9e5f0ca96
[^6]: kj · journey/WF-J08 · 3a462c0bcc44
[^7]: kj · journey/WF-J09 · 92c2140a6c2a
[^8]: kj · journey/WF-J17 · adbdce251781

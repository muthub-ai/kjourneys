---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Bill Pay (Online Bill Pay / Business Bill Pay): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p03-bill-pay",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P03",
  "line_of_business": "wf-cbl",
  "content_sha256": "d9059e3d536dc09f871e846e0ccfdce7eb3c2e7b38ce877f8bef6a8f40a58cbf",
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

[^1]: kj · finding/GAP-WF-0030 · 7bc98ff7c9c1
[^2]: kj · step/WF-J07#M02 · c0afed299775
[^3]: kj · step/WF-J09#M01 · c22f001039ca
[^4]: kj · step/WF-J17#M04 · 1cbfb111ef77
[^5]: kj · journey/WF-J07 · 8270f6fa66c5
[^6]: kj · journey/WF-J08 · 43861b5c7ba6
[^7]: kj · journey/WF-J09 · 57b4cafbf531
[^8]: kj · journey/WF-J17 · 161d120bfa87

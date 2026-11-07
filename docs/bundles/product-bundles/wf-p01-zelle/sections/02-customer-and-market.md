---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Zelle® delivers",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "f1abca90e84d4c9584d823a0fa01cc64f6b109a0de306b6d7ca788ddf385bd4f",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — customers and channels

Segments: consumer, small-business. Channels: mobile-app, web, voice-chat-assistant.[^1]

Network or vendor: Early Warning Services (Zelle network); Wells Fargo is an EWS owner bank.[^1]

## Customer journeys this product delivers

- **Consumer sends money to a new recipient with Zelle (mobile-first)** (consumer, send) — 11 best-practice steps[^2]
- **Consumer requests money or splits a bill with Zelle** (consumer, request) — 9 best-practice steps[^3]
- **Small business gets paid with a Zelle tag/QR and pays vendors under controls** (small_business, receive) — 9 best-practice steps[^4]

## Who the journeys are for

- `WF-J01` Consumer sends money to a new recipient with Zelle® (mobile) — persona: Retail checking customer, mobile-first; goal: “Pay a friend or landlord in minutes using only their email or U.S. mobile number”[^5]
- `WF-J02` Consumer requests money / splits a cost with Zelle® — persona: Consumer organizing a group dinner; goal: “Get paid back by friends without chasing them”[^6]
- `WF-J03` Small business gets paid with a Zelle® tag / QR code and pays a vendor — persona: Owner-operated service business (contractor, salon, landlord); goal: “Collect customer payments without card fees and pay vendors fast”[^7]
- `WF-J28` Consumer reports an unauthorized Zelle/online transfer or an imposter scam and seeks reimbursement — persona: Consumer who received a 'bank fraud department' call and sent Zelle to 'themselves'; goal: “Get my money back and secure my account”[^8]
- `WF-J29` Consumer sends, requests and manages Zelle® payments on the web (observed logged-in session) — persona: Tenured consumer checking customer using Wells Fargo Online on a desktop; goal: “Pay or request money from a person and keep control of who can pay me, including a teen's access”[^9]
- `sample` Send money with Zelle — persona: Retail checking customer paying a friend back; goal: “Get money to someone I know, in minutes, without worrying”[^10]

[^1]: kj · product/WF-P01 · 7db18a666d60
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 54cdbe9360ea
[^3]: kj · customer-journey/CJ-ZELLE-REQUEST · ff349a4a3d24
[^4]: kj · customer-journey/CJ-ZELLE-SMB-RECEIVE · 1a1ab5a1e86e
[^5]: kj · journey/WF-J01 · 5459e5785f84
[^6]: kj · journey/WF-J02 · 14bc08a80f04
[^7]: kj · journey/WF-J03 · b89c841e1309
[^8]: kj · journey/WF-J28 · b20fda0a115f
[^9]: kj · journey/WF-J29 · d718f795aee2
[^10]: kj · journey/sample · e85b2befb3b0

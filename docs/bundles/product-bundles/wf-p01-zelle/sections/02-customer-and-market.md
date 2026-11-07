---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys Zelle® delivers",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "beb202e30e460a3b3606ada4cf5662c6ece6a8c45dc16a4e97401c4f69d9fe66",
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

[^1]: kj · product/WF-P01 · f217122e121a
[^2]: kj · customer-journey/CJ-ZELLE-CONSUMER-SEND · 1f6b6a0e7521
[^3]: kj · customer-journey/CJ-ZELLE-REQUEST · cda300f4d27d
[^4]: kj · customer-journey/CJ-ZELLE-SMB-RECEIVE · dd3d94ee596e
[^5]: kj · journey/WF-J01 · c3b8e132fd5c
[^6]: kj · journey/WF-J02 · 2eca5861046f
[^7]: kj · journey/WF-J03 · 558dd3d0215c
[^8]: kj · journey/WF-J28 · cf400c417393
[^9]: kj · journey/WF-J29 · f76130105e87
[^10]: kj · journey/sample · e85b2befb3b0

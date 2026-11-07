---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Zelle®: security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p01-zelle",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P01",
  "line_of_business": "wf-cbl",
  "content_sha256": "cd191d3e2ae39550dd44ab41ed0a6aaba8bba4085541ed2f1e14a43e524c5aaf",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — risk and controls

## Security, trust and exception gaps

- **high** · Review screen carries only static 'only send to people you know and trust' copy; no risk-tiered interstitial, payment-purpose or contact-origin question is documented, and the Zelle-specific scam page now 404s. Observed on the web (Nov 2026): the only scam messaging before the amount screen is a static banner shown on every Zelle visit; the review screen itself was not reached.[^1]
- **high** · Unauthorized and scam claims start by phone (1-800-956-4442 / 1-866-867-5568) or by mail to a P.O. box; no in-app 'report a problem' on the Zelle transaction and no in-app claim status tracker for Zelle. Corroborated on the web (Nov 2026, S990): a completed Zelle payment's detail screen offers only 'Block'; on the observed profile the 'Track Claims > Dispute a charge' picker listed only debit-card purchases (whether non-card items are excluded is unconfirmed); 'Report Phish & Email Scams' leaves the secure session for a public education page.[^2]
- **high** · Business Zelle sends in Business Online can be executed by a single 'View and Transact' delegate; no secondary approval (INFERRED from OAA per WF-C003). Dual custody exists only for Vantage Treasury Management enrollees.[^3]

## Fail points along the journeys

- `WF-J01` M07 · No evidence of dynamic payment-purpose questions; warning copy is generic[^4]
- `WF-J03` M05 · No dual-control for Zelle sends on business accounts (delegates with View and Transact can send individually)[^5]
- `WF-J28` M04 · No Zelle or ACH item was offered in the online dispute picker on this profile; whether non-card items are filtered or merely absent could not be confirmed.[^6]
- `WF-J29` M01 · Zelle is the fourth item in the web hub (the app gives it a bottom-navigation tab, S005); the hub does not explain when to use Zelle vs transfer vs wire — the comparison lives inside Wire Money.[^7]
- `WF-J29` M06 · Whether the review screen carries a dynamic, risk-tiered scam warning for a new recipient remains unobserved (open question WF-C029); only the static landing banner was seen.[^8]
- `WF-J29` M08 · No 'report a problem', dispute or scam-report action on the payment detail screen.[^9]
- `WF-J29` M13 · No Zelle entry point in the online dispute flow: on the observed profile the 'Track Claims > Dispute a charge' picker listed only debit-card purchases (whether non-card items are excluded is unconfirmed), so a Zelle problem leaves the digital channel.[^10]
- `sample` M01 · Ineligible account hits a dead-end message[^11]
- `sample` M02 · Token already enrolled at another bank, so the customer must move it[^12]
- `sample` M02 · Code never arrives[^12]
- `sample` M03 · A typo pays a stranger's token[^13]
- `sample` M03 · Recipient not enrolled, so the payment will sit pending[^13]
- `sample` M04 · Imposters register names that look legitimate[^14]
- `sample` M05 · Limit hit with no path to raise it[^15]
- `sample` M06 · Genuine payments declined[^16]
- `sample` M06 · A scammer coaches the customer through step-up[^16]
- `sample` M07 · Network timeout leaves the status unknown[^17]
- `sample` M07 · Duplicate debit on retry[^17]
- `sample` M08 · Unworked breaks return weeks later as "missing money" calls[^18]
- `sample` M09 · Sender sees Completed while the recipient sees nothing yet[^19]
- `sample` M10 · Pending status isn't explained[^20]
- `sample` M11 · Authorized scam payments often aren't covered, an expectation gap[^21]
- `sample` M11 · Customer repeats the story across channels[^21]

## Exception paths

- `WF-J01` · Recipient not enrolled within 14 days (Addendum: suspense up to 15 business days): Payment shows 'Pending' in Zelle® Activity with 'Cancel payment' option; expires if recipient never enrolls → Funds returned automatically[^22]
- `WF-J01` · Customer wants to cancel a payment to an enrolled recipient: No cancel option — 'cannot be canceled or reversed once sent' → Customer must ask recipient to send money back[^22]
- `WF-J01` · Scheduled / repeat payment cancel: Cancel entire series or skip one payment in 'Scheduled' until 11:30 PM PT the day before; stop-payment via phone 1-800-869-3557 ≥3 business days before → Payment stopped[^22]
- `WF-J01` · Payment delayed or blocked by Wells Fargo/Zelle for fraud review or regulatory reasons: Payment may be delayed; customer notified per communication preferences → Released or declined[^22]
- `WF-J01` · Unauthorized Zelle transfer (account takeover) on a consumer account: Customer calls 1-800-956-4442 / 1-866-867-5568 or submits online form; Reg E error-resolution applies → Reimbursement for unauthorized transactions per Reg E tiers ($50/$500/unlimited by reporting delay)[^22]
- `WF-J01` · Authorized push-payment scam (e.g., bank-imposter 'pay yourself', marketplace): No in-flow scam interstitial documented; customer discovers loss after the fact. Intake: Wells Fargo Online Banking Customer Service 1-800-956-4442 (24/7) — 'Qualifying imposters scams may be eligible for reimbursement'; imposter calls/payments also to 1-866-867-5568 or reportimposter@wellsfargo.com; brochure guidance: 'Don't be pressured to move or send money by someone who contacts you claiming there is fraud on your account.' Purchase scams: 'Neither Wells Fargo nor Zelle® offers purchase protection.' → Case-by-case; reimbursement only for qualifying imposter scams[^22]
- `WF-J01` · Insufficient funds in funding account: Payment fails; 'email notifications if a payment fails or is canceled' (FAQ). NSF-specific handling unpublished. → Customer re-sends[^22]
- `WF-J01` · Incoming payment returned: Sender notified of return → Funds back to sender[^22]
- `WF-J02` · Requested party declines/ignores: Request stays pending; no payment → Customer follows up out of band[^23]
- `WF-J02` · Requested party not enrolled: Request cannot be sent → Customer asks them to enroll or uses another method[^23]
- `WF-J03` · Customer dispute over goods/services: No purchase protection → Business resolves with customer[^24]
- `WF-J03` · Unauthorized send on business account: Call 1-800-225-5935 / 1-866-867-5568 → Case-by-case[^24]
- `WF-J28` · Authorized marketplace scam: Denied — no purchase protection → [^25]
- `WF-J28` · Qualifying imposter scam: Reimbursement reviewed → Case-by-case[^25]
- `WF-J28` · Unauthorized (ATO): Phone/mail intake; online 'Dispute a charge' under Track Claims covers card transactions (observed: only debit-card purchases listed); status later visible under 'My claims' Open/Closed → Reimbursed[^25]
- `WF-J29` · Customer wants to report a scam or a problem with a Zelle payment: No action on the payment detail screen beyond 'Block'; no Zelle item was offered in the online 'Dispute a charge' picker on this profile; Help gives a phone number → Qualifying imposter scams may be eligible for reimbursement; protections are not those of a card transaction (Help)[^26]
- `WF-J29` · Saved recipient has unenrolled from Zelle: 'action required' badge on Recipients; 'Error, unenrolled … select to re-add or delete recipient' → Re-add with a current token or delete[^26]
- `WF-J29` · Parent wants to stop a teen's Zelle use: Family controls → Disable for the teen account holder → Teen cannot use Zelle until re-enabled[^26]

## Controls (sample blueprint)

*Assessment:* Controls below come from the hand-built sample and need GRC IDs from the enterprise control library before they can be relied on.

- **security** · Session must be strongly authenticated[^27]
- **operational** · Eligible deposit accounts only[^28]
- **security** · Possession check by one-time code[^29]
- **operational** · A token belongs to one user at one bank in the network[^30]
- **fraud** · Rate-limit directory lookups to stop enumeration[^31]
- **fraud** · New-payee flag passed to risk scoring[^32]
- **fraud** · Name shown before any send[^33]
- **fraud** · Scam warning on first payment to a new recipient[^34]
- **fraud** · Amount and velocity limits by customer segment[^35]
- **aml** · Memo screened for sanctions terms[^36]
- **fraud** · Real-time fraud score inside a decision time budget[^37]
- **security** · Step-up authentication[^38]
- **fraud** · Manual review queue for held payments[^39]
- **operational** · Idempotency key on every payment[^40]
- **regulatory** · Irrevocable once accepted; reversal only by recall[^41]
- **operational** · Daily three-way reconciliation[^42]
- **operational** · Settlement exposure monitoring[^43]
- **aml** · Post-transaction AML monitoring[^44]
- **operational** · Notification is the customer's record of the payment[^45]
- **operational** · Cancel only before funds are claimed[^46]
- **regulatory** · Regulation E timelines for unauthorized transfers[^47]
- **regulatory** · Network rules for imposter-scam recovery[^48]
- **aml** · Suspicious activity reporting where required[^49]

[^1]: kj · finding/GAP-WF-0001 · 38c101614c6a
[^2]: kj · finding/GAP-WF-0002 · 4e09e7353ec2
[^3]: kj · finding/GAP-WF-0008 · 35e06b5dbd70
[^4]: kj · step/WF-J01#M07 · 5047050ad99b
[^5]: kj · step/WF-J03#M05 · 48e6034a19c5
[^6]: kj · step/WF-J28#M04 · e6fd4a65fdf0
[^7]: kj · step/WF-J29#M01 · 2b8c960c1a6b
[^8]: kj · step/WF-J29#M06 · 5846e99f9d1d
[^9]: kj · step/WF-J29#M08 · 64deb811a4db
[^10]: kj · step/WF-J29#M13 · 227c86342bfa
[^11]: kj · step/sample#M01 · c84f96f74f28
[^12]: kj · step/sample#M02 · 3a758e72cca0
[^13]: kj · step/sample#M03 · ceb54c42afa5
[^14]: kj · step/sample#M04 · 7c45d62d7ace
[^15]: kj · step/sample#M05 · c18410a84942
[^16]: kj · step/sample#M06 · 44192edc6dfb
[^17]: kj · step/sample#M07 · 40af2f7c9348
[^18]: kj · step/sample#M08 · 92984d954c01
[^19]: kj · step/sample#M09 · 4722e6c6318e
[^20]: kj · step/sample#M10 · 7fc18dfcea5b
[^21]: kj · step/sample#M11 · 66d75bc680d5
[^22]: kj · journey/WF-J01 · 251e989b61ea
[^23]: kj · journey/WF-J02 · 14bc08a80f04
[^24]: kj · journey/WF-J03 · b89c841e1309
[^25]: kj · journey/WF-J28 · b20fda0a115f
[^26]: kj · journey/WF-J29 · d718f795aee2
[^27]: kj · control/p2p-m01-1 · f0ba8fa8a4d6
[^28]: kj · control/p2p-m01-2 · d5aa540ab653
[^29]: kj · control/p2p-m02-1 · 838164899796
[^30]: kj · control/p2p-m02-2 · d81577143a70
[^31]: kj · control/p2p-m03-1 · e1ed377846b7
[^32]: kj · control/p2p-m03-2 · c197cb214452
[^33]: kj · control/p2p-m04-1 · 862ecc750097
[^34]: kj · control/p2p-m04-2 · cd1555b49946
[^35]: kj · control/p2p-m05-1 · 7759b456723d
[^36]: kj · control/p2p-m05-2 · 37a978cce48c
[^37]: kj · control/p2p-m06-1 · 847858e7a419
[^38]: kj · control/p2p-m06-2 · 2acf5cc54833
[^39]: kj · control/p2p-m06-3 · 7ad80a1eb573
[^40]: kj · control/p2p-m07-1 · cfea9b819c45
[^41]: kj · control/p2p-m07-2 · 0a337ab539db
[^42]: kj · control/p2p-m08-1 · b9a84f0ef6a0
[^43]: kj · control/p2p-m08-2 · 11bf6eaa8b4a
[^44]: kj · control/p2p-m08-3 · a9c2b87811cd
[^45]: kj · control/p2p-m09-1 · bc17240a8d74
[^46]: kj · control/p2p-m10-1 · a3e2ccdf8719
[^47]: kj · control/p2p-m11-1 · c54352a9eb9a
[^48]: kj · control/p2p-m11-2 · de91d578fd3f
[^49]: kj · control/p2p-m11-3 · 2bb2c79f8fba

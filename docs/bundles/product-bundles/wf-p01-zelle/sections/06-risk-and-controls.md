---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Zelle®: security and exception gaps, fail points, exception paths and controls",
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
  "content_sha256": "18da4bc26f5ad270c53f620434742d27eb338bd29a14246ce53dec73ca499a70",
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
- **high** · Business Zelle sends in Business Online can be executed by a single 'View and Transact' delegate; no secondary approval (INFERRED from OAA per WF-C003; the second-wave check of the Zelle for Your Business FAQ confirms the review screen, recipient-name display and first-time access code but says nothing about dual approval, S956). Dual custody exists only for Vantage Treasury Management enrollees.[^3]

## Fail points along the journeys

- `WF-J01` M07 · No evidence of dynamic payment-purpose questions; warning copy is generic[^4]
- `WF-J03` M05 · No dual-control for Zelle sends on business accounts (delegates with View and Transact can send individually)[^5]
- `WF-J28` M04 · No Zelle or ACH item was offered in the online dispute picker on this profile; whether non-card items are filtered or merely absent could not be confirmed.[^6]
- `WF-J28` M11 · classification of scams as 'non-fraud' until 2023 limited reimbursement eligibility. CFPB alleged consumers were told to resolve disputes with the recipient (allegation, network-wide).[^7]
- `WF-J29` M01 · Zelle is the fourth item in the web hub (the app gives it a bottom-navigation tab, S005); the hub does not explain when to use Zelle vs transfer vs wire — the comparison lives inside Wire Money.[^8]
- `WF-J29` M06 · Whether the review screen carries a dynamic, risk-tiered scam warning for a new recipient remains unobserved (open question WF-C029); only the static landing banner was seen.[^9]
- `WF-J29` M08 · No 'report a problem', dispute or scam-report action on the payment detail screen.[^10]
- `WF-J29` M13 · No Zelle entry point in the online dispute flow: on the observed profile the 'Track Claims > Dispute a charge' picker listed only debit-card purchases (whether non-card items are excluded is unconfirmed), so a Zelle problem leaves the digital channel.[^11]
- `sample` M01 · Ineligible account hits a dead-end message[^12]
- `sample` M02 · Token already enrolled at another bank, so the customer must move it[^13]
- `sample` M02 · Code never arrives[^13]
- `sample` M03 · A typo pays a stranger's token[^14]
- `sample` M03 · Recipient not enrolled, so the payment will sit pending[^14]
- `sample` M04 · Imposters register names that look legitimate[^15]
- `sample` M05 · Limit hit with no path to raise it[^16]
- `sample` M06 · Genuine payments declined[^17]
- `sample` M06 · A scammer coaches the customer through step-up[^17]
- `sample` M07 · Network timeout leaves the status unknown[^18]
- `sample` M07 · Duplicate debit on retry[^18]
- `sample` M08 · Unworked breaks return weeks later as "missing money" calls[^19]
- `sample` M09 · Sender sees Completed while the recipient sees nothing yet[^20]
- `sample` M10 · Pending status isn't explained[^21]
- `sample` M11 · Authorized scam payments often aren't covered, an expectation gap[^22]
- `sample` M11 · Customer repeats the story across channels[^22]

## Exception paths

- `WF-J01` · Recipient not enrolled within 14 days (Addendum: suspense up to 15 business days): Payment shows 'Pending' in Zelle® Activity with 'Cancel payment' option; expires if recipient never enrolls → Funds returned automatically[^23]
- `WF-J01` · Customer wants to cancel a payment to an enrolled recipient: No cancel option — 'cannot be canceled or reversed once sent' → Customer must ask recipient to send money back[^23]
- `WF-J01` · Scheduled / repeat payment cancel: Cancel entire series or skip one payment in 'Scheduled' until 11:30 PM PT the day before; stop-payment via phone 1-800-869-3557 ≥3 business days before → Payment stopped[^23]
- `WF-J01` · Payment delayed or blocked by Wells Fargo/Zelle for fraud review or regulatory reasons: Payment may be delayed; customer notified per communication preferences → Released or declined[^23]
- `WF-J01` · Unauthorized Zelle transfer (account takeover) on a consumer account: Customer calls 1-800-956-4442 / 1-866-867-5568 or submits online form; Reg E error-resolution applies → Reimbursement for unauthorized transactions per Reg E tiers ($50/$500/unlimited by reporting delay)[^23]
- `WF-J01` · Authorized push-payment scam (e.g., bank-imposter 'pay yourself', marketplace): No in-flow scam interstitial documented; customer discovers loss after the fact. Intake: Wells Fargo Online Banking Customer Service 1-800-956-4442 (24/7) — 'Qualifying imposters scams may be eligible for reimbursement'; imposter calls/payments also to 1-866-867-5568 or reportimposter@wellsfargo.com; brochure guidance: 'Don't be pressured to move or send money by someone who contacts you claiming there is fraud on your account.' Purchase scams: 'Neither Wells Fargo nor Zelle® offers purchase protection.' → Case-by-case; reimbursement only for qualifying imposter scams[^23]
- `WF-J01` · Insufficient funds in funding account: Payment fails; 'email notifications if a payment fails or is canceled' (FAQ). NSF-specific handling unpublished. → Customer re-sends[^23]
- `WF-J01` · Incoming payment returned: Sender notified of return → Funds back to sender[^23]
- `WF-J02` · Requested party declines/ignores: Request stays pending; no payment → Customer follows up out of band[^24]
- `WF-J02` · Requested party not enrolled: Request cannot be sent → Customer asks them to enroll or uses another method[^24]
- `WF-J03` · Customer dispute over goods/services: No purchase protection → Business resolves with customer[^25]
- `WF-J03` · Unauthorized send on business account: Call 1-800-225-5935 / 1-866-867-5568 → Case-by-case[^25]
- `WF-J28` · Authorized marketplace scam: Denied — no purchase protection → [^26]
- `WF-J28` · Qualifying imposter scam: Reimbursement reviewed → Case-by-case[^26]
- `WF-J28` · Unauthorized (ATO): Phone/mail intake; online 'Dispute a charge' under Track Claims covers card transactions (observed: only debit-card purchases listed); status later visible under 'My claims' Open/Closed → Reimbursed[^26]
- `WF-J29` · Customer wants to report a scam or a problem with a Zelle payment: No action on the payment detail screen beyond 'Block'; no Zelle item was offered in the online 'Dispute a charge' picker on this profile; Help gives a phone number → Qualifying imposter scams may be eligible for reimbursement; protections are not those of a card transaction (Help)[^27]
- `WF-J29` · Saved recipient has unenrolled from Zelle: 'action required' badge on Recipients; 'Error, unenrolled … select to re-add or delete recipient' → Re-add with a current token or delete[^27]
- `WF-J29` · Parent wants to stop a teen's Zelle use: Family controls → Disable for the teen account holder → Teen cannot use Zelle until re-enabled[^27]

## Controls (sample blueprint)

*Assessment:* Controls below come from the hand-built sample and need GRC IDs from the enterprise control library before they can be relied on.

- **security** · Session must be strongly authenticated[^28]
- **operational** · Eligible deposit accounts only[^29]
- **security** · Possession check by one-time code[^30]
- **operational** · A token belongs to one user at one bank in the network[^31]
- **fraud** · Rate-limit directory lookups to stop enumeration[^32]
- **fraud** · New-payee flag passed to risk scoring[^33]
- **fraud** · Name shown before any send[^34]
- **fraud** · Scam warning on first payment to a new recipient[^35]
- **fraud** · Amount and velocity limits by customer segment[^36]
- **aml** · Memo screened for sanctions terms[^37]
- **fraud** · Real-time fraud score inside a decision time budget[^38]
- **security** · Step-up authentication[^39]
- **fraud** · Manual review queue for held payments[^40]
- **operational** · Idempotency key on every payment[^41]
- **regulatory** · Irrevocable once accepted; reversal only by recall[^42]
- **operational** · Daily three-way reconciliation[^43]
- **operational** · Settlement exposure monitoring[^44]
- **aml** · Post-transaction AML monitoring[^45]
- **operational** · Notification is the customer's record of the payment[^46]
- **operational** · Cancel only before funds are claimed[^47]
- **regulatory** · Regulation E timelines for unauthorized transfers[^48]
- **regulatory** · Network rules for imposter-scam recovery[^49]
- **aml** · Suspicious activity reporting where required[^50]

[^1]: kj · finding/GAP-WF-0001 · 1e4eff85a315
[^2]: kj · finding/GAP-WF-0002 · 5f257a86aa4a
[^3]: kj · finding/GAP-WF-0008 · 2074ba55f5b7
[^4]: kj · step/WF-J01#M07 · 342086e352a6
[^5]: kj · step/WF-J03#M05 · a159dea2cc82
[^6]: kj · step/WF-J28#M04 · c982a08afc68
[^7]: kj · step/WF-J28#M11 · a3be980215cb
[^8]: kj · step/WF-J29#M01 · def33ab3f335
[^9]: kj · step/WF-J29#M06 · 555e35c96c09
[^10]: kj · step/WF-J29#M08 · 2fa1a18127d7
[^11]: kj · step/WF-J29#M13 · 33a9ae888db7
[^12]: kj · step/sample#M01 · c84f96f74f28
[^13]: kj · step/sample#M02 · 3a758e72cca0
[^14]: kj · step/sample#M03 · ceb54c42afa5
[^15]: kj · step/sample#M04 · 7c45d62d7ace
[^16]: kj · step/sample#M05 · c18410a84942
[^17]: kj · step/sample#M06 · 44192edc6dfb
[^18]: kj · step/sample#M07 · 40af2f7c9348
[^19]: kj · step/sample#M08 · 92984d954c01
[^20]: kj · step/sample#M09 · 4722e6c6318e
[^21]: kj · step/sample#M10 · 7fc18dfcea5b
[^22]: kj · step/sample#M11 · 66d75bc680d5
[^23]: kj · journey/WF-J01 · c3b8e132fd5c
[^24]: kj · journey/WF-J02 · 2eca5861046f
[^25]: kj · journey/WF-J03 · 558dd3d0215c
[^26]: kj · journey/WF-J28 · cf400c417393
[^27]: kj · journey/WF-J29 · f76130105e87
[^28]: kj · control/p2p-m01-1 · f0ba8fa8a4d6
[^29]: kj · control/p2p-m01-2 · d5aa540ab653
[^30]: kj · control/p2p-m02-1 · 838164899796
[^31]: kj · control/p2p-m02-2 · d81577143a70
[^32]: kj · control/p2p-m03-1 · e1ed377846b7
[^33]: kj · control/p2p-m03-2 · c197cb214452
[^34]: kj · control/p2p-m04-1 · 862ecc750097
[^35]: kj · control/p2p-m04-2 · cd1555b49946
[^36]: kj · control/p2p-m05-1 · 7759b456723d
[^37]: kj · control/p2p-m05-2 · 37a978cce48c
[^38]: kj · control/p2p-m06-1 · 847858e7a419
[^39]: kj · control/p2p-m06-2 · 2acf5cc54833
[^40]: kj · control/p2p-m06-3 · 7ad80a1eb573
[^41]: kj · control/p2p-m07-1 · cfea9b819c45
[^42]: kj · control/p2p-m07-2 · 0a337ab539db
[^43]: kj · control/p2p-m08-1 · b9a84f0ef6a0
[^44]: kj · control/p2p-m08-2 · 11bf6eaa8b4a
[^45]: kj · control/p2p-m08-3 · a9c2b87811cd
[^46]: kj · control/p2p-m09-1 · bc17240a8d74
[^47]: kj · control/p2p-m10-1 · a3e2ccdf8719
[^48]: kj · control/p2p-m11-1 · c54352a9eb9a
[^49]: kj · control/p2p-m11-2 · de91d578fd3f
[^50]: kj · control/p2p-m11-3 · 2bb2c79f8fba

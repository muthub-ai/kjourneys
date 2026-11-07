---
{
 "type": "product-bundle/section",
 "title": "Product definition",
 "description": "Zelle®: sub-products, capabilities per sub-product, notes, limits and fees",
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
  "content_sha256": "60f8d0a7beb7d40d5c9ae0ff9d269b788b98534fe206781981039d2418266901",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Zelle® — product definition

Where it sits in the bank's app and site: Mobile: 'Zelle®' in bottom navigation bar. Desktop web (observed, logged in): 'Transfer & Pay' opens a panel headed 'Move Money & Pay Bills' listing Transfer Money · Pay WF Accounts · Pay Bills · Send Money with Zelle® · Wire Money · Send with ExpressSend® · Deposit a Check (Zelle is fourth). Zelle left menu: Send | Request | Scheduled | Activity | Family controls | Recipients | Manage payment profiles | Blocked contacts | Help. Fargo: purple Fargo icon in search bar.[^1]

## Sub-products

| Sub-product | Rail | Segments | Description |
|---|---|---|---|
| `WF-P01-S01` Send money with Zelle® | Zelle | consumer, small-business | Send to an enrolled recipient by email/U.S. mobile/Zelle tag, from phone contacts, or by scanning a Zelle QR code; one-time, future-dated or repeating.[^2] |
| `WF-P01-S02` Request money with Zelle® | Request to pay | consumer, small-business | Request a payment from an enrolled Zelle user by choosing your own enrolled email/mobile instead of a funding account on the 'Send or Request' screen.[^3] |
| `WF-P01-S03` Receive money with Zelle® (incl. Zelle tag & QR for business) | Zelle | consumer, small-business | Receive to the deposit account linked to enrolled email/mobile/tag; small business can share a Zelle tag and 'Show your QR code' to get paid.[^4] |
| `WF-P01-S04` Family controls (parent-managed Zelle® access for teen account holders) | Zelle | consumer | Zelle menu item 'Family controls' = 'Update Zelle® access for teens': lists any teen account holder(s) with an Enabled/Disabled state and 'Zelle® access enabled by <parent> on <date>'; the parent toggles Enable/Disable. Not described on any public Wells Fargo page captured in the study and not present in any peer inventory built from public sources.[^5] |
| `WF-P01-S05` Zelle® contact and profile controls (Blocked contacts; Manage payment profiles) | Zelle | consumer | Web screens for two capabilities the public record already documents: 'Blocked contacts' lists blocked senders/requesters ('To block someone, go to Zelle® Activity and open a past payment or request'; blocking is documented publicly, S005), and 'Manage payment profiles' ('Receive money with Zelle®') shows each enrolled token (mobile, email) mapped to a deposit account with 'Edit account' and 'Unenroll' per token (receive mapping documented publicly under WF-P01-S03) plus a link to update contact information.[^6] |

## Capabilities by sub-product

*Method:* ✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).

| Capability | WF-P01-S01 | WF-P01-S02 | WF-P01-S03 | WF-P01-S04 | WF-P01-S05 | Detail |
|---|---|---|---|---|---|---|
| Cancel before it is sent | ✓ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Pay from phone contacts | ✓ | ✓ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Dual approval (business) | ✗ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Email or text notifications | ✓ | ✓ | ✓ | — | — | [^2][^3][^4][^5][^6] |
| Instant delivery | ✓ | ✓ | ✓ | — | — | [^2][^3][^4][^5][^6] |
| International | ✗ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Push notifications | ✓ | ✓ | ✓ | — | — | [^2][^3][^4][^5][^6] |
| QR code | ✓ | ✓ | ✓ | — | — | [^2][^3][^4][^5][^6] |
| Recurring payments | ✓ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Request money | ✓ | ✓ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Same-day delivery | ✓ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Scam warning before sending | ✗ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Schedule for a future date | ✓ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Split a payment | ✗ | ✗ | ✗ | — | — | [^2][^3][^4][^5][^6] |
| Status tracking | ✓ | ✓ | ✓ | — | — | [^2][^3][^4][^5][^6] |
| Step-up authentication | — | — | — | — | — | WF-P01-S01: Access code (text to registered mobile or RSA SecurID) for first-time recipient and selected payments; Advanced Access[^2][^3][^4][^5][^6] |

## Notes from the study

- `WF-P01-S01`: Send flow verbatim (FAQ): Zelle® in bottom nav (web: Transfer and Pay > Send Money with Zelle®) → Send/Request → add or select recipient → amount + funding account → Continue → 'Carefully review the details of your payment before you send it. If it's the first time you've sent money to this recipient, we will send you an access code... If your recipient's U.S. mobile number or email address is enrolled with Zelle®, we'll display the name of the recipient on record before you continue (in some cases, this may only be a first name).' → confirmation screen. Notifications: email + secure inbox on schedule/change; email on fail/cancel; texts from 93557 or 93729 on new recipient / first-time send. Blocks are tied to the contact's enrollment at their bank (re-enrolling elsewhere clears a block). Refreshed marketing page frames use cases as split costs, recurring rent/utilities, QR 'Scan. Pay. Done.' for local merchants. No scam interstitial or payment-purpose prompt documented; scam victims call 1-800-956-4442; 'Qualifying imposters scams may be eligible for reimbursement.'[^2]
- `WF-P01-S02`: Requests limited to enrolled users; recipient may decline/ignore; up to 35 pending requests (non-small-business).[^3]
- `WF-P01-S03`: Zelle tags restricted to small business customers (FAQ + Addendum §3).[^4]
- `WF-P01-S04`: Observed in a logged-in web session (web screen only); mobile presence not observed.[^5]
- `WF-P01-S05`: Observed on web; mobile not observed. Not a new capability — the screens give the public capabilities a management surface.[^6]

## Limits, fees and timing (captured incidentally)

- `WF-J01` — cutoffs: Scheduled payments send shortly after midnight on scheduled day; cancel until 11:30 PM PT prior day; fees: None from WF; limits: Consumer $3,500/24h, $20,000/30d; business $15,000/$60,000 (FAQ & Addendum)[^7]
- `WF-J02` — fees: None; limits: 35 pending requests (consumer)[^8]
- `WF-J03` — fees: None from WF; Business Account Analysis may apply; limits: Business $15,000/24h, $60,000/30d[^9]
- `WF-J28` — cutoffs: Report within 60 days (Reg E); 2 business days for device loss tier[^10]
- `WF-J29` — cutoffs: Scheduled payments cancellable until 11:30 pm PT the day before (Help); fees: None shown; limits: Daily and 30-day limits shown inline on the amount screen (values not recorded)[^11]

[^1]: kj · product/WF-P01 · 7db18a666d60
[^2]: kj · sub-product/WF-P01-S01 · dac14fe19dea
[^3]: kj · sub-product/WF-P01-S02 · 22b37fa1ea11
[^4]: kj · sub-product/WF-P01-S03 · 677aab3d9fbb
[^5]: kj · sub-product/WF-P01-S04 · 05811c9bbdb1
[^6]: kj · sub-product/WF-P01-S05 · 8377db259ff9
[^7]: kj · journey/WF-J01 · 251e989b61ea
[^8]: kj · journey/WF-J02 · 14bc08a80f04
[^9]: kj · journey/WF-J03 · b89c841e1309
[^10]: kj · journey/WF-J28 · b20fda0a115f
[^11]: kj · journey/WF-J29 · d718f795aee2

---
{
 "type": "product-bundle/section",
 "title": "Risk and controls",
 "description": "Digital Wires (Wire Money): security and exception gaps, fail points, exception paths and controls",
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
  "bundle_id": "wf-p04-digital-wires",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P04",
  "line_of_business": "wf-cbl",
  "content_sha256": "42a1ec76677a1d1a720a4dc34f3633af900468d98738164e8296064db37d5e45",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# Digital Wires (Wire Money) — risk and controls

## Security, trust and exception gaps

- **high** · SMB wires from Business Online have no dual approval (INFERRED, WF-C003); a single delegate can release a foreign-currency wire.[^1]
- **medium** · Cancellation is possible only while 'Scheduled'; once Pending, recall requires a call to 877-499-6920 and there is no in-app recall request.[^2]

## Fail points along the journeys

- `WF-J10` M01 · All published steps reference Wells Fargo Online ('Sign on to Wells Fargo Online, go to Transfer & Pay, and select Wire Money'); product page states a flat $30 digital wire fee while the FAQ says fees 'range from $0-$30' — inconsistent fee messaging; mobile-app wire flow still undocumented.[^3]
- `WF-J18` M04 · No SMB dual control for wires (contrast: Vantage dual custody)[^4]

## Exception paths

- `WF-J10` · Wire placed 'Under review' by internal security: Status 'Under review'; WF may contact customer; delivery delayed; to cancel call 877-499-6920 → Bank may contact the customer to verify; 'While your wire is being reviewed, you may also have the option to cancel it by calling 877-499-6920'; once processing (Pending) it can no longer be canceled.[^5]
- `WF-J10` · Wire returned by beneficiary bank: Status 'Returned'; secure-inbox message + email; funds credited back less recipient-bank fees; FX wires may return less USD → [^5]
- `WF-J10` · Customer wants to cancel after processing: Only 'Scheduled' wires can be canceled in UI; Order is final once accepted; WF may attempt cancellation on request without liability → Uncertain[^5]
- `WF-J10` · Consumer international wire – 30-minute cancellation right: Cancel within 30 minutes of completing for full refund incl. fees, via Wire Transfers or phone on receipt → Refund[^5]
- `WF-J10` · Error on consumer international wire: Notify within 180 days; WF investigates within 90 days, reports within 3 business days → [^5]
- `WF-J10` · Error/unauthorized domestic wire: Notify within 14 days of acceptance/debit; orders verified via security procedure bind customer even if unauthorized → [^5]
- `WF-J10` · Wire fraud / changed payment instructions scam: Call immediately 1-866-867-5568; 'wire transfers typically cannot be canceled or reversed' → Rarely recovered[^5]
- `WF-J11` · Wire placed 'Under review' by internal security: Status 'Under review'; WF may contact customer; delivery delayed; to cancel call 877-499-6920 → Released or failed[^6]
- `WF-J11` · Wire returned by beneficiary bank: Status 'Returned'; secure-inbox message + email; funds credited back less recipient-bank fees; FX wires may return less USD → [^6]
- `WF-J11` · Customer wants to cancel after processing: Only 'Scheduled' wires can be canceled in UI; Order is final once accepted; WF may attempt cancellation on request without liability → Uncertain[^6]
- `WF-J11` · Consumer international wire – 30-minute cancellation right: Cancel within 30 minutes of completing for full refund incl. fees, via Wire Transfers or phone on receipt → Refund[^6]
- `WF-J11` · Error on consumer international wire: Notify within 180 days; WF investigates within 90 days, reports within 3 business days → [^6]
- `WF-J11` · Error/unauthorized domestic wire: Notify within 14 days of acceptance/debit; orders verified via security procedure bind customer even if unauthorized → [^6]
- `WF-J11` · Wire fraud / changed payment instructions scam: Call immediately 1-866-867-5568; 'wire transfers typically cannot be canceled or reversed' → Rarely recovered[^6]
- `WF-J18` · Return: Converted back; may be less → [^7]

[^1]: kj · finding/GAP-WF-0029 · a87fe000d932
[^2]: kj · finding/GAP-WF-0016 · 3613671e20fa
[^3]: kj · step/WF-J10#M01 · 8d1eef4271c1
[^4]: kj · step/WF-J18#M04 · f441c075049b
[^5]: kj · journey/WF-J10 · ca29755fbe66
[^6]: kj · journey/WF-J11 · 5759e78f0c18
[^7]: kj · journey/WF-J18 · da9c57fe16e4

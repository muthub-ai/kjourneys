---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys ExpressSend® delivers",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "8105fe85732a2b66bb3b9538b95882a23d6fa8a9157385cb7e696c2af67083e5",
  "review": {
   "submitted_as": "candidate",
   "approver": null
  }
 }
}
---

# ExpressSend® — customers and channels

Segments: consumer. Channels: mobile-app, web, branch, phone.[^1]

Network or vendor: Wells Fargo proprietary remittance network with named Remittance Network Members: Mexico – BBVA, Banorte, Banco Santander (account only), Soriana*, Telecomm Telégrafos (Financiera para el Bienestar)*, Farmacias Guadalajara*, Bodega Aurrera*, Walmart*, Superama*; Dominican Republic – Banco BHD León*, Banreservas*; El Salvador – Banco Agrícola, Banco Davivienda Salvadoreño, Sistema Fedecrédito, Banco Cuscatlán, Remesas BAC Credomatic, Despensa Don Juan*, Despensa Familiar*, Walmart*, Maxi Despensa*; Guatemala – Banrural, Banco Industrial, G&T Continental; Honduras – Banco Ficohsa, Banco Atlántida; Nicaragua – Banpro, Banco LAFISE BANCENTRO; Colombia – BBVA, Bancolombia, Banco Davivienda, Grupo Éxito*; Ecuador – Banco Guayaquil, SERVIPAGOS (via Produbanco)*, Banco Bolivariano; Peru – BBVA, Banco de Crédito del Perú, Interbank (account only); India – ICICI Bank, HDFC Bank, Axis Bank (account only); Philippines – BPI, BDO Unibank, Metrobank (account only), PNB, M. Lhuillier*, Cebuana Lhuillier*; Vietnam – Vietinbank, Vietcombank. (* cash pick-up only).[^1]

## Customer journeys this product delivers

- **Consumer sends a cross-border remittance (account credit or cash pickup)** (consumer, send) — 9 best-practice steps[^2]

## Who the journeys are for

- `WF-J12` Consumer sends an ExpressSend® remittance for cash pickup or account credit (mobile) — persona: Consumer sending money home to Mexico; goal: “Send money to family abroad cheaply, with cash pickup”[^3]

[^1]: kj · product/WF-P05 · 4247b60967aa
[^2]: kj · customer-journey/CJ-REMITTANCE-SEND · e13395512089
[^3]: kj · journey/WF-J12 · 94fc27116502

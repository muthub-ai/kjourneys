---
{
 "type": "product-bundle/section",
 "title": "Customers and channels",
 "description": "Segments, channels and the customer journeys ExpressSend® delivers",
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
  "bundle_id": "wf-p05-expresssend",
  "bank": "wells-fargo",
  "kind": "product-bundle",
  "product_id": "WF-P05",
  "line_of_business": "wf-cbl",
  "content_sha256": "b77bd8900250d67ccfec2e819e2c1579c2f3e4e1fbc9f59dd7f3a2a4326ab044",
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

[^1]: kj · product/WF-P05 · 0e61b73c4811
[^2]: kj · customer-journey/CJ-REMITTANCE-SEND · c2ae3445c9e7
[^3]: kj · journey/WF-J12 · 98b1c3096cb7

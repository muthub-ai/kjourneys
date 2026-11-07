#!/usr/bin/env python3
"""Output ports beyond the page: machine-readable exports for analytics, KOS ingestion and agents.

  dist/facts.jsonl     one line per current fact (comparison cells + moment layer evidence), flat and joinable
  dist/coverage.json   completeness by basis, bank and product: the data product's own health metrics
  dist/summary.md      human summary (also written to the CI job summary)
"""
import json, os
from collections import Counter, defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(ROOT, "dist/kjourneys.json")))
party = {p["id"]: p for p in d["parties"]}
current = lambda h: next((a for a in h if not a.get("valid_to")), h[-1])

facts = []
CMPS = d.get("comparisons", [])
for cmp in CMPS:
    attrs = {a["id"]: a for a in cmp["attributes"]}
    for bank, row in cmp["values"].items():
        for aid, hist in row.items():
            a = current(hist); at = attrs[aid]
            facts.append({"kind": "comparison", "product": cmp["product"], "bank": bank, "bank_name": party[bank]["name"],
                          "stage": at["stage"], "attribute": aid, "attribute_name": at["name"], "datatype": at["datatype"],
                          "value": a.get("value"), "display": a.get("display"), "qualifier": a.get("qualifier"),
                          "basis": a["basis"], "source_ids": a.get("source_ids", []), "assertion_id": a.get("id"),
                          "valid_from": a.get("valid_from"), "history_length": len(hist)})
for j in d["journeys"]:
    for m in j["moments"]:
        for layer, a in m["evidence"].items():
            facts.append({"kind": "moment_layer", "product": j["product"], "bank": j["bank"], "bank_name": party[j["bank"]]["name"],
                          "journey": j["id"], "stage": m["stage"], "moment": m["id"], "moment_code": m["code"],
                          "moment_title": m["title"], "layer": layer, "basis": a["basis"],
                          "intended_basis": a.get("intended_basis"), "source_ids": a.get("source_ids", [])})
with open(os.path.join(ROOT, "dist/facts.jsonl"), "w") as f:
    for x in facts: f.write(json.dumps(x, ensure_ascii=False) + "\n")

cmp_facts = [x for x in facts if x["kind"] == "comparison"]
by_bank = defaultdict(Counter)
for x in cmp_facts: by_bank[x["bank"]][x["basis"]] += 1
by_product = defaultdict(Counter)
for x in cmp_facts: by_product[x["product"]][x["basis"]] += 1
slots = len(d["portfolio"]["products"]) * len(d["portfolio"]["banks"])
mapped = sum(len(p["journeys"]) for p in d["products"])
real = lambda c: sum(v for k, v in c.items() if k in ("observed", "disclosed", "inferred", "internal"))
from datetime import date, timedelta
AS_OF = max((j["as_of"] for j in d["journeys"]), default=str(date.today()))
cutoff = date.fromisoformat(AS_OF) - timedelta(days=90)
stale = []
for cmp in CMPS:
    for bank, row in cmp["values"].items():
        for aid, hist in row.items():
            a = current(hist)
            if a["basis"] in ("observed", "disclosed", "inferred"):
                seen = a.get("observed_on") or (a.get("asserted_at") or "")[:10]
                if not seen or date.fromisoformat(seen) < cutoff: stale.append(f"{cmp['product']}/{bank}/{aid}")
coverage = {
    "ontology": d["ontology"],
    "journeys": {"mapped": mapped, "slots": slots},
    "comparison": {"products": {p: dict(c) for p, c in sorted(by_product.items())},
                   "cells": len(cmp_facts), "by_basis": dict(Counter(x["basis"] for x in cmp_facts)),
                   "by_bank": {b: dict(c) for b, c in sorted(by_bank.items())},
                   "real_data_ratio": round(real(Counter(x["basis"] for x in cmp_facts)) / max(1, len(cmp_facts)), 3)},
    "moment_layers": {"facts": len(facts) - len(cmp_facts),
                      "by_basis": dict(Counter(x["basis"] for x in facts if x["kind"] == "moment_layer"))},
    "freshness": {"as_of": AS_OF, "max_age_days": 90, "stale_facts": stale},
    "legal_review": {"comparisons": {c["product"]: c["governance"]["ci_legal_review"]["status"] for c in CMPS},
                     "journeys": {j["id"]: j["governance"]["ci_legal_review"]["status"] for j in d["journeys"]}},
}
json.dump(coverage, open(os.path.join(ROOT, "dist/coverage.json"), "w"), indent=2)

lines = ["## kjourneys — data status", "",
         f"- Ontology: `{d['ontology']}`",
         f"- Journeys mapped: **{mapped} of {slots}** bank × product slots",
         f"- Comparison cells with real data: **{coverage['comparison']['real_data_ratio']:.0%}** of {len(cmp_facts)}",
         "- Comparison legal review: " + (", ".join(f"{p} **{s}**" for p, s in coverage['legal_review']['comparisons'].items()) or "none"),
         f"- Stale competitor facts (> 90 days): **{len(stale)}**", "",
         "| Bank | observed | disclosed | inferred | sample | awaiting |", "|---|---:|---:|---:|---:|---:|"]
for b in d["portfolio"]["banks"]:
    c = by_bank.get(b, Counter())
    lines.append(f"| {party[b]['name']} | {c['observed']} | {c['disclosed']} | {c['inferred']} | {c['sample']} | {c['awaiting']} |")
lines += ["", "| Product | observed | disclosed | inferred | sample | awaiting |", "|---|---:|---:|---:|---:|---:|"]
names = {p["id"]: p["name"] for p in d["products"]}
for prod, c in sorted(by_product.items()):
    lines.append(f"| {names.get(prod, prod)} | {c['observed']} | {c['disclosed']} | {c['inferred']} | {c['sample']} | {c['awaiting']} |")
open(os.path.join(ROOT, "dist/summary.md"), "w").write("\n".join(lines) + "\n")
print(f"exported {len(facts)} facts, coverage.json, summary.md")

#!/usr/bin/env python3
"""Create (or extend) a product comparison: its questions plus an 'awaiting' slot for every bank.

  python3 tools/new_comparison.py <product-id> <attributes.json> [--title "..."]

<attributes.json> is a list of questions:
  [{"id": "attr-same-day", "stage": "move", "name": "Same-day option", "datatype": "boolean",
    "unit": null, "normalization": "Yes only if offered to standard consumers"}, ...]
Enum questions also need "allowed_values". Stages come from registries/codelists.json.

Writes data/comparisons/<product>/comparison.json and values/<bank>.json for every bank in
data/portfolio.json. Re-running with more questions adds the new ones and keeps existing facts.
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def jload(p): return json.load(open(os.path.join(ROOT, p)))
def jdump(p, o):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w") as f: json.dump(o, f, ensure_ascii=False, indent=2); f.write("\n")
    os.replace(tmp, p)

ap = argparse.ArgumentParser(); ap.add_argument("product"); ap.add_argument("attributes")
args = ap.parse_args()
P = args.product
products = {p["id"] for p in jload("registries/products.json")}
stages = {s["id"] for s in jload("registries/codelists.json")["stages"]}
portfolio = jload("data/portfolio.json")
attrs = json.load(open(args.attributes))
errs = []
if P not in products: errs.append(f"product '{P}' is not in registries/products.json")
if P not in portfolio["products"]: errs.append(f"product '{P}' is not in data/portfolio.json products")
ids = [a.get("id") for a in attrs]
if len(ids) != len(set(ids)): errs.append("attribute ids repeat")
for a in attrs:
    if not str(a.get("id", "")).startswith("attr-"): errs.append(f"{a.get('id')}: id must start with attr-")
    if a.get("stage") not in stages: errs.append(f"{a.get('id')}: stage must be one of {sorted(stages)}")
    if a.get("datatype") not in ("text", "integer", "boolean", "money", "duration", "enum", "enum_list"): errs.append(f"{a.get('id')}: bad datatype")
    if a.get("datatype") in ("enum", "enum_list") and not a.get("allowed_values"): errs.append(f"{a.get('id')}: enum needs allowed_values")
    if not a.get("normalization"): errs.append(f"{a.get('id')}: normalization rule required (how to read the bank's answer)")
if errs: print("FAIL"); [print(" -", e) for e in errs]; sys.exit(1)

cpath = f"data/comparisons/{P}/comparison.json"
if os.path.exists(os.path.join(ROOT, cpath)):
    comp = jload(cpath); have = {a["id"] for a in comp["attributes"]}
    comp["attributes"] += [a for a in attrs if a["id"] not in have]
else:
    zelle = jload("data/comparisons/zelle/comparison.json")       # inherit governance defaults
    comp = {"product": P, "governance": zelle["governance"], "attributes": attrs}
jdump(cpath, comp)

def placeholder(bank, aid):
    return [{"basis": "awaiting", "source_ids": [], "asserted_by": None, "asserted_at": None, "observed_on": None,
             "valid_to": None, "verified_by": None, "verified_at": None, "id": f"urn:kos:assertion:{bank}:{P}:{aid[5:]}:1"}]
for bank in portfolio["banks"]:
    vp = f"data/comparisons/{P}/values/{bank}.json"
    vf = jload(vp) if os.path.exists(os.path.join(ROOT, vp)) else {"bank": bank, "product": P, "values": {}}
    for a in comp["attributes"]:
        vf["values"].setdefault(a["id"], placeholder(bank, a["id"]))
    jdump(vp, vf)
print(f"{P}: {len(comp['attributes'])} question(s), {len(portfolio['banks'])} bank file(s) ready")

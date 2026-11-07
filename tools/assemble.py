#!/usr/bin/env python3
"""Assemble the split source files into one instance (dist/kjourneys.json) for validation and the site.

Sources (each owned and reviewed separately, so changes stay small and never collide):
  manifest.json                               manifest: ontology version
  registries/*.json                           shared catalogs (data office)
  data/portfolio.json                         banks and products in the study
  data/journeys/<bank>/<journey>.json         one journey per file
  data/comparisons/<product>/comparison.json  attributes + governance
  data/comparisons/<product>/values/<bank>.json   one bank's facts (market intelligence)
"""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(p): return json.load(open(os.path.join(ROOT, p)))
problems = []

manifest = load("manifest.json")
out = {"ontology": manifest["ontology"], "codelists": load("registries/codelists.json")}
for k in ["sources", "parties", "products", "capabilities", "applications", "metrics", "processes", "controls"]:
    out[k] = load(f"registries/{k}.json")

out["journeys"] = []
for p in sorted(glob.glob(os.path.join(ROOT, "data/journeys/*/*.json"))):
    j = json.load(open(p)); bank_dir = os.path.basename(os.path.dirname(p))
    if j.get("bank") != bank_dir:
        problems.append(f"{os.path.relpath(p, ROOT)}: bank '{j.get('bank')}' does not match folder '{bank_dir}'")
    out["journeys"].append(j)

out["portfolio"] = load("data/portfolio.json")

comps = sorted(glob.glob(os.path.join(ROOT, "data/comparisons/*/comparison.json")))
if len(comps) > 1:
    problems.append("only one comparison per instance is supported in kos-journey/0.4 (found %d)" % len(comps))
for c in comps[:1]:
    folder = os.path.dirname(c); product = os.path.basename(folder)
    cmp = json.load(open(c))
    if cmp["product"] != product:
        problems.append(f"{os.path.relpath(c, ROOT)}: product '{cmp['product']}' does not match folder '{product}'")
    cmp["values"] = {}
    for v in sorted(glob.glob(os.path.join(folder, "values/*.json"))):
        f = json.load(open(v)); stem = os.path.splitext(os.path.basename(v))[0]
        if f.get("bank") != stem: problems.append(f"{os.path.relpath(v, ROOT)}: bank '{f.get('bank')}' does not match file name")
        if f.get("product") != product: problems.append(f"{os.path.relpath(v, ROOT)}: product '{f.get('product')}' does not match folder")
        cmp["values"][f["bank"]] = f["values"]
    out["comparison"] = cmp

if problems:
    print("ASSEMBLE FAIL"); [print(" -", x) for x in problems]; sys.exit(1)
os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, "dist/kjourneys.json"), "w"), ensure_ascii=False, indent=1)
print(f"assembled dist/kjourneys.json — {len(out['journeys'])} journey(s), "
      f"{len(out.get('comparison', {}).get('values', {}))} bank comparison file(s)")

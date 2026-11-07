#!/usr/bin/env python3
"""Wells Fargo-only export: everything the knowledge map and the product / line-of-business bundles are built from.

  python3 tools/export_focus.py            writes docs/bundles/_source/wells-fargo.json (committed, pinned by sha256)
  python3 tools/export_focus.py --check    fails if the committed export differs from what dist/kjourneys.json produces

Only the focus bank's records go in. Other banks never appear:
  * records about other banks are left out entirely (their journeys, findings, catalog, scores, sources);
  * customer journeys (MI composites) keep their steps but drop which bank steps they were built from and MI's rationale;
  * where a Wells Fargo record's own text mentions another bank, that sentence, clause or aside is removed, and a URL that
    names another bank is dropped (tools/peers.py decides what a mention is, case-insensitively, including URL slugs);
  * stage scores keep Wells Fargo's score and the best score any bank reached, as a number, with no bank named;
  * rankings, comparisons across banks, verifications of other banks and reference-bank lists are left out.
The output is deterministic (sorted, no wall-clock time), so bundles can pin it by hash."""
import argparse, hashlib, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs/bundles/_source/wells-fargo.json")
ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); args = ap.parse_args()
d = json.load(open(os.path.join(ROOT, "dist/kjourneys.json")))
FOCUS = d["portfolio"]["focus_bank"]
others = [p for p in d["parties"] if p["id"] != FOCUS]

sys.path.insert(0, os.path.join(ROOT, "tools")); import peers   # one definition of "another bank", shared with validate_bundles.py
removed = 0
def scrub(t, key=None):
    global removed
    if not isinstance(t, str) or not peers.mentions(t): return t
    if key == "url": removed += 1; return None                   # a URL that names another bank is dropped, not edited
    t2, n = peers.strip(t); removed += n
    if key == "title" and t2.startswith("[Comparison"): t2 = "Source title withheld: it names other banks"
    return t2
def deep(o, key=None):
    if isinstance(o, dict): return {k: deep(v, k) for k, v in o.items()}
    if isinstance(o, list): return [deep(v, key) for v in o]
    return scrub(o, key)

journeys = [j for j in d["journeys"] if j["bank"] == FOCUS]
findings = [{k: v for k, v in f.items() if k not in ("reference_banks",)} for f in d.get("findings", []) if f["bank"] == FOCUS]
catalog = [p for p in d.get("catalog", []) if p["bank"] == FOCUS]
used_cj = {j.get("composite") for j in journeys if j.get("composite")}
customer_journeys = [{"id": c["id"], "title": c["title"], "product": c["product"], "segment": c.get("segment"), "direction": c.get("direction"),
                      "steps": [{"stage": s["stage"], "n": s["n"], "action": s["action"], "actor": s.get("actor"), "channel": s.get("channel"),
                                 "moment_of_truth": s.get("moment_of_truth")} for s in c["steps"]],
                      "report_version": c["report_version"]} for c in d.get("composites", []) if c["id"] in used_cj]
scores, flags = {}, {}
for cmp in d.get("comparisons", []):
    P = cmp["product"]
    cur = lambda h: next((a for a in h if a.get("valid_to") is None and a["basis"] != "awaiting"), None)
    for aid, h in cmp["values"].get(FOCUS, {}).items():
        a = cur(h)
        if aid.startswith("attr-score-"):
            best = max([x["value"] for b, row in cmp["values"].items() for x in [cur(row.get(aid, []))] if x is not None] or [None], key=lambda v: -1 if v is None else v)
            if a is not None or best is not None:
                scores.setdefault(P, {})[aid[11:]] = {"score": None if a is None else a["value"], "best_practice": best,
                                                      "evidence": None if a is None else (a.get("x-evidence") or {}).get("mi_level"),
                                                      "rationale": None if a is None else (a.get("x-evidence") or {}).get("quote")}
        elif aid.startswith("attr-cap-") and a is not None:
            flags.setdefault(P, {})[aid[9:]] = {"value": a["value"], "detail": a.get("display")}
cap_names = {a["id"][9:]: a["name"] for c in d.get("comparisons", []) for a in c["attributes"] if a["id"].startswith("attr-cap-")}
want_src = set()
def collect(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "source_ids" and isinstance(v, list): want_src.update(v)
            else: collect(v)
    elif isinstance(o, list):
        for v in o: collect(v)
for x in (journeys, findings, catalog, d.get("lines_of_business", {})): collect(x)
other_ids = {p["id"] for p in others}
sources = sorted([s for s in d["sources"] if s["id"] in want_src and s.get("bank") not in other_ids], key=lambda s: s["id"])
apps_used = sorted({a for j in journeys for m in j["moments"] for a in m.get("applications", [])})
party = next(p for p in d["parties"] if p["id"] == FOCUS)
out = deep({
    "bank": {"id": FOCUS, "name": party["name"]},
    "ontology": d["ontology"],
    "reports": sorted({j.get("report_version") for j in journeys if j.get("report_version")}),
    "lines_of_business": d.get("lines_of_business"),
    "products": catalog,
    "journeys": journeys,
    "customer_journeys": customer_journeys,
    "findings": findings,
    "observations": [o for o in d.get("observations", []) if o["bank"] == FOCUS],
    "stage_scores": scores, "rail_capabilities": flags, "capability_names": cap_names,
    "rails": [{"id": p["id"], "name": p["name"], "family": p.get("family")} for p in d["products"]],
    "stages": d["codelists"]["stages"],
    "applications": [a for a in d["applications"] if a["app_id"] in apps_used],
    "processes": [p for p in d["processes"] if p["id"].startswith(f"urn:kos:process:{FOCUS}:")],
    "controls": [c for c in d["controls"] if c["id"].startswith(f"urn:kos:control:{FOCUS}:")],
    "capabilities": d["capabilities"],
    "sources": sources,
})
for x in out["sources"]:                                        # the study's own title gives its scope away; keep it generic
    if x.get("kind") == "mi-report": x["title"] = f"Money-movement market intelligence, report {x.get('report_version')}"
out["meta"] = {"focus_only": True,
               "rules": "Other banks' records are excluded. Any sentence, clause or aside in Wells Fargo text that mentions another bank is "
                        "removed, and URLs that name one are dropped. Best-practice scores are the highest score any bank reached, with no bank named."}
# a second pass over everything, with the same detector the validator uses: no other bank may be named anywhere
left = []
def walk(o):
    if isinstance(o, dict): [walk(v) for v in o.values()]
    elif isinstance(o, list): [walk(v) for v in o]
    elif isinstance(o, str): left.extend(peers.find(o))
walk(out)
if left: sys.exit(f"export_focus: other banks still named after filtering: {sorted(set(left))[:10]}")
body = json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
if args.check:
    have = open(OUT).read() if os.path.exists(OUT) else ""
    if have != body: sys.exit("export_focus --check: docs/bundles/_source/wells-fargo.json is out of date; run python3 tools/export_focus.py")
    print("export ok — the Wells Fargo export matches the data"); sys.exit(0)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(body)
print(f"wrote docs/bundles/_source/wells-fargo.json — {len(catalog)} products, {sum(len(p['sub_products']) for p in catalog)} sub-products, "
      f"{len(journeys)} journeys, {len(customer_journeys)} customer journeys, {len(findings)} findings, {len(sources)} sources, "
      f"{removed} passages naming other banks removed; sha256 {hashlib.sha256(body.encode()).hexdigest()[:12]}")

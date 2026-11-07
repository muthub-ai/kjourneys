#!/usr/bin/env python3
"""Build Wells Fargo product and line-of-business bundles (OKF v0.2) from the Wells Fargo-only export.

  python3 tools/build_bundles.py           (re)writes docs/bundles/{lob-bundles,product-bundles}/ and the root index
  python3 tools/build_bundles.py --check   fails if docs/bundles/ differs from what the export produces

Layout follows application bundles in kbundles: control files (bundle-manifest.json, index.md, insert-only log.md,
knowledge-source.json), cited sections/, a script-built journey-graph/ (the analogue of code-graph/, never edited by
hand) and a human-only knowledge-sources/ folder this script never touches.

Citation regime: every paragraph, list item and table row carries at least one footnote
  [^n]: kj · <kind>/<id> · <sha12>
where <kind>/<id> is a record in docs/bundles/_source/wells-fargo.json and <sha12> the first 12 hex of the sha256 of
that record's canonical JSON. A block without a footnote must start with *Assessment:*. tools/validate_bundles.py
checks all of it, and that no other bank is named anywhere."""
import argparse, hashlib, json, os, re, shutil, sys, tempfile
from collections import Counter, defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_REL = "docs/bundles/_source/wells-fargo.json"
ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); ap.add_argument("--out", default=os.path.join(ROOT, "docs/bundles"))
args = ap.parse_args()
raw = open(os.path.join(ROOT, SRC_REL), "rb").read()
X = json.loads(raw); EXPORT_SHA = hashlib.sha256(raw).hexdigest()
BANK = X["bank"]["name"]
REPORTS = X["reports"]
GEN_AT = "2026-11-07T00:00:00-06:00" if not REPORTS else f"{REPORTS[-1][:10]}T23:59:00-06:00"   # deterministic: tied to the report, not the clock
SITE = "../../../../dist/index.html"
REPSRC = {x["report_version"]: x for x in X["sources"] if x.get("kind") == "mi-report"}

# ---------- the record index every citation points into (validate_bundles.py rebuilds the same index) ----------
def canon(o): return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
def sha12(o): return hashlib.sha256(canon(o).encode()).hexdigest()[:12]
def records(x):
    R = {}
    for l in (x.get("lines_of_business") or {}).get("lines_of_business", []): R[f"lob/{l['id']}"] = l
    for a in (x.get("lines_of_business") or {}).get("assignments", []): R[f"assignment/{a['product']}"] = a
    for p in x["products"]:
        R[f"product/{p['id']}"] = {k: v for k, v in p.items() if k != "sub_products"}
        for s in p["sub_products"]: R[f"sub-product/{s['id']}"] = s
    for j in x["journeys"]:
        key = j.get("source_journey_id") or "sample"
        R[f"journey/{key}"] = {k: v for k, v in j.items() if k != "moments"}
        for m in j["moments"]: R[f"step/{key}#{m['code']}"] = m
    for c in x["customer_journeys"]: R[f"customer-journey/{c['id']}"] = c
    for f in x["findings"]: R[f"finding/{f['id']}"] = f
    for rail, st in x["stage_scores"].items():
        for s, v in st.items(): R[f"score/{rail}/{s}"] = v
    for rail, fl in x["rail_capabilities"].items():
        for k, v in fl.items(): R[f"capability/{rail}/{k}"] = v
    for a in x["applications"]: R[f"app/{a['app_id']}"] = a
    for c in x["controls"]: R[f"control/{c['id'].rsplit(':', 1)[1]}"] = c
    for s in x["sources"]: R[f"source/{s['id']}"] = s
    return R
REC = records(X)

def slug(t): return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-")
STG = {s["id"]: s["name"] for s in X["stages"]}
RAIL = {r["id"]: r["name"] for r in X["rails"]}
LOBS = {l["id"]: l for l in X["lines_of_business"]["lines_of_business"]}
ASSIGN = {a["product"]: a for a in X["lines_of_business"]["assignments"]}
SEVO = {"critical": 0, "high": 1, "medium": 2, "low": 3}
JOUR = {j["id"]: j for j in X["journeys"]}
CJ = {c["id"]: c for c in X["customer_journeys"]}
FBYJ = defaultdict(list)
for f in X["findings"]:
    if f.get("journey"): FBYJ[f["journey"]].append(f)
def jkey(j): return j.get("source_journey_id") or "sample"
def esc_md(t): return (t or "").replace("|", "\\|").replace("\n", " ").strip()
def product_bundle_id(p): return f"{p['id'].lower()}-{slug(re.sub(r'[®℠™]', '', p['name']).split('(')[0])[:28].strip('-')}"

class Doc:
    """One section: blocks of markdown, each with its citations, rendered with numbered footnotes."""
    def __init__(self, about, title): self.title, self.blocks, self.notes, self.idx, self.about = title, [], [], {}, about   # about: the record absences are stated against
    def cite(self, *refs):
        out = ""
        for r in refs:
            if r not in REC: raise SystemExit(f"build_bundles: cites unknown record {r}")
            if r not in self.idx: self.notes.append(r); self.idx[r] = len(self.notes)
            out += f"[^{self.idx[r]}]"
        return out
    def h(self, text): self.blocks.append(f"## {text}")
    def p(self, text, *refs): self.blocks.append(f"{text}{self.cite(*refs)}")
    def assess(self, text): self.blocks.append(f"*Assessment:* {text}")
    def method(self, text): self.blocks.append(f"*Method:* {text}")          # how to read the section; states no fact about Wells Fargo
    def li(self, items, none="None recorded in this study."):
        self.blocks.append("\n".join(f"- {t}{self.cite(*r)}" for t, r in items) if items else f"{none}{self.cite(self.about)}")
    def table(self, head, rows):
        if not rows: self.blocks.append(f"None recorded in this study.{self.cite(self.about)}"); return
        lines = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
        for cells, refs in rows:
            cells = list(cells); cells[-1] = f"{cells[-1]}{self.cite(*refs)}"
            lines.append("| " + " | ".join(esc_md(str(c)) if i < len(cells) - 1 else str(c).replace("|", "\\|") for i, c in enumerate(cells)) + " |")
        self.blocks.append("\n".join(lines))
    def body(self):
        foot = "\n".join(f"[^{i}]: kj · {r} · {sha12(REC[r])}" for i, r in enumerate(self.notes, 1))
        return f"# {self.title}\n\n" + "\n\n".join(self.blocks) + ("\n\n" + foot if foot else "") + "\n"

def frontmatter(kind, bundle_id, title, desc, body, extra):
    meta = {"type": f"{kind}/section", "title": title, "description": desc,
            "sources": [{"id": "kj-wells-fargo", "path": SRC_REL, "sha256": EXPORT_SHA}] +
                       [{"id": f"mi-{v}", "report_version": v, "path": REPSRC[v]["path"], "sha256": REPSRC[v]["sha256"]} for v in REPORTS if v in REPSRC],
            "generated": {"by": "process:build-bundles", "at": GEN_AT}, "verified": [],
            "x_kf": {"schema": f"kf-{kind}/0.1", "bundle_id": bundle_id, "bank": X["bank"]["id"], **extra,
                     "content_sha256": hashlib.sha256(body.encode()).hexdigest(),
                     "review": {"submitted_as": "candidate", "approver": None}}}
    return "---\n" + json.dumps(meta, ensure_ascii=False, indent=1) + "\n---\n\n"   # JSON is valid YAML

# ---------- product bundles ----------
files = {}                                   # path relative to docs/bundles -> text
def put(rel, text): files[rel] = text if text.endswith("\n") else text + "\n"
def stage_rows(rails):
    rows = []
    for r in rails:
        for s in [x["id"] for x in X["stages"]]:
            v = X["stage_scores"].get(r, {}).get(s)
            if not v: continue
            gap = None if v["score"] is None or v["best_practice"] is None else v["best_practice"] - v["score"]
            rows.append(((RAIL.get(r, r), STG[s], "U" if v["score"] is None else v["score"], "—" if v["best_practice"] is None else v["best_practice"],
                          "—" if gap is None else ("at best practice" if gap == 0 else f"−{gap}")), [f"score/{r}/{s}"]))
    return rows
FLAG_ORDER = list(X["capability_names"])
prod_index = []
for p in X["products"]:
    bid = product_bundle_id(p); base = f"product-bundles/{bid}"
    a = ASSIGN[p["id"]]; owner = LOBS[a["owner"]]
    subs = p["sub_products"]
    js = [JOUR[u] for s in subs for u in s.get("journeys", []) if u in JOUR]
    js = sorted({j["id"]: j for j in js}.values(), key=lambda j: jkey(j))
    if p["id"] == "WF-P01":                 # the hand-built sample blueprint is a Zelle send journey
        js += [j for j in X["journeys"] if j.get("basis") == "sample"]
    fs = sorted([f for j in js for f in FBYJ[j["id"]]], key=lambda f: (f["type"] == "strength", SEVO.get(f.get("severity"), 9), f["id"]))
    gaps = [f for f in fs if f["type"] != "strength"]; strengths = [f for f in fs if f["type"] == "strength"]
    rails = sorted({s["product"] for s in subs} | set(p["rails"]))
    cjs = sorted({j.get("composite") for j in js if j.get("composite")})
    pr = f"product/{p['id']}"
    sec = {}
    # 1 executive summary
    D = Doc(pr, f"{p['name']} — executive summary")
    D.p(f"**{p['name']}** (`{p['id']}`) is a {BANK} product. {p.get('description') or ''}", pr)
    if p.get("former_names"): D.p(f"Former names: {p['former_names']}", pr)
    D.p(f"It is owned by **{owner['name']}** ({a.get('component') or 'segment level'}){'; it also serves ' + ', '.join(LOBS[x]['name'] for x in a.get('also', [])) if a.get('also') else ''}. Basis: {a['basis']} — {a['rule']}.", f"assignment/{p['id']}", f"lob/{owner['id']}")
    D.p(f"It has {len(subs)} sub-products, {sum(1 for s in subs if s.get('journeys'))} of them with a mapped journey, across the {', '.join(RAIL.get(r, r) for r in rails)} rail(s).", pr, *[f"sub-product/{s['id']}" for s in subs])
    nmi = sum(1 for j in js if j.get("basis") != "sample")
    if js: D.p(f"MI documented {nmi} journey(s) for it{' (plus the hand-built sample blueprint)' if nmi < len(js) else ''}, delivering {len(cjs)} customer journey(s); they carry {len(gaps)} gap(s) ({', '.join(f'{n} {k}' for k, n in sorted(Counter(f['severity'] for f in gaps).items(), key=lambda kv: SEVO[kv[0]]))}) and {len(strengths)} strength(s).",
               *[f"journey/{jkey(j)}" for j in js], *[f"finding/{f['id']}" for f in fs])
    else: D.p("MI documented no journey for this product yet; its sub-products are listed in the product definition.", pr)
    if gaps:
        D.h("Most severe gaps")
        D.li([(f"**{f['severity']}** · {STG.get(f.get('stage'), f.get('stage') or '')} · {f['description']}", [f"finding/{f['id']}"]) for f in gaps[:3]])
    sec["01-executive-summary"] = ("Executive summary", f"{p['name']}: ownership, scope, journeys and its most severe gaps", D)
    # 2 customer and market
    D = Doc(pr, f"{p['name']} — customers and channels")
    D.p(f"Segments: {', '.join(p.get('segments') or []) or 'not stated'}. Channels: {', '.join(p.get('channels') or []) or 'not stated'}.", pr)
    if p.get("network"): D.p(f"Network or vendor: {p['network']}.", pr)
    D.h("Customer journeys this product delivers")
    D.li([(f"**{CJ[c]['title']}** ({CJ[c].get('segment') or 'any segment'}, {(CJ[c].get('direction') or '').lower()}) — {len(CJ[c]['steps'])} best-practice steps", [f"customer-journey/{c}"]) for c in cjs])
    D.h("Who the journeys are for")
    D.li([(f"`{jkey(j)}` {j['title']} — persona: {j.get('persona')}; goal: “{j.get('customer_goal')}”", [f"journey/{jkey(j)}"]) for j in js])
    sec["02-customer-and-market"] = ("Customers and channels", f"Segments, channels and the customer journeys {p['name']} delivers", D)
    # 3 product definition
    D = Doc(pr, f"{p['name']} — product definition")
    if p.get("ui_position"): D.p(f"Where it sits in the bank's app and site: {p['ui_position']}", pr)
    D.h("Sub-products")
    D.table(["Sub-product", "Rail", "Segments", "Description"], [((f"`{s['id']}` {s['name']}", RAIL.get(s["product"], s["product"]), ", ".join(s.get("segments") or []), s.get("description") or "—"), [f"sub-product/{s['id']}"]) for s in subs])
    D.h("Capabilities by sub-product")
    D.method("✓ yes · ✗ no · — unknown or not assessed, counted the way MI counts them (only a literal Yes is yes).")
    D.table(["Capability"] + [s["id"] for s in subs] + ["Detail"], [
        ([X["capability_names"].get(k, k)] + [{True: "✓", False: "✗", None: "—"}[s["capabilities"].get(k)] for s in subs] +
         ["; ".join(f"{s['id']}: {s.get('capability_detail', {})[k]}" for s in subs if s.get("capability_detail", {}).get(k)) or ""], [f"sub-product/{s['id']}" for s in subs])
        for k in FLAG_ORDER if any(s["capabilities"].get(k) is not None or s.get("capability_detail", {}).get(k) for s in subs)])
    notes = [(f"`{s['id']}`: {s['notes']}", [f"sub-product/{s['id']}"]) for s in subs if s.get("notes")]
    if notes: D.h("Notes from the study"); D.li(notes)
    terms = [(f"`{jkey(j)}` — " + "; ".join(f"{k}: {v}" for k, v in j["terms"].items()), [f"journey/{jkey(j)}"]) for j in js if j.get("terms")]
    if terms: D.h("Limits, fees and timing (captured incidentally)"); D.li(terms)
    sec["03-product-definition"] = ("Product definition", f"{p['name']}: sub-products, capabilities per sub-product, notes, limits and fees", D)
    # 4 experience
    D = Doc(pr, f"{p['name']} — journeys and experience")
    if not js: D.p("MI documented no journey for this product.", pr)
    for j in js:
        k = jkey(j); st = [STG[s] for s in dict.fromkeys(m["stage"] for m in j["moments"])]
        D.h(f"`{k}` {j['title']}")
        D.p(f"{len(j['moments'])} steps across {', '.join(st)}. Channels: {', '.join((j.get('channels') or {}).get('entry', []) + (j.get('channels') or {}).get('other', [])) or 'not stated'}." +
            (f" Status tracking: {j['status_tracking'].get('where')}." if (j.get('status_tracking') or {}).get('where') else ""), f"journey/{k}")
        if j.get("composite"): D.p(f"Delivers the customer journey **{CJ[j['composite']]['title']}** (linked by {j.get('composite_match', 'reference').replace('-', ' ')}).", f"journey/{k}", f"customer-journey/{j['composite']}")
        if j.get("assessment"): D.p(f"MI assessment: {j['assessment']}", f"journey/{k}")
        if j.get("basis") == "sample": D.assess("This is the hand-built sample blueprint; its emotions, hot spots, process, controls and app IDs are placeholders for design review.")
    D.p(f"Every journey opens as a blueprint in the kjourneys site ([Journey]({SITE}#journeys) and [Blueprint]({SITE}#blueprint) views).", *[f"journey/{jkey(j)}" for j in js] or [pr])
    sec["04-experience"] = ("Journeys and experience", f"Each {p['name']} journey: steps, stages, channels and MI's assessment", D)
    # 5 experience assessment
    D = Doc(pr, f"{p['name']} — experience assessment")
    D.method("Stage scores use MI's rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only by switching channel or a critical gap, 0 absent, U not scored. Best practice is the highest score any bank in the study reached; no bank is named.")
    D.table(["Rail", "Stage", f"{BANK}", "Best practice", "Gap"], stage_rows(rails))
    D.h("Gaps")
    D.li([(f"**{f['severity']}** · {STG.get(f.get('stage'), '')} · {f['type'].replace('-', ' ')} · {f['description']}", [f"finding/{f['id']}"]) for f in gaps])
    D.h("Strengths")
    D.li([(f"{STG.get(f.get('stage'), '')} · {f['description']}", [f"finding/{f['id']}"]) for f in strengths])
    sec["05-experience-assessment"] = ("Experience assessment", f"{p['name']}: stage scores against best practice, gaps and strengths", D)
    # 6 risk and controls
    D = Doc(pr, f"{p['name']} — risk and controls")
    risk = [f for f in gaps if f["type"] in ("security-trust", "exception-handling")]
    D.h("Security, trust and exception gaps"); D.li([(f"**{f['severity']}** · {f['description']}", [f"finding/{f['id']}"]) for f in risk])
    fps = [(f"`{jkey(j)}` {m['code']} · {fp['text']}", [f"step/{jkey(j)}#{m['code']}"]) for j in js for m in j["moments"] for fp in m.get("fail_points", [])]
    D.h("Fail points along the journeys"); D.li(fps)
    exc = [(f"`{jkey(j)}` · {e.get('trigger')}: {e.get('customer_experience') or ''} → {e.get('resolution') or ''}", [f"journey/{jkey(j)}"]) for j in js for e in j.get("exceptions", [])]
    D.h("Exception paths"); D.li(exc)
    ctl = sorted({c for j in js for m in j["moments"] for c in m.get("controls", [])})
    if ctl:
        D.h("Controls (sample blueprint)")
        D.assess("Controls below come from the hand-built sample and need GRC IDs from the enterprise control library before they can be relied on.")
        D.li([(f"**{REC[f'control/{c.rsplit(chr(58), 1)[1]}']['type']}** · {REC[f'control/{c.rsplit(chr(58), 1)[1]}']['text']}", [f"control/{c.rsplit(':', 1)[1]}"]) for c in ctl if f"control/{c.rsplit(':', 1)[1]}" in REC])
    sec["06-risk-and-controls"] = ("Risk and controls", f"{p['name']}: security and exception gaps, fail points, exception paths and controls", D)
    # 7 operating model
    D = Doc(pr, f"{p['name']} — operating model")
    D.p(f"Owning line of business: **{owner['name']}**, {a.get('component') or 'segment level'}." + (f" Also serves: {', '.join(LOBS[x]['name'] for x in a.get('also', []))}." if a.get("also") else ""), f"assignment/{p['id']}", f"lob/{owner['id']}")
    if a.get("confirm"): D.assess("This assignment is inferred and needs confirmation by the line-of-business owner.")
    apps = sorted({x for j in js for m in j["moments"] for x in m.get("applications", [])})
    if apps:
        D.h("Applications behind it (sample)")
        D.table(["App ID", "Name", "Owner team", "Application bundle"], [((f"`{x}`", REC[f'app/{x}']['name'], REC[f'app/{x}'].get('owner_team') or '—', REC[f'app/{x}'].get('bundle') or 'third party'), [f"app/{x}"]) for x in apps if f"app/{x}" in REC])
    else: D.p("No application IDs are mapped to this product's journeys yet; they come from the application bundles of the systems that run it.", pr)
    D.assess("Product owner, steward and approver are not assigned; set them in knowledge-source.json before this bundle is submitted for review.")
    sec["07-operating-model"] = ("Operating model", f"{p['name']}: owning line of business, supporting applications and ownership to assign", D)

    extra = {"kind": "product-bundle", "product_id": p["id"], "line_of_business": owner["id"]}
    for name, (title, desc, D) in sec.items():
        body = D.body(); put(f"{base}/sections/{name}.md", frontmatter("product-bundle", bid, title, desc, body, extra) + body)
    # journey-graph/: script-built, the analogue of code-graph/
    nodes = [{"id": pr, "type": "product", "label": p["name"]}] + [{"id": f"sub-product/{s['id']}", "type": "sub-product", "label": s["name"]} for s in subs] + \
            [{"id": f"journey/{jkey(j)}", "type": "journey", "label": j["title"]} for j in js] + [{"id": f"customer-journey/{c}", "type": "customer-journey", "label": CJ[c]["title"]} for c in cjs] + \
            [{"id": f"finding/{f['id']}", "type": "strength" if f["type"] == "strength" else "gap", "label": f["description"][:80], "severity": f.get("severity")} for f in fs]
    edges = [{"from": pr, "to": f"sub-product/{s['id']}", "rel": "has"} for s in subs] + \
            [{"from": f"sub-product/{s['id']}", "to": f"journey/{jkey(JOUR[u])}", "rel": "used-by"} for s in subs for u in s.get("journeys", []) if u in JOUR] + \
            [{"from": f"journey/{jkey(j)}", "to": f"customer-journey/{j['composite']}", "rel": "delivers"} for j in js if j.get("composite")] + \
            [{"from": f"journey/{jkey(JOUR[f['journey']])}", "to": f"finding/{f['id']}", "rel": "finding"} for f in fs]
    put(f"{base}/journey-graph/graph.json", json.dumps({"bundle_id": bid, "nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1))
    metrics = {"bundle_id": bid, "sub_products": len(subs), "sub_products_with_journey": sum(1 for s in subs if s.get("journeys")),
               "journeys": sum(1 for j in js if j.get("basis") != "sample"), "sample_journeys": sum(1 for j in js if j.get("basis") == "sample"),
               "steps": sum(len(j["moments"]) for j in js), "customer_journeys": len(cjs), "gaps": dict(Counter(f["severity"] for f in gaps)),
               "strengths": len(strengths), "rails": rails, "export_sha256": EXPORT_SHA}
    put(f"{base}/journey-graph/metrics.json", json.dumps(metrics, ensure_ascii=False, indent=1, sort_keys=True))
    put(f"{base}/knowledge-sources/README.md", f"# Knowledge sources — {p['name']}\n\nHuman-authored material for this product goes here: PRDs, decisions (DEC-), roadmap notes, ceremony outputs. `tools/build_bundles.py` never writes to this folder.\n")
    put(f"{base}/knowledge-source.json", json.dumps({"bundle_id": bid, "kind": "product-bundle", "bank": X["bank"]["id"], "product_id": p["id"],
        "line_of_business": owner["id"], "source": {"path": SRC_REL, "sha256": EXPORT_SHA, "reports": REPORTS},
        "owners": [], "approver": None, "steward": None}, ensure_ascii=False, indent=1))
    prod_index.append((bid, p, owner, metrics, len(gaps)))

# ---------- line-of-business bundles ----------
lob_index = []
for lid, l in LOBS.items():
    base = f"lob-bundles/{lid}"
    own = [x for x in prod_index if x[2]["id"] == lid]
    also = [x for x in prod_index if lid in ASSIGN[x[1]["id"]].get("also", [])]
    lr = f"lob/{lid}"; sec = {}
    D = Doc(lr, f"{l['name']} — executive summary")
    D.p(f"**{l['name']}** is a {l['kind'].replace('-', ' ')} of {BANK}: {l['description']}", lr)
    if l.get("components"): D.p(f"It reports through: {', '.join(l['components'])}.", lr)
    if own or also:
        D.p(f"In this study it owns {len(own)} money-movement product(s) and also serves {len(also)} owned elsewhere.", lr, *[f"assignment/{x[1]['id']}" for x in own + also])
    else: D.p("The money-movement study has no product owned by or serving this line of business.", lr)
    gsum = Counter(); [gsum.update(x[3]["gaps"]) for x in own]
    if own: D.p(f"Across its products MI recorded {sum(gsum.values())} gap(s): {', '.join(f'{n} {k}' for k, n in sorted(gsum.items(), key=lambda kv: SEVO[kv[0]])) or 'none'}.", *[f"product/{x[1]['id']}" for x in own])
    sec["01-executive-summary"] = ("Executive summary", f"{l['name']}: what it is and the products it owns in this study", D)
    D = Doc(lr, f"{l['name']} — product portfolio")
    D.h("Products it owns")
    D.table(["Product", "Component", "Sub-products", "Journeys", "Gaps", "Bundle"], [((f"`{x[1]['id']}` {x[1]['name']}", ASSIGN[x[1]['id']].get("component") or "—", x[3]["sub_products"], x[3]["journeys"], x[4],
        f"[{x[0]}](../../product-bundles/{x[0]}/index.md)"), [f"product/{x[1]['id']}", f"assignment/{x[1]['id']}"]) for x in own])
    D.h("Products it also serves")
    D.table(["Product", "Owned by", "Bundle"], [((f"`{x[1]['id']}` {x[1]['name']}", x[2]["name"], f"[{x[0]}](../../product-bundles/{x[0]}/index.md)"), [f"assignment/{x[1]['id']}"]) for x in also])
    sec["02-portfolio"] = ("Product portfolio", f"{l['name']}: products owned and served, with links to their bundles", D)
    D = Doc(lr, f"{l['name']} — customer journeys")
    cj_here = defaultdict(list)
    for x in own:
        for s in x[1]["sub_products"]:
            for u in s.get("journeys", []):
                if u in JOUR and JOUR[u].get("composite"): cj_here[JOUR[u]["composite"]].append(JOUR[u])
    D.li([(f"**{CJ[c]['title']}** — delivered by {', '.join(sorted({'`' + jkey(j) + '`' for j in v}))}", [f"customer-journey/{c}"] + [f"journey/{jkey(j)}" for j in v]) for c, v in sorted(cj_here.items())])
    sec["03-customer-journeys"] = ("Customer journeys", f"Customer journeys delivered by {l['name']}'s products", D)
    D = Doc(lr, f"{l['name']} — experience assessment")
    rails = sorted({r for x in own for r in x[3]["rails"]})
    D.table(["Rail", "Stage", BANK, "Best practice", "Gap"], stage_rows(rails))
    top = sorted([f for x in own for f in [g for j in [JOUR[u] for s in x[1]["sub_products"] for u in s.get("journeys", []) if u in JOUR] for g in FBYJ[j["id"]]] if f["type"] != "strength"],
                 key=lambda f: (SEVO.get(f["severity"], 9), f["id"]))
    top = list({f["id"]: f for f in top}.values())[:10]
    D.h("Most severe gaps across its products")
    D.li([(f"**{f['severity']}** · {f['description']}", [f"finding/{f['id']}"]) for f in top])
    sec["04-experience-assessment"] = ("Experience assessment", f"{l['name']}: stage scores for its rails and its most severe gaps", D)
    D = Doc(lr, f"{l['name']} — operating model")
    conf = [x for x in own + also if ASSIGN[x[1]["id"]].get("confirm")]
    if conf: D.li([(f"Confirm: `{x[1]['id']}` {x[1]['name']} — {ASSIGN[x[1]['id']]['rule']}", [f"assignment/{x[1]['id']}"]) for x in conf])
    D.assess("Line-of-business owner, steward and approver are not assigned; set them in knowledge-source.json.")
    sec["05-operating-model"] = ("Operating model", f"{l['name']}: assignments to confirm and ownership to assign", D)
    extra = {"kind": "lob-bundle", "line_of_business": lid}
    for name, (title, desc, D) in sec.items():
        body = D.body(); put(f"{base}/sections/{name}.md", frontmatter("lob-bundle", lid, title, desc, body, extra) + body)
    put(f"{base}/journey-graph/metrics.json", json.dumps({"bundle_id": lid, "products_owned": [x[1]["id"] for x in own], "products_served": [x[1]["id"] for x in also],
        "gaps": dict(gsum), "export_sha256": EXPORT_SHA}, ensure_ascii=False, indent=1, sort_keys=True))
    put(f"{base}/knowledge-sources/README.md", f"# Knowledge sources — {l['name']}\n\nHuman-authored strategy, decisions and operating-model notes for this line of business go here. `tools/build_bundles.py` never writes to this folder.\n")
    put(f"{base}/knowledge-source.json", json.dumps({"bundle_id": lid, "kind": "lob-bundle", "bank": X["bank"]["id"], "line_of_business": lid,
        "source": {"path": SRC_REL, "sha256": EXPORT_SHA, "reports": REPORTS}, "owners": [], "approver": None, "steward": None}, ensure_ascii=False, indent=1))
    lob_index.append((lid, l, own, also))

# ---------- insert-only logs: keep every existing entry (including human ones), add one when the export changes ----------
def logfile(rel, title, line):
    p = os.path.join(args.out, rel)
    have = open(p).read() if os.path.exists(p) else f"# Log — {title}\n"
    head = f"## {GEN_AT[:10]} · Built from export {EXPORT_SHA[:12]} (MI report{'s' if len(REPORTS) > 1 else ''} {', '.join(REPORTS)})"
    if head not in have: have = have.rstrip("\n") + f"\n\n{head}\n\n{line}\n"
    put(rel, have)

# ---------- control files per bundle: index.md, log.md, bundle-manifest.json ----------
def controls(base, bid, kind, title):
    sec = sorted(k for k in files if k.startswith(base + "/sections/"))
    rows = []
    for k in sec:
        fm = json.loads(files[k].split("---\n")[1])
        rows.append(f"- [{fm['title']}]({k[len(base) + 1:]}) — {fm['description']}")
    put(f"{base}/index.md", f"# {title}\n\n{kind.replace('-', ' ').capitalize()} for {BANK}, built from the Wells Fargo-only kjourneys export (`{EXPORT_SHA[:12]}`).\n\n## Sections\n\n" + "\n".join(rows) +
        "\n\n## Derived (script-built, never edit by hand)\n\n" + "\n".join(f"- [{k[len(base) + 1:]}]({k[len(base) + 1:]})" for k in sorted(files) if k.startswith(base + "/journey-graph/")) +
        "\n\n## Control files\n\n- [bundle-manifest.json](bundle-manifest.json) · [knowledge-source.json](knowledge-source.json) · [log.md](log.md)\n- [knowledge-sources/](knowledge-sources/README.md) — human-authored, never generated\n")
    logfile(f"{base}/log.md", title, "- Generated by process:build-bundles from the Wells Fargo-only export.\n- Status: candidate; not yet verified by a human.")
    man = {"schema": "kf-bundle-manifest/0.1", "bundle_id": bid, "kind": kind, "bank": X["bank"]["id"], "okf": "0.2",
           "source": {"path": SRC_REL, "sha256": EXPORT_SHA, "reports": REPORTS}, "generated": {"by": "process:build-bundles", "at": GEN_AT},
           "files": [{"path": k[len(base) + 1:], "sha256": hashlib.sha256(files[k].encode()).hexdigest()} for k in sorted(files) if k.startswith(base + "/") and not k.endswith("bundle-manifest.json")]}
    put(f"{base}/bundle-manifest.json", json.dumps(man, ensure_ascii=False, indent=1))
for bid, p, owner, m, g in prod_index: controls(f"product-bundles/{bid}", bid, "product-bundle", f"{p['name']} · product bundle")
for lid, l, own, also in lob_index: controls(f"lob-bundles/{lid}", lid, "lob-bundle", f"{l['name']} · line-of-business bundle")

# ---------- root index ----------
put("index.md", f"# {BANK} bundles\n\nLine-of-business and product bundles in OKF v0.2, built by `tools/build_bundles.py` from the Wells Fargo-only export `_source/wells-fargo.json` (`{EXPORT_SHA[:12]}`, MI report{'s' if len(REPORTS) > 1 else ''} {', '.join(REPORTS)}).\n\n"
    "## Lines of business\n\n" + "\n".join(f"- [{l['name']}](lob-bundles/{lid}/index.md) — owns {len(own)} product(s), also serves {len(also)}" for lid, l, own, also in lob_index) +
    "\n\n## Products\n\n| Bundle | Product | Owned by | Sub-products | Journeys | Gaps |\n|---|---|---|---|---|---|\n" +
    "\n".join(f"| [{bid}](product-bundles/{bid}/index.md) | {p['name']} | {owner['name']} | {m['sub_products']} | {m['journeys']} | {g} |" for bid, p, owner, m, g in prod_index) +
    "\n\n" + (lambda un: ("## Findings not tied to a journey\n\nMI recorded these for Wells Fargo as a whole; no journey or product carries them.\n\n" +
        "\n".join(f"- **{f['severity'] if f['type'] != 'strength' else 'strength'}** · `{f['id']}` · {f['description']} (kj · finding/{f['id']} · {sha12(REC['finding/' + f['id']])})" for f in un) + "\n\n") if un else "")(
        [f for f in X["findings"] if not f.get("journey")]) +
    "See [README.md](README.md) for the layout, citation rules and how to rebuild.\n")
logfile("log.md", "bundles", f"- {len(prod_index)} product bundles and {len(lob_index)} line-of-business bundles generated by process:build-bundles.")

# ---------- write or check ----------
MANAGED = ("index.md", "log.md", "lob-bundles/", "product-bundles/")
def managed(rel): return (rel in MANAGED or rel.startswith(MANAGED[2:])) and "/knowledge-sources/" not in rel.replace("knowledge-sources/README.md", "")
existing = set()
for dp, _, fns in os.walk(args.out):
    for fn in fns:
        rel = os.path.relpath(os.path.join(dp, fn), args.out)
        if managed(rel): existing.add(rel)
if args.check:
    bad = sorted([r for r, t in files.items() if not os.path.exists(os.path.join(args.out, r)) or open(os.path.join(args.out, r)).read() != t] + [r for r in existing - set(files)])
    if bad: print(f"build_bundles --check: {len(bad)} file(s) differ from what the export produces:"); [print(" -", b) for b in bad[:20]]; sys.exit(1)
    print(f"bundles ok — {len(prod_index)} product and {len(lob_index)} line-of-business bundles match the export"); sys.exit(0)
for rel in existing - set(files): os.remove(os.path.join(args.out, rel))
for rel, t in files.items():
    p = os.path.join(args.out, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"; open(tmp, "w").write(t); os.replace(tmp, p)
print(f"wrote {len(prod_index)} product bundles and {len(lob_index)} line-of-business bundles ({len(files)} files) to docs/bundles/")

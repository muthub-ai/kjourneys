#!/usr/bin/env python3
"""Render dist/index.html from site/template.html + dist/kjourneys.json + schema/journey-ontology.yaml.

The page is self-contained: a compact view model (built here, not in the browser) is inlined, so the
page can be published as an artifact or a static file. Nothing in the view model is computed that the
data does not already state; it is only reshaped (current assertions only, short keys)."""
import json, os, glob, collections, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(ROOT, "dist/kjourneys.json")))
schema = open(os.path.join(ROOT, "schema/journey-ontology.yaml")).read()
FOCUS = d["portfolio"]["focus_bank"]

def cur(h):
    """the current assertion of a history (valid_to null), or None when the slot is awaiting"""
    c = [a for a in h if a.get("valid_to") is None]
    a = c[-1] if c else None
    return None if not a or a["basis"] == "awaiting" else a
def lvl(a):
    a = a or {}
    return a.get("x-mi_evidence") or (a.get("x-evidence") or {}).get("mi_level") or a.get("basis")

# ---- reports (newest first) ----
reports = []
for mp in sorted(glob.glob(os.path.join(ROOT, "reports/*/manifest.json")), reverse=True):
    m = json.load(open(mp))
    reports.append({"version": m["report_version"], "title": m.get("title"), "received_at": m.get("received_at"),
                    "produced_by": m.get("produced_by"), "workbook": m.get("workbook"),
                    "files": [{"path": f["path"], "kind": f.get("kind"), "sha256": f["sha256"]} for f in m["files"]]})

# ---- comparisons: capability flags and stage scores ----
caps, scores, cap_attrs = {}, {}, {}
for c in d["comparisons"]:
    p = c["product"]
    for a in c["attributes"]:
        if a["id"].startswith("attr-cap-"): cap_attrs[a["id"][9:]] = {"name": a["name"], "stage": a["stage"]}
    for bank, row in c["values"].items():
        for aid, h in row.items():
            a = cur(h)
            if aid.startswith("attr-cap-"):
                caps.setdefault(p, {}).setdefault(bank, {})[aid[9:]] = None if a is None else [a["value"], lvl(a), a["basis"], a.get("display"), a.get("source_ids", [])]
            elif aid.startswith("attr-score-") and a is not None:
                scores.setdefault(bank, {}).setdefault(p, {})[aid[11:]] = [a["value"], lvl(a), (a.get("x-evidence") or {}).get("quote")]

# ---- journeys ----
def step(m):
    tp = "; ".join(f"{t['channel']}" + (f": {t['screen']}" if t.get("screen") else "") for t in m.get("touchpoints", []))
    ev = m.get("evidence", {})
    a = ev.get("action") or next(iter(ev.values()), {})
    srcs = sorted({s for e in ev.values() for s in e.get("source_ids", [])})
    out = {"c": m["code"], "s": m["stage"], "t": m["title"], "a": m.get("action") or m.get("customer_action") or m["title"], "who": m.get("actor") or "customer",
           "tp": tp, "fs": m.get("frontstage"), "dec": m.get("decision"), "ntf": m.get("notification"),
           "fp": [f["text"] for f in m.get("fail_points", [])], "e": lvl(a), "b": a.get("basis"), "src": srcs}
    if m.get("process") is not None:       # the hand-built sample carries the backstage too
        out.update(proc=m.get("process"), ctl=m.get("controls", []), apps=m.get("applications", []), caps=m.get("capabilities", []),
                   kpi=[k.get("metric") for k in m.get("kpis", [])], emo=m.get("emotion"), hot=m.get("hotspot"))
    return out
journeys = []
for j in d["journeys"]:
    journeys.append({"id": j["id"], "bank": j["bank"], "p": j["product"], "t": j["title"], "goal": j.get("customer_goal"),
                     "persona": j.get("persona"), "seg": j.get("segment"), "sjid": j.get("source_journey_id"), "sub": j.get("sub_product"),
                     "basis": j["basis"], "e": j.get("x-mi_evidence") or j["basis"], "status": j["status"], "rv": j.get("report_version"),
                     "ch": j.get("channels"), "track": j.get("status_tracking"), "exc": j.get("exceptions", []), "ntf": j.get("notifications", []),
                     "assess": j.get("assessment"), "stages": j["stages"], "steps": [step(m) for m in j["moments"]],
                     "sample": j["basis"] == "sample", "bp": j.get("bank_product"), "cj": j.get("composite"), "cjm": j.get("composite_match"),
                     "terms": j.get("terms")})

# ---- findings, observations, verifications, composites ----
findings = [{"id": f["id"], "bank": f["bank"], "j": f.get("journey"), "p": f.get("product"), "s": f.get("stage"), "n": f.get("step"),
             "type": f["type"], "sev": f.get("severity"), "d": f["description"], "ss": f.get("step_stage"), "cj": f.get("composite"), "ref": f.get("reference_banks"),
             "fw": f.get("frameworks"), "e": f.get("x-mi_evidence") or f.get("basis"), "src": f.get("source_ids", [])} for f in d.get("findings", [])]
sources = {s["id"]: [s.get("title"), s.get("url"), s.get("kind"), s.get("bank"), s.get("local_id"), s.get("access_status")] for s in d["sources"]}
used = {x for p in d.get("catalog", []) for x in p["source_ids"] + [y for sp in p["sub_products"] for y in sp["source_ids"]]} | {x for c in caps.values() for row in c.values() for v in row.values() if v for x in v[4]} | {x for j in journeys for st in j["steps"] for x in st["src"]} | {x for f in findings for x in f["src"]} \
     | {x for j in d["journeys"] for e in j.get("exceptions", []) for x in e.get("source_ids", [])} \
     | {x for p in d.get("participation", []) for x in p.get("source_ids", [])}
by_bank = collections.Counter(v[3] for v in sources.values() if v[3])

V = {
    "ontology": d["ontology"], "focus": FOCUS, "reports": reports,
    "banks": [{"id": p["id"], "name": p["name"], "role": p["role"], "sources": by_bank.get(p["id"], 0)} for p in d["parties"]],
    "products": [{"id": p["id"], "name": p["name"], "family": p.get("family"), "rail": p.get("rail")} for p in d["products"]],
    "stages": d["codelists"]["stages"], "cap_attrs": cap_attrs, "caps": caps, "scores": scores,
    "rankings": [{**{k: v for k, v in r.items() if k != "x-computed"}, "calc": r.get("x-computed")} for r in d.get("rankings", [])],
    "warnings": next((json.load(open(mp)).get("import_warnings", []) for mp in sorted(glob.glob(os.path.join(ROOT, "reports/*/manifest.json")), reverse=True)), []), "journeys": journeys, "findings": findings,
    "observations": d.get("observations", []), "verifications": d.get("verifications", []),
    "composites": [{"id": c["id"], "t": c["title"], "p": c.get("product"), "seg": c.get("segment"), "dir": c.get("direction"),
                    "steps": [{"s": s["stage"], "n": s["n"], "a": s["action"], "who": s.get("actor"), "ch": s.get("channel"),
                               "mot": s.get("moment_of_truth"), "from": s.get("derived_from"), "why": s.get("rationale")} for s in c["steps"]]}
                   for c in d.get("composites", [])],
    "participation": d.get("participation", []),
    # each bank's products as marketed → sub-products (with their own capability flags) → the journeys that use them
    "catalog": [{"id": p["id"], "bank": p["bank"], "name": p["name"], "former": p.get("former_names"), "seg": p.get("segments", []),
                 "rails": p["rails"], "ch": p.get("channels", []), "net": p.get("network"), "ui": p.get("ui_position"), "d": p.get("description"),
                 "e": p.get("x-mi_evidence") or p["basis"], "src": p["source_ids"],
                 "subs": [{"id": x["id"], "name": x["name"], "p": x["product"], "seg": x.get("segments", []), "ch": x.get("channels", []),
                           "d": x.get("description"), "flags": x["capabilities"], "fd": x.get("capability_detail", {}), "other": x.get("other_flags"),
                           "notes": x.get("notes"), "e": x.get("x-mi_evidence") or x["basis"], "src": x["source_ids"], "j": x.get("journeys", [])}
                          for x in p["sub_products"]]} for p in d.get("catalog", [])],
    "sources": {k: v for k, v in sources.items() if k in used or k.startswith("src-mi-")},
    "counts": {"journeys": len(journeys), "steps": sum(len(j["steps"]) for j in journeys), "findings": len(findings),
               "sources": len(d["sources"]), "verifications": len(d.get("verifications", [])),
               "score_cells": sum(len(st) for b in scores.values() for st in b.values())},
    "governance": next((c["governance"] for c in d["comparisons"]), {}),
    # the hand-built sample blueprint keeps its full backstage: process steps, controls, app IDs, metrics, unhappy paths
    "sample": next(({"journey": j, "applications": d["applications"], "processes": d["processes"], "controls": d["controls"],
                     "capabilities": d["capabilities"], "metrics": d["metrics"]} for j in d["journeys"] if j["basis"] == "sample"), None),
}
# ---- Wells Fargo knowledge map: built only from the Wells Fargo export, so no other bank can appear ----
def wf_map():
    fp = os.path.join(ROOT, "docs/bundles/_source/wells-fargo.json")
    if not os.path.exists(fp): return None
    X = json.load(open(fp)); import networkx as nx
    LOB = X["lines_of_business"]; A = {a["product"]: a for a in LOB["assignments"]}
    J = {j["id"]: j for j in X["journeys"]}; CJ = {c["id"]: c for c in X["customer_journeys"]}
    jk = lambda j: j.get("source_journey_id") or "sample"
    N, E = {}, []
    def node(i, t, label, **kw): N[i] = {"id": i, "t": t, "l": label, **kw}
    served = {a["owner"] for a in LOB["assignments"]} | {x for a in LOB["assignments"] for x in a.get("also", [])}
    for l in LOB["lines_of_business"]:
        if l["id"] in served: node("lob/" + l["id"], "lob", l["name"])   # a line of business with no product in the study stays off the map (listed in the side panel)
    for p in X["products"]:
        node("product/" + p["id"], "product", re.sub(r"\s*\(.*", "", p["name"]), ref=p["id"])
        a = A[p["id"]]; E.append(("lob/" + a["owner"], "product/" + p["id"], "owns"))
        for o in a.get("also", []): E.append(("lob/" + o, "product/" + p["id"], "serves"))
        for sp in p["sub_products"]:
            node("sub/" + sp["id"], "sub", sp["name"], ref=sp["id"], bank=p["bank"], hollow=not sp.get("journeys"))
            E.append(("product/" + p["id"], "sub/" + sp["id"], "has"))
            for u in sp.get("journeys", []):
                if u in J: E.append(("sub/" + sp["id"], "journey/" + u, "used by"))
    for j in X["journeys"]:
        node("journey/" + j["id"], "journey", f"{jk(j)} {j['title']}", ref=j["id"], sample=j.get("basis") == "sample")
        if j.get("composite") in CJ: E.append(("journey/" + j["id"], "cj/" + j["composite"], "delivers"))
        for a in sorted({x for m in j["moments"] for x in m.get("applications", [])}):
            node("app/" + a, "app", a); E.append(("journey/" + j["id"], "app/" + a, "runs on"))
    sample = next((j for j in X["journeys"] if j.get("basis") == "sample"), None)
    if sample:   # the sample journey is a Zelle send: attach it to the Zelle product
        E.append(("product/WF-P01", "journey/" + sample["id"], "sample"))
    for c in X["customer_journeys"]: node("cj/" + c["id"], "cj", c["title"], ref=c["id"])
    for f in X["findings"]:
        if not f.get("journey") or f["journey"] not in J: continue
        t = "strength" if f["type"] == "strength" else "gap"
        node("finding/" + f["id"], t, f["description"][:90], ref=f["id"], sev=f.get("severity"))
        E.append(("journey/" + f["journey"], "finding/" + f["id"], t))
    E = [e for e in E if e[0] in N and e[1] in N]
    G = nx.Graph(); G.add_nodes_from(N); G.add_edges_from((a, b) for a, b, _ in E)
    w = {"lob": 6, "product": 4, "cj": 3}
    comp = max(nx.connected_components(G), key=len)
    pos = nx.kamada_kawai_layout(G.subgraph(comp))
    rest = [n for n in G if n not in pos]
    for i, n in enumerate(rest): pos[n] = (1.15, -1 + 2 * i / max(1, len(rest)))   # anything disconnected sits in a column at the right
    xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
    nx0, nx1, ny0, ny1 = min(xs), max(xs), min(ys), max(ys)
    for i, n in N.items():
        n["x"] = round((pos[i][0] - nx0) / ((nx1 - nx0) or 1) * 1000, 1); n["y"] = round((pos[i][1] - ny0) / ((ny1 - ny0) or 1) * 700, 1); n["d"] = G.degree(i)
    # flow (Sankey): line of business → product → sub-product → journey → customer journey
    cols = [[l["id"] for l in LOB["lines_of_business"] if any(A[p["id"]]["owner"] == l["id"] for p in X["products"])], [], [], [], []]
    links = []
    for lid in cols[0]:
        for p in X["products"]:
            if A[p["id"]]["owner"] != lid: continue
            cols[1].append(p["id"])
            for sp in p["sub_products"]:
                cols[2].append(sp["id"]); js = [u for u in sp.get("journeys", []) if u in J]
                links.append((lid, p["id"], max(1, len(js)) if js else 0.4)); links.append((p["id"], sp["id"], max(1, len(js)) if js else 0.4))
                for u in js:
                    if u not in cols[3]: cols[3].append(u)
                    links.append((sp["id"], u, 1))
    for u in cols[3]:
        c = J[u].get("composite") or "none"
        if c not in cols[4]: cols[4].append(c)
        links.append((u, c, 1))
    label = {**{l["id"]: l["name"] for l in LOB["lines_of_business"]}, **{p["id"]: re.sub(r"\s*\(.*", "", p["name"]) for p in X["products"]},
             **{sp["id"]: sp["name"] for p in X["products"] for sp in p["sub_products"]}, **{u: f"{jk(J[u])} {J[u]['title']}" for u in cols[3]},
             **{c: CJ[c]["title"] for c in cols[4] if c in CJ}, "none": "No customer journey linked"}
    return {"nodes": list(N.values()), "edges": [{"a": a, "b": b, "r": r} for a, b, r in E],
            "flow": {"cols": cols, "links": [{"a": a, "b": b, "v": v} for a, b, v in links], "label": label},
            "lobs": LOB["lines_of_business"], "assign": LOB["assignments"],
            "counts": {"products": len(X["products"]), "subs": sum(len(p["sub_products"]) for p in X["products"]),
                       "subs_unmapped": sum(1 for p in X["products"] for sp in p["sub_products"] if not sp.get("journeys")),
                       "journeys": len(X["journeys"]), "cjs": len(X["customer_journeys"]), "gaps": sum(1 for f in X["findings"] if f["type"] != "strength"),
                       "strengths": sum(1 for f in X["findings"] if f["type"] == "strength"), "peer_replaced": X["meta"]["peer_mentions_replaced"]}}
V["map"] = wf_map()

t = open(os.path.join(ROOT, "site/template.html")).read()
js = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")   # nothing in the data can close or comment out the script
frag = t.replace("__DATA__", js(V)).replace("__SCHEMA__", js(schema))
# dist/index.html is a complete document for any static host; dist/artifact.html is the body-only fragment the artifact host wraps itself
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
cut_at = frag.index('<div class="wrap">')                       # title, metas, font links and styles go in the head
doc = head + frag[:cut_at] + "</head>\n<body>\n" + frag[cut_at:] + "\n</body>\n</html>\n"
open(os.path.join(ROOT, "dist/index.html"), "w").write(doc)
open(os.path.join(ROOT, "dist/artifact.html"), "w").write(frag)
kb = len(doc.encode()) // 1024
print(f"built dist/index.html ({kb} KB) and dist/artifact.html")
if kb > 15 * 1024: raise SystemExit("dist/index.html is over 15 MB; the published page limit is 16 MB")

#!/usr/bin/env python3
"""Render dist/index.html from site/template.html + dist/kjourneys.json + schema/journey-ontology.yaml.

The page is self-contained: a compact view model (built here, not in the browser) is inlined, so the
page can be published as an artifact or a static file. Nothing in the view model is computed that the
data does not already state; it is only reshaped (current assertions only, short keys)."""
import json, os, glob, collections
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
    out = {"c": m["code"], "s": m["stage"], "t": m["title"], "a": m.get("customer_action") or m["title"], "who": m.get("actor") or "customer",
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
                     "sample": j["basis"] == "sample"})

# ---- findings, observations, verifications, composites ----
findings = [{"id": f["id"], "bank": f["bank"], "j": f.get("journey"), "p": f.get("product"), "s": f.get("stage"), "n": f.get("step"),
             "type": f["type"], "sev": f.get("severity"), "d": f["description"], "cj": f.get("composite"), "ref": f.get("reference_banks"),
             "fw": f.get("frameworks"), "e": f.get("x-mi_evidence") or f.get("basis"), "src": f.get("source_ids", [])} for f in d.get("findings", [])]
sources = {s["id"]: [s.get("title"), s.get("url"), s.get("kind"), s.get("bank"), s.get("local_id"), s.get("access_status")] for s in d["sources"]}
used = {x for c in caps.values() for row in c.values() for v in row.values() if v for x in v[4]} | {x for j in journeys for st in j["steps"] for x in st["src"]} | {x for f in findings for x in f["src"]} \
     | {x for j in d["journeys"] for e in j.get("exceptions", []) for x in e.get("source_ids", [])} \
     | {x for p in d.get("participation", []) for x in p.get("source_ids", [])}
by_bank = collections.Counter(v[3] for v in sources.values() if v[3])

V = {
    "ontology": d["ontology"], "focus": FOCUS, "reports": reports,
    "banks": [{"id": p["id"], "name": p["name"], "role": p["role"], "sources": by_bank.get(p["id"], 0)} for p in d["parties"]],
    "products": [{"id": p["id"], "name": p["name"], "family": p.get("family"), "rail": p.get("rail")} for p in d["products"]],
    "stages": d["codelists"]["stages"], "cap_attrs": cap_attrs, "caps": caps, "scores": scores,
    "rankings": d.get("rankings", []), "journeys": journeys, "findings": findings,
    "observations": d.get("observations", []), "verifications": d.get("verifications", []),
    "composites": [{"id": c["id"], "t": c["title"], "p": c.get("product"), "seg": c.get("segment"), "dir": c.get("direction"),
                    "steps": [{"s": s["stage"], "n": s["n"], "a": s["action"], "who": s.get("actor"), "ch": s.get("channel"),
                               "mot": s.get("moment_of_truth"), "from": s.get("derived_from"), "why": s.get("rationale")} for s in c["steps"]]}
                   for c in d.get("composites", [])],
    "participation": d.get("participation", []),
    "sources": {k: v for k, v in sources.items() if k in used or k.startswith("src-mi-")},
    "counts": {"journeys": len(journeys), "steps": sum(len(j["steps"]) for j in journeys), "findings": len(findings),
               "sources": len(d["sources"]), "verifications": len(d.get("verifications", [])),
               "score_cells": sum(len(st) for b in scores.values() for st in b.values())},
    "governance": next((c["governance"] for c in d["comparisons"]), {}),
    # the hand-built sample blueprint keeps its full backstage: process steps, controls, app IDs, metrics, unhappy paths
    "sample": next(({"journey": j, "applications": d["applications"], "processes": d["processes"], "controls": d["controls"],
                     "capabilities": d["capabilities"], "metrics": d["metrics"]} for j in d["journeys"] if j["basis"] == "sample"), None),
}
t = open(os.path.join(ROOT, "site/template.html")).read()
payload = json.dumps(V, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = t.replace("__DATA__", payload).replace("__SCHEMA__", json.dumps(schema, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(ROOT, "dist/index.html"), "w").write(html)
kb = len(html.encode()) // 1024
print(f"built dist/index.html ({kb} KB)")
if kb > 15 * 1024: raise SystemExit("dist/index.html is over 15 MB; the published page limit is 16 MB")

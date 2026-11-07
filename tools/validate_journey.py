#!/usr/bin/env python3
"""Validate a kos-journey instance: JSON Schema structure, referential integrity, typing,
temporal rules and publish gates.
Usage: python3 validate_journey.py <instance.json> [schema.json]   (exit 1 on any defect)"""
import json, sys, re
from collections import Counter
from datetime import date, datetime

try:
    import rfc3339_validator  # noqa: F401  (jsonschema silently skips date-time checks without it)
except ImportError:
    sys.exit("FAIL — rfc3339-validator is not installed; date-time formats would not be checked. pip install rfc3339-validator")
from jsonschema import Draft202012Validator, FormatChecker

inst_path = sys.argv[1]
schema_path = sys.argv[2] if len(sys.argv) > 2 else "journey-ontology.schema.json"
d = json.load(open(inst_path)); schema = json.load(open(schema_path))
errors = []
def need(ok, msg):
    if not ok: errors.append(msg)

# ---------- 1. structure ----------
for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(d):
    errors.append(f"schema: {'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}")
if errors:
    print(f"FAIL — {len(errors)} schema defect(s); later checks skipped"); [print(" -", e) for e in errors[:40]]; sys.exit(1)

# ---------- 2. uniqueness ----------
def unique(items, label):
    for k, n in Counter(items).items(): need(n == 1, f"unique: {label} '{k}' appears {n} times")
unique([s["id"] for s in d["codelists"]["stages"]], "stage")
unique([x["id"] for x in d["sources"]], "source")
unique([x["id"] for x in d["parties"]], "party")
unique([x["id"] for x in d["products"]], "product")
unique([x["id"] for x in d["capabilities"]], "capability")
unique([x["app_id"] for x in d["applications"]], "app_id")
unique([x["id"] for x in d["metrics"]], "metric")
unique([x["id"] for x in d["processes"]], "process")
unique([x["id"] for x in d["controls"]], "control")
unique([j["id"] for j in d["journeys"]], "journey")

ids = lambda coll, key="id": {x[key] for x in d.get(coll, [])}
STAGES, SOURCES, LAYERS = {s["id"] for s in d["codelists"]["stages"]}, ids("sources"), set(d["codelists"]["layers"])
PARTIES, PRODUCTS, CAPS = ids("parties"), ids("products"), ids("capabilities")
APPS, METS, PROCS, CTRLS = ids("applications", "app_id"), ids("metrics"), ids("processes"), ids("controls")
app_caps = {a["app_id"]: set(a["capabilities"]) for a in d["applications"]}
metric = {m["id"]: m for m in d["metrics"]}
assertion_ids = set()

def urn_kind(u, kind, bank=None, where=""):
    parts = u.split(":")
    need(parts[2] == kind, f"urn: {where} '{u}' should be a {kind} URN")
    if bank: need(parts[3] == bank, f"urn: {where} '{u}' is not scoped to bank {bank}")

def parse_date(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).date() if "T" in s else date.fromisoformat(s)

def check_assertion(a, where, attr=None):
    if a.get("id"): assertion_ids.add(a["id"])
    for s in a.get("source_ids", []): need(s in SOURCES, f"ref: {where} source {s}")
    if a.get("valid_from") and a.get("valid_to"):
        need(parse_date(a["valid_from"]) <= parse_date(a["valid_to"]), f"temporal: {where} valid_from after valid_to")
    if attr and a["basis"] != "awaiting" and a.get("value") is not None:
        v, dt = a["value"], attr["datatype"]
        ok = {"text": isinstance(v, str), "integer": isinstance(v, int) and not isinstance(v, bool),
              "boolean": isinstance(v, bool), "money": isinstance(v, (int, float)) and not isinstance(v, bool),
              "duration": isinstance(v, str) and re.fullmatch(r"P(?!$)(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+S)?)?", v or "") is not None,
              "enum": isinstance(v, str), "enum_list": isinstance(v, list)}[dt]
        need(ok, f"type: {where} value {v!r} is not a valid {dt}")
        if ok and "allowed_values" in attr:
            vals = v if isinstance(v, list) else [v]
            for x in vals: need(x in attr["allowed_values"], f"type: {where} '{x}' not in allowed values")
    return a

# ---------- 3. catalogs ----------
import hashlib, os
for s in d["sources"]:
    if s["kind"] == "mi-report":
        rp = s["path"]
        if not os.path.exists(rp): errors.append(f"report: source {s['id']} points to missing file {rp}")
        else:
            h = hashlib.sha256(open(rp, "rb").read()).hexdigest()
            need(h == s["sha256"], f"report: {rp} changed after ingestion (sha256 mismatch) — reports are immutable")
        need(s["path"].startswith(f"reports/{s['report_version']}/"), f"report: source {s['id']} path is not in its version folder")
for a in d["applications"]:
    for c in a["capabilities"]: need(c in CAPS, f"ref: app {a['app_id']} capability {c}")
    for x in a.get("depends_on", []): need(x in APPS, f"ref: app {a['app_id']} depends_on {x}")
    if a["layer"] != "external":
        need(a["bundle"] == f"application-bundles/{a['app_id']}/", f"ref: app {a['app_id']} bundle path must be application-bundles/{a['app_id']}/")
    else:
        need(a["bundle"] is None, f"ref: external app {a['app_id']} cannot have a KOS bundle")
for m in d["metrics"]:
    need(m["source_system"] in APPS, f"ref: metric {m['id']} source_system {m['source_system']}")
    need(m["bank"] in PARTIES and m["product"] in PRODUCTS, f"ref: metric {m['id']} bank/product scope")
for c in d["controls"]: urn_kind(c["id"], "control", where="control")
for p in d["processes"]: urn_kind(p["id"], "process", where="process")
focus_ids = [p["id"] for p in d["parties"] if p["role"] == "focus"]
need(len(focus_ids) == 1, f"party: exactly one focus bank (role focus) required, found {len(focus_ids)}")

# ---------- 4. journeys ----------
GATED = {"in-review", "published"}
for j in d["journeys"]:
    bank = j["bank"]
    urn_kind(j["id"], "journey", bank, "journey")
    need(bank in PARTIES, f"ref: journey bank {bank}"); need(j["product"] in PRODUCTS, f"ref: journey product {j['product']}")
    for s in j["stages"]: need(s in STAGES, f"ref: journey stage {s}")
    unique([m["id"] for m in j["moments"]], "moment id"); unique([m["code"] for m in j["moments"]], "moment code")
    mids = [m["id"] for m in j["moments"]]; order = {u: i for i, u in enumerate(mids)}
    stage_order = {s: i for i, s in enumerate(j["stages"])}
    prev_stage = -1
    for m in j["moments"]:
        w = m["code"]
        urn_kind(m["id"], "moment", bank, w)
        need(m["stage"] in j["stages"], f"ref: {w} stage {m['stage']} not in journey.stages")
        if m["stage"] in stage_order:
            need(stage_order[m["stage"]] >= prev_stage, f"order: {w} stage goes backwards"); prev_stage = stage_order[m["stage"]]
        need(m["process"] in PROCS, f"ref: {w} process {m['process']}")
        unique(m["controls"], f"{w} control ref"); unique(m["applications"], f"{w} app ref")
        for c in m["controls"]: need(c in CTRLS, f"ref: {w} control {c}")
        for a in m["applications"]: need(a in APPS, f"ref: {w} app {a}")
        for c in m["capabilities"]:
            need(c in CAPS, f"ref: {w} capability {c}")
            need(any(c in app_caps.get(a, set()) for a in m["applications"]), f"ref: {w} capability {c} not realized by any of its apps")
        unique([f["id"] for f in m["fail_points"]], f"{w} fail point")
        for k in m["kpis"]:
            need(k["metric"] in METS, f"ref: {w} metric {k['metric']}")
            if k.get("actual") is not None:
                mm = metric.get(k["metric"], {})
                need(mm.get("dq_status") == "certified" and mm.get("basis") not in ("sample", "awaiting"),
                     f"metric: {w} shows an actual for {k['metric']}, which is not certified real data")
                need(k.get("period_end") is not None, f"metric: {w} actual for {k['metric']} needs period_end")
        need(set(m["evidence"]) <= LAYERS, f"layer: {w} unknown evidence layer(s) {sorted(set(m['evidence']) - LAYERS)}")
        for L, a in m["evidence"].items(): check_assertion(a, f"{w} evidence.{L}")
    unique([f["id"] for m in j["moments"] for f in m["fail_points"]], "fail point (journey-wide)")
    for v in j.get("variants", []):
        urn_kind(v["id"], "variant", bank, f"variant {v['code']}")
        for x in [v["entry"], v["exit"], *v["moments"], *v["notes"].keys()]: need(x in order, f"ref: variant {v['code']} moment {x}")
        if all(x in order for x in v["moments"]):
            need([order[x] for x in v["moments"]] == sorted(order[x] for x in v["moments"]), f"order: variant {v['code']} moments out of journey order")
        need(v["entry"] in v["moments"] and v["exit"] in v["moments"], f"order: variant {v['code']} entry/exit must be on its own path")
        if v["entry"] in order and v["exit"] in order:
            need(order[v["entry"]] <= order[v["exit"]], f"order: variant {v['code']} entry after exit")
        need(set(v["notes"]) <= set(v["moments"]), f"ref: variant {v['code']} notes outside its moments")

    # publish gates
    g = j["governance"]
    need(not (g["mnpi"] and g["classification"] in ("public", "internal")), "governance: MNPI content must be confidential or restricted")
    need(not (g["contains_pii"] and g["classification"] == "public"), "governance: PII cannot be public")
    if j["status"] in GATED:
        bases = [a["basis"] for m in j["moments"] for a in m["evidence"].values()]
        need("sample" not in bases and "awaiting" not in bases, f"gate: journey is {j['status']} but still holds sample or awaiting facts")
        need(g["steward"] is not None and g["retention_class"], f"gate: journey is {j['status']} without steward and retention class")
        if j["bank"] not in focus_ids:
            need(g["ci_legal_review"]["status"] == "approved", f"gate: competitor journey is {j['status']} without approved CI legal review")
        for c in (CTRLS & {c for m in j["moments"] for c in m["controls"]}):
            cc = next(x for x in d["controls"] if x["id"] == c)
            need(cc["grc_control_id"], f"gate: control {c} has no GRC ID")
        for a in d["applications"]:
            if a["app_id"] in {x for m in j["moments"] for x in m["applications"]} and a["layer"] != "external":
                need(a["cmdb_ci"], f"gate: app {a['app_id']} has no CMDB link")
    need(g["ci_legal_review"]["status"] != "rejected" or j["status"] not in GATED, "gate: journey with rejected legal review cannot be in review or published")

# ---------- 5. portfolio and comparison ----------
pf = d.get("portfolio", {})
if pf:
    need(pf["focus_bank"] in focus_ids, "portfolio: focus_bank must be the party with role focus")
    need(pf["focus_bank"] in pf["banks"], "portfolio: focus_bank must be in banks")
    unique(pf["banks"], "portfolio bank"); unique(pf["products"], "portfolio product")
    for b in pf["banks"]: need(b in PARTIES, f"ref: portfolio bank {b}")
    for p in pf["products"]: need(p in PRODUCTS, f"ref: portfolio product {p}")
cmp = d.get("comparison")
if cmp:
    need(cmp["product"] in PRODUCTS, f"ref: comparison product {cmp['product']}")
    attrs = {a["id"]: a for a in cmp["attributes"]}
    unique([a["id"] for a in cmp["attributes"]], "attribute")
    for a in cmp["attributes"]:
        need(a["stage"] in STAGES, f"ref: attribute {a['id']} stage")
        need(a["datatype"] not in ("enum", "enum_list") or "allowed_values" in a, f"type: attribute {a['id']} is {a['datatype']} without allowed_values")
    for b in pf.get("banks", []):
        need(b in cmp["values"], f"slot: comparison missing bank {b}")
        for at in attrs: need(at in cmp["values"].get(b, {}), f"slot: comparison missing {b}/{at}")
    for b, row in cmp["values"].items():
        need(b in PARTIES, f"ref: comparison bank {b}")
        if b not in focus_ids:
            for at, hist in row.items():
                for a in hist:
                    need(a["basis"] in ("observed", "disclosed", "inferred", "awaiting"),
                         f"basis: competitor {b}/{at} cannot be {a['basis']} — named banks take observed, disclosed or inferred facts only")
        for at, hist in row.items():
            need(at in attrs, f"ref: comparison attribute {at}")
            current = [a for a in hist if not a.get("valid_to")]
            need(len(current) == 1, f"temporal: {b}/{at} must have exactly one current assertion, found {len(current)}")
            for a in hist: check_assertion(a, f"comparison {b}/{at}", attrs.get(at))
    for b, row in cmp["values"].items():
        for at, hist in row.items():
            for a in hist:
                if a.get("supersedes"): need(a["supersedes"] in assertion_ids, f"ref: {b}/{at} supersedes unknown {a['supersedes']}")
    filled_competitor = any(a["basis"] in ("observed", "disclosed", "inferred") for b, row in cmp["values"].items() if b not in focus_ids
                            for hist in row.values() for a in hist if not a.get("valid_to"))
    if filled_competitor:
        need(cmp["governance"]["ci_legal_review"]["status"] in ("pending", "approved"),
             "gate: competitor facts present while comparison legal review is rejected or not started")

if errors:
    print(f"FAIL — {len(errors)} defect(s)"); [print(" -", e) for e in errors[:60]]; sys.exit(1)
n = sum(len(j["moments"]) for j in d["journeys"])
print(f"PASS — {len(d['journeys'])} journey, {n} moments, {len(d['metrics'])} metrics, {len(d['controls'])} controls, "
      f"{sum(len(r) for r in cmp['values'].values()) if cmp else 0} comparison slots")

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
              "duration": isinstance(v, str) and re.fullmatch(r"P(?!$)(\d+(\.\d+)?Y)?(\d+(\.\d+)?M)?(\d+(\.\d+)?W)?(\d+(\.\d+)?D)?(T(?=\d)(\d+(\.\d+)?H)?(\d+(\.\d+)?M)?(\d+(\.\d+)?S)?)?", v or "") is not None,
              "enum": isinstance(v, str), "enum_list": isinstance(v, list)}[dt]
        need(ok, f"type: {where} value {v!r} is not a valid {dt}")
        if ok and dt == "enum_list": need(len(v) == len(set(v)), f"type: {where} lists a value twice")
        if ok and "allowed_values" in attr:
            vals = v if isinstance(v, list) else [v]
            for x in vals: need(x in attr["allowed_values"], f"type: {where} '{x}' not in allowed values")
    if attr and a["basis"] != "awaiting":
        need(a.get("value") is not None or a.get("display"), f"value: {where} has no value and no display wording")
        if a["basis"] == "inferred": need(a.get("confidence") == "low", f"value: {where} is inferred, so confidence must be low")
        if a.get("observed_on"): need(parse_date(a["observed_on"]) <= date.today(), f"temporal: {where} observed_on is in the future")
    return a

# ---------- 3. catalogs ----------
import hashlib, os
for s in d["sources"]:
    if s["kind"] == "mi-report":
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(inst_path)))   # dist/x.json and tests/fixtures/x.json → repo
        if not os.path.exists(os.path.join(repo_root, s["path"])) and os.path.exists(os.path.join(repo_root, "..", s["path"])):
            repo_root = os.path.dirname(repo_root)
        rp = os.path.join(repo_root, s["path"])
        if not os.path.exists(rp): errors.append(f"report: source {s['id']} points to missing file {s['path']}")
        else:
            h = hashlib.sha256(open(rp, "rb").read()).hexdigest()
            need(h == s["sha256"], f"report: {s['path']} changed after ingestion (sha256 mismatch) — reports are immutable")
        need(s["path"].startswith(f"reports/{s['report_version']}/"), f"report: source {s['id']} path is not in its version folder")
# every file every manifest pins, not only the one the report source names
_rr = os.path.dirname(os.path.dirname(os.path.abspath(inst_path)))
if not os.path.isdir(os.path.join(_rr, "reports")) and os.path.isdir(os.path.join(_rr, "..", "reports")): _rr = os.path.dirname(_rr)
import glob as _glob, json as _json
for _mp in sorted(_glob.glob(os.path.join(_rr, "reports", "*", "manifest.json"))):
    _m = _json.load(open(_mp)); _dir = os.path.dirname(_mp)
    for _f in _m.get("files", []):
        _fp = os.path.join(_dir, _f["path"])
        if not os.path.exists(_fp): errors.append(f"report: {_m['report_version']}/{_f['path']} is pinned in the manifest but missing")
        else: need(hashlib.sha256(open(_fp, "rb").read()).hexdigest() == _f["sha256"], f"report: {_m['report_version']}/{_f['path']} changed after it was pinned (sha256 mismatch) — reports are immutable")
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
        if m.get("process") is not None: need(m["process"] in PROCS, f"ref: {w} process {m['process']}")
        unique(m.get("controls", []), f"{w} control ref"); unique(m.get("applications", []), f"{w} app ref")
        for c in m.get("controls", []): need(c in CTRLS, f"ref: {w} control {c}")
        for a in m.get("applications", []): need(a in APPS, f"ref: {w} app {a}")
        for c in m.get("capabilities", []):
            need(c in CAPS, f"ref: {w} capability {c}")
            need(any(c in app_caps.get(a, set()) for a in m.get("applications", [])), f"ref: {w} capability {c} not realized by any of its apps")
        unique([f["id"] for f in m.get("fail_points", [])], f"{w} fail point")
        for k in m.get("kpis", []):
            need(k["metric"] in METS, f"ref: {w} metric {k['metric']}")
            if k.get("actual") is not None:
                mm = metric.get(k["metric"], {})
                need(mm.get("dq_status") == "certified" and mm.get("basis") not in ("sample", "awaiting"),
                     f"metric: {w} shows an actual for {k['metric']}, which is not certified real data")
                need(k.get("period_end") is not None, f"metric: {w} actual for {k['metric']} needs period_end")
        need(set(m["evidence"]) <= LAYERS, f"layer: {w} unknown evidence layer(s) {sorted(set(m['evidence']) - LAYERS)}")
        for L, a in m["evidence"].items(): check_assertion(a, f"{w} evidence.{L}")
    unique([f["id"] for m in j["moments"] for f in m.get("fail_points", [])], "fail point (journey-wide)")
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
        for c in (CTRLS & {c for m in j["moments"] for c in m.get("controls", [])}):
            cc = next(x for x in d["controls"] if x["id"] == c)
            need(cc["grc_control_id"], f"gate: control {c} has no GRC ID")
        for a in d["applications"]:
            if a["app_id"] in {x for m in j["moments"] for x in m.get("applications", [])} and a["layer"] != "external":
                need(a["cmdb_ci"], f"gate: app {a['app_id']} has no CMDB link")
    need(g["ci_legal_review"]["status"] != "rejected" or j["status"] not in GATED, "gate: journey with rejected legal review cannot be in review or published")

# ---------- 4b. journey extras ----------
JIDS = {j["id"] for j in d["journeys"]}
SRCJ = {(j["bank"], j.get("source_journey_id")): j["id"] for j in d["journeys"] if j.get("source_journey_id")}
unique([(j["bank"], j.get("source_journey_id")) for j in d["journeys"] if j.get("source_journey_id")], "MI journey id")
for j in d["journeys"]:
    for ex in j.get("exceptions", []):
        for s in ex.get("source_ids", []): need(s in SOURCES, f"ref: journey {j['id']} exception source {s}")

# line of visibility (ADR-0004): a competitor's backstage is what it discloses or what MI infers, never observed or internal
for j in d["journeys"]:
    if j["bank"] in focus_ids: continue
    for m in j["moments"]:
        a = m.get("evidence", {}).get("process")
        if a: need(a["basis"] in ("disclosed", "inferred"), f"basis: competitor {j['id']} {m['code']} backstage cannot be {a['basis']} (line of visibility)")

# ---------- 4c. MI analytical collections ----------
STAGE_IDS = STAGES
COMPS = {c["id"] for c in d.get("composites", [])}
COMPN = {c["id"]: {st["n"] for st in c["steps"]} for c in d.get("composites", [])}
COMPP = {c["id"]: c["product"] for c in d.get("composites", [])}
JBY = {j["id"]: j for j in d["journeys"]}
CAPFLAGS = {a["id"][9:] for c in d.get("comparisons", []) for a in c["attributes"] if a["id"].startswith("attr-cap-")}
unique([c["id"] for c in d.get("composites", [])], "composite")
for c in d.get("composites", []):
    need(c["product"] in PRODUCTS, f"ref: composite {c['id']} product {c['product']}")
    for st in c["steps"]: need(st["stage"] in STAGE_IDS, f"ref: composite {c['id']} step {st['n']} stage {st['stage']}")
    unique([st["n"] for st in c["steps"]], f"composite {c['id']} step number")
# catalog: each bank's products as marketed, and their sub-products
CAT = d.get("catalog", [])
unique([(p["bank"], p["id"]) for p in CAT], "catalog product")
unique([(p["bank"], sp["id"]) for p in CAT for sp in p["sub_products"]], "catalog sub-product")
SUBOF = {(p["bank"], sp["id"]): p["id"] for p in CAT for sp in p["sub_products"]}
for p in CAT:
    w = f"catalog product {p['bank']}/{p['id']}"
    need(p["bank"] in PARTIES, f"ref: {w} bank {p['bank']}")
    for r in p["rails"]: need(r in PRODUCTS, f"ref: {w} rail {r}")
    for x in p["source_ids"]: need(x in SOURCES, f"ref: {w} source {x}")
    for sp in p["sub_products"]:
        w2 = f"catalog sub-product {p['bank']}/{sp['id']}"
        need(sp["id"].startswith(p["id"] + "-"), f"ref: {w2} is not numbered under its product {p['id']}")
        need(sp["product"] in PRODUCTS, f"ref: {w2} rail product {sp['product']}")
        for x in sp["source_ids"]: need(x in SOURCES, f"ref: {w2} source {x}")
        for ju in sp.get("journeys", []): need(ju in JIDS, f"ref: {w2} journey {ju}")
        for k in sp["capabilities"]: need(k in CAPFLAGS, f"ref: {w2} capability flag {k} is not a comparison question")
for j in d["journeys"]:
    w = f"journey {j['id']}"
    if CAT and j.get("sub_product"):
        need((j["bank"], j["sub_product"]) in SUBOF, f"ref: {w} sub-product {j['sub_product']} is not in the {j['bank']} catalog")
        need(SUBOF.get((j["bank"], j["sub_product"])) == j.get("bank_product"), f"ref: {w} sub-product {j['sub_product']} does not belong to product {j.get('bank_product')}")
    if j.get("composite"):
        need(j["composite"] in COMPS, f"ref: {w} customer journey {j['composite']}")
        need(bool(j.get("composite_match")), f"ref: {w} links a customer journey without saying how (composite_match)")
        if j.get("composite_match") == "rail-segment" and j["composite"] in COMPP:
            need(COMPP[j["composite"]] == j["product"], f"ref: {w} is linked by rail and segment to {j['composite']}, a customer journey on another rail")
LOB = d.get("lines_of_business")
if LOB:
    ids = [l["id"] for l in LOB["lines_of_business"]]; unique(ids, "line of business")
    for l in LOB["lines_of_business"]:
        for x in l["source_ids"]: need(x in SOURCES, f"ref: line of business {l['id']} source {x}")
    focus_products = {p["id"] for p in CAT if p["bank"] == LOB["bank"]}
    unique([a["product"] for a in LOB["assignments"]], "line-of-business assignment")
    for a in LOB["assignments"]:
        need(a["product"] in focus_products, f"ref: line-of-business assignment product {a['product']} is not a {LOB['bank']} catalog product")
        for x in [a["owner"]] + a.get("also", []): need(x in ids, f"ref: line-of-business assignment {a['product']} names unknown line of business {x}")
        need(a["owner"] not in a.get("also", []), f"ref: line-of-business assignment {a['product']} lists its owner under also")
    for p in sorted(focus_products - {a["product"] for a in LOB["assignments"]}): errors.append(f"ref: {LOB['bank']} product {p} has no owning line of business")
unique([f["id"] for f in d.get("findings", [])], "finding")
for f in d.get("findings", []):
    w = f"finding {f['id']}"
    need(f["bank"] in PARTIES, f"ref: {w} bank {f['bank']}")
    if f.get("journey"):
        need(f["journey"] in JIDS, f"ref: {w} journey {f['journey']}")
        fj = JBY.get(f["journey"])
        if fj:
            need(fj["bank"] == f["bank"], f"ref: {w} bank {f['bank']} differs from its journey's bank {fj['bank']}")
            if f.get("product"): need(fj["product"] == f["product"], f"ref: {w} product {f['product']} differs from its journey's product {fj['product']}")
            if f.get("step") is not None:
                ok = 1 <= f["step"] <= len(fj["moments"])
                need(ok, f"ref: {w} step {f['step']} is outside its journey (1..{len(fj['moments'])})")
                if ok:
                    actual = fj["moments"][f["step"] - 1]["stage"]
                    need(f.get("step_stage", f.get("stage")) == actual, f"ref: {w} stage {f.get('step_stage', f.get('stage'))} is not the stage of step {f['step']} ({actual}); a best-practice stage that differs goes in stage, the step's in step_stage")
                    if f.get("step_stage"): need(f["step_stage"] != f.get("stage"), f"ref: {w} step_stage repeats stage")
    if f.get("composite") and f.get("composite_step") is not None and f["composite"] in COMPN:
        need(f["composite_step"] in COMPN[f["composite"]], f"ref: {w} composite step {f['composite_step']} is not in {f['composite']}")
    if f.get("product"): need(f["product"] in PRODUCTS, f"ref: {w} product {f['product']}")
    if f.get("stage"): need(f["stage"] in STAGE_IDS, f"ref: {w} stage {f['stage']}")
    if f.get("composite"): need(f["composite"] in COMPS, f"ref: {w} composite {f['composite']}")
    need((f["type"] == "strength") == f["id"].startswith("STR-"), f"type: {w} strength records must use STR- ids and gaps GAP- ids")
    for s in f["source_ids"]: need(s in SOURCES, f"ref: {w} source {s}")
for o in d.get("observations", []): need(o["bank"] in PARTIES, f"ref: observation bank {o['bank']}")
unique([(v["bank"], v["id"]) for v in d.get("verifications", [])], "verification")
for v in d.get("verifications", []): need(v["bank"] in PARTIES, f"ref: verification {v['id']} bank {v['bank']}")
unique([(x["bank"], x["network"]) for x in d.get("participation", [])], "participation")
for x in d.get("participation", []):
    need(x["bank"] in PARTIES, f"ref: participation bank {x['bank']}")
    for s in x.get("source_ids", []): need(s in SOURCES, f"ref: participation {x['bank']}/{x['network']} source {s}")
unique([r["bank"] for r in d.get("rankings", [])], "ranking bank"); unique([r["rank"] for r in d.get("rankings", [])], "ranking rank")
for r in d.get("rankings", []):
    need(r["bank"] in PARTIES, f"ref: ranking bank {r['bank']}")
    need(0 <= r["overall_index"] <= 100, f"range: ranking {r['bank']} overall_index {r['overall_index']} is outside 0-100")
    if r.get("domestic_core_index") is not None: need(0 <= r["domestic_core_index"] <= 100, f"range: ranking {r['bank']} domestic_core_index outside 0-100")
    if r.get("coverage") is not None: need(0 <= r["coverage"] <= 1, f"range: ranking {r['bank']} coverage outside 0-1")
    for k, v in (r.get("rail_means") or {}).items():
        need(k in PRODUCTS, f"ref: ranking {r['bank']} rail {k}")
        if v is not None: need(0 <= v <= 4, f"range: ranking {r['bank']} {k} mean {v} is outside 0-4")
REPORTS = {s["report_version"] for s in d["sources"] if s["kind"] == "mi-report"}
for coll in ("findings", "composites", "observations", "verifications", "participation", "rankings"):
    for x in d.get(coll, []):
        need(x["report_version"] in REPORTS or not REPORTS, f"ref: {coll} record cites report {x['report_version']}, which is not an ingested mi-report source")

# ---------- 5. portfolio and comparison ----------
pf = d.get("portfolio", {})
if pf:
    need(pf["focus_bank"] in focus_ids, "portfolio: focus_bank must be the party with role focus")
    need(pf["focus_bank"] in pf["banks"], "portfolio: focus_bank must be in banks")
    unique(pf["banks"], "portfolio bank"); unique(pf["products"], "portfolio product")
    for b in pf["banks"]: need(b in PARTIES, f"ref: portfolio bank {b}")
    for p in pf["products"]: need(p in PRODUCTS, f"ref: portfolio product {p}")
CMPS = d.get("comparisons", [])
unique([c["product"] for c in CMPS], "comparison product")
for cmp in CMPS:
    P = cmp["product"]
    need(P in PRODUCTS, f"ref: comparison product {P}")
    need(P in pf.get("products", []), f"ref: comparison product {P} is not in portfolio.products")
    attrs = {a["id"]: a for a in cmp["attributes"]}
    unique([a["id"] for a in cmp["attributes"]], f"{P} attribute")
    for a in cmp["attributes"]:
        need(a["stage"] in STAGES, f"ref: {P} attribute {a['id']} stage")
        need(a["datatype"] not in ("enum", "enum_list") or "allowed_values" in a, f"type: attribute {a['id']} is {a['datatype']} without allowed_values")
    for b, row in cmp["values"].items():
        for at, hist in row.items():
            if at.startswith("attr-score-"):
                for x in hist:
                    if x.get("basis") != "awaiting": need(isinstance(x.get("value"), int) and 0 <= x["value"] <= 4, f"range: {P} {b}/{at} score {x.get('value')!r} is outside the 0-4 rubric")
    for b in pf.get("banks", []):
        need(b in cmp["values"], f"slot: {P} comparison missing bank {b}")
        for at in attrs: need(at in cmp["values"].get(b, {}), f"slot: {P} comparison missing {b}/{at}")
    for b, row in cmp["values"].items():
        need(b in PARTIES, f"ref: {P} comparison bank {b}")
        if b not in focus_ids:
            for at, hist in row.items():
                for a in hist:
                    need(a["basis"] in ("observed", "disclosed", "inferred", "awaiting"),
                         f"basis: {P} competitor {b}/{at} cannot be {a['basis']} — named banks take observed, disclosed or inferred facts only")
        for at, hist in row.items():
            need(at in attrs, f"ref: {P} comparison attribute {at}")
            current = [a for a in hist if not a.get("valid_to")]
            need(len(current) == 1, f"temporal: {P} {b}/{at} must have exactly one current assertion, found {len(current)}")
            for a in hist: check_assertion(a, f"{P} comparison {b}/{at}", attrs.get(at))
    filled_competitor = any(a["basis"] in ("observed", "disclosed", "inferred") for b, row in cmp["values"].items() if b not in focus_ids
                            for hist in row.values() for a in hist if not a.get("valid_to"))
    if filled_competitor:
        need(cmp["governance"]["ci_legal_review"]["status"] in ("pending", "approved"),
             f"gate: {P} competitor facts present while comparison legal review is rejected or not started")

for cmp in CMPS:
    P = cmp["product"]
    for b, row in cmp["values"].items():
        for at, hist in row.items():
            for a in hist:
                if a.get("supersedes"): need(a["supersedes"] in assertion_ids, f"ref: {P} {b}/{at} supersedes unknown {a['supersedes']}")

if errors:
    print(f"FAIL — {len(errors)} defect(s)"); [print(" -", e) for e in errors[:60]]; sys.exit(1)
n = sum(len(j["moments"]) for j in d["journeys"])
print(f"PASS — {len(d['journeys'])} journey, {n} moments, {len(d['metrics'])} metrics, {len(d['controls'])} controls, "
      f"{sum(len(r) for c in CMPS for r in c['values'].values())} comparison slots across {len(CMPS)} product(s)")

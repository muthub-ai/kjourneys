#!/usr/bin/env python3
"""Import a market-intelligence (MI) data workbook into kjourneys.

  python3 tools/import_mi_workbook.py reports/<version> [--dry-run]

Reads the workbook named in reports/<version>/manifest.json ("workbook"), verifies its sha256, and writes:

  registries/sources.json                 MI source registry, ids src-<bank>-<source id>, e.g. src-wells-fargo-s990
  registries/products.json                each rail's product gets its MI journeys listed
  data/journeys/<bank>/mi-<id>.json       every MI journey: steps → moments, with exceptions, notifications, status
  data/findings/<bank>.json               gaps and strengths
  data/composites/<product>.json          best-in-class composite journeys
  data/observations/<bank>.json           strengths, weaknesses, differentiators, recent changes, open questions
  data/verifications/<bank>.json          the verification debate (challenge → verdict)
  data/participation.json                 network participation (Zelle, RTP, FedNow, push-to-card, Paze)
  data/rankings.json                      overall index, coverage and rail means per bank
  data/comparisons/<product>/             questions per product (16 capability flags, 9 stage scores) + bank slots
  reports/<version>/extract/<product>/<bank>.json   comparison facts, applied by tools/ingest_mi.py

Everything is regenerated from the workbook on every run, so rerunning is safe; git keeps history.
Comparison facts go through ingest, which keeps assertion history across report versions.
Evidence mapping (MI → kjourneys basis, confidence):
  CONFIRMED_BANK → disclosed/high · OBSERVED_SESSION → observed/high · THIRD_PARTY → disclosed/medium
  COMMUNITY → inferred/low · INFERRED → inferred/low · UNKNOWN → inferred/low (comparison cells: left awaiting)
The original MI level is kept on every record as x-mi_evidence.
"""
import argparse, glob, hashlib, json, os, re, shutil, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def jl(p): return json.load(open(os.path.join(ROOT, p)))
def die(msg): sys.exit(f"IMPORT FAIL — {msg}")

ap = argparse.ArgumentParser(); ap.add_argument("report_dir"); ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()
rdir = os.path.abspath(args.report_dir); version = os.path.basename(rdir.rstrip("/"))
mpath = os.path.join(rdir, "manifest.json")
if not os.path.isfile(mpath): die(f"{args.report_dir}/manifest.json not found")
man = json.load(open(mpath))
wbname = man.get("workbook") or next(iter(sorted(os.path.basename(p) for p in glob.glob(os.path.join(rdir, "*.xlsx")))), None)
if not wbname: die("no workbook: set \"workbook\" in the manifest or add one .xlsx to the report folder")
wbpath = os.path.join(rdir, wbname)
if not os.path.isfile(wbpath): die(f"workbook {wbname} not found in {args.report_dir}")
listed = {f["path"]: f["sha256"] for f in man.get("files", [])}
sha = hashlib.sha256(open(wbpath, "rb").read()).hexdigest()
if wbname in listed and listed[wbname] != sha: die(f"{wbname} sha256 does not match the manifest — reports are immutable")

try:
    import openpyxl
except ImportError:
    die("openpyxl is not installed: pip install -r requirements.txt")
wb = openpyxl.load_workbook(wbpath, read_only=True, data_only=True)
X = {}
for ws in wb.worksheets:
    rows = list(ws.iter_rows(values_only=True))
    hi = next((i for i, r in enumerate(rows[:10]) if sum(1 for c in r if c not in (None, "")) >= 3), 0)
    hdr = [str(c) if c is not None else f"col{j}" for j, c in enumerate(rows[hi])] if rows else []
    X[ws.title] = [dict(zip(hdr, r)) for r in rows[hi + 1:] if any(c not in (None, "") for c in r)]
NEED = ["Banks", "Products", "SubProducts", "Capabilities", "Journeys", "Steps", "Exceptions", "Notifications",
        "RailParticipation", "Composites", "Gaps", "Scores", "ScoreTotals", "Observations", "Verification", "Sources"]
missing = [s for s in NEED if s not in X]
if missing: die(f"workbook is missing sheet(s) {missing}")

# ---------- vocabularies ----------
problems = []
parties = {p["id"]: p for p in jl("registries/parties.json")}
products = jl("registries/products.json")
RAIL = {p["rail"]: p["id"] for p in products if p.get("rail")}
stages = [s["id"] for s in jl("registries/codelists.json")["stages"]]
STAGE = {s.replace("-", "_").upper(): s for s in stages}
EVID = {"CONFIRMED_BANK": ("disclosed", "high"), "OBSERVED_SESSION": ("observed", "high"), "THIRD_PARTY": ("disclosed", "medium"),
        "COMMUNITY": ("inferred", "low"), "INFERRED": ("inferred", "low"), "UNKNOWN": ("inferred", "low")}
CHANNEL = {"MOBILE_APP": "mobile-app", "WEB": "web", "BRANCH": "branch", "PHONE": "phone", "ATM": "atm",
           "VOICE_CHAT_ASSISTANT": "voice-chat-assistant", "API_TREASURY_PORTAL": "api-treasury-portal"}
SRC_KIND = {"bank_site": "bank-site", "bank_help_center": "bank-help-center", "press": "press", "bank_pdf": "bank-pdf",
            "bank_video": "bank-video", "network_operator": "network-operator", "app_store": "app-store", "regulator": "regulator",
            "community": "community", "observed_session": "observed-session", "analyst": "analyst", "other": "other"}
ACCESS = {"fetched": "fetched", "blocked": "blocked", "summary_only": "summary-only", "observed": "observed"}
OBS = {"strengths": "strength", "weaknesses": "weakness", "notable_differentiators": "differentiator",
       "recent_changes_2025_2026": "recent-change", "open_questions": "open-question"}
FLAG_STAGE = {"recurring": "manage", "scheduled_future_dated": "initiate", "request_money": "initiate", "split": "initiate",
              "qr_code": "initiate", "contact_sync": "set-up", "cancel_before_send": "manage", "status_tracking": "execute-track",
              "push_notifications": "confirm-complete", "email_sms_notifications": "confirm-complete",
              "scam_warning_interstitial": "review-authorize", "step_up_auth": "review-authorize",
              "dual_approval_smb": "review-authorize", "international": "initiate", "same_day": "execute-track", "instant": "execute-track"}
FLAG_NAME = {"recurring": "Recurring payments", "scheduled_future_dated": "Schedule for a future date", "request_money": "Request money",
             "split": "Split a payment", "qr_code": "QR code", "contact_sync": "Pay from phone contacts", "cancel_before_send": "Cancel before it is sent",
             "status_tracking": "Status tracking", "push_notifications": "Push notifications", "email_sms_notifications": "Email or text notifications",
             "scam_warning_interstitial": "Scam warning before sending", "step_up_auth": "Step-up authentication",
             "dual_approval_smb": "Dual approval (business)", "international": "International", "same_day": "Same-day delivery", "instant": "Instant delivery"}
received = man.get("received_at") or f"{version[:10]}T12:00:00-06:00"
REPORT_SRC = f"src-mi-{version}"          # the report itself; tools/ingest_mi.py registers it with its sha256
AS_OF = version[:10]
MI = "process:mi-session"
def s(v): return None if v in (None, "") else str(v).strip()
def bank_ok(b, where):
    if b not in parties: problems.append(f"{where}: bank '{b}' is not in registries/parties.json"); return False
    return True
def rail_ok(r, where):
    if r not in RAIL: problems.append(f"{where}: rail '{r}' has no product in registries/products.json"); return False
    return True
def split(v): return [x.strip() for x in re.split(r"[;,]", str(v or "")) if x.strip()]
def ev(code):
    if code not in EVID: problems.append(f"unknown evidence level '{code}'"); return ("inferred", "low")
    return EVID[code]

for b in X["Banks"]: bank_ok(b["bank_slug"], "Banks")
# ---------- sources ----------
src_rows = {}
for r in X["Sources"]:
    if not bank_ok(r["bank_slug"], "Sources"): continue
    sid = f"src-{r['bank_slug']}-{str(r['source_id']).lower()}"
    acc = s(r.get("Accessed"))
    src_rows[(r["bank_slug"], str(r["source_id"]))] = {
        "id": sid, "kind": SRC_KIND.get(r.get("Type"), "other"), "title": s(r.get("Title")) or sid, "origin": s(r.get("Publisher")) or "",
        "url": s(r.get("URL")), "retrieved_at": f"{acc[:10]}T12:00:00-06:00" if acc and re.match(r"\d{4}-\d{2}-\d{2}", acc) else received,
        "bank": r["bank_slug"], "local_id": str(r["source_id"]), "publisher": s(r.get("Publisher")),
        "access_status": ACCESS.get(r.get("Access status")), "notes": s(r.get("Notes")), "report_version": version}
def srcs(bank, refs, where):
    out = []
    for x in split(refs):
        if (bank, x) in src_rows: out.append(src_rows[(bank, x)]["id"])
        else: problems.append(f"{where}: source {x} is not in the Sources sheet for {bank}")
    return list(dict.fromkeys(out))

# ---------- journeys ----------
gov = {"owner": "role:ci-study-lead", "steward": None, "classification": "internal", "contains_pii": False, "mnpi": False,
       "ci_legal_review": {"status": "pending", "reviewer": None, "date": None}, "retention_class": None,
       "access_policy": "Public-source competitive intelligence; legal review before external sharing"}
steps_by = defaultdict(list)
for st in X["Steps"]: steps_by[(st["bank_slug"], st["journey_id"])].append(st)
exc_by = defaultdict(list)
for e in X["Exceptions"]: exc_by[(e["bank_slug"], e["journey_id"])].append(e)
not_by = defaultdict(list)
for n in X["Notifications"]: not_by[(n["bank_slug"], n["journey_id"])].append(n)
def tri(v):
    v = s(v); return True if v and v.lower() == "yes" else False if v and v.lower() == "no" else None
journeys, jurn = {}, {}
for r in X["Journeys"]:
    b, jid = r["bank_slug"], str(r["journey_id"]); where = f"Journeys {jid}"
    if not bank_ok(b, where) or not rail_ok(r["Rail"], where): continue
    local = jid.lower(); urn = f"urn:kos:journey:{b}:{local}"; jurn[(b, jid)] = urn
    basis, conf = ev(r.get("Overall evidence") or "UNKNOWN")
    moments = []
    for st in sorted(steps_by[(b, jid)], key=lambda x: x["Step #"]):
        n = int(st["Step #"]); code = f"M{n:02d}"; w = f"Steps {jid}#{n}"
        if st["Stage"] not in STAGE: problems.append(f"{w}: unknown stage {st['Stage']}"); continue
        sb, sc = ev(st.get("Evidence") or "UNKNOWN"); sids = srcs(b, st.get("Sources"), w)
        actor = str(st.get("Actor") or "CUSTOMER").lower().replace("_", "-")
        action = s(st.get("Action")) or ""
        is_customer = actor in ("customer", "recipient")
        frontstage = s(st.get("System behavior")) or ("" if is_customer else action)
        tps = [{"channel": CHANNEL.get(st.get("Channel"), "web"), "screen": s(st.get("Touchpoint"))}] if st.get("Channel") else []
        title = re.sub(r"\s+", " ", action)
        if len(title) > 72: title = title[:72].rsplit(" ", 1)[0] + "…"
        a = lambda: {"basis": sb, "source_ids": [REPORT_SRC] + sids, "asserted_by": MI, "asserted_at": received, "confidence": sc,
                     "x-mi_evidence": st.get("Evidence") or "UNKNOWN"}
        evidence = {}
        if is_customer and action: evidence["action"] = a()
        if tps: evidence["touchpoint"] = a()
        if frontstage: evidence["frontstage"] = a()
        m = {"id": f"urn:kos:moment:{b}:{local}:{code.lower()}", "code": code, "stage": STAGE[st["Stage"]], "title": title or code,
             "customer_action": action if is_customer else None, "touchpoints": tps, "frontstage": frontstage, "actor": actor,
             "decision": s(st.get("Decision point")), "notification": s(st.get("Notification")), "source_step": n, "evidence": evidence}
        if s(st.get("Friction / pain point")):
            m["fail_points"] = [{"id": f"fp-{b}-{local}-{n}", "text": s(st["Friction / pain point"])}]; evidence["fail_points"] = a()
        moments.append(m)
    if not moments: problems.append(f"{where}: journey has no steps"); continue
    j = {"id": urn, "title": s(r["Title"]), "bank": b, "product": RAIL[r["Rail"]], "persona": s(r.get("Persona")) or "Not stated",
         "segment": str(r.get("Segment") or "consumer").replace("_", "-"), "customer_goal": s(r.get("Job to be done")) or s(r["Title"]),
         "version": "1.0.0", "as_of": AS_OF, "status": "draft", "basis": basis, "governance": gov, "stages": stages, "moments": moments,
         "source_journey_id": jid, "report_version": version, "sub_product": s(r.get("sub_product_id")),
         "channels": {"entry": [CHANNEL.get(c, c.lower()) for c in split(r.get("Entry channels"))],
                      "other": [CHANNEL.get(c, c.lower()) for c in split(r.get("Other channels"))]},
         "status_tracking": {"where": s(r.get("Status visible where")), "states": split(r.get("Status states")),
                             "basis": ev(r.get("Status evidence") or "UNKNOWN")[0]},
         "exceptions": [{"trigger": s(e["Trigger"]) or "Not stated", "customer_experience": s(e.get("Customer experience")),
                         "bank_handling": s(e.get("Bank handling")), "resolution": s(e.get("Resolution")),
                         "basis": ev(e.get("Evidence") or "UNKNOWN")[0], "source_ids": [REPORT_SRC] + srcs(b, e.get("Sources"), f"Exceptions {jid}")}
                        for e in exc_by[(b, jid)]],
         "notifications": [{"event": s(n["Event"]) or "Not stated", "channels": split(n.get("Channels")), "configurable": tri(n.get("Configurable")),
                            "basis": ev(n.get("Evidence") or "UNKNOWN")[0]} for n in not_by[(b, jid)]],
         "assessment": s(r.get("Analyst assessment")), "x-mi_evidence": r.get("Overall evidence") or "UNKNOWN"}
    journeys[(b, local)] = j

# ---------- findings, composites, observations, verifications, participation, rankings ----------
jrail = {(r["bank_slug"], str(r["journey_id"])): r["Rail"] for r in X["Journeys"]}
findings = defaultdict(list)
for g in X["Gaps"]:
    b = g["bank_slug"]; w = f"Gaps {g['gap_id']}"
    if not bank_ok(b, w): continue
    jid = s(g.get("journey_id")); rail = s(g.get("Rail")) or jrail.get((b, jid))
    basis, _ = ev(g.get("Evidence") or "UNKNOWN")
    findings[b].append({"id": g["gap_id"], "bank": b, "journey": jurn.get((b, jid)) if jid else None, "product": RAIL.get(rail) if rail else None,
        "stage": STAGE.get(g.get("Stage")), "step": int(g["Step #"]) if g.get("Step #") not in (None, "") else None,
        "type": str(g["Gap type"]).lower().replace("_", "-"), "severity": str(g["Severity"]).lower(), "description": s(g["Description"]),
        "composite": s(g.get("Composite")), "composite_step": int(g["Composite step"]) if g.get("Composite step") not in (None, "") else None,
        "reference_banks": s(g.get("Reference bank(s)")), "basis": basis, "source_ids": [REPORT_SRC] + srcs(b, g.get("Sources"), w),
        "frameworks": s(g.get("Rolls up to (framework)")), "report_version": version, "x-mi_evidence": g.get("Evidence") or "UNKNOWN"})
comps = defaultdict(lambda: {"steps": []})
for c in X["Composites"]:
    if not rail_ok(c["Rail"], f"Composites {c['composite_id']}"): continue
    k = c["composite_id"]; comps[k].update({"id": k, "title": s(c["Title"]), "product": RAIL[c["Rail"]], "segment": s(c.get("Segment")),
                                            "direction": s(c.get("Direction")), "report_version": version})
    comps[k]["steps"].append({"stage": STAGE.get(c["Stage"], "support"), "n": int(c["Step #"]), "action": s(c["Action"]) or "",
        "actor": s(c.get("Actor")), "channel": s(c.get("Channel")), "job_step": s(c.get("JTBD job step")), "moment_of_truth": s(c.get("Moment of truth")),
        "derived_from": s(c.get("Derived from (bank:journey#step)")), "rationale": s(c.get("Rationale"))})
by_product_comp = defaultdict(list)
for c in comps.values(): c["steps"].sort(key=lambda x: x["n"]); by_product_comp[c["product"]].append(c)
observations = defaultdict(list)
for o in X["Observations"]:
    if bank_ok(o["bank_slug"], "Observations"):
        observations[o["bank_slug"]].append({"bank": o["bank_slug"], "type": OBS.get(o["Type"], "open-question"), "text": s(o["Observation"]), "report_version": version})
verifs = defaultdict(list)
for v in X["Verification"]:
    if bank_ok(v["bank_slug"], "Verification"):
        verifs[v["bank_slug"]].append({"id": s(v["challenge_id"]), "bank": v["bank_slug"], "target_type": s(v.get("Target type")), "target": s(v.get("Target")),
            "challenge_type": s(v.get("Challenge type")), "claim": s(v.get("Original claim")), "finding": s(v.get("Reviewer finding")),
            "verdict": str(v["Verdict"]).lower(), "resolution": s(v.get("Resolution")), "evidence": s(v.get("Evidence")),
            "reviewer": s(v.get("Reviewer model")), "report_version": version})
participation = [{"bank": p["bank_slug"], "network": str(p["Rail / network"]).replace("_", "-"), "participates": tri(p["Participates"]),
                  "note": s(p.get("Scope note")), "basis": ev(p.get("Evidence") or "UNKNOWN")[0],
                  "source_ids": [REPORT_SRC] + srcs(p["bank_slug"], p.get("Sources"), "RailParticipation"), "report_version": version}
                 for p in X["RailParticipation"] if bank_ok(p["bank_slug"], "RailParticipation")]
rankings = []
for r in X["ScoreTotals"]:
    if not bank_ok(r["bank_slug"], "ScoreTotals"): continue
    means = {RAIL[k.split(" mean")[0]]: v for k, v in r.items() if k.endswith("mean (0-4)") and k.split(" mean")[0] in RAIL}
    rankings.append({"bank": r["bank_slug"], "rank": int(r["Rank"]), "overall_index": float(r["Overall index (0-100)"]),
        "domestic_core_index": r.get("Domestic-core index"), "coverage": r.get("Scored cell coverage"), "rail_means": means, "report_version": version})

# ---------- comparisons: questions + facts ----------
caps_by = defaultdict(list)       # (bank, product) -> capability rows
sub_ev = {(r["bank_slug"], r["sub_product_id"]): r for r in X["SubProducts"]}
FLAGS = list(FLAG_STAGE)
for c in X["Capabilities"]:
    if bank_ok(c["bank_slug"], "Capabilities") and rail_ok(c["Rail"], f"Capabilities {c['sub_product_id']}"):
        caps_by[(c["bank_slug"], RAIL[c["Rail"]])].append(c)
scores_by = defaultdict(dict)     # (bank, product) -> {stage: row}
for r in X["Scores"]:
    if bank_ok(r["bank_slug"], "Scores") and rail_ok(r["Rail"], "Scores") and r["Stage"] in STAGE:
        scores_by[(r["bank_slug"], RAIL[r["Rail"]])][STAGE[r["Stage"]]] = r
cmp_products = sorted({p for _, p in caps_by} | {p for _, p in scores_by})
scored = {p for _, p in scores_by}
rubric = "MI rubric: 4 sets the reference, 3 at parity, 2 material friction, 1 only via channel switch or a critical/high gap, 0 absent (evidenced); U unknown is left awaiting"
def attributes_for(p):
    out = [{"id": f"attr-cap-{f.replace('_', '-')}", "stage": FLAG_STAGE[f], "name": FLAG_NAME[f], "datatype": "boolean", "unit": None,
            "normalization": "True if any of the bank's sub-products on this rail has it (MI Capabilities sheet); false only when every one is No; otherwise awaiting"}
           for f in FLAGS]
    if p in scored:
        out += [{"id": f"attr-score-{st}", "stage": st, "name": f"Stage score: {st.replace('-', ' ')}", "datatype": "integer", "unit": "score 0-4",
                 "normalization": rubric} for st in stages]
    return out
def flag_value(v):
    v = s(v)
    if v is None: return None
    lv = v.lower()
    if lv == "yes": return (True, None)
    if lv in ("no", "none observed", "none"): return (False, None)
    if lv in ("unknown", "n/a", "na", "u"): return None
    return (True, v)                                  # free-text detail means present, with detail
extracts = defaultdict(lambda: defaultdict(list))   # product -> bank -> facts
for (b, p), rows in caps_by.items():
    for f in FLAGS:
        vals = [(flag_value(r.get(f)), r) for r in rows]
        yes = [(v, r) for v, r in vals if v and v[0]]; no = [(v, r) for v, r in vals if v and not v[0]]
        if yes: value, contrib = True, yes
        elif no and len(no) == len(vals): value, contrib = False, no
        else: continue
        evs = [sub_ev.get((b, r["sub_product_id"]), {}).get("Evidence") or "UNKNOWN" for _, r in contrib]
        order = ["CONFIRMED_BANK", "OBSERVED_SESSION", "THIRD_PARTY", "COMMUNITY", "INFERRED", "UNKNOWN"]
        best = min(evs, key=lambda e: order.index(e) if e in order else 9)
        basis, conf = ev(best)
        sids = list(dict.fromkeys(x for _, r in contrib for x in srcs(b, sub_ev.get((b, r["sub_product_id"]), {}).get("Sources"), f"SubProducts {r['sub_product_id']}")))
        details = [d for (v, _) in contrib for d in [v[1]] if d]
        fact = {"attribute": f"attr-cap-{f.replace('_', '-')}", "value": value, "basis": basis, "confidence": conf, "observed_on": AS_OF,
                "source_ids": sids, "evidence": {"report_ref": f"Capabilities sheet: {', '.join(r['sub_product_id'] for _, r in contrib)}", "mi_level": best}}
        if details: fact["display"] = ("Yes — " if value else "No — ") + "; ".join(dict.fromkeys(details))[:300]
        extracts[p][b].append(fact)
for (b, p), byst in scores_by.items():
    for st, r in byst.items():
        sc = str(r["Score (0-4, U=unknown)"]).strip()
        if sc.upper() == "U" or not sc.isdigit(): continue
        basis, conf = ev(r.get("Evidence") or "UNKNOWN")
        extracts[p][b].append({"attribute": f"attr-score-{st}", "value": int(sc), "display": f"{sc} of 4", "basis": basis, "confidence": conf,
                               "observed_on": AS_OF, "source_ids": [], "evidence": {"quote": (s(r.get("Rationale")) or "")[:600], "report_ref": "Scores sheet",
                                                                          "mi_level": r.get("Evidence") or "UNKNOWN"}})

if problems:
    print(f"IMPORT FAIL — {len(problems)} problem(s), nothing written"); [print(" -", p) for p in problems[:40]]; sys.exit(1)

summary = (f"{version}: {len(src_rows)} sources, {len(journeys)} journeys ({sum(len(j['moments']) for j in journeys.values())} steps), "
           f"{sum(map(len, findings.values()))} findings, {len(comps)} composites, {sum(map(len, observations.values()))} observations, "
           f"{sum(map(len, verifs.values()))} verifications, {len(participation)} participation rows, {len(rankings)} rankings, "
           f"{len(cmp_products)} product comparisons, {sum(len(f) for bb in extracts.values() for f in bb.values())} comparison facts")
print(summary)
if args.dry_run: print("dry run — nothing written"); sys.exit(0)

# ---------- write ----------
def jd(rel, o):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True); tmp = p + ".tmp"
    with open(tmp, "w") as f: json.dump(o, f, ensure_ascii=False, indent=1); f.write("\n")
    os.replace(tmp, p)
sources = [x for x in jl("registries/sources.json") if not (x.get("report_version") == version and x.get("kind") != "mi-report")]
primary_file = next((f for f in sorted(os.listdir(rdir)) if f.endswith(".html")), wbname)
report_source = {"id": REPORT_SRC, "kind": "mi-report", "title": man.get("title") or f"Market-intelligence report {version}",
                 "origin": man.get("produced_by", MI), "url": None, "retrieved_at": received, "path": f"reports/{version}/{primary_file}",
                 "sha256": hashlib.sha256(open(os.path.join(rdir, primary_file), "rb").read()).hexdigest(), "report_version": version}
sources = [x for x in sources if x["id"] != REPORT_SRC]
jd("registries/sources.json", sources + [report_source] + list(src_rows.values()))
for old in glob.glob(os.path.join(ROOT, "data/journeys/*/mi-*.json")): os.remove(old)
for (b, local), j in journeys.items(): jd(f"data/journeys/{b}/mi-{local}.json", j)
mi_urns = {j["id"] for j in journeys.values()}
for p in products:
    p["journeys"] = [u for u in p.get("journeys", []) if u not in mi_urns and not re.search(r":[a-z0-9]+-j\d+$", u)]
    p["journeys"] += sorted(j["id"] for j in journeys.values() if j["product"] == p["id"])
jd("registries/products.json", products)
for folder, data in [("findings", findings), ("observations", observations), ("verifications", verifs), ("composites", by_product_comp)]:
    for old in glob.glob(os.path.join(ROOT, f"data/{folder}/*.json")): os.remove(old)
    for k, v in data.items(): jd(f"data/{folder}/{k}.json", v)
jd("data/participation.json", participation)
jd("data/rankings.json", sorted(rankings, key=lambda r: r["rank"]))
pf = jl("data/portfolio.json")
for p in cmp_products:
    cpath = f"data/comparisons/{p}/comparison.json"
    attrs = attributes_for(p)
    comp = jl(cpath) if os.path.exists(os.path.join(ROOT, cpath)) else {"product": p, "governance": gov, "attributes": []}
    have = {a["id"] for a in comp["attributes"]}; comp["attributes"] += [a for a in attrs if a["id"] not in have]
    jd(cpath, comp)
    for b in pf["banks"]:
        vp = f"data/comparisons/{p}/values/{b}.json"
        vf = jl(vp) if os.path.exists(os.path.join(ROOT, vp)) else {"bank": b, "product": p, "values": {}}
        for a in comp["attributes"]:
            vf["values"].setdefault(a["id"], [{"basis": "awaiting", "source_ids": [], "asserted_by": None, "asserted_at": None, "observed_on": None,
                "valid_to": None, "verified_by": None, "verified_at": None, "id": f"urn:kos:assertion:{b}:{p}:{a['id'][5:]}:1"}])
        jd(vp, vf)
xdir = os.path.join(rdir, "extract"); shutil.rmtree(xdir, ignore_errors=True)
for p, banks in extracts.items():
    for b, facts in banks.items():
        os.makedirs(os.path.join(xdir, p), exist_ok=True)
        json.dump({"bank": b, "product": p, "facts": facts}, open(os.path.join(xdir, p, f"{b}.json"), "w"), ensure_ascii=False, indent=1)
# finalize the manifest: every deliverable checksum-pinned, products listed
files = []
for f in sorted(os.listdir(rdir)):
    fp = os.path.join(rdir, f)
    if os.path.isfile(fp) and f != "manifest.json":
        kind = "data" if f.endswith(".xlsx") else "report"
        files.append({"path": f, "sha256": hashlib.sha256(open(fp, "rb").read()).hexdigest(), "kind": kind})
primary = [f for f in files if f["path"].endswith(".html")] + [f for f in files if not f["path"].endswith(".html")]
man.update({"products": sorted(extracts), "workbook": wbname, "files": primary})
man.pop("product", None)
man["notes"] = "Imported with tools/import_mi_workbook.py; " + summary
json.dump(man, open(mpath, "w"), ensure_ascii=False, indent=2); open(mpath, "a").write("\n")
print("written — now run: scripts/refresh.sh " + os.path.relpath(rdir, ROOT))

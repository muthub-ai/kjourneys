#!/usr/bin/env python3
"""Import a market-intelligence (MI) data workbook into kjourneys.

  python3 tools/import_mi_workbook.py reports/<version> [--dry-run | --check] [--repin] [--replace]

  --dry-run   read and check the workbook, print what would be written, write nothing
  --check     regenerate everything in memory and fail if the repo differs (CI uses this: data/ must equal f(workbook))
  --repin     accept report files whose sha256 no longer matches the manifest (only before first ingest)
  --replace   allow replacing MI data imported from a different report version (v1 IDs are not version-scoped)

Reads the workbook named in reports/<version>/manifest.json ("workbook"), verifies its sha256, and writes:

  registries/sources.json                 MI source registry, ids src-<bank>-<source id>, e.g. src-wells-fargo-s990
  registries/products.json                each rail's product gets its MI journeys listed
  data/journeys/<bank>/mi-<id>.json       every MI journey: steps → moments, with exceptions, notifications, status
  data/findings/<bank>.json               gaps and strengths
  data/composites/<product>.json          best-in-class composite journeys (the customer journeys)
  data/catalog/<bank>.json                each bank's products as marketed, their sub-products and per-sub-product capability flags
  data/observations/<bank>.json           strengths, weaknesses, differentiators, recent changes, open questions
  data/verifications/<bank>.json          the verification debate (challenge → verdict)
  data/participation.json                 network participation (Zelle, RTP, FedNow, push-to-card, Paze)
  data/rankings.json                      overall index, coverage and rail means per bank
  data/comparisons/<product>/             questions per product (16 capability flags, 9 stage scores) + bank slots
  reports/<version>/extract/<product>/<bank>.json   comparison facts, applied by tools/ingest_mi.py

Each bank journey is linked to the composite (customer journey) it delivers. The workbook has no column for this, so the
link is derived and labeled: "mi-reference" when MI's own composite steps or gaps cite the journey (the most-cited composite
wins), otherwise "rail-segment" when rail and segment match (direction words in the title break ties). Journeys with no
match stay unlinked rather than being forced onto a composite for another segment.

Capability flags follow MI's own counting (CapabilityClasses sheet): only a literal "Yes" is true; "No", "None observed"
and text starting "not evidenced" are false; any other text is unknown (kept as detail). Stage scores must be integers
0-4 or U. ScoreTotals are kept as MI published them, alongside means and an index recomputed from the Scores sheet,
with a warning where they differ. A finding keeps MI's stage (relative to the best-practice journey); when the bank step it
sits on is in another stage, that stage is kept as step_stage.

Writes are staged: every output is built in memory, applied to a scratch copy of the repo, assembled and validated
there, and only then written to the repo. A failed import leaves the repo untouched.

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
ap.add_argument("--check", action="store_true"); ap.add_argument("--repin", action="store_true"); ap.add_argument("--replace", action="store_true")
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
changed = [f for f, h in listed.items() if os.path.isfile(os.path.join(rdir, f)) and hashlib.sha256(open(os.path.join(rdir, f), "rb").read()).hexdigest() != h]
missing_files = [f for f in listed if not os.path.isfile(os.path.join(rdir, f))]
if missing_files: die(f"report file(s) listed in the manifest are missing: {missing_files}")
if changed and not args.repin: die(f"report file(s) changed since they were pinned: {changed}. Reports are immutable; deliver a new version (or --repin before first ingest)")

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
problems, warnings = [], []          # problems stop the import; warnings are data-quality notes about the workbook itself
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
    nums = [st.get("Step #") for st in steps_by[(b, jid)]]
    if any(not isinstance(x, (int, float)) or int(x) != x for x in nums): problems.append(f"{where}: a step has no integer Step #"); continue
    if len(set(nums)) != len(nums): problems.append(f"{where}: duplicate Step # values"); continue
    if sorted(int(x) for x in nums) != list(range(1, len(nums) + 1)): problems.append(f"{where}: Step # must run 1..{len(nums)} without gaps")
    for st in sorted(steps_by[(b, jid)], key=lambda x: x["Step #"]):
        n = int(st["Step #"]); code = f"M{n:02d}"; w = f"Steps {jid}#{n}"
        if st["Stage"] not in STAGE: problems.append(f"{w}: unknown stage {st['Stage']}"); continue
        sb, sc = ev(st.get("Evidence") or "UNKNOWN"); sids = srcs(b, st.get("Sources"), w)
        actor = str(st.get("Actor") or "CUSTOMER").lower().replace("_", "-")
        action = s(st.get("Action")) or ""
        is_customer = actor in ("customer", "recipient")
        backstage = actor in ("bank-system", "network", "third-party")
        frontstage = s(st.get("System behavior")) or ("" if is_customer or backstage else action)
        tps = [{"channel": CHANNEL.get(st.get("Channel"), "web"), "screen": s(st.get("Touchpoint"))}] if st.get("Channel") else []
        title = re.sub(r"\s+", " ", action)
        if len(title) > 72: title = title[:72].rsplit(" ", 1)[0] + "…"
        a = lambda: {"basis": sb, "source_ids": [REPORT_SRC] + sids, "asserted_by": MI, "asserted_at": received, "confidence": sc,
                     "x-mi_evidence": st.get("Evidence") or "UNKNOWN"}
        evidence = {}
        if is_customer and action: evidence["action"] = a()
        if tps: evidence["touchpoint"] = a()
        if frontstage: evidence["frontstage"] = a()
        if backstage and action: evidence["process"] = a()          # below the line of visibility: what the bank, network or third party does
        m = {"id": f"urn:kos:moment:{b}:{local}:{code.lower()}", "code": code, "stage": STAGE[st["Stage"]], "title": title or code,
             "customer_action": action if is_customer else None, "action": action or None, "touchpoints": tps, "frontstage": frontstage, "actor": actor,
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
         "assessment": s(r.get("Analyst assessment")), "x-mi_evidence": r.get("Overall evidence") or "UNKNOWN",
         "bank_product": s(r.get("product_id")),
         "terms": {k: v for k, v in {"limits": s(r.get("Limits (incidental)")), "fees": s(r.get("Fees (incidental)")),
                                     "cutoffs": s(r.get("Cutoffs/timing (incidental)"))}.items() if v}}
    if not j["terms"]: del j["terms"]
    journeys[(b, local)] = j

# ---------- findings, composites, observations, verifications, participation, rankings ----------
jrail = {(r["bank_slug"], str(r["journey_id"])): r["Rail"] for r in X["Journeys"]}
findings = defaultdict(list)
moment_stage = {(j["bank"], j["source_journey_id"]): [m["stage"] for m in j["moments"]] for j in journeys.values()}
restaged = 0
for g in X["Gaps"]:
    b = g["bank_slug"]; w = f"Gaps {g['gap_id']}"
    if not bank_ok(b, w): continue
    jid = s(g.get("journey_id")); rail = s(g.get("Rail")) or jrail.get((b, jid))
    basis, _ = ev(g.get("Evidence") or "UNKNOWN")
    if jid and (b, jid) not in jurn: problems.append(f"{w}: journey {jid} is not in the Journeys sheet")
    step = int(g["Step #"]) if g.get("Step #") not in (None, "") else None
    mi_stage = STAGE.get(g.get("Stage"))
    if g.get("Stage") and not mi_stage: problems.append(f"{w}: unknown stage {g.get('Stage')}")
    ms = moment_stage.get((b, jid), [])
    if step is not None and jid and not 1 <= step <= len(ms): problems.append(f"{w}: step {step} is outside journey {jid} (1..{len(ms)})")
    stage = ms[step - 1] if step and jid and 1 <= step <= len(ms) else mi_stage
    if stage != mi_stage: restaged += 1
    if g.get("Severity") and str(g["Severity"]).lower() not in ("critical", "high", "medium", "low"): problems.append(f"{w}: unknown severity {g['Severity']}")
    findings[b].append({"id": g["gap_id"], "bank": b, "journey": jurn.get((b, jid)) if jid else None, "product": RAIL.get(rail) if rail else None,
        "stage": mi_stage, "step": step, **({"step_stage": stage} if stage and stage != mi_stage else {}),
        "type": str(g["Gap type"]).lower().replace("_", "-"), "severity": str(g["Severity"]).lower(), "description": s(g["Description"]),
        "composite": s(g.get("Composite")), "composite_step": int(g["Composite step"]) if g.get("Composite step") not in (None, "") else None,
        "reference_banks": s(g.get("Reference bank(s)")), "basis": basis, "source_ids": [REPORT_SRC] + srcs(b, g.get("Sources"), w),
        "frameworks": s(g.get("Rolls up to (framework)")), "report_version": version, "x-mi_evidence": g.get("Evidence") or "UNKNOWN"})
comps = defaultdict(lambda: {"steps": []})
for c in X["Composites"]:
    if not rail_ok(c["Rail"], f"Composites {c['composite_id']}"): continue
    k = c["composite_id"]; comps[k].update({"id": k, "title": s(c["Title"]), "product": RAIL[c["Rail"]], "segment": s(c.get("Segment")),
                                            "direction": s(c.get("Direction")), "report_version": version})
    if c["Stage"] not in STAGE: problems.append(f"Composites {k}#{c['Step #']}: unknown stage {c['Stage']}")
    comps[k]["steps"].append({"stage": STAGE.get(c["Stage"], "support"), "n": int(c["Step #"]), "action": s(c["Action"]) or "",
        "actor": s(c.get("Actor")), "channel": s(c.get("Channel")), "job_step": s(c.get("JTBD job step")), "moment_of_truth": s(c.get("Moment of truth")),
        "derived_from": s(c.get("Derived from (bank:journey#step)")), "rationale": s(c.get("Rationale"))})
by_product_comp = defaultdict(list)
for c in comps.values(): c["steps"].sort(key=lambda x: x["n"]); by_product_comp[c["product"]].append(c)
# ---------- customer journeys: link each bank journey to the composite it delivers ----------
cref = defaultdict(lambda: defaultdict(int))       # (bank, journey id) -> composite -> evidence count
for c in X["Composites"]:
    for m in re.finditer(r"([a-z-]+):([A-Z]+-J\d+)", str(c.get("Derived from (bank:journey#step)") or "")): cref[(m.group(1), m.group(2))][c["composite_id"]] += 3
for g in X["Gaps"]:
    if s(g.get("Composite")) and s(g.get("journey_id")): cref[(g["bank_slug"], str(g["journey_id"]))][g["Composite"]] += 1
DIRKW = {"RECEIVE": r"receiv|pull|get paid|incoming|in from|request for payment|rfp|payer", "REQUEST": r"request|split",
         "DEPOSIT": r"deposit", "SEND": r"send|pay|push|transfer|move"}
crail = {k: next(r["Rail"] for r in X["Composites"] if r["composite_id"] == k) for k in comps}
for r in X["Journeys"]:
    b, jid = r["bank_slug"], str(r["journey_id"]); j = journeys.get((b, jid.lower()))
    if not j: continue
    t = (s(r["Title"]) or "").lower(); seg = str(r.get("Segment") or "")
    refs = cref[(b, jid)]
    if refs:                                                   # MI's own references decide; most-cited wins, ties → same rail, then id
        k = sorted(refs, key=lambda c: (-refs[c], crail.get(c) != r["Rail"], (comps.get(c, {}).get("segment") or "") != seg, c))[0]
        if len([c for c in refs if refs[c] == refs[k]]) > 1: warnings.append(f"Journeys {jid}: MI references tie between {sorted(c for c in refs if refs[c] == refs[k])}; chose {k}")
        j["composite"], j["composite_match"] = k, "mi-reference"; continue
    cands = [k for k, c in comps.items() if crail[k] == r["Rail"] and (c.get("segment") or "") == seg]
    if not cands: continue                                     # no best-practice journey for this rail and segment: stays unlinked
    def score(k):
        c = comps[k]; return (bool(re.search(DIRKW.get(c.get("direction") or "", "^$"), t)) + 2 * ("ebill" in k.lower() and bool(re.search("ebill|autopay", t))), k)
    k = sorted(cands, key=lambda k: (-score(k)[0], k))[0]
    j["composite"], j["composite_match"] = k, "rail-segment"

# ---------- catalog: products as marketed and their sub-products ----------
caprow = {(c["bank_slug"], c["sub_product_id"]): c for c in X["Capabilities"]}
FLAGLIST = list(FLAG_STAGE)
def flag(v):
    """MI's own counting (CapabilityClasses): only a literal Yes is true; other text is unknown, kept as detail"""
    v = s(v)
    if v is None: return None
    lv = v.lower()
    if lv == "yes": return True
    if lv in ("no", "none observed", "none") or lv.startswith("not evidenced"): return False
    return None
jby_sub = defaultdict(list)
for j in journeys.values():
    if j.get("sub_product"): jby_sub[(j["bank"], j["sub_product"])].append(j["id"])
catalog = defaultdict(list)
subs_by = defaultdict(list)
for sp in X["SubProducts"]: subs_by[(sp["bank_slug"], sp["product_id"])].append(sp)
for pr in X["Products"]:
    b = pr["bank_slug"]; w = f"Products {pr['product_id']}"
    if not bank_ok(b, w): continue
    rails = [RAIL[x] for x in split(pr.get("Rails")) if rail_ok(x, w)]
    pb, pc = ev(pr.get("Evidence") or "UNKNOWN")
    subs = []
    for sp in subs_by[(b, pr["product_id"])]:
        w2 = f"SubProducts {sp['sub_product_id']}"
        if not rail_ok(sp["Rail"], w2): continue
        cr = caprow.get((b, sp["sub_product_id"]), {}); sb, sc = ev(sp.get("Evidence") or "UNKNOWN")
        caps = {f.replace("_", "-"): flag(cr.get(f)) for f in FLAGLIST}
        detail = {f.replace("_", "-"): s(cr.get(f)) for f in FLAGLIST if s(cr.get(f)) and s(cr.get(f)).lower() not in ("yes", "no", "unknown", "n/a", "none observed", "none")}
        subs.append({"id": s(sp["sub_product_id"]), "name": s(sp.get("Sub-product")) or s(sp["sub_product_id"]), "product": RAIL[sp["Rail"]],
                     "segments": [x.replace("_", "-") for x in split(sp.get("Segments"))], "channels": [CHANNEL.get(c, c.lower()) for c in split(sp.get("Channels"))],
                     "description": s(sp.get("Description")), "other_flags": s(sp.get("Other flags")), "notes": s(sp.get("Notes")),
                     "capabilities": caps, **({"capability_detail": detail} if detail else {}),
                     "basis": sb, "confidence": sc, "source_ids": [REPORT_SRC] + srcs(b, sp.get("Sources"), w2),
                     "journeys": sorted(jby_sub[(b, s(sp["sub_product_id"]))]), "x-mi_evidence": sp.get("Evidence") or "UNKNOWN"})
    catalog[b].append({"id": s(pr["product_id"]), "bank": b, "name": s(pr.get("Product (as marketed)")) or s(pr["product_id"]),
                       "former_names": s(pr.get("Former names")), "segments": [x.replace("_", "-") for x in split(pr.get("Segments"))],
                       "rails": rails, "channels": [CHANNEL.get(c, c.lower()) for c in split(pr.get("Channels"))],
                       "network": s(pr.get("Network / vendor")), "ui_position": s(pr.get("Position in bank UI")), "description": s(pr.get("Description")),
                       "basis": pb, "confidence": pc, "source_ids": [REPORT_SRC] + srcs(b, pr.get("Sources"), w), "sub_products": subs,
                       "report_version": version, "x-mi_evidence": pr.get("Evidence") or "UNKNOWN"})
known_sub = {(b, sp["id"]): p["id"] for b, ps in catalog.items() for p in ps for sp in p["sub_products"]}
for j in journeys.values():
    if j.get("sub_product") and (j["bank"], j["sub_product"]) not in known_sub:
        problems.append(f"Journeys {j['source_journey_id']}: sub-product {j['sub_product']} is not in the SubProducts sheet")
    elif j.get("sub_product") and known_sub[(j["bank"], j["sub_product"])] != j.get("bank_product"):
        parent = known_sub[(j["bank"], j["sub_product"])]
        warnings.append(f"Journeys {j['source_journey_id']}: product_id {j.get('bank_product')} does not own sub-product {j['sub_product']}; "
                        f"using its parent {parent} (kept as x-mi_product_id)")
        j["x-mi_product_id"] = j.get("bank_product"); j["bank_product"] = parent

observations = defaultdict(list)
for o in X["Observations"]:
    if bank_ok(o["bank_slug"], "Observations"):
        if o["Type"] not in OBS: problems.append(f"Observations: unknown type {o['Type']}")
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
cell = defaultdict(list)                              # (bank, rail) -> stage scores, recomputed from the Scores sheet
for r in X["Scores"]:
    v = r["Score (0-4, U=unknown)"]
    if isinstance(v, (int, float)) and float(v).is_integer() and 0 <= v <= 4 and r["Rail"] in RAIL: cell[(r["bank_slug"], RAIL[r["Rail"]])].append(int(v))
rankings = []
for r in X["ScoreTotals"]:
    if not bank_ok(r["bank_slug"], "ScoreTotals"): continue
    means = {RAIL[k.split(" mean")[0]]: v for k, v in r.items() if k.endswith("mean (0-4)") and k.split(" mean")[0] in RAIL}
    b = r["bank_slug"]; mine = {p: round(sum(v) / len(v), 2) for (bb, p), v in cell.items() if bb == b and v}
    allv = [x for (bb, _), v in cell.items() if bb == b for x in v]
    rankings.append({"bank": b, "rank": int(r["Rank"]), "overall_index": float(r["Overall index (0-100)"]),
        "domestic_core_index": r.get("Domestic-core index"), "coverage": r.get("Scored cell coverage"), "rail_means": means, "report_version": version,
        "x-computed": {"overall_index": round(sum(allv) / len(allv) * 25, 1) if allv else None, "rail_means": mine,
                       "method": "mean of the bank's numeric stage scores on the Scores sheet × 25; rail means are the mean of that rail's stage scores; U excluded"}})
order = sorted(rankings, key=lambda x: -(x["x-computed"]["overall_index"] or 0))
for i, x in enumerate(order, 1): x["x-computed"]["rank"] = i
diff_means = [(x["bank"], p) for x in rankings for p, v in x["rail_means"].items() if v is not None and p in x["x-computed"]["rail_means"] and abs(v - x["x-computed"]["rail_means"][p]) > 0.05]
if diff_means: warnings.append(f"ScoreTotals: {len(diff_means)} bank × rail means differ from the mean of their Scores cells (e.g. {diff_means[0][0]} {diff_means[0][1]})")
diff_idx = [x["bank"] for x in rankings if x["x-computed"]["overall_index"] is not None and abs(x["overall_index"] - x["x-computed"]["overall_index"]) > 0.5]
if diff_idx: warnings.append(f"ScoreTotals: overall index differs from the Scores sheet by more than 0.5 points for {len(diff_idx)} of {len(rankings)} banks; the site shows both")

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
    if lv in ("no", "none observed", "none") or lv.startswith("not evidenced"): return (False, None)
    return None                                       # MI counts free text as unknown (CapabilityClasses); the text stays on the sub-product
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
        raw = r["Score (0-4, U=unknown)"]; sc = str(raw).strip()
        if sc.upper() == "U": continue
        if isinstance(raw, float) and raw.is_integer(): sc = str(int(raw))
        if not sc.isdigit() or not 0 <= int(sc) <= 4: problems.append(f"Scores {b}/{p}/{st}: score {raw!r} is not 0-4 or U"); continue
        basis, conf = ev(r.get("Evidence") or "UNKNOWN")
        extracts[p][b].append({"attribute": f"attr-score-{st}", "value": int(sc), "display": f"{sc} of 4", "basis": basis, "confidence": conf,
                               "observed_on": AS_OF, "source_ids": [], "evidence": {"quote": (s(r.get("Rationale")) or "")[:600], "report_ref": "Scores sheet",
                                                                          "mi_level": r.get("Evidence") or "UNKNOWN"}})

if problems:
    print(f"IMPORT FAIL — {len(problems)} problem(s), nothing written"); [print(" -", p) for p in problems[:40]]; sys.exit(1)

summary = (f"{version}: {len(src_rows)} sources, {len(journeys)} journeys ({sum(len(j['moments']) for j in journeys.values())} steps), "
           f"{sum(map(len, catalog.values()))} products ({sum(len(p['sub_products']) for ps in catalog.values() for p in ps)} sub-products), "
           f"{sum(1 for j in journeys.values() if j.get('composite'))} journeys linked to a customer journey, "
           f"{sum(map(len, findings.values()))} findings, {len(comps)} composites, {sum(map(len, observations.values()))} observations, "
           f"{sum(map(len, verifs.values()))} verifications, {len(participation)} participation rows, {len(rankings)} rankings, "
           f"{len(cmp_products)} product comparisons, {sum(len(f) for bb in extracts.values() for f in bb.values())} comparison facts")
print(summary)
if restaged: warnings.append(f"Gaps: {restaged} findings are filed under a best-practice stage that differs from the stage of the bank step they sit on; that step's stage is kept as step_stage")
for w in warnings: print(" warning:", w)
if args.dry_run: print("dry run — nothing written"); sys.exit(0)

# ---------- plan every write (nothing touches the repo until the plan validates) ----------
plan = {}                                  # repo-relative path -> object to write as JSON, or None to delete
def put(rel, o): plan[rel] = o
def drop(pattern):
    for old in glob.glob(os.path.join(ROOT, pattern), recursive=True):
        rel = os.path.relpath(old, ROOT)
        if rel not in plan: plan[rel] = None
others = sorted({json.load(open(f)).get("report_version") for f in glob.glob(os.path.join(ROOT, "data/journeys/*/mi-*.json"))} - {version, None})
if others and not args.replace:
    die(f"MI data from {others} is already imported. MI IDs (journeys, sources, findings) are not version-scoped yet, so a second "
        f"version replaces the first: rerun with --replace once that is intended")
rel_report = os.path.relpath(rdir, ROOT)
sources = [x for x in jl("registries/sources.json") if not (x.get("report_version") == version and x.get("kind") != "mi-report") and x["id"] != REPORT_SRC]
report_source = {"id": REPORT_SRC, "kind": "mi-report", "title": man.get("title") or f"Market-intelligence report {version}",
                 "origin": man.get("produced_by", MI), "url": None, "retrieved_at": received, "path": f"{rel_report}/{wbname}",
                 "sha256": sha, "report_version": version}       # the workbook is the canonical deliverable every MI record cites
put("registries/sources.json", sources + [report_source] + list(src_rows.values()))
drop("data/journeys/*/mi-*.json")
for (b, local), j in journeys.items(): put(f"data/journeys/{b}/mi-{local}.json", j)
mi_urns = {j["id"] for j in journeys.values()}
for pr in products:
    pr["journeys"] = [u for u in pr.get("journeys", []) if u not in mi_urns and not re.search(r":[a-z0-9]+-j\d+$", u)]
    pr["journeys"] += sorted(j["id"] for j in journeys.values() if j["product"] == pr["id"])
put("registries/products.json", products)
for folder, data in [("catalog", catalog), ("findings", findings), ("observations", observations), ("verifications", verifs), ("composites", by_product_comp)]:
    drop(f"data/{folder}/*.json")
    for k, v in data.items(): put(f"data/{folder}/{k}.json", v)
put("data/participation.json", participation)
put("data/rankings.json", sorted(rankings, key=lambda r: r["rank"]))
pf = jl("data/portfolio.json")
for pid in cmp_products:
    cpath = f"data/comparisons/{pid}/comparison.json"
    comp = jl(cpath) if os.path.exists(os.path.join(ROOT, cpath)) else {"product": pid, "governance": gov, "attributes": []}
    have = {a["id"] for a in comp["attributes"]}; comp["attributes"] += [a for a in attributes_for(pid) if a["id"] not in have]
    put(cpath, comp)
    for b in pf["banks"]:
        vp = f"data/comparisons/{pid}/values/{b}.json"
        vf = jl(vp) if os.path.exists(os.path.join(ROOT, vp)) else {"bank": b, "product": pid, "values": {}}
        for a in comp["attributes"]:
            vf["values"].setdefault(a["id"], [{"basis": "awaiting", "source_ids": [], "asserted_by": None, "asserted_at": None, "observed_on": None,
                "valid_to": None, "verified_by": None, "verified_at": None, "id": f"urn:kos:assertion:{b}:{pid}:{a['id'][5:]}:1"}])
        put(vp, vf)
drop(f"{rel_report}/extract/**/*.json")
for pid, banks in extracts.items():
    for b, facts in banks.items(): put(f"{rel_report}/extract/{pid}/{b}.json", {"bank": b, "product": pid, "facts": facts})
files = []
for f in sorted(os.listdir(rdir)):
    fp = os.path.join(rdir, f)
    if os.path.isfile(fp) and f != "manifest.json":
        files.append({"path": f, "sha256": listed.get(f) if f in listed and not args.repin else hashlib.sha256(open(fp, "rb").read()).hexdigest(),
                      "kind": "data" if f.endswith(".xlsx") else "report"})
files = [f for f in files if f["path"] == wbname] + [f for f in files if f["path"] != wbname]   # canonical file first: ingest cites it
man.update({"products": sorted(extracts), "workbook": wbname, "files": files})
man.pop("product", None)
man["notes"] = "Imported with tools/import_mi_workbook.py; " + summary
if warnings: man["import_warnings"] = warnings
else: man.pop("import_warnings", None)
put(f"{rel_report}/manifest.json", man)

def dump(rel, o):
    return json.dumps(o, ensure_ascii=False, indent=2 if rel.endswith("manifest.json") else 1) + "\n"
def differs(rel, o):
    p = os.path.join(ROOT, rel)
    if o is None: return os.path.exists(p)
    if not os.path.exists(p): return True
    norm = (lambda x: sorted(x, key=lambda y: y["id"])) if rel == "registries/sources.json" else (lambda x: x)   # ingest re-appends the report source
    try: return norm(json.load(open(p))) != norm(json.loads(dump(rel, o)))
    except ValueError: return True
if args.check:
    bad = sorted(rel for rel, o in plan.items() if differs(rel, o))
    if bad: print(f"CHECK FAIL — {len(bad)} file(s) differ from what the workbook produces:"); [print(" -", x) for x in bad[:30]]; sys.exit(1)
    print("check ok — data matches the workbook"); sys.exit(0)

# stage in a scratch copy, assemble and validate there, then write for real
import subprocess, tempfile
tmp = tempfile.mkdtemp(prefix="kjourneys-import-")
try:
    shutil.copytree(ROOT, tmp, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git", "dist", "fixtures", "__pycache__"))
    for rel, o in plan.items():
        p = os.path.join(tmp, rel)
        if o is None:
            if os.path.exists(p): os.remove(p)
        else:
            os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w").write(dump(rel, o))
    for cmd in (["python3", "tools/assemble.py"], ["python3", "tools/validate_journey.py", "dist/kjourneys.json", "schema/journey-ontology.schema.json"]):
        r = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
        if r.returncode:
            print("IMPORT FAIL — the imported data does not validate; nothing was written to the repo"); print((r.stdout + r.stderr)[-4000:]); sys.exit(1)
finally:
    shutil.rmtree(tmp, ignore_errors=True)
for rel, o in plan.items():
    p = os.path.join(ROOT, rel)
    if o is None:
        if os.path.exists(p): os.remove(p)
        continue
    os.makedirs(os.path.dirname(p), exist_ok=True); t = p + ".tmp"
    with open(t, "w") as f: f.write(dump(rel, o))
    os.replace(t, p)
for d0 in glob.glob(os.path.join(rdir, "extract", "*")):
    if os.path.isdir(d0) and not os.listdir(d0): os.rmdir(d0)
print("written — validated before writing. Now run: scripts/refresh.sh " + rel_report)

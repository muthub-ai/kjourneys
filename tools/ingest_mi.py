#!/usr/bin/env python3
"""Ingest one versioned market-intelligence (MI) report into the comparison data.

  python3 tools/ingest_mi.py reports/<version> [--dry-run]

Input  (reports/<version>/, immutable once committed):
  manifest.json                    version, products, producer, received_at, files[] with sha256
  <report files>                   the MI deliverable as received (html, docx, xlsx, pdf, ...)
  extract/<product>/<bank>.json    structured facts drawn from the report (see docs/mi-extraction.md);
                                   extract/<bank>.json is also accepted when the report covers one product

Effect:
  registries/sources.json                          + the report itself and every cited URL
  data/comparisons/<product>/values/<bank>.json    + one assertion per fact; a changed value
                                                     closes the previous one and supersedes it
  reports/ingest-log.json                          + one entry per version

Rerunnable: ingesting a version again first rolls back everything that version wrote (its facts,
reopening what they superseded, and its report source), then applies the extracts afresh. So you can
fix an extract and rerun on the same branch. Refused only if a later version already builds on it.
Usually run through scripts/refresh.sh.
"""
import argparse, glob, hashlib, json, os, re, sys
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_BASIS = {"observed", "disclosed", "inferred"}
ALLOWED_CONF = {"high", "medium", "low"}

def jload(p):
    try: return json.load(open(p))
    except FileNotFoundError: sys.exit(f"INGEST FAIL — {os.path.relpath(p, ROOT)} not found")
    except json.JSONDecodeError as e: sys.exit(f"INGEST FAIL — {os.path.relpath(p, ROOT)} is not valid JSON: {e}")
def jdump(p, o):                                   # atomic: write a temp file, then rename over the target
    tmp = p + ".tmp"
    with open(tmp, "w") as f: json.dump(o, f, ensure_ascii=False, indent=2); f.write("\n")
    os.replace(tmp, p)
MANIFEST_KEYS = {"report_version", "product", "products", "workbook", "title", "produced_by", "received_at", "files", "notes", "import_warnings"}
EXTRACT_KEYS = {"bank", "product", "facts"}
FACT_KEYS = {"attribute", "value", "display", "qualifier", "basis", "confidence", "observed_on", "sources", "source_ids", "evidence"}
SOURCE_KEYS = {"title", "url", "retrieved_at", "kind"}
def unknown(obj, allowed, where):
    extra = sorted(set(obj) - allowed)
    if extra: fail(f"{where}: unknown field(s) {extra} — allowed: {sorted(allowed)}")
    return not extra
def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""): h.update(chunk)
    return h.hexdigest()
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

problems = []
def fail(msg): problems.append(msg)

ap = argparse.ArgumentParser(); ap.add_argument("report_dir"); ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()
rdir = os.path.abspath(args.report_dir)
version = os.path.basename(rdir.rstrip("/"))
# ---------- manifest and immutability ----------
if not os.path.isfile(os.path.join(rdir, "manifest.json")): sys.exit(f"INGEST FAIL — {args.report_dir}/manifest.json not found (see reports/README.md)")
man = jload(os.path.join(rdir, "manifest.json"))
unknown(man, MANIFEST_KEYS, "manifest")
try: datetime.fromisoformat(str(man.get("received_at", "")).replace("Z", "+00:00"))
except ValueError: fail("manifest: received_at must be an ISO 8601 date-time, e.g. 2026-11-20T17:30:00-06:00")
for k in ["report_version", "produced_by", "received_at", "files"]:
    if k not in man: fail(f"manifest: missing '{k}'")
if ("product" in man) == ("products" in man): fail("manifest: give either 'products' (a list) or 'product' (one), not both or neither")
if man.get("report_version") != version: fail(f"manifest: report_version '{man.get('report_version')}' must equal folder name '{version}'")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-v\d+", version): fail(f"version folder '{version}' must look like YYYY-MM-DD-vN")
else:
    try: date.fromisoformat(version[:10])
    except ValueError: fail(f"version folder '{version}' does not start with a real date")
if not str(man.get("produced_by", "")).startswith(("process:", "human:", "group:", "role:")): fail("manifest: produced_by must be a principal (process:, human:, group:, role:)")
for f in man.get("files", []):
    p = os.path.join(rdir, f["path"])
    if not os.path.exists(p): fail(f"manifest: file {f['path']} is missing")
    elif sha256(p) != f.get("sha256"): fail(f"manifest: {f['path']} sha256 mismatch — reports are immutable; add a new version instead")
if not man.get("files"): fail("manifest: list at least the report file itself under files[]")

products = man.get("products") or ([man["product"]] if man.get("product") else [])
if not isinstance(products, list) or not products: fail("manifest: products must be a non-empty list")
products = [str(x) for x in products] if isinstance(products, list) else []
for product in products:
    if not os.path.isfile(os.path.join(ROOT, "data/comparisons", product, "comparison.json")):
        fail(f"no comparison for product '{product}' — create data/comparisons/{product}/comparison.json (its questions) first")
log_path = os.path.join(ROOT, "reports/ingest-log.json")
log = jload(log_path) if os.path.exists(log_path) else []
rerun = any(e["report_version"] == version for e in log)
if problems: print("INGEST FAIL"); [print(" -", p) for p in problems]; sys.exit(1)

ATTRS = {p: {a["id"]: a for a in jload(os.path.join(ROOT, "data/comparisons", p, "comparison.json"))["attributes"]} for p in products}
sources = jload(os.path.join(ROOT, "registries/sources.json"))
src_ids = {s["id"] for s in sources}
parties = {p["id"]: p for p in jload(os.path.join(ROOT, "registries/parties.json"))}

report_src = f"src-mi-{version}"
touched = {}

# ---------- rerun: roll back what this version wrote ----------
rolled_back = 0
if rerun:
    for vpath in sorted(glob.glob(os.path.join(ROOT, "data/comparisons", "*", "values", "*.json"))):
        vfile = jload(vpath); changed = False
        for aid, hist in vfile["values"].items():
            mine = [a for a in hist if report_src in a.get("source_ids", [])]
            if not mine: continue
            mine_ids = {a["id"] for a in mine}
            rest = [a for a in hist if a["id"] not in mine_ids]
            if any(a.get("supersedes") in mine_ids for a in rest):
                fail(f"{os.path.relpath(vpath, ROOT)} {aid}: a later version supersedes {version}; rerun the latest version instead")
                continue
            for a in rest:
                if a.get("valid_to") and any(m.get("supersedes") == a["id"] for m in mine): a["valid_to"] = None
            bank = vfile["bank"]
            vfile["values"][aid] = rest or [{"basis": "awaiting", "source_ids": [], "asserted_by": None, "asserted_at": None,
                                             "observed_on": None, "valid_to": None, "verified_by": None, "verified_at": None,
                                             "id": f"urn:kos:assertion:{bank}:{vfile['product']}:{aid[5:]}:1"}]
            rolled_back += len(mine); changed = True
        if changed: touched[vpath] = vfile
    sources = [s for s in sources if s["id"] != report_src]
    src_ids = {s["id"] for s in sources}
    log = [e for e in log if e["report_version"] != version]
    if problems: print("INGEST FAIL — nothing written"); [print(" -", p) for p in problems]; sys.exit(1)

# ---------- register the report as a source (replacing any copy the workbook importer wrote) ----------
sources = [s for s in sources if s["id"] != report_src]
src_ids = {s["id"] for s in sources} | {report_src}
primary = man["files"][0]
new_sources = [{"id": report_src, "kind": "mi-report", "title": man.get("title", f"Market-intelligence report {version}"),
                "origin": man["produced_by"], "url": None, "retrieved_at": man["received_at"],
                "path": f"reports/{version}/{primary['path']}", "sha256": primary["sha256"], "report_version": version}]

def url_source(s):
    s = dict(s)
    sid = "src-" + slug(s.get("title") or s["url"])[:40] + "-" + hashlib.sha256(s["url"].encode()).hexdigest()[:8]
    if sid not in src_ids and all(n["id"] != sid for n in new_sources):
        new_sources.append({"id": sid, "kind": s.get("kind", "web-page"), "title": s.get("title") or s["url"],
                            "origin": re.sub(r"^https?://([^/]+).*$", r"\1", s["url"]), "url": s["url"],
                            "retrieved_at": s.get("retrieved_at", man["received_at"])})
    return sid

# ---------- apply facts ----------
applied, unchanged = 0, 0
runs = 1 + next((e.get("runs", 1) for e in (jload(log_path) if os.path.exists(log_path) else []) if e["report_version"] == version), 0)
extracts = [(p, ex) for p in products for ex in sorted(glob.glob(os.path.join(rdir, "extract", p, "*.json")))]
loose = sorted(glob.glob(os.path.join(rdir, "extract", "*.json")))
if loose and len(products) == 1: extracts += [(products[0], ex) for ex in loose]
elif loose: fail(f"extract/: this report covers several products, so put extracts in extract/<product>/<bank>.json ({len(loose)} file(s) at the top level)")
for d_ in sorted(glob.glob(os.path.join(rdir, "extract", "*", ""))):
    if os.path.basename(os.path.dirname(d_)) not in products: fail(f"extract/{os.path.basename(os.path.dirname(d_))}/: product not listed in the manifest")
if not extracts: fail("no extract files found — see docs/mi-extraction.md")
for product, ex in extracts:
    attrs = ATTRS[product]; cdir = os.path.join(ROOT, "data/comparisons", product)
    e = jload(ex); bank = e.get("bank"); where = os.path.relpath(ex, ROOT)
    if os.path.splitext(os.path.basename(ex))[0] != bank: fail(f"{where}: file name must equal bank id"); continue
    if bank not in parties: fail(f"{where}: unknown bank '{bank}'"); continue
    if e.get("product") != product: fail(f"{where}: product must be '{product}'"); continue
    vpath = os.path.join(cdir, "values", f"{bank}.json")
    if not unknown(e, EXTRACT_KEYS, where): continue
    if not os.path.exists(vpath): fail(f"{where}: {bank} has no comparison file {os.path.relpath(vpath, ROOT)}; add the bank to the study first"); continue
    vfile = touched.get(vpath) or jload(vpath)
    seen_attrs = set()
    for i, f in enumerate(e.get("facts", []), 1):
        w = f"{where} fact {i}"
        if not isinstance(f, dict) or not unknown(f, FACT_KEYS, w): continue
        bad_src = [s for s in f.get("sources", []) if not isinstance(s, dict) or not s.get("url") or not unknown(s, SOURCE_KEYS, f"{w} source")]
        if bad_src: fail(f"{w}: every source needs a url (and only title, url, retrieved_at, kind)"); continue
        if f.get("value") is None and not f.get("display"): fail(f"{w}: value is null, so display (the bank's wording) is required"); continue
        aid = f.get("attribute")
        if aid not in attrs: fail(f"{w}: unknown attribute '{aid}'"); continue
        if aid in seen_attrs: fail(f"{w}: attribute {aid} appears twice"); continue
        seen_attrs.add(aid)
        if f.get("basis") not in ALLOWED_BASIS: fail(f"{w}: basis must be observed, disclosed or inferred"); continue
        if f.get("confidence") not in ALLOWED_CONF: fail(f"{w}: confidence must be high, medium or low"); continue
        if f["basis"] == "inferred" and f["confidence"] != "low": fail(f"{w}: inferred facts must have confidence low"); continue
        bad_ids = [x for x in f.get("source_ids", []) if x not in src_ids]
        if bad_ids: fail(f"{w}: source_ids {bad_ids[:3]} are not in registries/sources.json"); continue
        cites_report = bool((f.get("evidence") or {}).get("report_ref"))
        if not f.get("sources") and not f.get("source_ids") and f["basis"] != "inferred" and not cites_report:
            fail(f"{w}: observed/disclosed facts need a source (sources[] URL, source_ids, or evidence.report_ref citing the report)"); continue
        try: obs = date.fromisoformat(f["observed_on"])
        except Exception: fail(f"{w}: observed_on must be YYYY-MM-DD"); continue
        if obs > date.today(): fail(f"{w}: observed_on {obs} is in the future"); continue
        sids = list(dict.fromkeys([report_src] + list(f.get("source_ids", [])) + [url_source(s) for s in f.get("sources", [])]))
        hist = vfile["values"][aid]
        cur = next((a for a in hist if not a.get("valid_to")), None)
        same = (cur and cur["basis"] == f["basis"] and cur.get("value") == f.get("value") and cur.get("display") == f.get("display")
                and cur.get("qualifier") == f.get("qualifier") and cur.get("confidence") == f["confidence"]
                and sorted(x for x in cur.get("source_ids", []) if not x.startswith("src-mi-")) == sorted(x for x in sids if not x.startswith("src-mi-")) and cur.get("x-evidence") == f.get("evidence"))
        if same: unchanged += 1; continue
        short = aid[5:]
        nxt = 1 + max([int(a["id"].rsplit(":", 1)[1]) for a in hist if a.get("id")] or [0])
        new = {"id": f"urn:kos:assertion:{bank}:{product}:{short}:{nxt}", "value": f.get("value")}
        if f.get("display"): new["display"] = f["display"]
        if f.get("qualifier"): new["qualifier"] = f["qualifier"]
        new.update({"basis": f["basis"], "source_ids": sids, "asserted_by": man["produced_by"], "asserted_at": man["received_at"],
                    "observed_on": f["observed_on"], "valid_from": f["observed_on"], "valid_to": None,
                    "verified_by": None, "verified_at": None, "confidence": f["confidence"]})
        if f.get("evidence"): new["x-evidence"] = f["evidence"]           # quote + report location, kept as an extension
        if cur is None or cur["basis"] == "awaiting":
            vfile["values"][aid] = [new]                                   # a placeholder is not history
        else:
            if date.fromisoformat(cur["valid_from"]) > obs: fail(f"{w}: observed_on is earlier than the current fact's valid_from"); continue
            cur["valid_to"] = f["observed_on"]; new["supersedes"] = cur["id"]
            hist.append(new)
        applied += 1
    touched[vpath] = vfile

if problems: print("INGEST FAIL — nothing written"); [print(" -", p) for p in problems]; sys.exit(1)
print(f"{version}: {'rerun — rolled back ' + str(rolled_back) + ' fact(s); ' if rerun else ''}{applied} fact(s) applied, {unchanged} unchanged, {len(new_sources)} new source(s), {len(touched)} bank file(s)")
log.append({"report_version": version, "products": products, "produced_by": man["produced_by"], "ingested_facts": applied,
            "unchanged": unchanged, "runs": runs, "ingested_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "files": sorted(os.path.relpath(p, ROOT) for p in touched)})
outputs = {**touched, os.path.join(ROOT, "registries/sources.json"): sources + new_sources, log_path: log}

# ---------- validate the result before touching the repo ----------
import shutil, subprocess, tempfile
scratch = tempfile.mkdtemp(prefix="kj-ingest-")
try:
    shutil.copytree(ROOT, scratch, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git", "dist", "fixtures", "__pycache__"))
    for p, v in outputs.items():
        q = os.path.join(scratch, os.path.relpath(p, ROOT)); json.dump(v, open(q, "w"), ensure_ascii=False, indent=2)
    for cmd in (["python3", "tools/assemble.py"], ["python3", "tools/validate_journey.py", "dist/kjourneys.json", "schema/journey-ontology.schema.json"]):
        r = subprocess.run(cmd, cwd=scratch, capture_output=True, text=True)
        if r.returncode:
            print("INGEST FAIL — the extracts would make the data invalid; nothing written"); print(r.stdout + r.stderr); sys.exit(1)
finally:
    shutil.rmtree(scratch, ignore_errors=True)
if args.dry_run: print("dry run — valid; nothing written"); sys.exit(0)
for p, v in outputs.items(): jdump(p, v)          # ingest log last, so a crash never records an unapplied version
print("written — validated before writing")

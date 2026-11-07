#!/usr/bin/env python3
"""Ingest one versioned market-intelligence (MI) report into the comparison data.

  python3 tools/ingest_mi.py reports/<version> [--dry-run]

Input  (reports/<version>/, immutable once committed):
  manifest.json          version, product, producer, received_at, files[] with sha256
  <report files>         the MI deliverable as received (md, pdf, docx, ...)
  extract/<bank>.json    structured facts drawn from the report (see docs/mi-extraction.md)

Effect:
  registries/sources.json                          + the report itself and every cited URL
  data/comparisons/<product>/values/<bank>.json    + one assertion per fact; a changed value
                                                     closes the previous one and supersedes it
  reports/ingest-log.json                          + one entry per version (re-ingest is refused)
Then run `make check`; CI gates the result like any other change.
"""
import argparse, glob, hashlib, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_BASIS = {"observed", "disclosed", "inferred"}
ALLOWED_CONF = {"high", "medium", "low"}

def jload(p): return json.load(open(p))
def jdump(p, o): json.dump(o, open(p, "w"), ensure_ascii=False, indent=2); open(p, "a").write("\n")
def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""): h.update(chunk)
    return h.hexdigest()
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

ap = argparse.ArgumentParser(); ap.add_argument("report_dir"); ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()
rdir = os.path.abspath(args.report_dir)
version = os.path.basename(rdir.rstrip("/"))
problems = []
def fail(msg): problems.append(msg)

# ---------- manifest and immutability ----------
man = jload(os.path.join(rdir, "manifest.json"))
for k in ["report_version", "product", "produced_by", "received_at", "files"]:
    if k not in man: fail(f"manifest: missing '{k}'")
if man.get("report_version") != version: fail(f"manifest: report_version '{man.get('report_version')}' must equal folder name '{version}'")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-v\d+", version): fail(f"version folder '{version}' must look like YYYY-MM-DD-vN")
if not str(man.get("produced_by", "")).startswith(("process:", "human:", "group:", "role:")): fail("manifest: produced_by must be a principal (process:, human:, group:, role:)")
for f in man.get("files", []):
    p = os.path.join(rdir, f["path"])
    if not os.path.exists(p): fail(f"manifest: file {f['path']} is missing")
    elif sha256(p) != f.get("sha256"): fail(f"manifest: {f['path']} sha256 mismatch — reports are immutable; add a new version instead")
if not man.get("files"): fail("manifest: list at least the report file itself under files[]")

product = man.get("product")
cdir = os.path.join(ROOT, "data/comparisons", str(product))
if not os.path.isdir(cdir): fail(f"no comparison folder for product '{product}'")
log_path = os.path.join(ROOT, "reports/ingest-log.json")
log = jload(log_path) if os.path.exists(log_path) else []
if any(e["report_version"] == version for e in log): fail(f"{version} was already ingested — add a new version folder for corrections")
if problems: print("INGEST FAIL"); [print(" -", p) for p in problems]; sys.exit(1)

comparison = jload(os.path.join(cdir, "comparison.json"))
attrs = {a["id"]: a for a in comparison["attributes"]}
sources = jload(os.path.join(ROOT, "registries/sources.json"))
src_ids = {s["id"] for s in sources}
parties = {p["id"]: p for p in jload(os.path.join(ROOT, "registries/parties.json"))}

# ---------- register the report as a source ----------
report_src = f"src-mi-{version}"
primary = man["files"][0]
new_sources = [{"id": report_src, "kind": "mi-report", "title": man.get("title", f"Market-intelligence report {version}"),
                "origin": man["produced_by"], "url": None, "retrieved_at": man["received_at"],
                "path": f"reports/{version}/{primary['path']}", "sha256": primary["sha256"], "report_version": version}]

def url_source(s):
    sid = "src-" + slug(s.get("title") or s["url"])[:40] + "-" + hashlib.sha256(s["url"].encode()).hexdigest()[:8]
    if sid not in src_ids and all(n["id"] != sid for n in new_sources):
        new_sources.append({"id": sid, "kind": s.get("kind", "web-page"), "title": s.get("title") or s["url"],
                            "origin": re.sub(r"^https?://([^/]+).*$", r"\1", s["url"]), "url": s["url"],
                            "retrieved_at": s.get("retrieved_at", man["received_at"])})
    return sid

# ---------- apply facts ----------
applied, unchanged, touched = 0, 0, {}
for ex in sorted(glob.glob(os.path.join(rdir, "extract/*.json"))):
    e = jload(ex); bank = e.get("bank"); where = os.path.relpath(ex, ROOT)
    if os.path.splitext(os.path.basename(ex))[0] != bank: fail(f"{where}: file name must equal bank id"); continue
    if bank not in parties: fail(f"{where}: unknown bank '{bank}'"); continue
    if parties[bank]["role"] == "focus": fail(f"{where}: MI extracts are for competitors; {bank} facts come from journey owners"); continue
    if e.get("product") != product: fail(f"{where}: product must be '{product}'"); continue
    vpath = os.path.join(cdir, "values", f"{bank}.json")
    vfile = touched.get(vpath) or jload(vpath)
    seen_attrs = set()
    for i, f in enumerate(e.get("facts", []), 1):
        w = f"{where} fact {i}"
        aid = f.get("attribute")
        if aid not in attrs: fail(f"{w}: unknown attribute '{aid}'"); continue
        if aid in seen_attrs: fail(f"{w}: attribute {aid} appears twice"); continue
        seen_attrs.add(aid)
        if f.get("basis") not in ALLOWED_BASIS: fail(f"{w}: basis must be observed, disclosed or inferred"); continue
        if f.get("confidence") not in ALLOWED_CONF: fail(f"{w}: confidence must be high, medium or low"); continue
        if not f.get("sources") and f["basis"] != "inferred": fail(f"{w}: observed/disclosed facts need at least one source URL"); continue
        try: obs = date.fromisoformat(f["observed_on"])
        except Exception: fail(f"{w}: observed_on must be YYYY-MM-DD"); continue
        sids = [report_src] + [url_source(s) for s in f.get("sources", [])]
        hist = vfile["values"][aid]
        cur = next((a for a in hist if not a.get("valid_to")), None)
        same = cur and cur["basis"] == f["basis"] and cur.get("value") == f.get("value") and cur.get("display") == f.get("display") and cur.get("qualifier") == f.get("qualifier")
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
print(f"{version}: {applied} fact(s) applied, {unchanged} unchanged, {len(new_sources)} new source(s), {len(touched)} bank file(s)")
if args.dry_run: print("dry run — nothing written"); sys.exit(0)
for p, v in touched.items(): jdump(p, v)
jdump(os.path.join(ROOT, "registries/sources.json"), sources + new_sources)
log.append({"report_version": version, "product": product, "produced_by": man["produced_by"], "ingested_facts": applied,
            "unchanged": unchanged, "banks": sorted(os.path.splitext(os.path.basename(p))[0] for p in touched)})
jdump(log_path, log)
print("written — now run: make check")

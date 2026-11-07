#!/usr/bin/env python3
"""End-to-end test of the MI ingest flow, run in a throwaway copy of the repo.
Uses obviously fake TEST values and example.invalid URLs; nothing touches the real reports/ folder."""
import hashlib, json, os, shutil, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tmp = tempfile.mkdtemp(prefix="kjourneys-ingest-")
# copy the working tree as it is now (including uncommitted reports), never the generated outputs
shutil.copytree(REPO, tmp, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git", "dist", "fixtures", "__pycache__"))

# start every test from placeholders, whatever real MI data the repo already holds
import glob as _glob
for path in _glob.glob(os.path.join(tmp, "data/comparisons/*/values/*.json")):
    vf = json.load(open(path))
    if vf["bank"] == "wells-fargo": continue
    for aid in vf["values"]:
        vf["values"][aid] = [{"basis": "awaiting", "source_ids": [], "asserted_by": None, "asserted_at": None, "observed_on": None,
                              "valid_to": None, "verified_by": None, "verified_at": None, "id": f"urn:kos:assertion:{vf['bank']}:{vf['product']}:{aid[5:]}:1"}]
    json.dump(vf, open(path, "w"), indent=2)
json.dump([], open(os.path.join(tmp, "reports/ingest-log.json"), "w"))

def run(*cmd): return subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
def check():
    for c in (["python3", "tools/assemble.py"], ["python3", "tools/validate_journey.py", "dist/kjourneys.json", "schema/journey-ontology.schema.json"]):
        r = run(*c)
        if r.returncode: return False, r.stdout + r.stderr
    return True, ""
fails = []
def expect(ok, label):
    print(("ok    " if ok else "FAIL  ") + label)
    if not ok: fails.append(label)

def make_report(version, facts_by_bank, report_text="TEST REPORT — not real data\n"):
    d = os.path.join(tmp, "reports", version); os.makedirs(os.path.join(d, "extract"), exist_ok=True)
    open(os.path.join(d, "report.md"), "w").write(report_text)
    sha = hashlib.sha256(open(os.path.join(d, "report.md"), "rb").read()).hexdigest()
    json.dump({"report_version": version, "product": "zelle", "title": f"TEST MI report {version}", "produced_by": "process:mi-session",
               "received_at": "2000-01-02T12:00:00-06:00", "files": [{"path": "report.md", "sha256": sha, "kind": "report"}]},
              open(os.path.join(d, "manifest.json"), "w"), indent=2)
    for bank, facts in facts_by_bank.items():
        json.dump({"bank": bank, "product": "zelle", "facts": facts}, open(os.path.join(d, "extract", f"{bank}.json"), "w"), indent=2)
    return f"reports/{version}"

src = [{"title": "TEST source", "url": "https://example.invalid/zelle-faq", "retrieved_at": "2000-01-01T10:00:00-06:00"}]
v1 = make_report("2000-01-01-v1", {"citi": [
    {"attribute": "attr-daily-limit", "value": 1111, "display": "TEST $1,111", "qualifier": "segment: TEST",
     "basis": "disclosed", "confidence": "medium", "observed_on": "2000-01-01", "sources": src,
     "evidence": {"quote": "TEST quote", "report_ref": "report.md §1"}},
    {"attribute": "attr-new-payee-warning", "value": "first-payment", "basis": "observed", "confidence": "high",
     "observed_on": "2000-01-01", "sources": src}]})

r = run("python3", "tools/ingest_mi.py", v1); expect(r.returncode == 0, "ingest v1 applies")
ok, out = check(); expect(ok, "repo validates after v1" + ("" if ok else f"\n{out}"))
snap = open(os.path.join(tmp, "data/comparisons/zelle/values/citi.json")).read()
r = run("python3", "tools/ingest_mi.py", v1)
expect(r.returncode == 0 and "rolled back 2" in r.stdout and open(os.path.join(tmp, "data/comparisons/zelle/values/citi.json")).read() == snap,
       "rerunning v1 unchanged is a no-op on the data")
ex = os.path.join(tmp, v1, "extract", "citi.json"); e = json.load(open(ex))
e["facts"][0].update(value=1112, display="TEST $1,112"); json.dump(e, open(ex, "w"), indent=2)
r = run("python3", "tools/ingest_mi.py", v1)
h = json.load(open(os.path.join(tmp, "data/comparisons/zelle/values/citi.json")))["values"]["attr-daily-limit"]
expect(r.returncode == 0 and len(h) == 1 and h[0]["value"] == 1112, "rerun after fixing an extract replaces the fact, no extra history")
e["facts"][0].update(value=1111, display="TEST $1,111"); json.dump(e, open(ex, "w"), indent=2)
r = run("python3", "tools/ingest_mi.py", v1); expect(r.returncode == 0, "rerun restores v1")
log = json.load(open(os.path.join(tmp, "reports/ingest-log.json")))
mine = [x for x in log if x["report_version"].startswith("2000-")]
expect([x["report_version"] for x in mine] == ["2000-01-01-v1"] and mine[0]["runs"] == 4, "ingest log keeps one entry per version and counts runs")

v2 = make_report("2000-02-01-v1", {"citi": [
    {"attribute": "attr-daily-limit", "value": 2222, "display": "TEST $2,222", "qualifier": "segment: TEST",
     "basis": "disclosed", "confidence": "high", "observed_on": "2000-02-01", "sources": src},
    {"attribute": "attr-new-payee-warning", "value": "first-payment", "basis": "observed", "confidence": "high",
     "observed_on": "2000-02-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", v2); expect(r.returncode == 0 and "1 fact(s) applied, 1 unchanged" in r.stdout, "v2 applies the changed fact and skips the unchanged one")
hist = json.load(open(os.path.join(tmp, "data/comparisons/zelle/values/citi.json")))["values"]["attr-daily-limit"]
expect(len(hist) == 2 and hist[0]["valid_to"] == "2000-02-01" and hist[1]["supersedes"] == hist[0]["id"], "history kept: old fact closed, new one supersedes it")
ok, out = check(); expect(ok, "repo validates after v2" + ("" if ok else f"\n{out}"))
r = run("python3", "tools/ingest_mi.py", v1); expect(r.returncode != 0 and "later version" in r.stdout, "rerunning v1 is refused once v2 builds on it")
r = run("python3", "tools/ingest_mi.py", v2); h = json.load(open(os.path.join(tmp, "data/comparisons/zelle/values/citi.json")))["values"]["attr-daily-limit"]
expect(r.returncode == 0 and len(h) == 2 and h[0]["valid_to"] == "2000-02-01" and h[1]["value"] == 2222, "rerunning the latest version is safe")

open(os.path.join(tmp, v1, "report.md"), "a").write("edited later\n")
ok, out = check(); expect(not ok and "sha256 mismatch" in out, "editing an ingested report fails validation")
open(os.path.join(tmp, v1, "report.md"), "w").write("TEST REPORT — not real data\n")

bad = make_report("2000-03-01-v1", {"wells-fargo": [{"attribute": "attr-daily-limit", "value": 1, "basis": "disclosed", "confidence": "low", "observed_on": "2000-03-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", bad); expect(r.returncode != 0 and "competitors" in r.stdout, "MI facts for Wells Fargo are refused")
bad = make_report("2000-04-01-v1", {"pnc": [{"attribute": "attr-daily-limit", "value": 1, "basis": "sample", "confidence": "low", "observed_on": "2000-04-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", bad); expect(r.returncode != 0 and "basis" in r.stdout, "sample basis is refused")
bad = make_report("2000-05-01-v1", {"pnc": [{"attribute": "attr-daily-limit", "value": "lots", "basis": "disclosed", "confidence": "low", "observed_on": "2000-05-01", "sources": src}]})
snap = open(os.path.join(tmp, "data/comparisons/zelle/values/pnc.json")).read()
r = run("python3", "tools/ingest_mi.py", bad)
expect(r.returncode != 0 and "not a valid money" in r.stdout and open(os.path.join(tmp, "data/comparisons/zelle/values/pnc.json")).read() == snap,
       "wrongly typed values are refused before anything is written")
def refused(version, facts, needle, label, bank="pnc"):
    rd = make_report(version, {bank: facts}); r = run("python3", "tools/ingest_mi.py", rd)
    expect(r.returncode != 0 and needle in (r.stdout + r.stderr), label)
base = {"attribute": "attr-new-payee-warning", "value": "first-payment", "basis": "disclosed", "confidence": "low", "observed_on": "2000-06-01", "sources": src}
refused("2000-06-01-v1", [dict(base, valeu="x")], "unknown field", "a typo'd field name is refused")
refused("2000-06-02-v1", [dict(base, value=None)], "display", "a null value without display wording is refused")
refused("2000-06-03-v1", [dict(base, basis="inferred", confidence="high")], "confidence low", "inferred facts must be low confidence")
refused("2000-06-04-v1", [dict(base, value="First-Payment")], "not in allowed values", "an enum in the wrong case is refused")
refused("2000-06-05-v1", [dict(base, sources=[{"title": "no url"}])], "needs a url", "a source without a url is refused")
os.makedirs(os.path.join(tmp, "reports/2000-06-07-v1"), exist_ok=True)
r = run("python3", "tools/ingest_mi.py", "reports/2000-06-07-v1"); expect(r.returncode != 0 and "manifest.json not found" in r.stdout + r.stderr and "Traceback" not in r.stderr, "a missing manifest gives a message, not a traceback")
r = run("python3", "tools/ingest_mi.py", "reports/2000-06-04-v1", "--dry-run"); expect(r.returncode != 0, "dry run reports the same failure")

# ---------- several products in one report ----------
json.dump([{"id": "attr-same-day", "stage": "move", "name": "TEST same-day option", "datatype": "boolean", "unit": None,
            "normalization": "TEST rule"}], open(os.path.join(tmp, "ach-attrs.json"), "w"))
r = run("python3", "tools/new_comparison.py", "ach", "ach-attrs.json"); expect(r.returncode == 0, "a new product comparison can be scaffolded")
ok, out = check(); expect(ok, "repo validates with two product comparisons" + ("" if ok else f"\n{out}"))
def make_multi(version, layout):
    d = os.path.join(tmp, "reports", version); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "report.html"), "w").write("<p>TEST multi-product report</p>")
    sha = hashlib.sha256(open(os.path.join(d, "report.html"), "rb").read()).hexdigest()
    json.dump({"report_version": version, "products": ["zelle", "ach"], "produced_by": "process:mi-session",
               "received_at": "2000-07-02T12:00:00-06:00", "files": [{"path": "report.html", "sha256": sha, "kind": "report"}]},
              open(os.path.join(d, "manifest.json"), "w"))
    for rel, obj in layout.items():
        os.makedirs(os.path.dirname(os.path.join(d, rel)), exist_ok=True); json.dump(obj, open(os.path.join(d, rel), "w"))
    return f"reports/{version}"
zf = {"bank": "truist", "product": "zelle", "facts": [dict(base, observed_on="2000-07-01")]}
af = {"bank": "truist", "product": "ach", "facts": [{"attribute": "attr-same-day", "value": True, "basis": "disclosed", "confidence": "medium",
      "observed_on": "2000-07-01", "sources": src}]}
mv = make_multi("2000-07-01-v1", {"extract/zelle/truist.json": zf, "extract/ach/truist.json": af})
r = run("python3", "tools/ingest_mi.py", mv); ok, out = check()
expect(r.returncode == 0 and "2 fact(s) applied" in r.stdout and ok, "one report fills two products" + ("" if ok else f"\n{out}"))
r = run("python3", "tools/ingest_mi.py", make_multi("2000-07-02-v1", {"extract/truist.json": zf}))
expect(r.returncode != 0 and "several products" in r.stdout, "multi-product reports need extract/<product>/ folders")
r = run("python3", "tools/ingest_mi.py", make_multi("2000-07-03-v1", {"extract/wire/truist.json": zf}))
expect(r.returncode != 0 and "not listed in the manifest" in r.stdout, "an extract folder for an unlisted product is refused")

shutil.rmtree(tmp)
print(f"\n{'PASS' if not fails else 'FAIL'} — ingest flow ({len(fails)} failure(s))"); sys.exit(1 if fails else 0)

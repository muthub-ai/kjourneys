#!/usr/bin/env python3
"""End-to-end test of the MI ingest flow, run in a throwaway copy of the repo.
Uses obviously fake TEST values and example.invalid URLs; nothing touches the real reports/ folder."""
import hashlib, json, os, shutil, subprocess, sys, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tmp = tempfile.mkdtemp(prefix="kjourneys-ingest-")
files = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True).stdout.split()
if not files:  # not a git checkout (e.g. zip): copy the tree
    shutil.copytree(REPO, tmp, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git", "dist", "fixtures"))
else:
    for f in files:
        os.makedirs(os.path.join(tmp, os.path.dirname(f)), exist_ok=True); shutil.copy2(os.path.join(REPO, f), os.path.join(tmp, f))
for f in ["tools/ingest_mi.py", "tools/validate_journey.py", "tests/test_ingest.py"]:   # use working-tree versions
    shutil.copy2(os.path.join(REPO, f), os.path.join(tmp, f))

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
r = run("python3", "tools/ingest_mi.py", v1); expect(r.returncode != 0 and "already ingested" in r.stdout, "re-ingesting v1 is refused")

v2 = make_report("2000-02-01-v1", {"citi": [
    {"attribute": "attr-daily-limit", "value": 2222, "display": "TEST $2,222", "qualifier": "segment: TEST",
     "basis": "disclosed", "confidence": "high", "observed_on": "2000-02-01", "sources": src},
    {"attribute": "attr-new-payee-warning", "value": "first-payment", "basis": "observed", "confidence": "high",
     "observed_on": "2000-02-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", v2); expect(r.returncode == 0 and "1 fact(s) applied, 1 unchanged" in r.stdout, "v2 applies the changed fact and skips the unchanged one")
hist = json.load(open(os.path.join(tmp, "data/comparisons/zelle/values/citi.json")))["values"]["attr-daily-limit"]
expect(len(hist) == 2 and hist[0]["valid_to"] == "2000-02-01" and hist[1]["supersedes"] == hist[0]["id"], "history kept: old fact closed, new one supersedes it")
ok, out = check(); expect(ok, "repo validates after v2" + ("" if ok else f"\n{out}"))

open(os.path.join(tmp, v1, "report.md"), "a").write("edited later\n")
ok, out = check(); expect(not ok and "sha256 mismatch" in out, "editing an ingested report fails validation")
open(os.path.join(tmp, v1, "report.md"), "w").write("TEST REPORT — not real data\n")

bad = make_report("2000-03-01-v1", {"wells-fargo": [{"attribute": "attr-daily-limit", "value": 1, "basis": "disclosed", "confidence": "low", "observed_on": "2000-03-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", bad); expect(r.returncode != 0 and "competitors" in r.stdout, "MI facts for Wells Fargo are refused")
bad = make_report("2000-04-01-v1", {"pnc": [{"attribute": "attr-daily-limit", "value": 1, "basis": "sample", "confidence": "low", "observed_on": "2000-04-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", bad); expect(r.returncode != 0 and "basis" in r.stdout, "sample basis is refused")
bad = make_report("2000-05-01-v1", {"pnc": [{"attribute": "attr-daily-limit", "value": "lots", "basis": "disclosed", "confidence": "low", "observed_on": "2000-05-01", "sources": src}]})
r = run("python3", "tools/ingest_mi.py", bad); ok, out = check()
expect(r.returncode == 0 and not ok and "not a valid money" in out, "wrongly typed values are caught by validation")

shutil.rmtree(tmp)
print(f"\n{'PASS' if not fails else 'FAIL'} — ingest flow ({len(fails)} failure(s))"); sys.exit(1 if fails else 0)

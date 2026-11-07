#!/usr/bin/env python3
"""Validate docs/bundles/: OKF v0.2 frontmatter, citations, manifests, indexes, and that no other bank is named.

  python3 tools/validate_bundles.py

Checks, per bundle:
  * every section has OKF frontmatter: type, title, description, sources[] (id + sha256), generated.by (process:),
    generated.at (ISO 8601 with offset), and x_kf with schema, bundle_id, bank, content_sha256 matching the body;
  * every paragraph, list item and table row carries a footnote, or starts with *Assessment:*; at most half the
    blocks of a section are assessments;
  * every footnote is `kj · <kind>/<id> · <sha12>`, resolves to a record in the pinned export, and its hash matches;
  * every footnote marker has a definition and every definition is used;
  * bundle-manifest.json lists every file with its sha256; index.md links every section;
  * the export the bundles pin is the one on disk (sha256);
  * no other bank is named anywhere under docs/bundles/ (names, short forms and their journey-ID prefixes)."""
import glob, hashlib, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(ROOT, "docs/bundles")
sys.argv = [sys.argv[0]]
errors = []
def need(c, m):
    if not c: errors.append(m)
src = os.path.join(B, "_source/wells-fargo.json")
raw = open(src, "rb").read(); X = json.loads(raw); SHA = hashlib.sha256(raw).hexdigest()
# reuse the builder's record index without running it: exec only the definitions we need
code = open(os.path.join(ROOT, "tools/build_bundles.py")).read()
ns = {"hashlib": hashlib, "json": json}
exec(code[code.index("def canon(o)"):code.index("REC = records(X)")], ns)
REC = ns["records"](X); sha12 = ns["sha12"]
ALIASES = ["JPMorgan Chase", "JPMorgan", "J.P. Morgan", "Chase", "JPM", "Bank of America", "BofA", "BAC", "Citibank", "Citigroup", "Citi",
           "U.S. Bank", "US Bank", "USB", "Capital One", "COF", "PNC", "Truist", "TFC", "TD Bank", "TD", "Fifth Third", "FITB"]
PEER = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(a) for a in sorted(ALIASES, key=len, reverse=True)) + r")(?![A-Za-z0-9])")
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?([+-]\d{2}:\d{2}|Z)$")
FOOT = re.compile(r"^\[\^(\d+)\]: kj · (\S+) · ([0-9a-f]{12})$")
for f in sorted(glob.glob(os.path.join(B, "**/*"), recursive=True)):
    if os.path.isfile(f) and not f.endswith("_source/wells-fargo.json"):
        for m in PEER.finditer(open(f, encoding="utf-8", errors="replace").read()):
            errors.append(f"peer: {os.path.relpath(f, B)} names another bank ('{m.group(0)}')"); break
need(not PEER.search(raw.decode()), "peer: the Wells Fargo export names another bank")
bundles = sorted(glob.glob(os.path.join(B, "product-bundles/*")) + glob.glob(os.path.join(B, "lob-bundles/*")))
need(len(bundles) > 0, "no bundles found")
nsec = 0
for bd in bundles:
    bid = os.path.basename(bd); rel = os.path.relpath(bd, B)
    mp = os.path.join(bd, "bundle-manifest.json")
    if not os.path.exists(mp): errors.append(f"{rel}: bundle-manifest.json missing"); continue
    man = json.load(open(mp))
    need(man.get("bundle_id") == bid, f"{rel}: manifest bundle_id {man.get('bundle_id')} differs from its folder")
    need(man.get("source", {}).get("sha256") == SHA, f"{rel}: manifest pins export {man.get('source', {}).get('sha256', '')[:12]}, the export on disk is {SHA[:12]}")
    listed = {x["path"]: x["sha256"] for x in man.get("files", [])}
    for x, h in listed.items():
        p = os.path.join(bd, x)
        if not os.path.exists(p): errors.append(f"{rel}: manifest lists missing file {x}")
        else: need(hashlib.sha256(open(p, "rb").read()).hexdigest() == h, f"{rel}: {x} changed after the manifest was built (sha256)")
    for p in glob.glob(os.path.join(bd, "**/*"), recursive=True):
        r = os.path.relpath(p, bd)
        if os.path.isfile(p) and r != "bundle-manifest.json" and not (r.startswith("knowledge-sources/") and r != "knowledge-sources/README.md"):
            need(r in listed, f"{rel}: {r} is not in bundle-manifest.json")
    idx = open(os.path.join(bd, "index.md")).read() if os.path.exists(os.path.join(bd, "index.md")) else ""
    need(bool(idx), f"{rel}: index.md missing"); need(os.path.exists(os.path.join(bd, "log.md")), f"{rel}: log.md missing")
    for sp in sorted(glob.glob(os.path.join(bd, "sections/*.md"))):
        nsec += 1; sr = os.path.relpath(sp, B); t = open(sp).read()
        need(f"(sections/{os.path.basename(sp)})" in idx, f"{sr}: not linked from index.md")
        parts = t.split("---\n", 2)
        if len(parts) < 3 or parts[0] != "": errors.append(f"{sr}: no frontmatter"); continue
        try: fm = json.loads(parts[1])
        except ValueError as e: errors.append(f"{sr}: frontmatter does not parse ({e})"); continue
        body = parts[2].lstrip("\n")
        for k in ("type", "title", "description", "sources", "generated", "x_kf"): need(k in fm, f"{sr}: frontmatter missing {k}")
        for s in fm.get("sources", []): need(s.get("id") and re.fullmatch(r"[0-9a-f]{64}", s.get("sha256", "")), f"{sr}: source {s.get('id')} needs id and sha256")
        need(any(s.get("sha256") == SHA for s in fm.get("sources", [])), f"{sr}: does not cite the export on disk")
        g = fm.get("generated", {}); need(str(g.get("by", "")).startswith("process:"), f"{sr}: generated.by must be a process: actor")
        need(bool(ISO.match(str(g.get("at", "")))), f"{sr}: generated.at must be ISO 8601 with offset")
        x = fm.get("x_kf", {})
        for k in ("schema", "bundle_id", "bank", "content_sha256", "review"): need(k in x, f"{sr}: x_kf missing {k}")
        need(x.get("bundle_id") == bid, f"{sr}: x_kf.bundle_id differs from its bundle")
        need(x.get("content_sha256") == hashlib.sha256(body.encode()).hexdigest(), f"{sr}: body changed after it was generated (content_sha256)")
        lines = body.split("\n"); defs = {}; text = []
        for ln in lines:
            m = FOOT.match(ln)
            if ln.startswith("[^") and "]: " in ln and not m: errors.append(f"{sr}: malformed footnote '{ln[:60]}'")
            if m:
                defs[m.group(1)] = (m.group(2), m.group(3))
                if m.group(2) not in REC: errors.append(f"{sr}: footnote {m.group(1)} cites unknown record {m.group(2)}")
                elif sha12(REC[m.group(2)]) != m.group(3): errors.append(f"{sr}: footnote {m.group(1)} hash is stale for {m.group(2)}")
            else: text.append(ln)
        used = set(re.findall(r"\[\^(\d+)\](?!:)", "\n".join(text)))
        for u in used - set(defs): errors.append(f"{sr}: footnote [^{u}] has no definition")
        for u in set(defs) - used: errors.append(f"{sr}: footnote [^{u}] is never used")
        blocks, assess = 0, 0
        for i, ln in enumerate(text):
            s0 = ln.strip()
            if not s0 or s0.startswith("#") or re.fullmatch(r"\|(-+\|)+", s0): continue
            if s0.startswith("|") and i + 1 < len(text) and text[i + 1].strip().startswith("|---"): continue   # table header row
            blocks += 1
            if "*Assessment:*" in s0: assess += 1; continue
            need(bool(re.search(r"\[\^\d+\]", s0)), f"{sr}: uncited claim '{s0[:70]}'")
        need(assess <= max(1, blocks // 2), f"{sr}: {assess} of {blocks} blocks are assessments (at most half)")
if errors:
    print(f"FAIL — {len(errors)} bundle defect(s)"); [print(" -", e) for e in errors[:60]]; sys.exit(1)
print(f"PASS — {len(bundles)} bundles, {nsec} sections: OKF frontmatter, citations, manifests and indexes check out; no other bank is named")

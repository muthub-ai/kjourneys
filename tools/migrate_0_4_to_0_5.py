#!/usr/bin/env python3
"""Migrate a kjourneys repo from kos-journey/0.4.0 to 0.5.0 (breaking rename).

  portfolio.our_bank      -> portfolio.focus_bank
  party role "our_bank"   -> "focus"
  manifest ontology       -> kos-journey/0.5.0

Usage: python3 tools/migrate_0_4_to_0_5.py   (from the repo root; idempotent)"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def edit(rel, fn):
    p = os.path.join(ROOT, rel); d = json.load(open(p)); changed = fn(d)
    if changed:
        json.dump(d, open(p, "w"), ensure_ascii=False, indent=2); open(p, "a").write("\n")
    print(("migrated  " if changed else "unchanged ") + rel)

def portfolio(d):
    if "our_bank" in d: d["focus_bank"] = d.pop("our_bank"); return True
def parties(d):
    hit = False
    for p in d:
        if p.get("role") == "our_bank": p["role"] = "focus"; hit = True
    return hit
def manifest(d):
    if d.get("ontology") == "kos-journey/0.4.0": d["ontology"] = "kos-journey/0.5.0"; return True

edit("data/portfolio.json", portfolio)
edit("registries/parties.json", parties)
edit("manifest.json", manifest)
print("done — now run scripts/refresh.sh")

#!/usr/bin/env python3
"""Migrate a kjourneys repo from kos-journey/0.5.0 to 0.6.0.

The split source files already keep one folder per product (data/comparisons/<product>/), so the
only file change is the ontology version in manifest.json. The assembled instance changes shape
(comparison -> comparisons[]), which tools/assemble.py produces automatically. Idempotent."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "manifest.json"); m = json.load(open(p))
if m.get("ontology") == "kos-journey/0.5.0":
    m["ontology"] = "kos-journey/0.6.0"; json.dump(m, open(p, "w"), indent=2); open(p, "a").write("\n"); print("migrated  manifest.json")
else:
    print("unchanged manifest.json")
print("done — now run scripts/refresh.sh")

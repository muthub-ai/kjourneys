#!/usr/bin/env python3
"""Render dist/index.html from site/template.html + dist/kjourneys.json + schema/journey-ontology.yaml.
The page is self-contained (data inlined), so it can be published as an artifact or static file."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t = open(os.path.join(ROOT, "site/template.html")).read()
data = json.load(open(os.path.join(ROOT, "dist/kjourneys.json")))
schema = open(os.path.join(ROOT, "schema/journey-ontology.yaml")).read()
html = t.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__SCHEMA__", json.dumps(schema, ensure_ascii=False))
open(os.path.join(ROOT, "dist/index.html"), "w").write(html)
print(f"built dist/index.html ({len(html)//1024} KB)")

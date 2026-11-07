# Wells Fargo bundles

Line-of-business and product bundles for Wells Fargo money movement, in [OKF v0.2](https://github.com/inkeep/open-knowledge), laid out like the application bundles in kbundles. Wells Fargo only: no other bank appears, by construction.

```
docs/bundles/
  index.md  log.md                    root index and insert-only log (generated)
  _source/wells-fargo.json            the Wells Fargo-only export every bundle pins by sha256
  lob-bundles/<lob>/                  one per Wells Fargo reportable segment (wf-cbl, wf-cb, wf-cib, wf-wim)
  product-bundles/<product>/          one per marketed product (wf-p01-zelle … wf-p15-…)
    bundle-manifest.json              every file and its sha256, the pinned export, generated.by/at
    index.md · log.md                 OKF reserved files: index of sections, insert-only log
    knowledge-source.json             owners, steward and approver (to assign)
    sections/01-…07-*.md              cited sections (lines of business have five)
    journey-graph/                    script-built facts: metrics.json, graph.json — never edit by hand
    knowledge-sources/                human-authored material (PRDs, decisions, roadmap); never generated
```

**Hierarchy.** Line of business → product → application. A product bundle names its owning line of business and any others it serves; its journeys link to application bundles through app IDs.

## How it is built

```bash
python3 tools/export_focus.py      # dist/kjourneys.json → _source/wells-fargo.json (Wells Fargo records only)
python3 tools/build_bundles.py     # export → bundles (deterministic: rebuilding gives the same bytes)
python3 tools/validate_bundles.py  # OKF frontmatter, citations, manifests, indexes, no other bank named
```

`scripts/refresh.sh` and `make check` run all three. CI fails if the export or bundles are out of date (`--check`) or invalid.

## Rules

- **Wells Fargo only.** The export leaves out every other bank's records. Where a Wells Fargo record's own text names another bank, the name becomes "a peer bank". Best practice appears as a number (the highest score any bank reached), never as a bank. The validator fails on any other bank's name anywhere in this folder.
- **Every claim is cited.** Each paragraph, list item and table row ends with a footnote `kj · <kind>/<id> · <sha12>` pointing at a record in the pinned export, with that record's hash. A block with no citation must start with `*Assessment:*`, and at most half the blocks of a section may be assessments.
- **Machine-generated, human-verified.** Sections are `generated.by: process:build-bundles` and submitted as candidates. `verified[]` is appended when an owner reviews them. Add human material under `knowledge-sources/` only.
- **Lines of business** come from Wells Fargo's Q3 2026 Form 10-Q (`registries/lines-of-business.json`). Each product's owning line of business is inferred from its MI segments; the three commercial products are marked to confirm.

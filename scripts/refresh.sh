#!/usr/bin/env bash
# Rebuild kjourneys on the current branch. Safe to rerun as often as you like.
#
#   scripts/refresh.sh                                   validate, test, rebuild site and exports
#   scripts/refresh.sh reports/2026-11-20-v1             ingest (or re-ingest) that MI report first
#   scripts/refresh.sh reports/2026-11-20-v1 --commit    ...then commit data + report on this branch
#   scripts/refresh.sh reports/2026-11-20-v1 --commit --push
#
# Rerunning a report version rolls back what it wrote before and applies its extracts afresh,
# so fix an extract and run the same command again.
# Output: dist/index.html (journey site), dist/kjourneys.json, dist/facts.jsonl, dist/coverage.json, dist/summary.md
set -euo pipefail
cd "$(dirname "$0")/.."

REPORT=""; COMMIT=0; PUSH=0
for a in "$@"; do
  case "$a" in
    --commit) COMMIT=1 ;;
    --push)   PUSH=1; COMMIT=1 ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    reports/*) REPORT="${a%/}" ;;
    *) echo "unknown argument: $a (see --help)"; exit 2 ;;
  esac
done

step() { printf '\n\033[1m▸ %s\033[0m\n' "$1"; }
python3 -c "import jsonschema, rfc3339_validator" 2>/dev/null || { echo "Missing Python packages. Run: pip install -r requirements.txt"; exit 1; }

if [[ -n "$REPORT" ]]; then
  [[ -f "$REPORT/manifest.json" ]] || { echo "$REPORT/manifest.json not found"; exit 1; }
  step "Ingest $REPORT"
  if ! python3 tools/ingest_mi.py "$REPORT"; then
    echo; echo "Nothing was written. Fix the report folder and rerun the same command."; exit 1
  fi
fi

step "Assemble, validate, test, build site, export"
if ! make -B -s check; then
  echo
  echo "Checks failed. Fix the extract (or data) and rerun the same command;"
  echo "re-ingesting a version replaces what it wrote. To discard instead:"
  echo "  git checkout -- data registries reports/ingest-log.json"
  exit 1
fi

step "Data status"
cat dist/summary.md
echo; echo "Site: dist/index.html"

if [[ $COMMIT -eq 1 ]]; then
  step "Commit on $(git rev-parse --abbrev-ref HEAD)"
  git add data registries reports
  if git diff --cached --quiet; then
    echo "No data changes to commit."
  else
    msg="refresh: ${REPORT:+ingest ${REPORT#reports/}}"; [[ -z "$REPORT" ]] && msg="refresh: data update"
    git commit -q -m "$msg" && git log --oneline -1
  fi
  if [[ $PUSH -eq 1 ]]; then
    step "Push"
    git push origin HEAD
  fi
fi

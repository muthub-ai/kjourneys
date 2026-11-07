#!/usr/bin/env bash
# CI gate: the assembled instance must PASS; every negative fixture must FAIL.
set -u
cd "$(dirname "$0")/.."
S=schema/journey-ontology.schema.json
status=0
python3 tools/validate_journey.py dist/kjourneys.json $S >/dev/null || { echo "FAIL assembled instance"; status=1; }
python3 tests/make_fixtures.py >/dev/null
for f in tests/fixtures/*.json; do
  if python3 tools/validate_journey.py "$f" $S >/dev/null 2>&1; then echo "HOLE  $(basename "$f") passed but should fail"; status=1
  else echo "ok    $(basename "$f")"; fi
done
exit $status

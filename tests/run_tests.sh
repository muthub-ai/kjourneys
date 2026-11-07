#!/usr/bin/env bash
# CI gate: the assembled instance must PASS; every negative fixture must FAIL, and for its own reason
# (the validator's output must contain the message listed in tests/fixtures/expect.json). A crash is not a pass.
set -u
cd "$(dirname "$0")/.."
S=schema/journey-ontology.schema.json
status=0
python3 tools/validate_journey.py dist/kjourneys.json $S >/dev/null || { echo "FAIL assembled instance"; status=1; }
python3 tests/make_fixtures.py >/dev/null || { echo "FAIL could not write fixtures"; exit 1; }
for f in tests/fixtures/m*.json; do
  n=$(basename "$f" .json)
  want=$(python3 -c "import json,sys; print(json.load(open('tests/fixtures/expect.json'))[sys.argv[1]])" "$n")
  out=$(python3 tools/validate_journey.py "$f" $S 2>&1); rc=$?
  if [ $rc -eq 0 ]; then echo "HOLE  $n passed but should fail"; status=1
  elif echo "$out" | grep -q "Traceback"; then echo "CRASH $n (validator raised instead of reporting)"; status=1
  elif ! echo "$out" | grep -qF -- "$want"; then echo "WRONG $n failed, but not with: $want"; status=1
  else echo "ok    $n"; fi
done
exit $status

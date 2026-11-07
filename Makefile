.PHONY: check validate test site export ingest clean
check: validate test site export   ## everything CI runs

dist/kjourneys.json: $(shell find manifest.json registries data -name '*.json')
	python3 tools/assemble.py

validate: dist/kjourneys.json
	python3 tools/validate_journey.py dist/kjourneys.json schema/journey-ontology.schema.json

test: dist/kjourneys.json
	bash tests/run_tests.sh
	python3 tests/test_ingest.py

site: dist/kjourneys.json
	python3 tools/build_site.py

export: dist/kjourneys.json
	python3 tools/export.py

ingest:                             ## make ingest REPORT=reports/2026-11-20-v1
	@test -n "$(REPORT)" || (echo "usage: make ingest REPORT=reports/<version>"; exit 1)
	python3 tools/ingest_mi.py $(REPORT)
	$(MAKE) -B check

clean:
	rm -rf dist tests/fixtures

.PHONY: check validate test bundles site export ingest refresh clean
check: validate test bundles site export   ## what scripts/refresh.sh runs

dist/kjourneys.json: $(shell find manifest.json registries data -name '*.json')
	python3 tools/assemble.py

validate: dist/kjourneys.json
	python3 tools/validate_journey.py dist/kjourneys.json schema/journey-ontology.schema.json

test: dist/kjourneys.json
	bash tests/run_tests.sh
	python3 tests/test_ingest.py

bundles: dist/kjourneys.json         ## Wells Fargo-only export → product and line-of-business bundles (docs/bundles)
	python3 tools/export_focus.py
	python3 tools/build_bundles.py
	python3 tools/validate_bundles.py

site: dist/kjourneys.json bundles
	python3 tools/build_site.py

export: dist/kjourneys.json
	python3 tools/export.py

ingest:                             ## make ingest REPORT=reports/2026-11-20-v1
	@test -n "$(REPORT)" || (echo "usage: make ingest REPORT=reports/<version>"; exit 1)
	scripts/refresh.sh $(REPORT)

refresh:                            ## make refresh [REPORT=reports/<version>]
	scripts/refresh.sh $(REPORT)

clean:
	rm -rf dist tests/fixtures

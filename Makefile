.PHONY: check validate test site export clean
check: validate test site export   ## everything CI runs

dist/kjourneys.json: $(shell find manifest.json registries data -name '*.json')
	python3 tools/assemble.py

validate: dist/kjourneys.json
	python3 tools/validate_journey.py dist/kjourneys.json schema/journey-ontology.schema.json

test: dist/kjourneys.json
	bash tests/run_tests.sh

site: dist/kjourneys.json
	python3 tools/build_site.py

export: dist/kjourneys.json
	python3 tools/export.py

clean:
	rm -rf dist tests/fixtures

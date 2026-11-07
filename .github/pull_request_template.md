## What this changes

<!-- e.g. Adds market-intelligence facts for Citi Zelle (11 attributes) -->

## Checklist

- [ ] `make check` prints PASS and no HOLE lines
- [ ] Every new fact has a source in `registries/sources.json`
- [ ] Competitor facts are observed, disclosed or inferred (never sample or internal)
- [ ] Changed facts were superseded, not overwritten (old entry has `valid_to`)

### Competitor data only (`data/comparisons/**`)

- [ ] Sources are public or first-hand observation, not from logins we aren't entitled to, NDAs or former employees
- [ ] No personal information and no material non-public information
- [ ] Legal reviewer requested

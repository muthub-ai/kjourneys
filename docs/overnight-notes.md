# Overnight notes — 2026-11-07

What was built while you were away, and what needs your decision. Newest first.

## MI v2 landed and is live

`reports/2026-11-07-v2/` arrived at 01:09 Central and is imported, checked, pushed and republished.

- **Wells Fargo:** index **69.6, #3** (v1: 69.3, #3), domestic core 68.4. Only the ACH-origination rail mean moved (2.33 → 2.44). 63 findings (24 strengths, 6 high, 18 medium, 15 low); one is new, STR-WF-0024 (domestic wire: in-flow routing-number lookup). Nothing was dropped.
- **Ranking:** Chase 74.4, Citi 72.7, Wells Fargo 69.6, Bank of America 68.6, PNC 68.1, Truist 63.5, U.S. Bank 63.4, Fifth Third 54.3, TD Bank 53.8, Capital One 52.0. The top 10 order is unchanged from v1.
- **The index now reproduces.** v2 publishes its rule (25 × the mean of eleven rail means, push-to-card excluded). The recompute follows it and matches MI exactly, so the "totals don't match" callout is gone. To be candid about v1: my recompute there averaged all cells instead of rail means, so part of v1's 69.3 vs 61.8 gap was method, not only MI's rounding defect.
- **What I changed to take v2:** half-point scores (cells are means), duplicate v1 sources cleared on replace, `supersedes` accepted in manifests. See CHANGELOG 0.9.0.
- **For you:** v2 merges a Wells Fargo logged-in session as its own evidence tier (WF-J29, "observed session"). You deferred the public-repo/observed-session question; it now covers a whole journey, not just one source.

## Decisions to confirm

1. **Commercial products' line of business.** Treasury management and payments is reported in both Commercial Banking and Corporate and Investment Banking (Q3 2026 10-Q). I made Commercial Banking the owner, with Corporate and Investment Banking as "also serves", for WF-P13 Vantage, WF-P14 Gateway APIs and WF-P15 commercial receivables. Vantage also lists Consumer Banking and Lending, because small businesses use it. Change these in `registries/lines-of-business.json`.
2. **Wealth and Investment Management** has a line-of-business bundle but no money-movement product in this study. Keep it (it shows the full Wells Fargo structure), or drop it?
3. **Mentions of other banks in Wells Fargo text.** After the second review, every sentence, clause or aside in a Wells Fargo record that mentions another bank is removed outright (28 passages), not just renamed, so comparisons can't be read back. Source URLs that name another bank are dropped. MI's customer-journey best-practice steps are kept, with the banks they came from removed; say if you'd rather drop those steps too.
4. **Best practice as a number.** Bundles and the map show "best practice" as the highest score any bank reached, without naming the bank. Say if you'd rather drop even the number.
5. **Owners, stewards and approvers** in every `knowledge-source.json` are empty, and every section is a candidate (`verified: []`). Bundles need a named approver before review.
6. **The sample blueprint** is attached to WF-P01 Zelle® (it's a Zelle send). Its apps, controls and KPIs are placeholders.

## Built tonight

- **Second independent review (map and bundles), debated and fixed:** see CHANGELOG 0.8.1. The main fixes: a shared other-bank detector (`tools/peers.py`) with sentence-level removal; the validator now rebuilds and compares byte for byte; insert-only logs; the unattached push-to-card gap shown under a Wells Fargo root node; the map side panel stays Wells Fargo-only; keyboard access on the map.
- **Wells Fargo map** (site, "Wells Fargo map" tab): network and flow views of line of business → product → sub-product → journey → customer journey, with gaps, strengths and sample app IDs. Built only from the Wells Fargo export.
- **Bundles** in `docs/bundles/`: 15 product bundles and 4 line-of-business bundles, OKF v0.2, every claim cited to a hashed record, validated (`tools/validate_bundles.py`), rebuilt identically by CI.
- **`registries/lines-of-business.json`**: Wells Fargo's four reportable segments from the Q3 2026 10-Q, with each product's owning line of business and the rule used.

## MI v2

Checked every 30 minutes. See the log below; when v2 lands it is imported, everything is re-run, and the result is pushed only if all checks pass.

| Time (Central) | Result |
|---|---|
| 01:40 | v2 found on main; imported, all checks passed, pushed, republished |

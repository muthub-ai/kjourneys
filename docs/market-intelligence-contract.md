# Market-intelligence data contract

How the market-intelligence (MI) session delivers its study into kjourneys. Follow it and `scripts/refresh.sh` passes; break a rule and it stops with the reason, before anything is written.

## What you deliver

One folder per delivery, kept exactly as received:

```
reports/<YYYY-MM-DD-vN>/
  manifest.json                              version, producer, received_at, workbook, files + sha256
  money-movement-intelligence.html           the report as read by people (any formats, all preserved)
  Money_Movement_CI_Dossier.docx
  Money_Movement_CI_Sources_and_Verification.docx
  Money_Movement_CI_Data.xlsx                the workbook: the single source the repo reads
```

`manifest.json` names the workbook (`"workbook": "Money_Movement_CI_Data.xlsx"`) and pins every file by sha256. See [reports/README.md](../reports/README.md).

## The workbook

`tools/import_mi_workbook.py` reads these sheets. Others (README, Pivot_Journeys) are ignored.

| Sheet | Becomes |
|---|---|
| Banks | checked against `registries/parties.json` (ten banks, `bank_slug`) |
| Products, SubProducts, Capabilities | the bank's catalog in `data/catalog/<bank>.json` (flags per sub-product), rolled up to capability flags per rail in `data/comparisons/<product>/` |
| Journeys, Steps, Exceptions, Notifications | `data/journeys/<bank>/mi-<journey id>.json`, one moment per step |
| Gaps | `data/findings/<bank>.json` (GAP- and STR- IDs) |
| Composites | `data/composites/<product>.json`: the customer journeys. Each bank journey is linked to one (derived; see the importer) |
| Scores | stage scores 0–4 per bank, rail and stage, in `data/comparisons/<product>/` |
| ScoreTotals | `data/rankings.json` |
| RailParticipation | `data/participation.json` |
| Observations, Verification | `data/observations/<bank>.json`, `data/verifications/<bank>.json` |
| Sources | `registries/sources.json` as `src-<bank>-<sNNN>` (source IDs are numbered per bank) |

Vocabularies the importer accepts, and nothing else:

- **Banks:** `jpmorgan-chase`, `bank-of-america`, `citi`, `wells-fargo`, `us-bank`, `capital-one`, `pnc`, `truist`, `td-bank`, `fifth-third`.
- **Rails:** ZELLE, REQUEST_TO_PAY, ACH_EXTERNAL_TRANSFER, ACH_ORIGINATION, WIRE_DOMESTIC, WIRE_INTERNATIONAL, REMITTANCE, RTP, FEDNOW, PUSH_TO_CARD, BILL_PAY, INTERNAL_TRANSFER, CHECK_DEPOSIT_MOBILE, CASH_ATM_BRANCH, WALLET_INTERSECT, OTHER.
- **Stages:** DISCOVER, SET_UP, INITIATE, REVIEW_AUTHORIZE, EXECUTE_TRACK, CONFIRM_COMPLETE, MANAGE, EXCEPTION, SUPPORT.
- **Evidence levels**, and how they land in the ontology (the original level is kept on every record):

| MI level | basis | confidence |
|---|---|---|
| CONFIRMED_BANK | disclosed | high |
| OBSERVED_SESSION | observed | high |
| THIRD_PARTY | disclosed | medium |
| COMMUNITY, INFERRED, UNKNOWN | inferred | low |

- **Scores:** 0–4 on the MI rubric (4 sets the reference, 3 parity, 2 material friction, 1 only by switching channel or a critical/high gap, 0 absent) or `U`. U stays awaiting and is never counted as 0.
- **Capability flags:** Yes, No, Unknown, or free text (read as Yes, with the text kept as detail). A rail's flag is Yes if any of the bank's sub-products on it has it, No only if every one lacks it, and awaiting otherwise.

## Rules the import and validator enforce

1. **The workbook matches its sha256** in the manifest, and the report files never change after ingest. Corrections arrive as a new version.
2. **Every reference resolves:** sources cited by steps, exceptions, findings and capabilities exist in the Sources sheet; findings point at real journeys, stages and composites; journey IDs are unique per bank.
3. **IDs and types agree:** STR- findings are strengths and GAP- findings are gaps; severities are critical, high, medium or low.
4. **Every record cites its report.** Each imported fact also cites `src-mi-<version>`, the report itself.
5. **Competitors never take sample or internal facts.** Below the line of visibility, competitor steps are what the bank discloses or what MI infers.
6. **History, never overwrite.** A later version that changes a fact closes the old one (`valid_to`) and supersedes it.

## How to submit

1. Add the folder and `manifest.json` (with `workbook` and every file's sha256).
2. Run `scripts/refresh.sh reports/<version>`. It imports the workbook, ingests the comparison facts, validates, runs the tests, and rebuilds the site and exports.
3. If it stops, fix the workbook (as a new version once ingested) and run the same command again. Rerunning a version replaces what it wrote before.
4. When it passes, run it once more with `--commit` (and `--push` if you want).

Have CI legal review competitor facts before the site is shared.

A report without a workbook can still be ingested from hand-written extracts ([mi-extraction.md](mi-extraction.md)).

## What not to collect

- Anything behind a login you are not entitled to, from a former employee, or under NDA. Observed sessions (OBSERVED_SESSION) are Wells Fargo's own accounts only.
- Personal information about bank customers or staff, including account numbers and balances seen in an observed session.
- Material non-public information of any kind.

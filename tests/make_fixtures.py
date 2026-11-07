"""Negative fixtures: each must FAIL validation. Adapted from the CDO round-2 mutation set.
Run from the repo root:  make test"""
import json, copy, os
SRC = json.load(open("dist/kjourneys.json"))
OUT = "tests/fixtures"; os.makedirs(OUT, exist_ok=True)
SAMPLE = "urn:kos:journey:wells-fargo:zelle-send"     # the hand-built blueprint: every optional layer filled in
J = lambda d: next(j for j in d["journeys"] if j["id"] == SAMPLE)
MI = lambda d: next(j for j in d["journeys"] if j.get("source_journey_id"))
C = lambda d: d["comparisons"][0]
WF = lambda d: C(d)["values"]["wells-fargo"]
def cur(d, datatype):
    """the focus bank's current assertion for the first attribute of this datatype that has a value"""
    for a in C(d)["attributes"]:
        if a["datatype"] == datatype:
            h = WF(d).get(a["id"]) or []
            if h and h[-1]["basis"] != "awaiting": return h
    raise SystemExit(f"fixtures: no filled {datatype} attribute in {C(d)['product']}")
def add_enum(d, with_values=True):
    a = {"id": "attr-fixture-enum", "stage": C(d)["attributes"][0]["stage"], "name": "fixture enum", "datatype": "enum", "unit": None,
         "normalization": "fixture"}
    if with_values: a["allowed_values"] = ["a", "b"]
    C(d)["attributes"].append(a)
    for b, row in C(d)["values"].items():
        row[a["id"]] = [{"id": f"urn:kos:assertion:{b}:{C(d)['product']}:fixture-enum:1", "basis": "awaiting", "source_ids": [],
                         "asserted_by": None, "asserted_at": None, "observed_on": None, "valid_to": None, "verified_by": None, "verified_at": None}]
    return a["id"]
cases = {}
def case(name):
    def deco(f): cases[name] = f; return f
    return deco

@case("m1a_duplicate_app_id")
def _(d): a = copy.deepcopy(d["applications"][0]); a["name"] = "Shadow"; d["applications"].append(a)
@case("m1b_duplicate_metric")
def _(d): d["metrics"].append(dict(d["metrics"][0], formula="other"))
@case("m1c_duplicate_control")
def _(d): d["controls"].append(dict(d["controls"][0], type="aml"))
@case("m1d_duplicate_fail_point")
def _(d): J(d)["moments"][1]["fail_points"][0]["id"] = J(d)["moments"][0]["fail_points"][0]["id"]
@case("m2a_variant_reversed")
def _(d): v = J(d)["variants"][1]; v["entry"], v["exit"] = v["exit"], v["entry"]; v["moments"] = list(reversed(v["moments"]))
@case("m2b_variant_entry_off_path")
def _(d): J(d)["variants"][2]["entry"] = J(d)["moments"][10]["id"]
@case("m3a_boolean_not_boolean")
def _(d): cur(d, "boolean")[-1]["value"] = "lots"
@case("m3b_enum_not_allowed")
def _(d):
    aid = add_enum(d); src = cur(d, "boolean")[-1]
    WF(d)[aid] = [dict(src, id=src["id"].rsplit(":", 2)[0] + ":fixture-enum:1", value="whenever-you-like")]
@case("m3c_integer_as_text")
def _(d): cur(d, "number")[-1]["value"] = "three"
@case("m3j_score_not_half_point")
def _(d): cur(d, "number")[-1]["value"] = 2.3
@case("m3d_valid_from_after_to")
def _(d): h = cur(d, "boolean"); h.insert(0, dict(h[-1], id=h[-1]["id"] + "0", valid_from="2027-01-01", valid_to="2026-01-01"))
@case("m3e_bad_datetime")
def _(d): cur(d, "boolean")[-1]["asserted_at"] = "last tuesday"
@case("m3f_dangling_supersedes")
def _(d): cur(d, "number")[-1]["supersedes"] = "urn:kos:assertion:does-not-exist:1"
@case("m3g_unprefixed_principal")
def _(d): cur(d, "number")[-1]["verified_by"] = "bob"
@case("m3h_awaiting_with_value")
def _(d):
    slot = next(h for b, row in d["comparisons"][0]["values"].items() if b != d["portfolio"]["focus_bank"]
                for h in row.values() if h[-1]["basis"] == "awaiting")
    slot[-1]["value"] = 5000
@case("m3i_two_current_assertions")
def _(d): h = cur(d, "number"); h.append(dict(h[-1], id=h[-1]["id"] + "0"))
@case("m4a_published_with_sample")
def _(d): J(d)["status"] = "published"
@case("m4b_mnpi_public")
def _(d): J(d)["governance"].update(classification="public", mnpi=True)
@case("m4c_rejected_in_review")
def _(d): J(d)["status"] = "in-review"; J(d)["governance"]["ci_legal_review"]["status"] = "rejected"
@case("m4d_actual_from_uncertified")
def _(d): J(d)["moments"][0]["kpis"][0].update(actual=99.0, period_end="2026-10-31")
@case("m5a_stage_not_in_journey")
def _(d): J(d)["stages"] = ["set-up", "initiate"]
@case("m5b_wrong_kind_urn")
def _(d):
    old = J(d)["moments"][0]["id"]; new = "urn:kos:control:citi:whatever:m01"
    J(d)["moments"][0]["id"] = new
    for v in J(d)["variants"]:
        v["moments"] = [new if x == old else x for x in v["moments"]]
        if v["entry"] == old: v["entry"] = new
@case("m5c_duplicate_moment_code")
def _(d): J(d)["moments"][0]["code"] = "M07"
@case("m5d_bundle_wrong_app")
def _(d): d["applications"][0]["bundle"] = "application-bundles/zzzzz/"
@case("m5e_unknown_layer")
def _(d): J(d)["moments"][0]["evidence"]["vibes"] = dict(J(d)["moments"][0]["evidence"]["action"])
@case("m5f_duplicate_control_ref")
def _(d): m = J(d)["moments"][0]; m["controls"].append(m["controls"][0])
@case("m5g_focus_bank_missing")
def _(d): d["portfolio"]["banks"].remove("wells-fargo"); del d["comparisons"][0]["values"]["wells-fargo"]
@case("m5h_two_focus_banks")
def _(d): d["parties"][0]["role"] = "focus"
@case("m8a_duplicate_product_comparison")
def _(d): d["comparisons"].append(copy.deepcopy(d["comparisons"][0]))
@case("m8b_comparison_product_not_in_portfolio")
def _(d): d["portfolio"]["products"].remove(d["comparisons"][0]["product"])
@case("m6_enum_without_allowed_values")
def _(d): add_enum(d, with_values=False)
# ---------- MI analytical collections (0.7.0) ----------
@case("m9a_finding_unknown_bank")
def _(d): d["findings"][0]["bank"] = "nowhere-bank"
@case("m9b_gap_typed_as_strength")
def _(d): next(f for f in d["findings"] if f["id"].startswith("GAP-"))["type"] = "strength"
@case("m9c_finding_unknown_journey")
def _(d): d["findings"][0]["journey"] = "urn:kos:journey:citi:does-not-exist"
@case("m9d_duplicate_finding")
def _(d): d["findings"].append(copy.deepcopy(d["findings"][0]))
@case("m9e_composite_unknown_product")
def _(d): d["composites"][0]["product"] = "carrier-pigeon"
@case("m9f_ranking_duplicate_bank")
def _(d): d["rankings"].append(copy.deepcopy(d["rankings"][0]))
@case("m9g_report_version_unknown")
def _(d): d["observations"][0]["report_version"] = "1999-01-01-v1"
@case("m9h_mi_journey_duplicate_source_id")
def _(d):
    a, b = [j for j in d["journeys"] if j.get("source_journey_id") and j["bank"] == MI(d)["bank"]][:2]
    b["source_journey_id"] = a["source_journey_id"]
@case("m10a_journey_unknown_sub_product")
def _(d): next(j for j in d["journeys"] if j.get("sub_product"))["sub_product"] = "WF-P99-S99"
@case("m10b_sub_product_under_wrong_product")
def _(d):
    j = next(j for j in d["journeys"] if j.get("sub_product") and j.get("bank_product"))
    other = next(p for p in d["catalog"] if p["bank"] == j["bank"] and p["id"] != j["bank_product"])
    j["bank_product"] = other["id"]
@case("m10c_customer_journey_unknown")
def _(d): next(j for j in d["journeys"] if j.get("composite"))["composite"] = "CJ-DOES-NOT-EXIST"
@case("m10d_customer_journey_link_unlabeled")
def _(d): next(j for j in d["journeys"] if j.get("composite"))["composite_match"] = None
@case("m10e_catalog_duplicate_sub_product")
def _(d): p = d["catalog"][0]; p["sub_products"].append(copy.deepcopy(p["sub_products"][0]))
@case("m10f_catalog_unknown_capability_flag")
def _(d): d["catalog"][0]["sub_products"][0]["capabilities"]["teleport"] = True
@case("m11a_finding_step_outside_journey")
def _(d): next(f for f in d["findings"] if f.get("journey") and f.get("step"))["step"] = 999
@case("m11b_finding_stage_not_its_step")
def _(d):
    f = next(f for f in d["findings"] if f.get("journey") and f.get("step") and not f.get("step_stage"))
    f["step_stage"] = next(s for s in ["discover", "support"] if s != f["stage"])
@case("m11c_finding_bank_not_its_journey")
def _(d): f = next(f for f in d["findings"] if f.get("journey")); f["bank"] = next(b for b in d["portfolio"]["banks"] if b != f["bank"])
@case("m11d_score_outside_rubric")
def _(d):
    c = next(c for c in d["comparisons"] if any(a["id"].startswith("attr-score-") for a in c["attributes"]))
    h = next(h for row in c["values"].values() for k, h in row.items() if k.startswith("attr-score-") and h[-1]["basis"] != "awaiting"); h[-1]["value"] = 9
@case("m11e_ranking_index_out_of_range")
def _(d): d["rankings"][0]["overall_index"] = -5
@case("m11f_competitor_backstage_observed")
def _(d):
    m = next(m for j in d["journeys"] if j["bank"] != d["portfolio"]["focus_bank"] for m in j["moments"] if "process" in m.get("evidence", {}))
    m["evidence"]["process"]["basis"] = "observed"
@case("m11g_composite_step_unknown")
def _(d): next(f for f in d["findings"] if f.get("composite") and f.get("composite_step"))["composite_step"] = 500
@case("m11h_rail_segment_link_on_other_rail")
def _(d):
    j = next(j for j in d["journeys"] if j.get("composite_match") == "rail-segment")
    j["composite"] = next(c["id"] for c in d["composites"] if c["product"] != j["product"])
@case("m9i_mi_step_unknown_stage")
def _(d): MI(d)["moments"][0]["stage"] = "teleport"

for name, f in cases.items():
    d = copy.deepcopy(SRC); f(d); json.dump(d, open(f"{OUT}/{name}.json", "w"), indent=1)

# competitor facts may never be sample or internal (added with the repo)
d = copy.deepcopy(SRC)
comp = next(b for b in C(d)["values"] if b != d["portfolio"]["focus_bank"])
aid = next(a for a, h in C(d)["values"][comp].items())
h = C(d)["values"][comp][aid]; h[-1] = dict(h[-1], basis="sample", value=True)
json.dump(d, open(f"{OUT}/m7_competitor_sample_fact.json", "w"), indent=1)
# each fixture must fail for its own reason: run_tests.sh checks the validator output contains this text
EXPECT = {"m1a": "unique: app_id", "m1b": "unique: metric", "m1c": "unique: control", "m1d": "unique: fail point",
  "m2a": "out of journey order", "m2b": "must be on its own path", "m3a": "is not a valid boolean", "m3j": "half points allowed", "m3b": "whenever-you-like",
  "m3c": "score 'three'", "m3d": "valid_from after valid_to", "m3e": "last tuesday", "m3f": "supersedes unknown", "m3g": "'bob'",
  "m3h": "awaiting", "m3i": "exactly one current", "m4a": "published but still holds sample", "m4b": "MNPI content must be",
  "m4c": "rejected legal review", "m4d": "not certified real data", "m5a": "not in journey.stages", "m5b": "should be a moment URN",
  "m5c": "moment code 'M07'", "m5d": "bundle path must be", "m5e": "unknown evidence layer", "m5f": "control ref",
  "m5g": "focus_bank must be in banks", "m5h": "exactly one focus bank", "m6_": "without allowed_values", "m7_": "cannot be sample",
  "m8a": "unique: comparison product", "m8b": "is not in portfolio.products", "m9a": "bank nowhere-bank", "m9b": "must use STR- ids",
  "m9c": "journey urn:kos:journey:citi:does-not-exist", "m9d": "unique: finding", "m9e": "product carrier-pigeon",
  "m9f": "unique: ranking bank", "m9g": "1999-01-01-v1", "m9h": "unique: MI journey id", "m9i": "stage teleport",
  "m10a": "WF-P99-S99", "m10b": "does not belong to product", "m10c": "CJ-DOES-NOT-EXIST", "m10d": "without saying how",
  "m10e": "unique: catalog sub-product", "m10f": "capability flag teleport", "m11a": "step 999 is outside", "m11b": "is not the stage of step",
  "m11c": "differs from its journey's bank", "m11d": "score 9 is outside", "m11e": "overall_index -5", "m11f": "backstage cannot be observed",
  "m11g": "composite step 500", "m11h": "a customer journey on another rail"}
names = list(cases) + ["m7_competitor_sample_fact"]
exp = {}
for n in names:
    k = next((k for k in sorted(EXPECT, key=len, reverse=True) if n.startswith(k)), None)
    assert k, f"fixture {n} has no expected message"
    exp[n] = EXPECT[k]
json.dump(exp, open(f"{OUT}/expect.json", "w"), indent=1)
import glob as _g
for f in _g.glob(f"{OUT}/*.json"):
    if os.path.basename(f)[:-5] not in names and not f.endswith("expect.json"): os.remove(f)
print(len(cases) + 1, "fixtures written")

"""Negative fixtures: each must FAIL validation. Adapted from the CDO round-2 mutation set.
Run from the repo root:  make test"""
import json, copy, os
SRC = json.load(open("dist/kjourneys.json"))
OUT = "tests/fixtures"; os.makedirs(OUT, exist_ok=True)
J = lambda d: d["journeys"][0]
WF = lambda d: d["comparison"]["values"]["wells-fargo"]
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
@case("m3a_money_not_number")
def _(d): WF(d)["attr-daily-limit"][0].update(value="lots of money", basis="disclosed")
@case("m3b_enum_not_allowed")
def _(d): WF(d)["attr-cancel-pending"][0]["value"] = "whenever-you-like"
@case("m3c_integer_as_text")
def _(d): WF(d)["attr-enroll-steps"][0]["value"] = "three"
@case("m3d_valid_from_after_to")
def _(d): WF(d)["attr-payee-name-shown"][0].update(valid_from="2027-01-01", valid_to="2026-01-01")
@case("m3e_bad_datetime")
def _(d): WF(d)["attr-notifications"][0]["asserted_at"] = "last tuesday"
@case("m3f_dangling_supersedes")
def _(d): WF(d)["attr-stepup-trigger"][0]["supersedes"] = "urn:kos:assertion:does-not-exist:1"
@case("m3g_unprefixed_principal")
def _(d): WF(d)["attr-stepup-trigger"][0]["verified_by"] = "bob"
@case("m3h_awaiting_with_value")
def _(d):
    slot = next(h for b, row in d["comparison"]["values"].items() if b != d["portfolio"]["focus_bank"]
                for h in row.values() if h[-1]["basis"] == "awaiting")
    slot[-1]["value"] = 5000
@case("m3i_two_current_assertions")
def _(d): h = WF(d)["attr-enroll-steps"]; h.append(dict(h[0], id=h[0]["id"][:-1] + "2"))
@case("m4a_published_with_sample")
def _(d): J(d)["status"] = "published"
@case("m4b_mnpi_public")
def _(d): J(d)["governance"].update(classification="public", mnpi=True)
@case("m4c_rejected_in_review")
def _(d): J(d)["status"] = "in-review"; J(d)["governance"]["ci_legal_review"]["status"] = "rejected"
@case("m4d_actual_from_uncertified")
def _(d): J(d)["moments"][0]["kpis"][0].update(actual=99.0, period_end="2026-10-31")
@case("m5a_stage_not_in_journey")
def _(d): J(d)["stages"] = ["setup", "choose"]
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
def _(d): d["portfolio"]["banks"].remove("wells-fargo"); del d["comparison"]["values"]["wells-fargo"]
@case("m5h_two_focus_banks")
def _(d): d["parties"][0]["role"] = "focus"
@case("m6_enum_without_allowed_values")
def _(d): d["comparison"]["attributes"][0].pop("allowed_values")

for name, f in cases.items():
    d = copy.deepcopy(SRC); f(d); json.dump(d, open(f"{OUT}/{name}.json", "w"), indent=1)

# competitor facts may never be sample or internal (added with the repo)
d = copy.deepcopy(SRC)
comp = next(b for b in d["comparison"]["values"] if b != d["portfolio"]["focus_bank"])
d["comparison"]["values"][comp]["attr-enroll-steps"] = [dict(SRC["comparison"]["values"]["wells-fargo"]["attr-enroll-steps"][0],
    id=f"urn:kos:assertion:{comp}:zelle:enroll-steps:9")]
json.dump(d, open(f"{OUT}/m7_competitor_sample_fact.json", "w"), indent=1)
print(len(cases) + 1, "fixtures written")

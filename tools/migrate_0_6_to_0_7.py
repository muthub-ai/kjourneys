#!/usr/bin/env python3
"""Migrate kjourneys from kos-journey/0.6.0 to 0.7.0: adopt the market-intelligence taxonomy.

  banks     the study's ten banks (Fifth Third replaces the Citizens placeholder; U.S. Bank is us-bank)
  products  one product per payment rail (16), each with a family for grouping
  stages    the nine journey stages DISCOVER … SUPPORT
  channels  adds phone, voice/chat assistant and API/treasury portal
  journey   the Wells Fargo sample blueprint's moments move onto the nine stages
  zelle     the placeholder Zelle comparison (11 drafted questions, sample data) is removed;
            comparisons are now generated from the MI workbook by tools/import_mi_workbook.py

Usage: python3 tools/migrate_0_6_to_0_7.py   (from the repo root; idempotent)"""
import json, os, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def jl(p): return json.load(open(os.path.join(ROOT, p)))
def jd(p, o):
    p = os.path.join(ROOT, p); tmp = p + ".tmp"
    with open(tmp, "w") as f: json.dump(o, f, ensure_ascii=False, indent=2); f.write("\n")
    os.replace(tmp, p)

BANKS = [("jpmorgan-chase", "JPMorgan Chase"), ("bank-of-america", "Bank of America"), ("citi", "Citi"),
         ("wells-fargo", "Wells Fargo"), ("us-bank", "U.S. Bank"), ("capital-one", "Capital One"), ("pnc", "PNC"),
         ("truist", "Truist"), ("td-bank", "TD Bank"), ("fifth-third", "Fifth Third")]
PRODUCTS = [("zelle", "Zelle", "ZELLE", "zelle"), ("request-to-pay", "Request to pay", "REQUEST_TO_PAY", "request"),
            ("ach-external-transfer", "ACH external transfer", "ACH_EXTERNAL_TRANSFER", "ach"),
            ("ach-origination", "ACH origination (business)", "ACH_ORIGINATION", "ach"),
            ("wire-domestic", "Domestic wire", "WIRE_DOMESTIC", "wire"), ("wire-international", "International wire", "WIRE_INTERNATIONAL", "wire"),
            ("remittance", "Remittance", "REMITTANCE", "wire"), ("rtp", "RTP (The Clearing House)", "RTP", "instant"),
            ("fednow", "FedNow", "FEDNOW", "instant"), ("push-to-card", "Push to card", "PUSH_TO_CARD", "instant"),
            ("bill-pay", "Bill pay", "BILL_PAY", "bill-pay"), ("internal-transfer", "Internal transfer", "INTERNAL_TRANSFER", "internal"),
            ("check-deposit-mobile", "Mobile check deposit", "CHECK_DEPOSIT_MOBILE", "deposit"),
            ("cash-atm-branch", "Cash, ATM and branch", "CASH_ATM_BRANCH", "cash"),
            ("wallet-intersect", "Digital wallets", "WALLET_INTERSECT", "wallet"), ("other", "Other money movement", "OTHER", "other")]
STAGES = [("discover", "Discover", "Find the right way to move money"), ("set-up", "Set up", "Be ready to pay or be paid"),
          ("initiate", "Initiate", "Say who, how much and when"), ("review-authorize", "Review & authorize", "Be sure before it goes"),
          ("execute-track", "Execute & track", "See it move"), ("confirm-complete", "Confirm & complete", "Know it arrived"),
          ("manage", "Manage", "Change, cancel or repeat"), ("exception", "Exception", "Recover when something goes wrong"),
          ("support", "Support", "Get help from a person or assistant")]
REMAP = {"M01": "discover", "M02": "set-up", "M03": "initiate", "M04": "initiate", "M05": "initiate", "M06": "review-authorize",
         "M07": "execute-track", "M08": "execute-track", "M09": "confirm-complete", "M10": "manage", "M11": "exception"}

man = jl("manifest.json")
if man["ontology"] == "kos-journey/0.7.0":
    print("already 0.7.0 — nothing to do"); raise SystemExit
assert man["ontology"] == "kos-journey/0.6.0", man["ontology"]

old = {p["id"]: p for p in jl("registries/parties.json")}
jd("registries/parties.json", [{"id": i, "name": n, "lei": old.get(i, {}).get("lei"), "lei_basis": "awaiting",
                                 "role": "focus" if i == "wells-fargo" else "competitor"} for i, n in BANKS])
oldp = {p["id"]: p for p in jl("registries/products.json")}
jd("registries/products.json", [{"id": i, "name": n, "rail": r, "family": f, "fibo_class": None,
                                  "journeys": oldp.get(i, {}).get("journeys", [])} for i, n, r, f in PRODUCTS])
cl = jl("registries/codelists.json")
cl["stages"] = [{"id": i, "name": n, "customer_goal": g} for i, n, g in STAGES]
for ch in ["phone", "voice-chat-assistant", "api-treasury-portal"]:
    if ch not in cl["channels"]: cl["channels"].append(ch)
jd("registries/codelists.json", cl)
pf = jl("data/portfolio.json")
pf.update({"banks": [i for i, _ in BANKS], "products": [i for i, *_ in PRODUCTS],
           "banks_note": "Ten largest US retail banks by holding-company assets (June 30, 2026), as scoped by the MI study"})
jd("data/portfolio.json", pf)
jp = "data/journeys/wells-fargo/zelle-send.json"; j = jl(jp)
j["stages"] = [i for i, *_ in STAGES]
for m in j["moments"]: m["stage"] = REMAP[m["code"]]
jd(jp, j)
shutil.rmtree(os.path.join(ROOT, "data/comparisons/zelle"), ignore_errors=True)
man["ontology"] = "kos-journey/0.7.0"; jd("manifest.json", man)
print("migrated to kos-journey/0.7.0 — now run tools/import_mi_workbook.py, then scripts/refresh.sh")

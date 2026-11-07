"""Who counts as "another bank", and how to find them in text. Shared by tools/export_focus.py and tools/validate_bundles.py,
so the export and its validator can never disagree about what a peer mention is.

Three detectors, all case-insensitive:
  1. long names, matched with spaces and punctuation removed ("JPMorganChase", "J.P. Morgan", "bank-of-america",
     "usbank.com", URL slugs like cfpb-sues-jpmorgan-chase-bank-of-america-…);
  2. short names, tickers and journey-ID prefixes, matched as whole words or ID forms ("Chase", "Citi's", "PNC",
     "BofA", "TD Bank", "JPM-J06#1", "CITI-J01", "53-J01", "5/3");
  3. web domains of other banks (chase.com, bankofamerica.com, citi.com, usbank.com, capitalone.com, pnc.com,
     truist.com, td.com, tdbank.com, 53.com).
Known false positives are allowed explicitly (BAC Credomatic is a Central American bank, not Bank of America)."""
import re

LONG = ["jpmorganchase", "jpmorgan", "bankofamerica", "capitalone", "fifththird", "usbank", "truist", "citibank", "citigroup",
        "tdbank", "merrilledge", "pncbank"]
SHORT = ["chase", "citi", "pnc", "bofa", "boa", "jpm", "j\\.p\\. ?morgan", "jp morgan", "u\\.? ?s\\.? bank", "td bank", "td", "fifth third",
         "5/3", "capital one", "truist"]
ID_PREFIX = ["JPM", "BAC", "CITI", "USB", "COF", "PNC", "TFC", "TD", "FITB", "53"]
DOMAINS = ["chase.com", "jpmorganchase.com", "jpmorgan.com", "bankofamerica.com", "bofa.com", "citi.com", "citibank.com", "online.citi.com",
           "usbank.com", "capitalone.com", "pnc.com", "truist.com", "td.com", "tdbank.com", "53.com"]
ALLOW = [re.compile(r"\bBAC Credomatic\b", re.I)]           # not Bank of America
SHORT_RE = re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(SHORT) + r")(?:'s|’s)?(?![A-Za-z0-9])", re.I)
ID_RE = re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(ID_PREFIX) + r")-(?:[JPC]\d+|P\d+-S\d+|\d)", re.I)
DOM_RE = re.compile(r"(?<![A-Za-z0-9.-])(?:www\.|[a-z0-9-]+\.)*(?:" + "|".join(re.escape(x) for x in DOMAINS) + r")\b", re.I)

def _mask_allowed(t):
    for a in ALLOW: t = a.sub(lambda m: "#" * len(m.group(0)), t)
    return t

def find(text):
    """Return the peer mentions in text (empty list when clean)."""
    if not isinstance(text, str) or not text: return []
    t = _mask_allowed(text)
    hits = [m.group(0) for m in SHORT_RE.finditer(t)] + [m.group(0) for m in ID_RE.finditer(t)] + [m.group(0) for m in DOM_RE.finditer(t)]
    squashed = re.sub(r"[^a-z0-9]", "", t.lower())
    hits += [n for n in LONG if n in squashed]
    return hits

def mentions(text): return bool(find(text))

_SENT = re.compile(r"(?<=[.!?;])\s+(?=[A-Z(\"'])")
def strip(text):
    """Remove every parenthetical, clause and sentence that mentions another bank. Returns (clean_text, removed_count)."""
    if not mentions(text): return text, 0
    removed = 0
    # parentheticals and bracketed asides first: "(e.g., Chase, BofA)", "[composite: …]"
    def drop_paren(m):
        nonlocal removed
        if mentions(m.group(0)): removed += 1; return ""
        return m.group(0)
    prev = None
    while prev != text:
        prev = text; text = re.sub(r"\s*[\(\[][^()\[\]]*[\)\]]", drop_paren, text)
    # then whole sentences, then em-dash or semicolon clauses inside a sentence
    out = []
    for s in _SENT.split(text):
        if mentions(s):
            parts = re.split(r"\s+[—–]\s+|;\s+", s)
            keep = [p for p in parts if not mentions(p)]
            removed += len(parts) - len(keep)
            if keep and len(keep) < len(parts): out.append("; ".join(keep).rstrip(" ;,") + ("" if keep[-1].rstrip().endswith((".", "!", "?")) else "."))
        else: out.append(s)
    clean = re.sub(r"\s{2,}", " ", " ".join(out)).strip()
    clean = re.sub(r"\s+([.,;:])", r"\1", clean)
    return (clean or "[Comparison with other banks removed.]"), max(removed, 1)

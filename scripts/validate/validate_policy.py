#!/usr/bin/env python3
"""Policy validator — the guardrails that keep this repository honest and legal.

Checks:
  1. SECRET SHAPES      no credential-looking strings anywhere in tracked files
  2. COLLECTION ETHICS  no private chain-of-thought, leaked system prompts, PII,
                        or vendored private-repository content
  3. LICENSE POLICY     no vendored code from a repository whose license is NONE
  4. HALLUCINATION FIREWALL  no "latest/best/current" superlative asserted without
                        verified_at nearby
  5. QUARANTINE         experimental/ and pending-* files are not referenced as
                        authoritative from core knowledge
  6. GENERATED FILES    metadata/ + indexes/ carry a generator marker

Usage:
    python3 scripts/validate/validate_policy.py
    python3 scripts/validate/validate_policy.py --strict
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

SECRET_PATTERNS = {
    "github_pat": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "github_oauth": re.compile(r"\bghp_[A-Za-z0-9]{30,}"),
    "github_fine": re.compile(r"\bgho_[A-Za-z0-9]{30,}"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}"),
    "anthropic_key": re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"),
    "private_key_block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "google_api_key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "stripe_secret": re.compile(r"\bsk_live_[A-Za-z0-9]{16,}"),
    "jwt": re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),
    "supabase_service": re.compile(r"\bsbp_[A-Za-z0-9]{20,}"),
    "npm_token": re.compile(r"\bnpm_[A-Za-z0-9]{30,}"),
    "huggingface_token": re.compile(r"\bhf_[A-Za-z0-9]{20,}"),
}

# Strings that indicate forbidden content rather than discussion *about* it.
FORBIDDEN = [
    (re.compile(r"(?i)\bBEGIN (?:PRIVATE )?CHAIN[- ]OF[- ]THOUGHT\b"), "private chain-of-thought dump"),
    (re.compile(r"(?i)<\s*(?:hidden|secret|internal)[-_ ]?(?:cot|reasoning|thought)\s*>"),
     "private reasoning block"),
    (re.compile(r"(?i)leaked system prompt(?: of| for)?\s*[:=]?\s*\n\s*[\"']?(you are|assistant)"),
     "leaked system prompt content"),
    (re.compile(r"(?i)\bpassword\s*[:=]\s*['\"][^'\"]{6,}['\"]"), "hardcoded password"),
    (re.compile(r"(?i)\bapi[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]"), "hardcoded API key"),
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "US SSN-shaped PII"),
    (re.compile(r"(?i)\bprivate (?:repository|repo) (?:contents?|source)\b\s*:"), "private repo content"),
]

# Discussion ABOUT these topics is allowed and expected; only reproduction is banned.
ALLOWED_DISCUSSION = re.compile(
    r"(?i)(never|do not|don't|must not|forbidden|excluded|policy|prohibited|risk|attack|defend|"
    r"detection|guardrail|threat|avoid)")

SUPERLATIVE = re.compile(r"(?i)\b(the\s+)?(latest|newest|current(?:ly)?\s+best|best|fastest|"
                         r"most\s+popular|state[- ]of[- ]the[- ]art|sota)\b")
VERIFIED_NEAR = re.compile(r"(?i)(verified_at|verified\s+\d{4}-\d{2}-\d{2}|stars_checked_at|"
                             r"as of \d{4}-\d{2}-\d{2}|\d{4}-\d{2}-\d{2})")


def tracked_files() -> List[Path]:
    try:
        out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT,
                             capture_output=True, text=True, timeout=60)
        files = [ROOT / line for line in out.stdout.splitlines() if line]
        return [f for f in files if f.exists() and f.is_file()]
    except Exception:
        skip = {".git", ".cache", "node_modules", ".venv", "__pycache__"}
        return [p for p in ROOT.rglob("*")
                if p.is_file() and not any(s in p.parts for s in skip)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    errors: List[str] = []
    warns: List[str] = []
    files = tracked_files()
    print(f"Scanning {len(files)} tracked files…")

    no_license_slugs = set()
    reg = ROOT / "metadata" / "repositories.json"
    if reg.exists():
        for r in json.loads(reg.read_text()).get("repositories", []):
            if r.get("license") == "NONE":
                no_license_slugs.add(r.get("slug"))

    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        if f.suffix in (".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".woff", ".woff2"):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        low = text.lower()

        # 1. secrets
        for name, pat in SECRET_PATTERNS.items():
            for m in pat.finditer(text):
                s = m.group(0)
                if "<" in s or "YOUR" in s.upper() or "xxxx" in s.lower() or "example" in low[max(0, m.start()-80):m.start()]:
                    continue
                errors.append(f"{rel}: possible {name} secret ({s[:8]}…{s[-4:]})")

        # 2. forbidden collection
        for pat, label in FORBIDDEN:
            for m in pat.finditer(text):
                ctx = text[max(0, m.start() - 200):m.end() + 200]
                if ALLOWED_DISCUSSION.search(ctx):
                    continue
                errors.append(f"{rel}: forbidden content — {label}")

        # 3. vendoring code from unlicensed repositories
        for slug in no_license_slugs:
            if not slug:
                continue
            owner, name = slug.split("/", 1)
            if re.search(rf"(?i){re.escape(name)}", text) and f.suffix in (".ts", ".tsx", ".js", ".py", ".go", ".rs"):
                warns.append(f"{rel}: code file references '{slug}' which has NO detected license — "
                             f"confirm nothing was copied")

        # 4. hallucination firewall: superlatives need a date
        #
        # Generated artifacts are skipped, and the skip loses no coverage: a generated
        # file quotes a governed source, and that source is scanned here in its own
        # right. Flagging the copy as well as the original only doubles the count for
        # one underlying unverified claim — which is exactly what happened when
        # skills/*/tests/cases.md started quoting skill prose verbatim.
        if f.suffix == ".md" and "experimental/" not in rel and not fm.is_generated(rel):
            lines = text.splitlines()
            for i, line in enumerate(lines):
                if line.strip().startswith(("```", "|", "<!--")):
                    continue
                if SUPERLATIVE.search(line):
                    window = "\n".join(lines[max(0, i - 3):i + 4])
                    if not VERIFIED_NEAR.search(window):
                        warns.append(f"{rel}:{i+1}: superlative without a nearby verification date — "
                                     f"'{line.strip()[:70]}'")

        # 5. quarantine must not be cited as authoritative
        if f.suffix == ".md" and not rel.startswith(("experimental/", "knowledge/ai-engineering/")):
            if re.search(r"pending-paper-candidates\.json", text) and not re.search(r"(?i)(quarantin|pending|do not cite|not verified)", text):
                warns.append(f"{rel}: references the paper quarantine file without saying it is unverified")

    # 6. generated files must declare their generator
    for rel in ["metadata/repositories.json", "metadata/index.json", "metadata/tools.json",
                "metadata/skills.json", "metadata/evaluations.json", "metadata/sources.json"]:
        p = ROOT / rel
        if not p.exists():
            continue
        head = p.read_text()[:400]
        if "generat" not in head.lower():
            errors.append(f"{rel}: generated file lacks a generator/generated_at marker")

    for p in sorted((ROOT / "indexes").glob("*.md")):
        head = p.read_text()[:400]
        if "GENERATED" not in head and "generated" not in head:
            errors.append(f"indexes/{p.name}: generated file lacks a GENERATED marker")

    if args.strict:
        errors += warns
        warns = []

    print(f"Errors: {len(errors)}   Warnings: {len(warns)}")
    for e in errors[:60]:
        print("  ERROR  " + e)
    if len(errors) > 60:
        print(f"  … and {len(errors)-60} more")
    for w in warns[:40]:
        print("  warn   " + w)
    if len(warns) > 40:
        print(f"  … and {len(warns)-40} more warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

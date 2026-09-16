#!/usr/bin/env python3
"""Generate human-readable repository cards from metadata/repositories.json.

Direction of truth:  GitHub API -> metadata/repositories.json -> repositories/**/*.md
The Markdown cards are DERIVED. Curated judgement is added in
scripts/update/curation.json, never by editing a card.

Usage:
    python3 scripts/generate-index/generate_repository_cards.py
    python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from lib.sanitize import injection_marks, untrusted, untrusted_url  # noqa: E402

NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")
TODAY = datetime.now(timezone.utc).date().isoformat()

CATEGORY_TITLE = {
    "agent-frameworks": "Agent frameworks & SDKs",
    "agent-skills": "Coding agents, harnesses & skill catalogues",
    "mcp-servers": "MCP servers & SDKs",
    "browser-automation": "Browser automation & computer use",
    "frontend": "Frontend",
    "backend": "Backend",
    "databases": "Databases & data access",
    "ai": "AI / model tooling",
    "evaluation": "Evaluation, benchmarks & observability",
    "reasoning-research": "Reasoning research & open models",
    "developer-tools": "Developer tools, CI/CD & infrastructure",
    "instructions-standards": "Agent instruction formats & standards",
    "misc": "Miscellaneous",
}

STATUS_BADGE = {
    "ACTIVE": "🟢 ACTIVE", "STABLE": "🔵 STABLE", "MAINTENANCE": "🟡 MAINTENANCE",
    "ARCHIVED": "⛔ ARCHIVED", "ABANDONED": "🔴 ABANDONED", "EXPERIMENTAL": "🧪 EXPERIMENTAL",
    "UNKNOWN": "❓ UNKNOWN",
}


# Wording is deliberately about the consequence, not the score. "Low quality" invites an
# agent to weigh it against other factors; "do not redistribute" does not.
LICENSE_BANNERS = {
    "no-license-do-not-redistribute": """
> ⚠️ **LICENSE RISK — `no-license-do-not-redistribute`.** GitHub detected **no license file**
> on {date}. Default copyright applies, so all rights are reserved: **reference and link only**.
> Do not vendor, copy, quote at length, or redistribute any file from this repository, however
> useful it looks. A high star count does not create a license.
""",
    "custom-license-review-before-vendoring": """
> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on {date}, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.
""",
}


def bullet(items: List[str]) -> str:
    return "\n".join(f"- {i}" for i in items) if items else "- _not curated yet_"


def card(r: Dict[str, Any]) -> str:
    stars = r.get("stars") or 0
    stars_s = f"{stars:,}"
    q = r.get("quality") or {}
    qrows = "\n".join(f"| {k.replace('_',' ')} | {v} |" for k, v in q.items())
    struct = r.get("structure") or {}
    srows = "\n".join(f"| {k.replace('_',' ').replace('has ','')} | {'yes' if v else 'no'} |"
                      for k, v in struct.items() if k != "readme_bytes")
    notes = r.get("notes") or "_No anomalies detected._"

    # `description` and `homepage` are set by whoever owns the repository. They are recorded
    # verbatim in metadata/repositories.json because that is the observed fact, and sanitised
    # here because this is where they stop being data and start being rendering — in a document
    # this repository publishes for agents to read as trusted guidance. See
    # scripts/lib/sanitize.py.
    desc_raw = r.get("description") or ""
    safe_desc = untrusted(desc_raw) or "_No description published._"
    safe_home = untrusted_url(r.get("homepage")) or "—"
    # Framing the quote is not decoration. Without it the card reads as though this repository
    # asserts the description, which is how a vendor's "the first and the best" came to be
    # presented as content on a card ranked #1 in indexes/best-of.md.
    desc_block = ("> _Upstream description, quoted as published and not verified here:_\n>\n"
                  f"> {safe_desc}") if desc_raw else f"> {safe_desc}"

    # Escaping makes the text inert as markdown. It does nothing about a description whose
    # *content* is an instruction to whoever reads the card next, which is the more serious
    # case: this repository is built to be ingested by agents as external memory. Such a
    # record is quarantined rather than rendered — the fact that upstream published something
    # is preserved, the text itself is not repeated.
    inject = injection_marks(desc_raw) + injection_marks(r.get("homepage"))
    for topic in (r.get("topics") or []):
        inject += injection_marks(topic)
    if inject:
        marks = ", ".join(sorted(set(inject)))
        desc_block = ("> ⛔ **UPSTREAM DESCRIPTION QUARANTINED.** The text this repository "
                      f"returned matched injection patterns ({marks}) and is not reproduced "
                      "here. The raw string remains in `metadata/repositories.json` as the "
                      "observed fact, and `validate_policy.py` fails the build until the "
                      "record is reviewed. Nothing in this card should be read as endorsing "
                      "or repeating it.")

    # The license policy has to reach the markdown, not just the data file. A record in
    # repositories.json can carry `license_risk` and still leave the card a human or an agent
    # actually reads saying only `license: NONE` — an observed fact that stops nobody from
    # vendoring the content. So the risk is emitted twice: as a machine-checkable frontmatter
    # field, and as a banner above the fold.
    risk = r.get("license_risk") or "none"
    license_banner = LICENSE_BANNERS.get(risk, "")
    if license_banner:
        license_banner = "\n".join(
            ln.replace("{date}", str(r.get("verified_at") or "the last verification"))
            for ln in license_banner.strip().splitlines()
        ) + "\n\n"
    return f"""---
id: {r['slug'].lower().replace('/', '--')}
title: "{r['slug']}"
domain: {r['category']}
summary: >-
  {r['slug']} — {STATUS_BADGE.get(r['status'], r['status']).split(' ',1)[-1]}, tier {r['tier']},
  {stars_s} stars, license {r['license']}, quality {r['quality_score']}/10, trust {r['trust_score']}/10.
  Verified against the GitHub API on {r['verified_at']}.
status: {"deprecated" if r['status'] in ('ARCHIVED','ABANDONED') else "active"}
confidence: {r['confidence']}
claim_type: fact
evidence_level: verified-github-api
tags: {json.dumps(sorted(set((r.get('curated_tags') or []) + ['github-repository', r['category']]))[:14])}
version: 1.0.0
updated: {TODAY}
verified_at: {r['verified_at']}
expires_at: {r['expires_at']}
scoring:
  components: {json.dumps(q)}
  quality_score: {r['quality_score']}
  trust_score: {r['trust_score']}
  tier: {r['tier']}
  maturity: {r['maturity']}
  scored_by: scripts/lib/scoring.py
  scored_at: {r['verified_at']}
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: {str(bool(r.get('curated_at'))).lower()}
sources:
  - title: "{r['slug']} on GitHub"
    url: {r['url']}
    type: github-repository
    organization: {r['owner']}
    license: {r['license']}
    license_risk: {risk}
    confidence: {r['confidence']}
    claim_type: fact
    verified_at: {r['verified_at']}
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, {r['verified_at']})
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# {r['slug']}

{STATUS_BADGE.get(r['status'], r['status'])} · tier **{r['tier']}** · {r['maturity']} · confidence **{r['confidence']}**

{desc_block}

{license_banner}## Facts (verified {r['verified_at']} via the GitHub API)

| Field | Value |
|---|---|
| URL | <{r['url']}> |
| Owner | {r['owner']} ({r['owner_type']}) |
| Official upstream | {'yes' if r['official'] else 'no'} |
| Language | {r.get('language') or '—'} |
| License | `{r['license']}` |
| Stars | {stars_s} (checked {r['stars_checked_at']}) |
| Forks | {r.get('forks'):,} |
| Open issues | {r.get('open_issues'):,} |
| Contributors | {r.get('contributors') if r.get('contributors') is not None else '—'} |
| Last push | {str(r.get('pushed_at'))[:10]} ({r.get('days_since_push')} days before verification) |
| Latest release | {r.get('latest_release') or '—'} ({str(r.get('latest_release_published_at'))[:10] if r.get('latest_release_published_at') else 'no release'}) |
| Archived | {'**YES**' if r['archived'] else 'no'} |
| Fork | {'yes' if r['is_fork'] else 'no'} |
| Homepage | {safe_home} |
| SECURITY.md | {'yes' if struct.get('has_security_md') else 'no'} → `{r.get('security_status')}` |
| Repository kind | `{r.get('repo_kind')}`{' (static artifact — quiet history is expected)' if r.get('static_artifact') else ''} |

## Scores

| Component | 0–10 |
|---|---|
{qrows}
| **quality_score** (weighted) | **{r['quality_score']}** |
| **trust_score** | **{r['trust_score']}** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
{srows}
| README size | {struct.get('readme_bytes', 0):,} bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
({'on ' + str(r.get('curated_at')) if r.get('curated_at') else 'not yet curated'}) and must be
re-checked against your own constraints._

**Recommended for**

{bullet(r.get('recommended_for') or [])}

**Not recommended for**

{bullet(r.get('not_recommended_for') or [])}

**Strengths**

{bullet(r.get('strengths') or [])}

**Weaknesses**

{bullet(r.get('weaknesses') or [])}

**Related projects**

{bullet(r.get('related_projects') or [])}

## Verification notes

{notes}

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug {r['slug']}
python3 scripts/generate-index/generate_repository_cards.py --category {r['category']}
```
"""


def readme(cat: str, recs: List[Dict[str, Any]]) -> str:
    live = [r for r in recs if r["status"] not in ("ARCHIVED", "ABANDONED")]
    dead = [r for r in recs if r["status"] in ("ARCHIVED", "ABANDONED")]
    top = sorted(live, key=lambda r: -(r.get("trust_score") or 0))[:15]
    rows = "\n".join(
        f"| [{r['slug']}](./{r['slug'].replace('/', '--').lower()}.md) | {r['stars']:,} | {r['tier']} | "
        f"{STATUS_BADGE.get(r['status'], r['status'])} | `{r['license']}` | {r['trust_score']} | {r['verified_at']} |"
        for r in top)
    deadrows = "\n".join(
        f"| [{r['slug']}](./{r['slug'].replace('/', '--').lower()}.md) | {r['stars']:,} | "
        f"{STATUS_BADGE.get(r['status'], r['status'])} | {r.get('days_since_push')}d |"
        for r in sorted(dead, key=lambda r: -r["stars"])) or "| _none_ | | | |"
    return f"""<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# {CATEGORY_TITLE.get(cat, cat)}

{len(recs)} repositories · {len(live)} usable · {len(dead)} archived or abandoned ·
all facts verified against the GitHub API on {max((r['verified_at'] for r in recs), default='—')}.

## Highest trust

| Repository | Stars | Tier | Status | License | Trust | Verified |
|---|---|---|---|---|---|---|
{rows}

## Do not adopt

| Repository | Stars | Status | Days since push |
|---|---|---|---|
{deadrows}

## Cards

{chr(10).join(f"- [{r['slug']}](./{r['slug'].replace('/', '--').lower()}.md) — tier {r['tier']}, {r['status']}" for r in sorted(recs, key=lambda x: x['slug'].lower()))}
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", default=None)
    args = ap.parse_args()

    reg = json.loads((ROOT / "metadata" / "repositories.json").read_text())
    recs = [r for r in reg["repositories"] if r.get("fetch_ok")]
    by_cat = defaultdict(list)
    for r in recs:
        by_cat[r["category"]].append(r)

    n = 0
    for cat, items in sorted(by_cat.items()):
        if args.category and cat != args.category:
            continue
        d = ROOT / "repositories" / cat
        d.mkdir(parents=True, exist_ok=True)
        for r in items:
            (d / (r["slug"].replace("/", "--").lower() + ".md")).write_text(card(r))
            n += 1
        (d / "README.md").write_text(readme(cat, items))
        print(f"  repositories/{cat:26} {len(items):>4} cards")
    print(f"\nWrote {n} repository cards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

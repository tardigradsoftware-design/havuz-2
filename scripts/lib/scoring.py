#!/usr/bin/env python3
"""Shared scoring model for the knowledge base.

Implements the weighted source-score defined in
`knowledge/ai-engineering/source-scoring.md` (section 61 of the project brief):

    Authority        20%
    Maintenance      15%
    Adoption         15%
    Documentation    10%
    Reproducibility  10%
    Security         10%
    Recency          10%
    Evidence         10%

All inputs are *observable facts* (GitHub API responses, presence of files,
licenses, releases) rather than opinions, so scores are reproducible.

Nothing in here invents data: every component exposes the signal it used.
"""
from __future__ import annotations

import math
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

WEIGHTS: Dict[str, float] = {
    "authority": 0.20,
    "maintenance": 0.15,
    "adoption": 0.15,
    "documentation": 0.10,
    "reproducibility": 0.10,
    "security": 0.10,
    "recency": 0.10,
    "evidence": 0.10,
}

# Owners that publish the canonical upstream for the project they host.
# Keep this list small and defensible: it drives the `official` flag.
OFFICIAL_ORGS = {
    "vercel", "facebook", "microsoft", "google", "googleapis", "google-deepmind",
    "openai", "anthropics", "huggingface", "langchain-ai", "pydantic", "tailwindlabs",
    "shadcn-ui", "radix-ui", "nodejs", "denoland", "oven-sh", "fastapi", "nestjs",
    "expressjs", "honojs", "trpc", "prisma", "drizzle-team", "postgres", "sqlite",
    "redis", "mongodb", "supabase", "neondatabase", "neondatabase-labs", "pgvector",
    "clickhouse", "duckdb", "libsql", "pocketbase", "electric-sql", "timescale",
    "cockroachdb", "moby", "docker", "kubernetes", "hashicorp", "pulumi", "aws",
    "awslabs", "cloudflare", "firebase", "superfly", "argoproj", "actions", "github",
    "gitlab", "grafana", "prometheus", "open-telemetry", "getsentry", "posthog",
    "modelcontextprotocol", "browser-use", "browserbase", "microsoft", "playwright",
    "puppeteer", "seleniumhq", "cypress-io", "vitest-dev", "jestjs", "storybookjs",
    "testing-library", "eslint", "prettier", "biomejs", "oxc-project", "astral-sh",
    "typescript-eslint", "python", "microsoft", "tanstack", "pmndrs", "xyflow",
    "recharts", "apache", "d3", "observablehq", "motiondivision", "greensock",
    "mrdoob", "colinhacks", "vuejs", "sveltejs", "withastro", "nuxt", "solidjs",
    "vitejs", "rolldown", "deepseek-ai", "qwenlm", "meta-llama", "eleutherai",
    "stanford-crfm", "bigcode-project", "evalplus", "swe-bench", "sierra-research",
    "livecodebench", "laude-institute", "promptfoo", "confident-ai", "truera",
    "arize-ai", "langfuse", "explodinggradients", "open-compass", "tatsu-lab",
    "huggingface", "princeton-nlp", "osu-nlp-group", "ysymyth", "noahshinn",
    "madaan", "joonspk-research", "volcengine", "openrlhf", "nousresearch",
    "owasp", "ossf", "nvidia", "protectai", "giskard-ai", "trufflesecurity",
    "aquasecurity", "semgrep", "gitleaks", "renovatebot", "dependabot", "pre-commit",
    "typicode", "lint-staged", "changesets", "semantic-release", "conventional-changelog",
    "googlechrome", "dequelabs", "pa11y", "argos-ci", "lost-pixel", "reg-viz",
    "grafana", "k6", "artilleryio", "usebruno", "hoppscotch", "httpie", "burntsushi",
    "junegunn", "koalaman", "jesseduffield", "nrwl", "zed-industries", "tabby-ml",
    "cline", "continuedev", "block", "roocodeinc", "aider-ai", "plandex-ai",
    "all-hands-ai", "charmbracelet", "sst", "crewaiinc", "run-llama", "deepset-ai",
    "mastra-ai", "stanfordnlp", "agno-agi", "letta-ai", "camel-ai", "geekan",
    "significant-gravitas", "berriai", "skyvern-ai", "steel-dev", "nanobrowser",
    "alumnium-hq", "lavague-ai", "openadaptai", "open-interpreter", "xlang-ai",
    "web-arena-x", "gaia-benchmark", "lmarena-ai", "upstash", "sooperset",
    "makenotion", "slackapi", "stripe", "crystaldba", "punkpeye", "exa-labs",
    "firecrawl", "tavily-ai", "agentdeskai", "vercel", "microsoft", "google",
    "supabase-community", "mongodb-js", "redis", "cloudflare", "getsentry",
    "sentry-experts", "better-auth", "lucia-auth", "ory", "keycloak", "openfga",
    "casbin", "permify", "taskforcesh", "temporalio", "nats-io", "graphql",
    "tiangolo", "calcom", "dubinc", "midday-ai", "formbricks", "documenso",
    "plane-so", "refinedev", "appsmithorg", "nocodb", "payloadcms", "lobehub",
    "open-webui", "t3-oss", "tremorlabs", "magicuidesign", "mui", "rsms",
    "fontsource", "mlabonne", "rasbt", "unslothai", "axolotl-ai-cloud", "ml-explore",
    "ggml-org", "ollama", "vllm-project", "donnemartin", "adr", "npryce",
    "mingrammer", "mermaid-js", "12factor", "agentsmd", "patrickjs", "steipete",
    "voltagent", "obra", "hesreallyhim", "sourcegraph", "sweepai", "getcursor",
    "woodpecker-ci", "nektos", "railwayapp", "highlight", "mlcommons",
    "invariantlabs-ai", "rebuff-ai", "kysely-org", "firebase",
}

LICENSE_STRENGTH = {
    # permissive, redistribution-friendly
    "mit": 10, "apache-2.0": 10, "bsd-2-clause": 9, "bsd-3-clause": 9,
    "isc": 9, "0bsd": 9, "unlicense": 8, "cc0-1.0": 8, "mpl-2.0": 7,
    "python-2.0": 8, "postgresql": 8, "zlib": 8, "blueoak-1.0.0": 8,
    # weak copyleft
    "lgpl-2.1": 5, "lgpl-3.0": 5, "epl-2.0": 5, "cc-by-4.0": 7, "cc-by-sa-4.0": 6,
    # strong copyleft (fine to use as reference, careful to vendor)
    "gpl-2.0": 3, "gpl-3.0": 3, "agpl-3.0": 2, "sspl-1.0": 2, "busl-1.1": 2,
    "elastic-2.0": 3, "commons-clause": 2,
}


def _clamp(x: float, lo: float = 0.0, hi: float = 10.0) -> float:
    return max(lo, min(hi, x))


def days_since(iso: Optional[str], now: Optional[datetime] = None) -> Optional[int]:
    if not iso:
        return None
    now = now or datetime.now(timezone.utc)
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return max(0, (now - dt).days)


STATIC_KINDS = {"research-artifact", "benchmark", "dataset", "paper-code", "model-release"}


def infer_repo_kind(slug: str, description: str, topics: List[str], stars: int,
                    has_release: bool, seeded_kind: Optional[str] = None) -> str:
    """Classify what kind of thing a repository *is*.

    This matters because "no commit in 400 days" means very different things for
    a library and for a paper's reference implementation. Without this, the
    status classifier mislabels stable research artifacts as ABANDONED
    (observed on deepseek-ai/DeepSeek-R1, ysymyth/ReAct, noahshinn/reflexion).
    """
    if seeded_kind:
        return seeded_kind
    d = (description or "").lower()
    t = set(x.lower() for x in topics)
    if re.search(r"\[(iclr|neurips|acl|emnlp|cvpr|icml|aaai|sigir|colm)", d) or "paper" in t:
        return "research-artifact"
    if "benchmarking" in d or "benchmark" in t or d.startswith("benchmark"):
        return "benchmark"
    if "dataset" in d or "dataset" in t:
        return "dataset"
    if "awesome" in slug.lower() or "awesome" in d[:40]:
        return "catalog"
    if slug.split("/")[1].lower().endswith((".md", "-docs", "-spec", "-specification")):
        return "docs"
    if "-models" in slug.lower() or slug.lower().endswith("-r1") or "model card" in d:
        return "model-release"
    if "issue" in d and stars > 5000 and not has_release:
        return "issue-tracker"
    return "software"


def classify_status(
    *,
    archived: bool,
    days_since_push: Optional[int],
    days_since_commit: Optional[int],
    open_issues: int,
    stars: int,
    has_releases: bool,
    note: str = "",
    kind: str = "software",
) -> str:
    """ACTIVE | STABLE | MAINTENANCE | ARCHIVED | EXPERIMENTAL | ABANDONED | UNKNOWN

    Deterministic and documented in `knowledge/ai-engineering/repository-status.md`.
    """
    if archived:
        return "ARCHIVED"
    n = note.lower()
    if "maintenance" in n:
        return "MAINTENANCE"
    if "deprecated" in n or "abandoned" in n:
        return "ABANDONED"
    activity = min(x for x in [days_since_push, days_since_commit] if x is not None) if (
        days_since_push is not None or days_since_commit is not None) else None
    if activity is None:
        return "UNKNOWN"
    if kind in STATIC_KINDS:
        # A published paper artifact / benchmark / model release is not
        # "abandoned" because nobody commits to it. It is stable-by-design.
        return "STABLE"
    if activity > 365:
        return "ABANDONED"
    if activity > 120:
        return "MAINTENANCE"
    if stars < 300 and not has_releases and activity < 90:
        return "EXPERIMENTAL"
    if activity <= 14:
        return "ACTIVE"
    return "STABLE"


def score_repository(repo: Dict[str, Any], tree: Dict[str, Any], meta: Dict[str, Any]) -> Dict[str, Any]:
    """repo   = GitHub /repos payload
       tree   = parsed root tree listing (names + types)
       meta   = curated seed data + fetch extras (contributors, release, notes)
    """
    now = datetime.now(timezone.utc)
    stars = int(repo.get("stargazers_count") or 0)
    forks = int(repo.get("forks_count") or 0)
    open_issues = int(repo.get("open_issues_count") or 0)
    archived = bool(repo.get("archived"))
    disabled = bool(repo.get("disabled"))
    is_fork = bool(repo.get("fork"))

    d_push = days_since(repo.get("pushed_at"), now)
    d_commit = days_since(meta.get("last_commit_at"), now)
    d_release = days_since(meta.get("release_published_at"), now)
    contributors = meta.get("contributors")
    lic_obj = repo.get("license")
    license_id = ((lic_obj or {}).get("spdx_id") or "").lower()
    has_license_file = bool(lic_obj)          # null == no license detected at all
    license_nonstandard = has_license_file and license_id in ("noassertion", "other", "")
    names = set(tree.get("names", []))
    lower_names = {n.lower() for n in names}
    dirs = set(tree.get("dirs", []))
    lower_dirs = {d.lower() for d in dirs}
    has_ci = bool(tree.get("workflows")) or ".github" in lower_dirs
    has_tests = any(d in lower_dirs for d in ("tests", "test", "__tests__", "spec", "specs")) \
        or any(n.startswith("test_") or n.endswith((".test.ts", ".test.tsx", ".spec.ts")) for n in lower_names)
    has_docs = "docs" in lower_dirs or "documentation" in lower_dirs or bool(repo.get("has_pages"))
    has_examples = any(d in lower_dirs for d in ("examples", "example", "samples", "demo", "demos", "playground"))
    has_security_md = "security.md" in lower_names
    has_changelog = any(n in lower_names for n in ("changelog.md", "changes.md", "history.md", "releases.md"))
    has_contributing = "contributing.md" in lower_names
    has_readme = any(n.startswith("readme") for n in lower_names)
    readme_bytes = int(meta.get("readme_bytes") or 0)
    homepage = bool(repo.get("homepage"))
    topics = repo.get("topics") or []
    official = (repo.get("owner", {}).get("login", "").lower() in OFFICIAL_ORGS) or meta.get("force_official", False)

    # ---- authority (20%) -------------------------------------------------
    authority = 4.0
    if official:
        authority += 3.0
    if repo.get("owner", {}).get("type") == "Organization":
        authority += 1.0
    if homepage:
        authority += 0.5
    if len(topics) >= 5:
        authority += 0.5
    if is_fork:
        authority -= 2.5
    if repo.get("owner", {}).get("login", "").endswith("[bot]"):
        authority -= 1.0
    authority = _clamp(authority)

    # ---- maintenance (15%) ----------------------------------------------
    if archived or disabled:
        maintenance = 0.5
    elif d_push is None:
        maintenance = 3.0
    elif d_push <= 7:
        maintenance = 10.0
    elif d_push <= 30:
        maintenance = 8.5
    elif d_push <= 90:
        maintenance = 7.0
    elif d_push <= 180:
        maintenance = 5.0
    elif d_push <= 365:
        maintenance = 3.0
    else:
        maintenance = 1.0
    if contributors is not None:
        if contributors >= 100:
            maintenance += 1.0
        elif contributors >= 25:
            maintenance += 0.5
        elif contributors <= 1:
            maintenance -= 1.5
    if d_release is not None and d_release <= 90:
        maintenance += 0.5
    if open_issues > 0 and stars > 0 and open_issues / max(stars, 1) > 0.15:
        maintenance -= 0.5
    maintenance = _clamp(maintenance)

    # ---- adoption (15%) -------------------------------------------------
    # log-scaled so a star-farmed repo cannot dominate the score.
    adoption = _clamp(2.0 + 2.4 * math.log10(stars + 1) + 0.4 * math.log10(forks + 1))
    if contributors is not None and contributors >= 50:
        adoption += 0.5
    if is_fork:
        adoption -= 1.0
    adoption = _clamp(adoption)

    # ---- documentation (10%) --------------------------------------------
    documentation = 1.0
    if has_readme:
        documentation += 2.0
    documentation += _clamp(readme_bytes / 12000.0, 0, 3.0)
    if has_docs:
        documentation += 1.5
    if homepage:
        documentation += 1.0
    if has_contributing:
        documentation += 0.5
    if has_changelog:
        documentation += 0.5
    if repo.get("description"):
        documentation += 0.5
    documentation = _clamp(documentation)

    # ---- reproducibility (10%) ------------------------------------------
    reproducibility = 1.0
    if has_license_file:
        reproducibility += 2.0 + LICENSE_STRENGTH.get(license_id, 4) * 0.15
    if has_tests:
        reproducibility += 2.0
    if has_ci:
        reproducibility += 1.5
    if meta.get("has_release"):
        reproducibility += 1.0
    if has_examples:
        reproducibility += 1.0
    if any(n in lower_names for n in ("makefile", "justfile", "taskfile.yml", "dockerfile", "docker-compose.yml")):
        reproducibility += 0.5
    reproducibility = _clamp(reproducibility)

    # ---- security (10%) -------------------------------------------------
    security = 3.5
    if has_security_md:
        security += 2.5
    if official:
        security += 1.0
    if license_id in ("agpl-3.0", "sspl-1.0", "commons-clause"):
        security -= 1.0  # redistribution risk, not vulnerability risk
    if not has_license_file:
        security -= 2.0  # "no license" = legally unsafe to redistribute
    elif license_nonstandard:
        security -= 0.5  # custom terms: reference OK, vendoring needs review
    if archived:
        security -= 2.0  # archived code receives no security fixes
    if d_push is not None and d_push > 365:
        security -= 1.0
    security = _clamp(security)

    # ---- recency (10%) --------------------------------------------------
    if d_push is None:
        recency = 3.0
    else:
        recency = _clamp(10.0 - (d_push / 73.0))  # ~0 at 2 years

    # ---- evidence (10%) -------------------------------------------------
    evidence = 1.0
    if has_tests:
        evidence += 2.0
    if has_ci:
        evidence += 1.5
    if meta.get("has_release"):
        evidence += 1.0
    if contributors is not None and contributors >= 10:
        evidence += 1.0
    if homepage:
        evidence += 0.5
    if has_examples:
        evidence += 1.0
    if readme_bytes >= 20000:
        evidence += 0.5
    if is_fork:
        evidence -= 1.0
    evidence = _clamp(evidence)

    components = {
        "authority": round(authority, 2),
        "maintenance": round(maintenance, 2),
        "adoption": round(adoption, 2),
        "documentation": round(documentation, 2),
        "reproducibility": round(reproducibility, 2),
        "security": round(security, 2),
        "recency": round(recency, 2),
        "evidence": round(evidence, 2),
    }
    total = sum(components[k] * WEIGHTS[k] for k in WEIGHTS)

    return {
        "components": components,
        "quality_score": round(total, 2),
        "trust_score": round(_trust(components, archived=archived, official=official,
                                    license_id=license_id, has_license_file=has_license_file), 2),
        # fetch_ok travels in `meta` because the tier must be able to say "we could not
        # verify this" separately from "we verified it and it has no license".
        "tier": tier_for(total, archived=archived, license_ok=has_license_file,
                         nonstandard=license_nonstandard,
                         fetch_ok=bool(meta.get("fetch_ok", True))),
        "signals": {
            "official": official,
            "archived": archived,
            "disabled": disabled,
            "is_fork": is_fork,
            "license": (lic_obj or {}).get("spdx_id") or ("NONE" if not has_license_file else "NOASSERTION"),
            "license_nonstandard": license_nonstandard,
            "has_license_file": has_license_file,
            "has_readme": has_readme,
            "readme_bytes": readme_bytes,
            "has_docs": has_docs,
            "has_tests": has_tests,
            "has_ci": has_ci,
            "has_examples": has_examples,
            "has_security_md": has_security_md,
            "has_changelog": has_changelog,
            "has_contributing": has_contributing,
            "contributors": contributors,
            "days_since_push": d_push,
            "days_since_release": d_release,
            "homepage": repo.get("homepage") or None,
            "topics": topics,
        },
    }


def _trust(c: Dict[str, float], *, archived: bool, official: bool, license_id: str,
           has_license_file: bool = True) -> float:
    """Trust = can an agent act on this without a human double-check?

    Quality measures how good the project is; trust measures how safe it is to
    treat it as ground truth. An archived project can still be high quality but
    is lower trust for *current* guidance.
    """
    base = (c["authority"] * 0.30 + c["evidence"] * 0.25 + c["maintenance"] * 0.20
            + c["documentation"] * 0.15 + c["security"] * 0.10)
    if archived:
        base -= 2.0
    if official:
        base += 0.5
    if not has_license_file:
        base -= 1.5
    return _clamp(base)


def tier_for(score: float, *, archived: bool = False, license_ok: bool = True,
             nonstandard: bool = False, fetch_ok: bool = True) -> str:
    """S / A / B / C / EXPERIMENTAL / ARCHIVED / NO-LICENSE / UNVERIFIED.

    Two of these are frequently confused and mean unrelated things, so they are kept
    strictly apart:

      * `UNVERIFIED` is about **epistemic status** — the record could not be checked
        against its source (the GitHub fetch failed, the repository 404'd). Nothing
        else asserted about such a record is trustworthy, which is why this is tested
        first: it overrides even `ARCHIVED`, since a flag we could not fetch is a flag
        we are only repeating from stale data.
      * `NO-LICENSE` is about **legal status** — the metadata was verified perfectly
        well, and what verification found is that no license is published. The record
        is reliable; redistributing it is not.

    An earlier revision returned `UNVERIFIED` for the license case, so all 15 records
    in that tier carried `fetch_ok: true` while being labelled as though their metadata
    were untrustworthy — and the signal that actually mattered, do-not-redistribute, was
    carried in a separate field the tier name obscured. `knowledge/ai-engineering/
    source-scoring.md` had already defined `UNVERIFIED` as "could not be verified" and
    mapped only "unresolvable / 404" to it; the code disagreed with the documentation.

    A custom (NOASSERTION) license caps the tier at A: the project may be
    excellent, but its redistribution terms need a human read before vendoring.
    """
    if not fetch_ok:
        return "UNVERIFIED"
    if archived:
        return "ARCHIVED"
    if not license_ok:
        return "NO-LICENSE"
    if score >= 8.0 and not nonstandard:
        return "S"
    if score >= 7.0 or (score >= 8.0 and nonstandard):
        return "A"
    if score >= 5.8:
        return "B"
    if score >= 4.3:
        return "C"
    return "EXPERIMENTAL"


def maturity_for(status: str, tier: str, stars: int) -> str:
    if status in ("ARCHIVED", "ABANDONED"):
        return "end-of-life"
    if status == "EXPERIMENTAL":
        return "experimental"
    if status == "MAINTENANCE":
        return "maintenance-mode"
    if tier in ("S", "A") and stars >= 5000:
        return "production-grade"
    if tier in ("S", "A", "B"):
        return "production-ready"
    return "early"


def confidence_for(score: Dict[str, Any], verified: bool) -> str:
    if not verified:
        return "unverified"
    t = score.get("trust_score", 0)
    if t >= 7.5:
        return "very-high"
    if t >= 6.0:
        return "high"
    if t >= 4.0:
        return "medium"
    return "low"


def expires_for(kind: str, verified_at: str) -> Optional[str]:
    """Freshness policy (brief section 31)."""
    ttl_days = {
        "model": 21,
        "framework": 60,
        "mcp": 45,
        "github-repository": 45,
        "tool": 45,
        "benchmark": 90,
        "dataset": 180,
        "research-paper": 365,
        "official-docs": 90,
        "specification": 365,
        "blog": 120,
        "default": 90,
    }[kind]
    try:
        d = datetime.fromisoformat(verified_at)
    except ValueError:
        return None
    from datetime import timedelta
    return (d + timedelta(days=ttl_days)).date().isoformat()

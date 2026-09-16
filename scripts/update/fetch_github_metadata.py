#!/usr/bin/env python3
"""Fetch and verify GitHub facts for every seed repository.

Design rule of this repository: **no guessed metadata**. Stars, licenses,
archive flags, last-push dates, release info, contributor counts and the
presence of tests/CI/SECURITY.md are all read from the GitHub API at run time
and stamped with `stars_checked_at` / `verified_at`.

Usage:
    python3 scripts/update/fetch_github_metadata.py            # refresh all seeds
    python3 scripts/update/fetch_github_metadata.py --limit 20 # smoke test
    python3 scripts/update/fetch_github_metadata.py --no-cache # ignore local cache
    python3 scripts/update/fetch_github_metadata.py --slug microsoft/autogen

Outputs:
    metadata/repositories.json   (machine-readable registry, generated)
    metadata/fetch-report.json   (404s, renames, rate-limit, run summary)

Auth: uses GITHUB_TOKEN / GH_TOKEN when present (5000 req/h), otherwise falls
back to unauthenticated access (60 req/h) and warns loudly.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from lib.scoring import (  # noqa: E402
    classify_status, confidence_for, expires_for, infer_repo_kind, maturity_for,
    score_repository,
)

CACHE = ROOT / ".cache" / "gh"
API = "https://api.github.com"
SEEDS = ROOT / "scripts" / "update" / "seeds.json"
CURATION = ROOT / "scripts" / "update" / "curation.json"


def load_curation() -> Dict[str, Any]:
    """Human judgement, keyed by slug. Facts never live here."""
    if not CURATION.exists():
        return {}
    try:
        return json.loads(CURATION.read_text()).get("curation", {})
    except json.JSONDecodeError:
        return {}
OUT = ROOT / "metadata" / "repositories.json"
REPORT = ROOT / "metadata" / "fetch-report.json"

TIER_TO_PRODUCTION = {
    "core": "recommended",
    "seed": "recommended",
    "reference": "situational",
    "candidate": "evaluate-first",
    "status-check": "verify-status",
}


def token() -> Optional[str]:
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        v = os.environ.get(var)
        if v:
            return v.strip()
    return None


def cache_path(url: str) -> Path:
    return CACHE / (hashlib.sha256(url.encode()).hexdigest()[:32] + ".json")


def http_json(url: str, tok: Optional[str], use_cache: bool = True, ttl_hours: int = 6,
              accept: str = "application/vnd.github+json") -> Tuple[Optional[Any], int, Dict[str, str]]:
    """Returns (payload, status, headers). payload is None on 404/403/422."""
    cp = cache_path(url)
    if use_cache and cp.exists() and (time.time() - cp.stat().st_mtime) < ttl_hours * 3600:
        blob = json.loads(cp.read_text())
        return blob.get("payload"), blob.get("status", 200), blob.get("headers", {})

    req = urllib.request.Request(url, headers={
        "Accept": accept,
        "User-Agent": "havuz-knowledge-base/1.0 (+https://github.com/tardigradsoftware-design/havuz-2)",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = json.loads(r.read().decode())
            status, headers = r.status, dict(r.headers)
    except urllib.error.HTTPError as e:
        body, status, headers = None, e.code, dict(e.headers or {})
        if e.code == 403 and "rate limit" in (e.headers.get("X-RateLimit-Remaining", "") or ""):
            pass
    except Exception as e:  # network hiccup
        body, status, headers = None, -1, {"error": str(e)}

    CACHE.mkdir(parents=True, exist_ok=True)
    cp.write_text(json.dumps({"payload": body, "status": status, "headers": headers}))
    return body, status, headers


def parse_link_count(headers: Dict[str, str]) -> Optional[int]:
    """Extract the last page number from a Link header (used for contributor counts)."""
    link = headers.get("Link") or headers.get("link") or ""
    m = re.search(r'[?&]page=(\d+)>;\s*rel="last"', link)
    return int(m.group(1)) if m else None


def root_tree(full_name: str, branch: str, tok, use_cache) -> Dict[str, Any]:
    payload, status, _ = http_json(f"{API}/repos/{full_name}/git/trees/{branch}", tok, use_cache)
    names, dirs, blobs, workflows = [], [], [], False
    if payload:
        for e in payload.get("tree", []):
            p = e.get("path", "")
            if e.get("type") == "tree":
                dirs.append(p)
            else:
                names.append(p)
                if e.get("size"):
                    blobs.append((p, e["size"]))
    readme_bytes = 0
    for p, s in blobs:
        if p.lower().startswith("readme"):
            readme_bytes = max(readme_bytes, s)
    # workflows need the .github subtree
    payload2, status2, _ = http_json(f"{API}/repos/{full_name}/contents/.github/workflows", tok, use_cache)
    if status2 == 200 and isinstance(payload2, list):
        workflows = any(str(x.get("name", "")).endswith((".yml", ".yaml")) for x in payload2)
    return {"names": names, "dirs": dirs, "readme_bytes": readme_bytes, "workflows": workflows,
            "tree_status": status}


def fetch_one(seed: Dict[str, Any], tok, use_cache: bool, curation: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    slug = seed["slug"].strip()
    rec: Dict[str, Any] = {
        "requested_slug": slug,
        "category": seed.get("category", "misc"),
        "curated_tier": seed.get("tier", "candidate"),
        "curated_tags": seed.get("tags", []),
        "fetch_ok": False,
    }
    repo, status, _ = http_json(f"{API}/repos/{slug}", tok, use_cache)
    if status != 200 or not repo:
        rec["error"] = {
            404: "NOT_FOUND", 403: "RATE_LIMITED_OR_FORBIDDEN", 451: "DMCA_TAKEDOWN",
            301: "MOVED", -1: "NETWORK_ERROR",
        }.get(status, f"HTTP_{status}")
        rec["http_status"] = status
        return rec

    full = repo["full_name"]
    rec["renamed_to"] = full if full.lower() != slug.lower() else None
    branch = repo.get("default_branch") or "main"
    tree = root_tree(full, branch, tok, use_cache)

    rel, rel_status, _ = http_json(f"{API}/repos/{full}/releases/latest", tok, use_cache)
    has_release = rel_status == 200 and bool(rel)

    _, _, cheaders = http_json(f"{API}/repos/{full}/contributors?per_page=1&anon=false", tok, use_cache)
    contributors = parse_link_count(cheaders)

    last_commit_at = None
    commits, cstat, _ = http_json(f"{API}/repos/{full}/commits?per_page=1", tok, use_cache)
    if cstat == 200 and isinstance(commits, list) and commits:
        last_commit_at = (commits[0].get("commit", {}).get("committer") or {}).get("date")

    meta = {
        "last_commit_at": last_commit_at,
        "release_published_at": (rel or {}).get("published_at") if has_release else None,
        "release_tag": (rel or {}).get("tag_name") if has_release else None,
        "has_release": has_release,
        "contributors": contributors,
        "readme_bytes": tree["readme_bytes"],
    }
    scored = score_repository(repo, tree, meta)

    d_push = scored["signals"]["days_since_push"]
    d_commit = scored["signals"].get("days_since_push")
    kind = infer_repo_kind(
        full, repo.get("description") or "", repo.get("topics") or [],
        int(repo.get("stargazers_count") or 0), has_release, seed.get("repo_kind"),
    )
    status_cls = classify_status(
        archived=bool(repo.get("archived")),
        days_since_push=d_push,
        days_since_commit=None,
        open_issues=int(repo.get("open_issues_count") or 0),
        stars=int(repo.get("stargazers_count") or 0),
        has_releases=has_release,
        kind=kind,
    )
    static_artifact = kind in ("research-artifact", "benchmark", "dataset", "model-release")
    verified_at = datetime.now(timezone.utc).date().isoformat()

    rec.update({
        "fetch_ok": True,
        "name": repo["name"],
        "owner": repo["owner"]["login"],
        "owner_type": repo["owner"]["type"],
        "slug": full,
        "url": repo["html_url"],
        "description": (repo.get("description") or "").strip() or None,
        "homepage": repo.get("homepage") or None,
        "language": repo.get("language"),
        "license": scored["signals"]["license"],
        "license_nonstandard": scored["signals"]["license_nonstandard"],
        "stars": int(repo.get("stargazers_count") or 0),
        "forks": int(repo.get("forks_count") or 0),
        "open_issues": int(repo.get("open_issues_count") or 0),
        "watchers": int(repo.get("subscribers_count") or 0) if "subscribers_count" in repo else None,
        "default_branch": branch,
        "created_at": repo.get("created_at"),
        "pushed_at": repo.get("pushed_at"),
        "last_commit": last_commit_at,
        "days_since_push": d_push,
        "latest_release": meta["release_tag"],
        "latest_release_published_at": meta["release_published_at"],
        "contributors": contributors,
        "archived": bool(repo.get("archived")),
        "disabled": bool(repo.get("disabled")),
        "is_fork": bool(repo.get("fork")),
        "has_issues": bool(repo.get("has_issues")),
        "has_discussions": bool(repo.get("has_discussions")),
        "has_wiki": bool(repo.get("has_wiki")),
        "topics": repo.get("topics") or [],
        "official": scored["signals"]["official"],
        "structure": {
            "has_readme": scored["signals"]["has_readme"],
            "readme_bytes": tree["readme_bytes"],
            "has_docs": scored["signals"]["has_docs"],
            "has_tests": scored["signals"]["has_tests"],
            "has_ci": scored["signals"]["has_ci"],
            "has_examples": scored["signals"]["has_examples"],
            "has_security_md": scored["signals"]["has_security_md"],
            "has_changelog": scored["signals"]["has_changelog"],
            "has_contributing": scored["signals"]["has_contributing"],
            "root_entries": len(tree["names"]) + len(tree["dirs"]),
        },
        "repo_kind": kind,
        "static_artifact": static_artifact,
        "status": status_cls,
        "license_risk": ("no-license-do-not-redistribute" if scored["signals"]["license"] == "NONE"
                         else "custom-license-review-before-vendoring" if scored["signals"]["license_nonstandard"]
                         else "none"),
        "production_ready": (status_cls in ("ACTIVE", "STABLE") and scored["tier"] in ("S", "A", "B")
                             and kind == "software"),
        "maintenance_status": status_cls,
        "security_status": ("archived-no-patches" if repo.get("archived")
                            else "policy-published" if scored["signals"]["has_security_md"]
                            else "no-policy"),
        "documentation_quality": _doc_quality(scored["components"]["documentation"], tree["readme_bytes"]),
        "community_adoption": _adoption_band(int(repo.get("stargazers_count") or 0)),
        "quality": scored["components"],
        "quality_score": scored["quality_score"],
        "trust_score": scored["trust_score"],
        "tier": scored["tier"],
        "maturity": ("published-artifact" if static_artifact and not repo.get("archived")
                     else maturity_for(status_cls, scored["tier"], int(repo.get("stargazers_count") or 0))),
        "confidence": confidence_for(scored, True),
        "evidence_level": "verified-github-api",
        "source_type": "github-repository",
        "verified_at": verified_at,
        "stars_checked_at": verified_at,
        "expires_at": expires_for("github-repository", verified_at),
        "recommended_for": [],
        "not_recommended_for": [],
        "related_projects": [],
        "notes": _auto_notes(repo, rec, scored, kind, status_cls, has_release),
        "provenance": "curated-seed+github-api",
        "claim_type": "fact",
    })

    cur = (curation or {})
    for key in (full, slug, rec.get("requested_slug")):
        if key and key in cur:
            c = dict(cur[key])
            # curated fields only; facts stay authoritative from the API
            for f in ("recommended_for", "not_recommended_for", "strengths", "weaknesses",
                      "related_projects", "relevance"):
                if c.get(f) is not None:
                    rec[f] = c[f]
            extra = []
            if rec.get("notes"):
                extra.append(rec["notes"])
            for f in ("notes", "status_note", "repo_kind_note"):
                if c.get(f):
                    extra.append(c[f])
            rec["notes"] = " ".join(dict.fromkeys(extra)) or None
            rec["curation_claim_type"] = "recommendation"
            rec["curated_at"] = verified_at
            break
    return rec


def _auto_notes(repo, rec, scored, kind, status_cls, has_release):
    """Generate only notes that are supported by an observed signal."""
    sig = scored["signals"]
    dp = sig["days_since_push"]
    n = []
    if rec.get("renamed_to"):
        n.append("Repository moved: `%s` -> `%s`. Update any hard-coded URLs; the old path "
                 "404s once GitHub drops the redirect." % (rec["requested_slug"], rec["renamed_to"]))
    if repo.get("archived"):
        n.append("ARCHIVED by owner: read-only, receives no fixes or security patches. "
                 "Do not start new work on it; look for the successor project.")
    if status_cls == "MAINTENANCE":
        n.append("No push in %s days (>120d). Treat as maintenance mode: usable, but check for a "
                 "recommended successor before adopting." % dp)
    if status_cls == "ABANDONED":
        n.append("No push in %s days (>365d). Likely abandoned; prefer an actively maintained "
                 "alternative." % dp)
    if sig["license"] == "NONE":
        n.append("NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: "
                 "do not vendor, copy or redistribute code from this repository. Reference and link only.")
    elif sig["license_nonstandard"]:
        n.append("Non-SPDX/custom license (%s). Read the license text before vendoring; "
                 "referencing is fine." % sig["license"])
    if kind in ("research-artifact", "benchmark", "dataset", "model-release") and status_cls == "STABLE":
        n.append("Reference implementation published with a %s. Quiet commit history is expected and "
                 "is NOT evidence of abandonment; the value is the paper/method, not the maintenance." % kind)
    if sig["is_fork"]:
        n.append("This is a fork. Check the upstream parent before trusting provenance.")
    return " ".join(n) or None


def _doc_quality(score: float, readme_bytes: int) -> str:
    if score >= 8 and readme_bytes >= 15000:
        return "excellent"
    if score >= 6:
        return "good"
    if score >= 3.5:
        return "adequate"
    return "poor"


def _adoption_band(stars: int) -> str:
    if stars >= 50000:
        return "very-high"
    if stars >= 10000:
        return "high"
    if stars >= 2000:
        return "moderate"
    if stars >= 300:
        return "low"
    return "minimal"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--slug", action="append", default=[])
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--dry", action="store_true", help="print summary, do not write files")
    args = ap.parse_args()

    tok = token()
    if not tok:
        print("WARN: no GITHUB_TOKEN/GH_TOKEN in env — unauthenticated limit is 60 req/hour", file=sys.stderr)
    else:
        print(f"OK: authenticated GitHub API ({len(tok[:4])}… token detected)")

    seeds = json.loads(SEEDS.read_text())["seeds"]
    if args.slug:
        wanted = {s.lower() for s in args.slug}
        seeds = [s for s in seeds if s["slug"].lower() in wanted]
    if args.limit:
        seeds = seeds[: args.limit]
    print(f"Fetching {len(seeds)} repositories…")

    use_cache = not args.no_cache
    results: List[Dict[str, Any]] = []
    report_dupes: List[str] = []
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        cur = load_curation()
        futs = {ex.submit(fetch_one, s, tok, use_cache, cur): s for s in seeds}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            try:
                results.append(fut.result())
            except Exception as e:
                s = futs[fut]
                results.append({"requested_slug": s["slug"], "fetch_ok": False,
                                "error": f"EXCEPTION:{e}", "category": s.get("category")})
            if i % 25 == 0:
                print(f"  {i}/{len(seeds)} done ({time.time()-t0:.0f}s)")

    ok, bad = [], []
    for r in results:
        (ok if r.get("fetch_ok") else bad).append(r)

    # Two seeds can resolve to the same repository (a rename, or a seed that was
    # added twice). Keep the richer record and preserve the alias so that any
    # document citing the old slug still resolves.
    by_slug: dict = {}
    for r in ok:
        slug = r["slug"]
        if slug not in by_slug:
            r.setdefault("aliases", [])
            if r.get("requested_slug") and r["requested_slug"] != slug:
                r["aliases"].append(r["requested_slug"])
            by_slug[slug] = r
            continue
        prev = by_slug[slug]
        for a in {r.get("requested_slug"), slug}:
            if a and a != slug and a not in prev["aliases"]:
                prev["aliases"].append(a)
        if r.get("curated_at") and not prev.get("curated_at"):
            prev = r
            by_slug[slug] = prev
        elif r.get("contributors") and not prev.get("contributors"):
            prev.update({k: v for k, v in r.items() if k in ("contributors", "last_commit")})
        report_dupes.append(slug)
    ok = list(by_slug.values())
    ok.sort(key=lambda r: (r["category"], -r["stars"]))

    registry = {
        "$schema": "../schemas/repositories.schema.json",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": "scripts/update/fetch_github_metadata.py",
        "verification_method": "GitHub REST API (repos, git/trees, releases/latest, commits, contributors)",
        "records_fetched": len(ok),
        "records_failed": len(bad),
        "repositories": ok,
    }
    report = {
        "generated_at": registry["generated_at"],
        "requested": len(results),
        "ok": len(ok),
        "failed": len(bad),
        "authenticated": bool(tok),
        "duration_seconds": round(time.time() - t0, 1),
        "failures": [{"slug": r.get("requested_slug"), "error": r.get("error"),
                      "http_status": r.get("http_status")} for r in bad],
        "renamed": [{"from": r["requested_slug"], "to": r["renamed_to"]} for r in ok if r.get("renamed_to")],
        "duplicate_seeds_collapsed": sorted(set(report_dupes)),
        "archived": [{"slug": r["slug"], "stars": r["stars"]} for r in ok if r["archived"]],
        "no_license": [r["slug"] for r in ok if r["license"] == "NONE"],
        "custom_license": [r["slug"] for r in ok if r["license"] == "NOASSERTION"],
        "stale_over_180d": sorted(
            [(r["slug"], r["days_since_push"]) for r in ok if (r["days_since_push"] or 0) > 180],
            key=lambda x: -(x[1] or 0)),
        "tier_distribution": _dist([r["tier"] for r in ok]),
        "status_distribution": _dist([r["status"] for r in ok]),
        "category_distribution": _dist([r["category"] for r in ok]),
    }

    if args.dry:
        print(json.dumps(report, indent=2))
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n")
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUT.relative_to(ROOT)} ({len(ok)} repos) and {REPORT.relative_to(ROOT)}")
    fails = [f["slug"] + "(" + str(f["error"])[:40] + ")" for f in report["failures"]]
    print("Failures:", (", ".join(fails[:12]) + (f" … +{len(fails)-12} more" if len(fails) > 12 else "")) or "none")
    print("Tiers:", report["tier_distribution"])
    print("Status:", report["status_distribution"])
    return 0


def _dist(vals: List[str]) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for v in vals:
        d[v] = d.get(v, 0) + 1
    return dict(sorted(d.items(), key=lambda kv: -kv[1]))


if __name__ == "__main__":
    raise SystemExit(main())

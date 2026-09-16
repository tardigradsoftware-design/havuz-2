#!/usr/bin/env python3
"""Resolve seed slugs that 404 on the GitHub API.

A 404 is a *finding*, not an error to hide. This script tries, in order:
  1. case-insensitive exact match under the same owner (search API)
  2. name match across GitHub, ranked by stars, restricted to plausible owners
  3. leaves the slug unresolved and records it as REMOVED_OR_RENAMED

Results are written to metadata/unresolved-seeds.json for human triage;
nothing is silently substituted.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
API = "https://api.github.com"
TOK = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def get(url: str):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "havuz-kb-seed-resolver",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    if TOK:
        req.add_header("Authorization", f"Bearer {TOK}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode()), r.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception:
        return None, -1


def search(q: str, per_page: int = 5):
    url = f"{API}/search/repositories?q={urllib.parse.quote(q)}&per_page={per_page}&sort=stars"
    body, status = get(url)
    if status == 403:
        time.sleep(20)
        body, status = get(url)
    return (body or {}).get("items", []), status


def resolve(slug: str):
    owner, name = slug.split("/", 1)
    out = {"requested": slug, "candidates": [], "resolution": None}

    items, st = search(f"{name} in:name user:{owner}")
    for it in items:
        out["candidates"].append({
            "slug": it["full_name"], "stars": it["stargazers_count"],
            "archived": it["archived"], "desc": ((it.get("description") or "")[:90]),
            "match": "same-owner-name",
        })
    time.sleep(2.5)

    if not out["candidates"]:
        items, st = search(f"{name} in:name")
        for it in items[:6]:
            out["candidates"].append({
                "slug": it["full_name"], "stars": it["stargazers_count"],
                "archived": it["archived"], "desc": ((it.get("description") or "")[:90]),
                "match": "global-name",
            })
        time.sleep(2.5)

    if len(out["candidates"]) == 1:
        out["resolution"] = out["candidates"][0]["slug"]
    elif out["candidates"]:
        top = sorted(out["candidates"], key=lambda c: -c["stars"])
        # only auto-resolve when the top candidate is an order of magnitude more
        # adopted than the runner-up AND shares the name exactly
        if (top[0]["match"] == "same-owner-name" or top[0]["stars"] > 10 * max(top[1]["stars"], 1)):
            if top[0]["slug"].split("/")[1].lower() == name.lower():
                out["resolution"] = top[0]["slug"]
            else:
                out["resolution"] = "NEEDS_HUMAN"
        else:
            out["resolution"] = "NEEDS_HUMAN"
    else:
        out["resolution"] = "NOT_FOUND"
    return out


def main() -> int:
    report = json.loads((ROOT / "metadata" / "fetch-report.json").read_text())
    failures = [f["slug"] for f in report["failures"]]
    print(f"Resolving {len(failures)} failed seeds…")
    results = [resolve(s) for s in failures]
    (ROOT / "metadata" / "unresolved-seeds.json").write_text(
        json.dumps({"generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "results": results}, indent=2) + "\n")
    for r in results:
        print(f"  {r['requested']:42} -> {r['resolution']}")
        for c in r["candidates"][:3]:
            print(f"       · {c['slug']:40} ★{c['stars']:<8} {c['desc'][:60]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

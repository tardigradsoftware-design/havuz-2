#!/usr/bin/env python3
"""Reachability check for every external URL referenced by the knowledge base.

Distinct from `scripts/validate/validate_links.py --external`: that validator gates
CI; this crawler produces a durable report with per-URL history so a URL that fails
once (outage) is distinguishable from a URL that fails every run (dead).

Usage:
    python3 scripts/crawl/verify_urls.py
    python3 scripts/crawl/verify_urls.py --report metadata/url-report.json
    python3 scripts/crawl/verify_urls.py --only-failing
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")
HISTORY = ROOT / "metadata" / "url-history.json"

URL_RE = re.compile(r"https?://[^\s)>\]\"'`<,;]+")
SKIP_DIRS = {".git", ".cache", "node_modules", ".venv"}

# Domains that reliably reject non-browser clients. A 403/429 from these is not
# evidence of a dead link, so they are recorded as "soft-blocked" instead.
SOFT = ("x.com", "twitter.com", "linkedin.com", "medium.com", "reddit.com",
        "scholar.google.com", "facebook.com", "instagram.com", "tiktok.com")


def collect() -> Dict[str, List[str]]:
    found: Dict[str, List[str]] = defaultdict(list)
    for f in fm.iter_markdown(ROOT):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(encoding="utf-8", errors="replace")
        for u in URL_RE.findall(text):
            u = u.rstrip(").,;:'\"")
            if "localhost" in u or "127.0.0.1" in u or u.endswith((".png", ".jpg", ".svg", ".ico")):
                continue
            found[u].append(rel)
    for p in (ROOT / "metadata").glob("*.json"):
        txt = p.read_text(errors="replace")
        for u in re.findall(r'"(https?://[^"]+)"', txt):
            found[u.rstrip(").,;")].append(f"metadata/{p.name}")
    return dict(found)


def check(url: str, timeout: int) -> Tuple[str, int, str]:
    soft = any(d in url for d in SOFT)
    last = 0
    for attempt in range(3):
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (compatible; havuz-kb-urlcheck/1.0)",
                "Accept": "*/*",
            }, method=method)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return url, r.status, "soft-blocked" if soft else "ok"
            except urllib.error.HTTPError as e:
                last = e.code
                if e.code in (403, 429) and soft:
                    return url, e.code, "soft-blocked"
                if e.code in (405, 501) and method == "HEAD":
                    continue
                if e.code in (429, 500, 502, 503, 504) and attempt < 2:
                    time.sleep(3 * (attempt + 1))
                    break
                return url, e.code, "http-error"
            except Exception as e:
                last = -1
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    break
                return url, -1, f"{type(e).__name__}"
    return url, last, "unreachable-after-retries"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--report", default="metadata/url-report.json")
    ap.add_argument("--only-failing", action="store_true")
    args = ap.parse_args()

    urls = collect()
    print(f"Discovered {len(urls)} unique external URLs. Checking…")

    history = {}
    if HISTORY.exists():
        try:
            history = json.loads(HISTORY.read_text()).get("urls", {})
        except json.JSONDecodeError:
            history = {}

    results = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(check, u, args.timeout) for u in sorted(urls)]
        done = 0
        for fut in cf.as_completed(futs):
            url, status, why = fut.result()
            done += 1
            if done % 100 == 0:
                print(f"  {done}/{len(urls)}")
            results.append({"url": url, "status": status, "result": why,
                            "referenced_from": sorted(set(urls[url]))[:6],
                            "references": len(urls[url])})

    ok = [r for r in results if r["result"] in ("ok", "soft-blocked")]
    bad = [r for r in results if r["result"] not in ("ok", "soft-blocked")]

    # consecutive-failure tracking: a first failure is a warning, a repeat is dead
    for r in bad:
        prev = history.get(r["url"], {})
        r["consecutive_failures"] = int(prev.get("consecutive_failures", 0)) + 1
        r["first_failed_at"] = prev.get("first_failed_at", NOW)
        r["verdict"] = "DEAD" if r["consecutive_failures"] >= 2 else "TRANSIENT_OR_DEAD"
    for r in ok:
        history[r["url"]] = {"consecutive_failures": 0, "last_ok": NOW, "status": r["status"]}
    for r in bad:
        history[r["url"]] = {"consecutive_failures": r["consecutive_failures"],
                             "first_failed_at": r["first_failed_at"], "status": r["status"]}

    report = {
        "generated_at": NOW,
        "generator": "scripts/crawl/verify_urls.py",
        "total_urls": len(urls),
        "reachable": len(ok),
        "unreachable": len(bad),
        "dead_after_repeat": sum(1 for r in bad if r.get("verdict") == "DEAD"),
        "policy": "A URL that fails once is TRANSIENT_OR_DEAD. It becomes DEAD only after "
                  "failing on two separate runs, so a provider outage never breaks the build.",
        "failures": sorted(bad, key=lambda r: -r["references"]),
    }
    (ROOT / args.report).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / args.report).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    HISTORY.write_text(json.dumps({"updated": NOW, "urls": history}, indent=2, ensure_ascii=False) + "\n")

    print(f"\nReachable {len(ok)} / {len(urls)}   Unreachable {len(bad)}   "
          f"Confirmed dead {report['dead_after_repeat']}")
    shown = [r for r in report["failures"] if not args.only_failing or r["verdict"] == "DEAD"]
    for r in shown[:40]:
        print(f"  {r['status']:>5} {r['verdict']:<18} x{r['consecutive_failures']} {r['url'][:88]}")
        print(f"        referenced from: {', '.join(r['referenced_from'][:3])}")
    if len(shown) > 40:
        print(f"  … and {len(shown)-40} more (see {args.report})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

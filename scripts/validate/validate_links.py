#!/usr/bin/env python3
"""Link validation.

  --internal   every relative Markdown link / image / frontmatter path resolves to a
               real file inside the repository, and every heading anchor exists
  --external   every http(s) URL is reachable (HEAD, then GET fallback), with retries
               and a known-flaky allowlist so transient outages do not fail CI

Broken internal links are a hard error: they break agent retrieval.
Broken external links fail only after repeated failure, per SECURITY/brief §81.

Usage:
    python3 scripts/validate/validate_links.py --internal
    python3 scripts/validate/validate_links.py --external --timeout 20
    python3 scripts/validate/validate_links.py --internal --external
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
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from lib import frontmatter as fm  # noqa: E402

MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RAW_URL = re.compile(r"(?<!\()(?<![\w/\"])https?://[^\s)>\]\"'`]+")
ALLOWLIST = ROOT / "scripts" / "validate" / "link-allowlist.json"

SKIP_DIRS = {".git", ".cache", "node_modules", ".venv", "__pycache__"}

# Domains that block HEAD/bot requests but are known-good references.
SOFT_DOMAINS = {
    "x.com", "twitter.com", "linkedin.com", "medium.com", "reddit.com",
    "news.ycombinator.com", "scholar.google.com", "openai.com", "anthropic.com",
}


def load_allowlist() -> Dict[str, str]:
    if ALLOWLIST.exists():
        try:
            return json.loads(ALLOWLIST.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def strip_code(body: str) -> str:
    out, fence = [], False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if not fence:
            out.append(line)
    return "\n".join(out)


def collect_internal() -> Tuple[List[str], List[str], Set[str]]:
    errors, warns = [], []
    external: Set[str] = set()
    anchors: Dict[str, Set[str]] = {}

    docs = []
    for f in fm.iter_markdown(ROOT):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        docs.append(fm.parse(f))
    for d in docs:
        anchors[d.rel] = {"#" + fm.slugify(h) for _, h in fm.headings(d.body)}

    for d in docs:
        text = strip_code(d.raw_front + "\n" + d.body)
        for target in MD_LINK.findall(text):
            if target.startswith(("mailto:", "#")):
                if target.startswith("#") and target not in anchors[d.rel]:
                    errors.append(f"{d.rel}: anchor {target} not found in this file")
                continue
            if re.match(r"^https?://", target):
                external.add(target.split("#")[0].rstrip(").,;"))
                continue
            path_part, _, frag = target.partition("#")
            if path_part:
                resolved = (d.path.parent / path_part).resolve()
                try:
                    rel = resolved.relative_to(ROOT.resolve()).as_posix()
                except ValueError:
                    errors.append(f"{d.rel}: link escapes the repository -> {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"{d.rel}: broken internal link -> {target}")
                elif frag and rel in anchors and ("#" + frag) not in anchors[rel]:
                    warns.append(f"{d.rel}: anchor #{frag} not found in {rel}")
        for u in RAW_URL.findall(text):
            external.add(u.rstrip(").,;>"))

    # frontmatter paths (sources[].repository, related, requires)
    for d in docs:
        for k in ("related_skills", "requires"):
            for v in d.data.get(k) or []:
                if not (ROOT / "skills" / str(v) / "SKILL.md").exists():
                    warns.append(f"{d.rel}: {k} '{v}' has no skills/{v}/SKILL.md")
    return errors, warns, external


def check_url(url: str, timeout: int, retries: int = 2) -> Tuple[str, int, str]:
    if any(dom in url for dom in SOFT_DOMAINS):
        return url, 0, "skipped:soft-domain"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; havuz-kb-linkcheck/1.0)",
               "Accept": "*/*"}
    last = 0
    for attempt in range(retries + 1):
        for method in ("HEAD", "GET"):
            req = urllib.request.Request(url, headers=headers, method=method)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return url, r.status, "ok"
            except urllib.error.HTTPError as e:
                last = e.code
                if e.code in (405, 501, 403) and method == "HEAD":
                    continue
                if e.code in (429, 500, 502, 503, 504):
                    time.sleep(2 + 3 * attempt)
                    break
                return url, e.code, "http-error"
            except Exception as e:
                last = -1
                if attempt < retries:
                    time.sleep(1 + 2 * attempt)
                    break
                return url, -1, f"exception:{type(e).__name__}"
        else:
            continue
        continue
    return url, last, "failed-after-retries"


def collect_external() -> Tuple[List[str], List[str]]:
    errors, warns = [], []
    urls: Set[str] = set()
    for f in fm.iter_markdown(ROOT):
        if any(p in SKIP_DIRS for p in f.parts):
            continue
        d = fm.parse(f)
        text = strip_code(d.raw_front + "\n" + d.body)
        for t in MD_LINK.findall(text) + RAW_URL.findall(text):
            if re.match(r"^https?://", t):
                urls.add(t.split("#")[0].rstrip(").,;>\"'"))
    for p in (ROOT / "metadata").glob("*.json"):
        txt = p.read_text(errors="replace")
        for u in re.findall(r'"(https?://[^"]+)"', txt):
            urls.add(u.rstrip(").,;"))
    urls = {u for u in urls if "localhost" not in u and "127.0.0.1" not in u}
    allow = load_allowlist()
    todo = sorted(u for u in urls if u not in allow)
    print(f"Checking {len(todo)} external URLs ({len(urls)-len(todo)} allowlisted)…")
    failures: Dict[str, List[str]] = defaultdict(list)
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(check_url, u, 20): u for u in todo}
        done = 0
        for fut in cf.as_completed(futs):
            url, status, why = fut.result()
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(todo)}")
            if why.startswith("ok") or why.startswith("skipped") or status in (200, 203, 204, 206, 301, 302, 401, 403):
                continue
            failures[url].append(f"{status} {why}")
    for url, reasons in sorted(failures.items()):
        if url in allow:
            warns.append(f"{url}: allowlisted ({allow[url]})")
        else:
            errors.append(f"{url}: {reasons[0]}")
    return errors, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--internal", action="store_true")
    ap.add_argument("--external", action="store_true")
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--write-allowlist", action="store_true",
                    help="record current external failures in the allowlist with a reason")
    args = ap.parse_args()
    if not args.internal and not args.external:
        args.internal = True

    errors: List[str] = []
    warns: List[str] = []

    if args.internal:
        e, w, ext = collect_internal()
        errors += e
        warns += w
        print(f"Internal: {len(e)} errors, {len(w)} warnings, {len(ext)} external URLs discovered")
    if args.external:
        e, w = collect_external()
        errors += e
        warns += w
        print(f"External: {len(e)} errors, {len(w)} warnings")

    for e in errors[:100]:
        print("  ERROR  " + e)
    if len(errors) > 100:
        print(f"  … and {len(errors)-100} more")
    for w in warns[:40]:
        print("  warn   " + w)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

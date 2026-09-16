#!/usr/bin/env python3
"""The collection-ethics exclusions, as data that code can enforce.

`SECURITY.md` declares a list of things this repository will *never* collect, store,
summarise in reproducing form, or redistribute, and
`knowledge/security/llm-security/excluded-sources.md` names two high-popularity
repositories as excluded under it. Both documents described the policy as mechanical —
"the policy is mechanical, not aspirational" — and listed five things
`scripts/validate/validate_policy.py` supposedly did about it. Three of the five did not
exist: there was no exclusion list anywhere in the codebase, no check consulted one, and
`fetch_github_metadata.py` would have fetched an excluded repository on request.

The policy was honoured only because nobody had added those repositories. That is the
failure mode the documents themselves anticipated: the reason an exclusion is recorded
rather than silently omitted is so a later contributor does not rediscover a popular
repository and add it in good faith. A contributor seeding one would have passed every
check — it fetches fine, it scores well, and it has a license.

This module is the single source of truth for the exclusion list. Both the validator and
the fetcher read it, so there is one answer to "is this source excluded?" and it lives in
`metadata/excluded-sources.json` next to the prose that explains it.

Reads are tolerant: a missing or malformed file yields no exclusions and a diagnostic,
because a validator that crashes cannot report anything else either. The caller decides
whether an unreadable policy file is itself an error — `validate_policy.py` treats it as
one, which is the correct answer, since an unenforceable exclusion is the defect.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
EXCLUSIONS_FILE = ROOT / "metadata" / "excluded-sources.json"

# Files where a mention is legitimate because the file *is* the policy: the data itself
# and the prose reasoning behind it. Everywhere else a mention has to be in a passage that
# states the exclusion, which is checked by wording rather than by a path allowlist — an
# allowlist would grow every time someone needed to discuss the policy and would eventually
# exempt the very files the check exists to protect.
POLICY_FILES = frozenset({
    "metadata/excluded-sources.json",
    "knowledge/security/llm-security/excluded-sources.md",
})

# Ingestion and retrieval paths. A mention here is never excusable by wording: a seed list
# entry, a registry record or a retrieval-index entry *is* collection, whatever the
# surrounding prose says about it.
INGESTION_PATHS = (
    "scripts/update/seeds.json",
    "scripts/update/curation.json",
    "metadata/repositories.json",
    "metadata/index.json",
    "metadata/graph.json",
    "metadata/tools.json",
    "metadata/sources.json",
    "indexes/",
    "repositories/",
    "sources/",
)

# Wording that establishes a passage is stating an exclusion rather than using the source.
EXCLUSION_WORDING = re.compile(
    r"(?i)(excluded|exclusion|never (?:collect|ingest|store|vendor|cite)|do not (?:ingest|collect|"
    r"vendor|cite|add)|must not (?:ingest|collect|vendor|cite)|prohibited|forbidden|not ingested|"
    r"refuse[sd]? to fetch|will not (?:be )?(?:ingested|collected|fetched)|hard exclusion)")


class Exclusions:
    """The exclusion list, loaded once and queried by slug, name and pattern."""

    def __init__(self, data: Optional[Dict[str, Any]] = None,
                 load_error: Optional[str] = None) -> None:
        self.load_error = load_error
        raw = (data or {}).get("exclusions") or []
        self.records: List[Dict[str, Any]] = [r for r in raw if isinstance(r, dict) and r.get("slug")]
        self.patterns: List[Dict[str, Any]] = [
            p for p in ((data or {}).get("content_patterns") or [])
            if isinstance(p, dict) and p.get("pattern")
        ]
        self._compiled = []
        for p in self.patterns:
            try:
                self._compiled.append((p, re.compile(p["pattern"])))
            except re.error as e:
                self._compiled.append((p, None))
                self.load_error = (self.load_error or "") + f"\nbad pattern {p.get('id')}: {e}"

    # ---- loading -----------------------------------------------------------

    @classmethod
    def load(cls, path: Path = EXCLUSIONS_FILE) -> "Exclusions":
        # Never relative_to(ROOT) unconditionally: reporting an unreadable policy file must not
        # itself raise. A caller may point at a scratch copy outside the repository, and the
        # diagnostic is the whole point of the tolerant read.
        def where() -> str:
            try:
                return str(path.relative_to(ROOT))
            except ValueError:
                return str(path)

        if not path.exists():
            return cls(None, f"{where()} is missing — the collection-ethics "
                             f"exclusions have no machine-readable form and cannot be enforced")
        try:
            return cls(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            return cls(None, f"{where()} is not valid JSON: {e}")

    # ---- queries -----------------------------------------------------------

    @property
    def slugs(self) -> List[str]:
        return [str(r["slug"]) for r in self.records]

    def names(self) -> List[str]:
        """Repository names, for reporting. Never used for matching — see `slug_in`."""
        return sorted({str(r["slug"]).split("/", 1)[1] for r in self.records if "/" in str(r["slug"])})

    def is_empty(self) -> bool:
        return not self.records

    def slug_in(self, text: str) -> List[str]:
        """Excluded slugs occurring in `text`, matched as whole slugs.

        Case-insensitive on the owner and name, and boundary-anchored, because a substring
        test would implicate unrelated text: the name `registry` occurs in dozens of
        legitimate places, and an exclusion list that cries wolf gets ignored.
        """
        found = []
        for slug in self.slugs:
            if re.search(rf"(?i)(?<![\w/.-]){re.escape(slug)}(?![\w/-])", text):
                found.append(slug)
        return found

    def pattern_hits(self, text: str) -> List[Tuple[Dict[str, Any], str]]:
        """Content-pattern matches, e.g. the filenames the leaked-prompt collections use."""
        out = []
        for p, rx in self._compiled:
            if rx is None:
                continue
            m = rx.search(text)
            if m:
                out.append((p, m.group(0)))
        return out

    def is_policy_file(self, rel: str) -> bool:
        return rel in POLICY_FILES

    def is_ingestion_path(self, rel: str) -> bool:
        return rel in INGESTION_PATHS or rel.startswith(INGESTION_PATHS)

    def passage_states_exclusion(self, text: str, needle: str) -> bool:
        """True when the paragraph containing `needle` states that it is excluded.

        Scoped to the paragraph rather than the whole file, so a document that both uses an
        excluded source and elsewhere mentions the word "excluded" does not excuse itself.
        The needle's own quotation marks and code spans are ignored when looking for the
        wording: the statement has to be in prose.
        """
        for para in re.split(r"\n\s*\n", text):
            if needle.lower() not in para.lower():
                continue
            prose = re.sub(r"`[^`]*`", " ", para)
            if EXCLUSION_WORDING.search(prose):
                return True
        return False

    # ---- enforcement helpers ------------------------------------------------

    def fetch_refusal(self, slug: str) -> Optional[str]:
        """Why `slug` must not be fetched, or None when it may be."""
        for r in self.records:
            if str(r["slug"]).lower() == str(slug).strip().lower():
                return (f"{r['slug']} is excluded from this repository "
                        f"({r.get('category', 'collection ethics')}, decided "
                        f"{r.get('decided_on', 'date not recorded')}): {r.get('reason', '')} "
                        f"See {r.get('documented_in', 'the exclusion policy')} — the exclusion, "
                        f"not the content, is what this repository records.")
        return None


def load_exclusions(path: Path = EXCLUSIONS_FILE) -> Exclusions:
    return Exclusions.load(path)

#!/usr/bin/env python3
"""Generate the MCP registry from verified GitHub metadata.

Reads metadata/repositories.json (produced by scripts/update/fetch_github_metadata.py
from live GitHub REST API calls) and emits, for every record in the `mcp-servers`
category:

  * knowledge/mcp/registry/<slug>.md  — a graded registry entry

metadata/tools.json is NOT written here. It is derived from these markdown files by
scripts/generate-index/extract_registries.py, exactly as skills.json is derived from
skills/*/SKILL.md. Two writers for one file is how a registry silently drifts from
the documents it claims to describe, so the chain is one-directional:

    metadata/repositories.json  ->  knowledge/mcp/registry/*.md  ->  metadata/tools.json
    (GitHub REST API)               (this script)                    (extract_registries.py)

Honesty rules this generator is built around, because an MCP registry that guesses
is worse than no registry:

  1. Every factual field comes from an observed GitHub API value. Nothing is inferred
     from the name of the repository.
  2. Capability fields that the GitHub API cannot tell us — transport, tool list,
     resource list, prompt list, authentication scheme — are emitted as null or empty
     and flagged `capability_evidence: unverified`. They are NOT guessed. A wrong
     transport claim sends an integrator down a dead end.
  3. `purpose` is the repository's own description, attributed as such. Where that
     description is too thin to satisfy the schema minimum, the entry is emitted with
     `purpose_evidence: repository-description-thin` so a human knows to expand it
     from the README rather than trusting the generator.
  4. License risk is carried through verbatim. `NOASSERTION` and absent licenses are
     surfaced, not smoothed over.
  5. Archived repositories are emitted with `production_readiness: deprecated` and are
     never marked production-ready, regardless of star count.

Usage:
    python3 scripts/generate-index/generate_mcp_registry.py [--check]

--check exits non-zero if the committed output differs from a fresh regeneration,
so CI can prove the registry is in sync with the metadata it was built from.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from lib.sanitize import untrusted, yaml_folded  # noqa: E402
REPOS = ROOT / "metadata" / "repositories.json"
OUT_MD = ROOT / "knowledge" / "mcp" / "registry"

NOW = datetime.now(timezone.utc)
TODAY = NOW.date().isoformat()
# MCP registry entries describe fast-moving tooling: 90-day window per the freshness policy.
EXPIRES = (NOW + timedelta(days=90)).date().isoformat()

# Repository topics/description keywords -> registry category. Derived only from
# fields the API actually returned; no category is asserted without a signal.
CATEGORY_SIGNALS: List[tuple[str, tuple[str, ...]]] = [
    ("browser", ("browser", "playwright", "puppeteer", "chrome", "devtools", "web-scraping", "crawl")),
    ("database", ("database", "postgres", "postgresql", "mysql", "mongodb", "redis", "sqlite", "neon", "supabase", "sql")),
    ("vcs", ("github", "gitlab", "git", "bitbucket", "pull-request")),
    ("search", ("search", "retrieval", "exa", "tavily", "serp")),
    ("documentation", ("documentation", "docs", "context7", "readme", "knowledge")),
    ("cloud", ("aws", "cloud", "cloudflare", "azure", "gcp", "cloud-run", "firebase", "vercel", "deploy")),
    ("communication", ("slack", "notion", "atlassian", "jira", "confluence", "discord", "email", "gmail")),
    ("observability", ("sentry", "observability", "monitoring", "logging", "trace", "metrics", "grafana", "datadog")),
    ("ci-cd", ("ci", "cd", "pipeline", "n8n", "workflow", "actions")),
    ("filesystem", ("filesystem", "file", "directory", "memory")),
    # `payments` was already a member of the category enum in mcp.schema.json but no
    # signal could ever select it, so a payments server fell through to whatever short
    # signal happened to appear in its prose.
    ("payments", ("stripe", "payment", "payments", "billing", "checkout")),
]

DISTRIBUTION_HINTS: List[tuple[str, tuple[str, ...]]] = [
    ("npm", ("npmjs.com", "npmjs.org")),
    ("pypi", ("pypi.org", "pypi.python.org")),
    ("docker", ("hub.docker.com", "docker.com")),
]


# Fields this generator promises not to infer. The GitHub API does not expose them,
# so any non-empty value can only have come from a guess or from a human who read the
# project's own documentation. `assert_no_guesses` allows the latter only when the
# entry declares that it happened.
CAPABILITY_FIELDS = ("transport", "tools", "resources", "prompts", "permissions",
                     "authentication", "recommended_for")
UNVERIFIED = "unverified"


def assert_no_guesses(tools: List[Dict[str, Any]]) -> List[str]:
    """Enforce the module's central guarantee. Returns a list of violations."""
    bad: List[str] = []
    for t in tools:
        if t.get("capability_evidence") != UNVERIFIED:
            continue          # a human reviewed this entry; the fields are theirs
        for f in CAPABILITY_FIELDS:
            v = t.get(f)
            if v:             # non-empty list/dict/string is an unsupported claim
                bad.append(f"{t.get('repository')}: capability_evidence is '{UNVERIFIED}' "
                           f"but '{f}' is populated ({v!r}) — that value cannot have come "
                           f"from the GitHub API, so it was guessed")
    return bad


TOOLS_JSON = ROOT / "metadata" / "tools.json"
MCP_SCHEMA = ROOT / "schemas" / "mcp.schema.json"
# Added by extract_registries.py for its own bookkeeping; not registry fields.
INTERNAL_KEYS = ("_path", "_tokens", "_headings")

# record_to_tool() keys whose frontmatter line is written under a different name or
# folded into another line, so a literal name match against MD_TMPL would report a
# false loss. Each entry names the template slot that carries it.
# record_to_tool() keys that the template carries under a different mechanism, so a
# literal top-level name match against rendered frontmatter would report a false loss.
TEMPLATE_ALIASES = {
    "authentication": "authentication_line",   # conditional: emitted only when observed
}


def frontmatter_keys(rendered: str) -> set:
    """Top-level keys of a rendered entry's YAML frontmatter."""
    m = re.match(r"(?s)\A---\n(.*?)\n---\n", rendered)
    if not m:
        return set()
    return set(re.findall(r"(?m)^([A-Za-z_][A-Za-z0-9_]*):", m.group(1)))


def _kind_counts(tools: List[Dict[str, Any]]) -> str:
    """One line of the --check report, so the split is visible without opening the JSON."""
    import collections
    c = collections.Counter(t.get("registry_kind") for t in tools)
    order = [k for k in REGISTRY_KINDS if c.get(k)]
    return "registry kinds " + ", ".join(f"{k}:{c[k]}" for k in order) + (
        f" — {c['server']} of {len(tools)} entries counted as MCP servers" if c.get("server") else "")


def _union_keys(tools: List[Dict[str, Any]]) -> set:
    out: set = set()
    for t in tools:
        out |= set(t)
    return out


def assert_chain_complete(tools: List[Dict[str, Any]]) -> List[str]:
    """Prove that nothing computed here is lost on the hop to `metadata/tools.json`.

    The chain is one-directional by design —
    `repositories.json -> knowledge/mcp/registry/*.md -> metadata/tools.json` — and
    `extract_registries.py` reads only the markdown frontmatter. A field this module
    computes but `MD_TMPL` does not emit therefore disappears silently: every such
    field is optional in `mcp.schema.json`, so the schema validator reports nothing,
    and the drift job passes because regeneration reproduces the same loss. That is
    how nine fields went missing, including the archived server's
    `not_recommended_for` warning — the one field in the registry that tells a reader
    not to adopt something.

    Two directions are checked, because a field can be lost or invented:

      1. every key `record_to_tool()` produces must appear in `tools.json`;
      2. every key in `tools.json` must be a property declared by the schema.

    Comparison is per record, not on the union, so a field emitted for one repository
    and dropped for another cannot hide in the aggregate.
    """
    bad: List[str] = []
    if not TOOLS_JSON.exists():
        return [f"{TOOLS_JSON.relative_to(ROOT)} missing — run extract_registries.py"]
    if not MCP_SCHEMA.exists():
        return [f"{MCP_SCHEMA.relative_to(ROOT)} missing"]
    declared = set(json.loads(MCP_SCHEMA.read_text()).get("properties", {}))
    final = {r.get("repository"): r
             for r in json.loads(TOOLS_JSON.read_text()).get("tools", [])}

    for t in tools:
        slug = t.get("repository")
        got = final.get(slug)
        if got is None:
            bad.append(f"{slug}: computed here but absent from metadata/tools.json")
            continue
        have = set(got) - set(INTERNAL_KEYS)
        lost = sorted(set(t) - have)
        if lost:
            bad.append(f"{slug}: field(s) lost between the registry markdown and "
                       f"tools.json: {', '.join(lost)} — MD_TMPL does not emit them")
        undeclared = sorted(have - declared)
        if undeclared:
            bad.append(f"{slug}: tools.json carries key(s) not declared in "
                       f"mcp.schema.json: {', '.join(undeclared)}")
    return bad


def yaml_scalar(v: Any) -> str:
    """Render a Python value as a YAML flow scalar that round-trips through a parser.

    Every value written into the frontmatter has to survive
    `extract_registries.py` re-reading it, or the field is silently lost on the hop
    to `metadata/tools.json`. Quoting is decided by the value, not by the field name:
    `@playwright/mcp` must be quoted because `@` is a reserved YAML indicator, a
    language named `null` would otherwise parse as None, and a list containing an
    em dash is safest as JSON (which is valid YAML flow syntax).
    """
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, dict)):
        return json.dumps(v, ensure_ascii=False)
    s = str(v)
    # Quote when YAML would otherwise reinterpret the value: reserved indicators,
    # values that look like another type, or anything with leading/trailing space.
    if (s == "" or s.strip() != s
            or s[0] in "@`#&*!|>%'\"{}[],-?:"
            or s.lower() in ("null", "true", "false", "yes", "no", "on", "off", "~")
            or ": " in s or " #" in s
            or any(c in s for c in '"\'\\')):
        return json.dumps(s, ensure_ascii=False)
    return s


def slug_to_id(slug: str) -> str:
    return "mcp-" + slug.replace("/", "-").replace(".", "-").lower()


def assert_categories_are_whole_tokens(recs: List[Dict[str, Any]],
                                       tools: List[Dict[str, Any]]) -> List[str]:
    """Prove no category was assigned on the strength of a substring.

    Re-derives each classification from the source record and checks it three ways: that
    it agrees with what is stored, that every signal recorded as having matched is a whole
    token of the field it is claimed from, and that a signal claimed from topics or the
    slug does not in fact only appear in the description. A gate that merely re-ran
    `detect_category` would pass against any matcher, including the broken one, because it
    would be comparing the function with itself. Checking the *tokens* is what makes the
    substring version fail: under it `'ci'` is recorded as having matched, and `'ci'` is
    not a token of anything the official SDKs publish.
    """
    bad: List[str] = []
    by_slug = {r["slug"]: r for r in recs}
    for tool in tools:
        slug = tool["repository"]
        rec = by_slug.get(slug)
        if rec is None:
            bad.append(f"{slug}: not in metadata/repositories.json; cannot re-derive category")
            continue
        cat, evidence, signals = detect_category(rec)
        if (cat, evidence, signals) != (tool.get("category"), tool.get("category_evidence"),
                                        tool.get("category_signals")):
            bad.append(f"{slug}: stored category "
                       f"{tool.get('category')}/{tool.get('category_evidence')}/"
                       f"{tool.get('category_signals')} does not re-derive to "
                       f"{cat}/{evidence}/{signals}")

        # The stored claim is then audited on its own terms. Re-derivation and this check
        # are independent: if re-derivation disagreed and we skipped ahead, a category
        # justified by a substring would be reported only as "does not re-derive" and the
        # more specific diagnosis — which token was claimed, and why it cannot have matched
        # — would be lost. Both messages matter when someone has to fix it.
        stored_evidence = tool.get("category_evidence")
        stored_signals = tool.get("category_signals") or []
        if stored_evidence == "no-signal-matched":
            continue
        structured = _tokens(str(rec.get("slug", "").replace("/", " ")) + " "
                             + " ".join(rec.get("topics") or []))
        described = _tokens(rec.get("description") or "")
        for sig in stored_signals:
            if stored_evidence == "topics-or-slug" and sig not in structured:
                bad.append(f"{slug}: category '{cat}' claims signal '{sig}' from topics or "
                           f"the slug, but '{sig}' is not a whole token of either — it can "
                           f"only have matched inside a word")
            if stored_evidence == "description-fallback" and sig not in described:
                bad.append(f"{slug}: category '{cat}' claims signal '{sig}' from the "
                           f"description, but '{sig}' is not a whole token of it")
    return bad

# ---------------------------------------------------------------------------
# What kind of thing each registry entry actually is.
#
# The registry was built by filtering repositories.json for category == "mcp-servers",
# which is a *seed-list* category assigned when the repository was added, not a verified
# property of it. Five of the resulting entries were not servers at all, and each entry's
# own `purpose` quoted the description that said so — the registry contradicted its own
# label. Consumers are skills/dont-reinvent-the-wheel and skills/mcp-integration, which
# tell an agent to consult this registry before building or installing a server; an agent
# handed an SDK, a catalog or a testing tool gets nothing usable.
#
# Classification uses only text the GitHub API returned, and records the fragment it
# matched so every decision can be re-derived and challenged. Ordered most specific
# first: a repository that calls itself a registry or a catalog is that even though it
# also contains the words "MCP server", which every entry in this registry does.
KIND_SDK = re.compile(r"(?i)\bsdk\b|\bspin up\b|\bsoftware development kit\b")
KIND_REGISTRY = re.compile(r"(?i)\bregistry\b")
KIND_CATALOG = re.compile(r"(?i)\bcatalog(?:ue)?\b|\bcollection of\b|\bawesome[- ]")
KIND_TOOLING = re.compile(
    r"(?i)\btesting tool\b|\bvisual testing\b|\bdebug(?:ging)? tool\b|\bcommand line\b|\bcli\b|\binspector\b")
KIND_SERVER = re.compile(
    r"(?i)\b(?:mcp|model context protocol)\b[^.]{0,40}\bservers?\b"
    r"|\bservers?\b[^.]{0,40}\b(?:mcp|model context protocol)\b")

# Ordered. The first rule whose signal is present in the observed text decides.
KIND_RULES: List[tuple] = [
    ("sdk", KIND_SDK),
    ("registry", KIND_REGISTRY),
    ("catalog", KIND_CATALOG),
    ("tooling", KIND_TOOLING),
]

# A topic the owner set that asserts the repository is a server. Stronger evidence than
# prose, because it is structured and set for discoverability.
SERVER_TOPICS = ("mcp-server", "mcp-servers")


# What each kind means to a reader who came here looking for a server to install. The
# sentence is generated rather than left to the entry's prose so that the label and its
# consequence cannot drift apart, and so `unproven` says what it does not know instead of
# sitting there looking like a classification somebody made.
KIND_SENTENCES = {
    "server": "Counted as an MCP server in `indexes/mcp.md` and in the README statistics. "
              "This is what the registry's consumers — `skills/mcp-integration` and "
              "`skills/dont-reinvent-the-wheel` — mean when they say consult the registry "
              "before installing a server.",
    "sdk": "**This is not a server you can connect to.** It is a library for *building* one. "
           "Installing it as an MCP server will not work; it is recorded here so that "
           "somebody about to write a server finds it instead of writing their own.",
    "tooling": "**This is not a server you can connect to.** It is a tool for testing or "
               "debugging servers. Recorded here because it is the right answer to the "
               "question “how do I check the server I just built”, not to the question "
               "“which server should I install”.",
    "registry": "**This is a registry, not an entry.** It is a peer of this one. Recorded so "
                "that it is not mistaken for a server, and so that its existence is not "
                "rediscovered as though it were news.",
    "catalog": "**This is a curated list of other servers, not a server.** Consult it to find "
               "candidates; do not install it. Recorded here because a catalog with a high star "
               "count looks exactly like a popular server in a filtered list.",
    "unproven": "**Nothing the GitHub API returned establishes what this repository is.** It was "
                "seeded into this registry under the seed-list category `mcp-servers`, which is "
                "an assertion made when the record was added rather than a verified property, and "
                "the repository's own published description and topics do not confirm it. It is "
                "not counted as an MCP server. Confirm from the README before adopting it, then "
                "set `registry_kind` and record what you read.",
}


def kind_sentence(tool: Dict[str, Any]) -> str:
    """Explain the consequence of the kind, and quote the evidence that decided it."""
    kind = tool.get("registry_kind") or "unproven"
    base = KIND_SENTENCES.get(kind, KIND_SENTENCES["unproven"])
    evidence = (tool.get("registry_kind_evidence") or "").strip()
    if evidence:
        base += f" Evidence: {evidence}."
    return base


def detect_registry_kind(rec: Dict[str, Any]) -> tuple[str, str]:
    """Return `(registry_kind, registry_kind_evidence)` from observed text only.

    `unproven` is a real answer, not a fallback for the timid. Where nothing the API
    returned asserts what the repository is, saying so is more useful than defaulting to
    `server`: an entry counted as a server inflates the registry's apparent coverage, and
    the count is what a reader uses to decide whether to keep looking.
    """
    desc = str(rec.get("description") or "").strip()
    slug = str(rec.get("slug") or "")
    last_segment = slug.split("/")[-1].lower()
    topics = [str(x).lower() for x in (rec.get("topics") or [])]

    for kind, rx in KIND_RULES:
        m = rx.search(desc)
        if m:
            return kind, f'description says "{m.group(0).strip()}"'
        if kind == "sdk" and last_segment.endswith("-sdk"):
            return kind, f'slug "{slug}" ends in "-sdk"'
        if kind == "catalog" and last_segment.startswith("awesome-"):
            return kind, f'slug "{slug}" begins "awesome-", the convention for a curated list'

    for topic in topics:
        if topic in SERVER_TOPICS:
            return "server", f'owner-set topic "{topic}"'
    m = KIND_SERVER.search(desc)
    if m:
        return "server", f'description says "{m.group(0).strip()}"'
    if "mcp-server" in last_segment or last_segment == "mcp" or last_segment.endswith("-mcp"):
        return "server", f'slug "{slug}" names the repository as MCP'

    if "mcp" in topics:
        return "unproven", ('the topic "mcp" says the repository relates to MCP; nothing '
                            "observed asserts that it is a server")
    return "unproven", "no observed text asserts what this repository is"


REGISTRY_KINDS = ("server", "sdk", "tooling", "catalog", "registry", "unproven")


def assert_kinds_are_evidenced(recs: List[Dict[str, Any]],
                               tools: List[Dict[str, Any]]) -> List[str]:
    """Prove every kind re-derives from the record and quotes real observed text.

    The evidence string has to be a fragment of the description, the slug or a topic the
    API actually returned — a kind justified by text that is not in the record is a kind
    that was guessed. This is the check that stops `unproven` from being used as a bin for
    records someone simply did not look at, and stops `server` from being asserted on the
    strength of the seed-list category the entry was filtered by.
    """
    bad: List[str] = []
    by_slug = {r["slug"]: r for r in recs}
    for tool in tools:
        slug = tool["repository"]
        rec = by_slug.get(slug)
        if rec is None:
            bad.append(f"{slug}: not in metadata/repositories.json; cannot re-derive kind")
            continue
        kind, evidence = detect_registry_kind(rec)
        if kind != tool.get("registry_kind"):
            bad.append(f"{slug}: stored registry_kind '{tool.get('registry_kind')}' does not "
                       f"re-derive to '{kind}'")
        if evidence != tool.get("registry_kind_evidence"):
            bad.append(f"{slug}: stored registry_kind_evidence does not re-derive")
        if tool.get("registry_kind") not in REGISTRY_KINDS:
            bad.append(f"{slug}: registry_kind '{tool.get('registry_kind')}' is not one of "
                       f"{', '.join(REGISTRY_KINDS)}")

        # The stored claim is audited on its own terms, independently of re-derivation —
        # the same separation the category gate needs. If these checks read the re-derived
        # values instead, a fabricated justification is reported only as "does not
        # re-derive" and the specific diagnosis (which text was quoted, and that the
        # repository never published it) is lost.
        stored_kind = tool.get("registry_kind")
        stored_evidence = tool.get("registry_kind_evidence") or ""
        quoted = re.search(r'"(.+?)"', stored_evidence)
        if quoted:
            fragment = quoted.group(1)
            hay = " ".join([str(rec.get("description") or ""), slug,
                            " ".join(rec.get("topics") or [])]).lower()
            if fragment.lower() not in hay:
                bad.append(f"{slug}: registry_kind_evidence quotes \"{fragment}\", which does "
                           f"not occur in anything the API returned for this repository")
        if stored_kind == "server" and stored_evidence.startswith("the topic"):
            bad.append(f"{slug}: claimed to be a server on the strength of a bare 'mcp' topic, "
                       f"which says the repository relates to MCP but not that it is a server")
        if stored_kind == "server" and not stored_evidence.strip():
            bad.append(f"{slug}: claimed to be a server with no recorded evidence")
    return bad


def _tokens(text: str) -> set:
    """Split into whole lowercase tokens, so a signal can only match a whole word.

    The previous implementation asked `if signal in haystack`, which is a substring test
    over free prose. Short signals therefore matched inside ordinary words: `'ci'` occurs
    inside *"offi**ci**al"*, which classified both official Model Context Protocol SDKs as
    `ci-cd`. The same class of error was latent for `'cd'`, `'git'`, `'file'`, `'sql'`,
    `'docs'` and `'ci'` — every signal short enough to hide in a common word. Splitting
    on every non-alphanumeric run makes the comparison exact.

    Hyphenated forms are kept whole *as well as* split, because several signals are
    themselves hyphenated — `web-scraping`, `cloud-run`, `pull-request`. Splitting alone
    would make those signals unmatchable and silently reclassify whatever carried them:
    `firecrawl/firecrawl-mcp-server` publishes the topic `web-scraping` and dropped from
    `browser` to `search` under a split-only tokenizer. Both forms are still whole tokens,
    so nothing here reintroduces substring matching.
    """
    out: set = set()
    for raw in re.split(r"[^a-z0-9\-]+", str(text).lower()):
        if not raw:
            continue
        out.add(raw)                       # keep hyphenated forms whole: "web-scraping"
        out.update(part for part in raw.split("-") if part)
    out.discard("")
    return out


def detect_category(rec: Dict[str, Any]) -> tuple[str, str, List[str]]:
    """Return `(category, evidence_source, matched_signals)`.

    Matching is on whole tokens only, and the sources are tried in order of how much
    they can be trusted to mean what they say:

      1. **topics and slug segments.** Topics are curated by the owner specifically so
         the repository is discoverable under them, and slug segments are the name the
         owner chose. Both are structured: a token is either there or it is not.
      2. **the description**, only when nothing structured matched. Free prose is the
         weakest evidence — it is where *"official"* lives — but dropping it entirely
         would leave nine of the 35 records that publish no topics unclassified, so it
         stays as a fallback rather than as a peer of the curated fields.
      3. **`other`**, which is the honest answer when nothing matches and is already a
         member of the schema enum. Guessing a category from a repository's general
         subject matter would put a confident-looking wrong value into a field
         consumers filter on.

    The matched signals are returned with the category so the decision is auditable: a
    classification nobody can re-derive is a classification nobody can check, which is
    how the `ci-cd` error survived review of the generator that produced it.
    """
    slug = rec.get("slug", "")
    topics = rec.get("topics") or []
    structured = _tokens(slug.replace("/", " ")) | _tokens(" ".join(topics))
    for cat, signals in CATEGORY_SIGNALS:
        hit = sorted(s for s in signals if s in structured)
        if hit:
            return cat, "topics-or-slug", hit
    described = _tokens(rec.get("description") or "")
    for cat, signals in CATEGORY_SIGNALS:
        hit = sorted(s for s in signals if s in described)
        if hit:
            return cat, "description-fallback", hit
    return "other", "no-signal-matched", []


def detect_distribution(rec: Dict[str, Any]) -> tuple[str, Optional[str], Optional[str]]:
    """Return (distribution, npm_package, pypi_package) from observed fields only.

    The package name is taken from the path *after* the registry's own `/package/`
    segment, not from the last `/`-delimited token. Splitting on `/` alone truncates
    npm's scoped packages: `https://www.npmjs.com/package/@playwright/mcp` yields
    `mcp` instead of `@playwright/mcp`, which is not an installable name. The bug was
    invisible while `npm_package` was dropped between the markdown and `tools.json`;
    emitting the field surfaced it.
    """
    homepage = str(rec.get("homepage") or "")
    for dist, hints in DISTRIBUTION_HINTS:
        if not any(h in homepage for h in hints):
            continue
        pkg = package_from_url(homepage, dist)
        return dist, (pkg if dist == "npm" else None), (pkg if dist == "pypi" else None)
    # No package URL observed. Distribution is genuinely unknown from the API alone;
    # `source` is the only claim we can defend — the repository is buildable from source.
    return "source", None, None


def package_from_url(homepage: str, dist: str) -> Optional[str]:
    """Extract the installable package name from a registry URL, or None if absent.

    Returns None rather than a truncated guess when the URL does not have the shape
    the registry actually uses for package pages.
    """
    from urllib.parse import urlparse, unquote
    path = unquote(urlparse(homepage).path).strip("/")
    if dist == "npm":
        # npm package pages are /package/<name>; scoped names keep their @scope/ prefix.
        if not path.startswith("package/"):
            return None
        name = path[len("package/"):]
        return name or None
    if dist == "pypi":
        # PyPI package pages are /project/<name> (and legacy /pypi/<name>).
        for prefix in ("project/", "pypi/"):
            if path.startswith(prefix):
                name = path[len(prefix):].split("/")[0]
                return name or None
        return None
    return None


def risk_level(rec: Dict[str, Any]) -> str:
    """Security risk tier from observed signals, not from the name."""
    if rec.get("archived"):
        return "high"
    if rec.get("license_risk") not in (None, "none"):
        return "high"
    struct = rec.get("structure") or {}
    q = (rec.get("quality") or {}).get("security")
    if not struct.get("has_security_md"):
        return "medium"
    if q is not None and q < 6:
        return "medium"
    return "low"


def build_purpose(rec: Dict[str, Any]) -> tuple[str, str]:
    """Purpose text plus an evidence label. Never invents a capability."""
    desc = (rec.get("description") or "").strip()
    slug = rec["slug"]
    if len(desc) >= 20:
        return f'As stated by the repository itself: "{desc}"', "repository-description"
    parts = [f'Registered as an MCP server under `{slug}`.']
    if desc:
        parts.append(f'The repository describes itself only as "{desc}", which is too thin to rely on.')
    else:
        parts.append("The repository returned no description from the GitHub API.")
    parts.append(
        "Purpose must be confirmed from the README before adoption; this entry deliberately "
        "does not guess at capabilities."
    )
    return " ".join(parts), "repository-description-thin"


def record_to_tool(rec: Dict[str, Any]) -> Dict[str, Any]:
    purpose, purpose_evidence = build_purpose(rec)
    dist, npm_pkg, pypi_pkg = detect_distribution(rec)
    cat, cat_evidence, cat_signals = detect_category(rec)
    kind, kind_evidence = detect_registry_kind(rec)
    q = rec.get("quality") or {}
    archived = bool(rec.get("archived"))
    lic = rec.get("license")
    lic_risk = rec.get("license_risk")

    tool: Dict[str, Any] = {
        "id": slug_to_id(rec["slug"]),
        "name": rec.get("name") or rec["slug"].split("/")[-1],
        "repository": rec["slug"],
        "url": rec.get("url"),
        "npm_package": npm_pkg,
        "pypi_package": pypi_pkg,
        "distribution": dist,
        "official": bool(rec.get("official")),
        "maintainer": rec.get("owner"),
        "purpose": purpose,
        "category": cat,
        "category_evidence": cat_evidence,
        "category_signals": cat_signals,
        # What the repository IS, as opposed to what it connects to. `category` came from
        # the seed list; this comes from the repository's own observed text.
        "registry_kind": kind,
        "registry_kind_evidence": kind_evidence,
        # The GitHub API does not expose MCP transport, tool, resource or prompt lists.
        # Emitting empty rather than plausible values is the point of this generator.
        "transport": [],
        "tools": [],
        "resources": [],
        "prompts": [],
        # Authentication scheme is NOT observable from the GitHub API, so it is never
        # populated here. An earlier revision inferred "mixed" from the `official`
        # flag; that was a guess in a security-relevant field, and it contradicted
        # this module's own guarantee. `official` says who owns the repository — it
        # says nothing about how the server authenticates. Absence of the field, plus
        # capability_evidence: unverified, is the honest representation. Fill it in
        # only from the project's own documentation, then set capability_evidence to
        # "readme-reviewed" or "verified" and date it.
        "authentication": None,
        "permissions": {},
        "security": {
            "risk_level": risk_level(rec),
            "notes": (
                "Archived: no further fixes expected." if archived
                else ("No SECURITY.md published." if not (rec.get("structure") or {}).get("has_security_md")
                      else "SECURITY.md published.")
            ),
        },
        "local_or_remote": "local" if dist in ("npm", "pypi", "source") else "both",
        "setup_complexity": "low" if dist in ("npm", "pypi") else "medium",
        "production_readiness": "deprecated" if archived else (
            "production" if rec.get("production_ready") else "beta"),
        "status": rec.get("maintenance_status") or rec.get("status"),
        "license": None if lic in (None, "NONE", "NOASSERTION") else lic,
        "stars": rec.get("stars"),
        "tier": rec.get("tier"),
        "quality_score": rec.get("quality_score"),
        "confidence": "high" if rec.get("fetch_ok") else "low",
        "recommended_for": [],
        "not_recommended_for": (["adoption in new work — archived"] if archived else []),
        "tags": sorted(set((rec.get("curated_tags") or []) + (rec.get("topics") or []) + ["mcp"])),
        "sources": [{
            "title": f'{rec["slug"]} — GitHub repository metadata',
            "url": rec.get("url"),
            "type": "github-repository",
            "license": lic if lic not in (None, "NONE") else None,
            "claim_type": "fact",
            "confidence": "very-high" if rec.get("fetch_ok") else "low",
            "verified_at": TODAY,
            "note": "Observed via the GitHub REST API on the verified_at date. Star count, license, "
                    "archival status, push date and repository structure are API facts; capability "
                    "fields are not available from the API and are left empty rather than guessed.",
        }],
        "verified_at": TODAY,
        "expires_at": EXPIRES,
        # Provenance of the generator's own honesty boundaries.
        "capability_evidence": "unverified",
        "purpose_evidence": purpose_evidence,
        "license_risk": lic_risk,
        "stars_checked_at": TODAY,
        "days_since_push": rec.get("days_since_push"),
        "language": rec.get("language"),
    }
    return {k: v for k, v in tool.items() if v is not None or k in (
        "transport", "tools", "resources", "prompts", "permissions", "recommended_for",
        "not_recommended_for", "category", "category_evidence", "category_signals",
        "registry_kind", "registry_kind_evidence", "npm_package", "pypi_package")}


MD_TMPL = """---
id: {id}
name: {name}
purpose: >-
  {purpose_yaml}
category: {category}
category_evidence: {category_evidence}
category_signals: {category_signals}
registry_kind: {registry_kind}
registry_kind_evidence: >-
  {registry_kind_evidence}
distribution: {distribution}
official: {official}
maintainer: {maintainer}
repository: {repository}
url: {url}
npm_package: {npm_package}
pypi_package: {pypi_package}
transport: []
tools: []
resources: []
prompts: []
{authentication_line}permissions: {{}}
security:
  risk_level: {risk_level}
  notes: >-
    {security_notes}
local_or_remote: {local_or_remote}
setup_complexity: {setup_complexity}
production_readiness: {production_readiness}
status: {status}
license: {license}
license_risk: {license_risk}
stars: {stars}
stars_checked_at: {today}
tier: {tier}
quality_score: {quality_score}
confidence: {confidence}
recommended_for: {recommended_for}
not_recommended_for: {not_recommended_for}
capability_evidence: unverified
purpose_evidence: {purpose_evidence}
days_since_push: {days_since_push_fm}
language: {language_fm}
tags: {tags}
verified_at: {today}
expires_at: {expires}
sources:
  - title: "{source_title}"
    url: {url}
    type: github-repository
    license: {source_license}
    claim_type: fact
    confidence: {source_confidence}
    verified_at: {today}
    note: >-
      Observed via the GitHub REST API on {today}. Star count, license, archival status,
      push date, language and repository structure are API facts. MCP transport, tool,
      resource and prompt lists are not exposed by the API and are deliberately left
      empty rather than inferred from the repository name.
---

# {name}

`{repository}` — {one_line}

**Registry kind: `{registry_kind}`.** {registry_kind_sentence}

## What is verified

These fields were read from the GitHub REST API on **{today}** and are facts, not judgements:

| Field | Value |
|---|---|
| Repository | [`{repository}`]({url}) |
| Stars | {stars_fmt} (checked {today}) |
| License | {license_display} |
| Archived | {archived} |
| Last push | {pushed_at} ({days_since_push} days ago) |
| Language | {language} |
| Latest release | {latest_release} |
| Contributors | {contributors} |
| SECURITY.md published | {has_security_md} |
| Tests present | {has_tests} |
| CI present | {has_ci} |
| Tier / quality score | {tier} / {quality_score} |

## What is NOT verified

**MCP capability fields are empty on purpose.** The GitHub API does not expose a server's transport
list, tool list, resource list, prompt list or authentication scheme. Inferring them from the
repository name or description is how an integrator ends up configuring `stdio` against a server that
only speaks `streamable-http`, or granting filesystem permissions to a server that never asked for
them.

Before adopting this server, confirm from its own README:

- [ ] Which transports it supports (`stdio`, `sse`, `streamable-http`)
- [ ] The exact tool names it exposes, and what each one can mutate
- [ ] Whether it exposes resources or prompts, and what they return
- [ ] How it authenticates, and what scope the credential carries
- [ ] Which permissions it requires at the OS, network and account level
- [ ] Whether the published package matches this repository at this commit

Record the answers back into this file and set `capability_evidence: verified` with the date. Until
then this entry is a **pointer with verified provenance**, not a capability description.

## Purpose

{purpose_block}

## Adoption guidance

{adoption}

## References

- [`knowledge/mcp/security.md`](../security.md) — the security grading applied here
- [`skills/mcp-integration/SKILL.md`](../../../skills/mcp-integration/SKILL.md) — how to evaluate and wire a server
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../../skills/dont-reinvent-the-wheel/SKILL.md) — check here before building
- [`indexes/mcp.md`](../../../indexes/mcp.md) — the generated index over this registry
- [`metadata/tools.json`](../../../metadata/tools.json) — the machine-readable form of this entry
"""


def wrap_yaml(text: str, width: int, indent: str) -> str:
    """Wrap a string for use under a YAML `>-` block scalar."""
    import textwrap
    flat = " ".join(str(text).split())
    return textwrap.fill(flat, width,
                         initial_indent=indent, subsequent_indent=indent).lstrip()


def render_md(t: Dict[str, Any], rec: Dict[str, Any]) -> str:
    import textwrap
    struct = rec.get("structure") or {}
    archived = bool(rec.get("archived"))
    lic = rec.get("license")
    if archived:
        adoption = (
            "**Do not adopt for new work.** This repository is archived: no further fixes, no further "
            "dependency updates and no security patches should be expected. It remains in the registry "
            "because an archived server can still be the correct answer for a frozen integration, and "
            "because hiding it would send the next reader to rediscover it without the warning. If you "
            "are already running it, treat it as a pinned dependency with a known end of life and plan "
            "the migration."
        )
    elif t.get("license_risk") not in (None, "none"):
        adoption = (
            f"**Legally unsafe to redistribute.** The GitHub API reports the license as `{lic}`. "
            "Absence of a license is not permission: without one, the default is all rights reserved, "
            "so vendoring, bundling or mirroring this code is a copyright risk regardless of how good "
            "the project is or how many stars it has. Using it as a running service under its own terms "
            "may be fine; copying it into this repository or into a product is not. Ask the maintainer "
            "for a license before depending on it."
        )
    elif lic in (None, "NONE", "NOASSERTION"):
        adoption = (
            f"**License is non-standard (`{lic}`).** The API returned a license the SPDX list does not "
            "recognise, which usually means a custom or composite notice. Read the LICENSE file itself "
            "before redistributing or vendoring. Do not assume MIT-equivalent terms."
        )
    elif not struct.get("has_security_md"):
        adoption = (
            "Usable, with a caveat: **no SECURITY.md is published**, so there is no stated disclosure "
            "channel and no published security posture. For a server that will hold a credential or "
            "reach a private system, that is a real gap — raise it with the maintainer, pin a version, "
            "and scope the credential as narrowly as the integration allows."
        )
    else:
        adoption = (
            "Actively maintained, license clear, security policy published. Adopt on the usual terms: "
            "pin a version, scope the credential to the minimum the integration needs, and confirm the "
            "capability checklist above before granting permissions. Re-verify after the expiry date on "
            "this entry — MCP servers move quickly and a tier earned in one quarter is not a tier earned "
            "in the next."
        )
    # Body prose, so escaped: this is rendered markdown, and `purpose` is built from the
    # repository's own description, which its owner controls.
    purpose_block = untrusted(t["purpose"])
    if t.get("purpose_evidence") == "repository-description-thin":
        purpose_block += (
            "\n\n> The repository's own description was too thin to serve as a purpose statement. "
            "Expand this section from the README, then change `purpose_evidence` to "
            "`readme-reviewed` and date it."
        )
    return MD_TMPL.format(
        id=t["id"], name=t["name"],
        # Frontmatter is data rather than prose, so it is made YAML-safe (newlines collapsed,
        # which also stops an upstream newline from starting a new mapping key) instead of
        # markdown-escaped. The dead `if False else` branch that used to sit here is gone.
        purpose_yaml=textwrap.fill(yaml_folded(t["purpose"]), 96).replace("\n", "\n  "),
        category=t.get("category") or "other",
        category_evidence=yaml_scalar(t.get("category_evidence") or "no-signal-matched"),
        category_signals=yaml_scalar(t.get("category_signals") or []),
        registry_kind=t.get("registry_kind") or "unproven",
        registry_kind_sentence=kind_sentence(t),
        registry_kind_evidence=textwrap.fill(t.get("registry_kind_evidence") or "", 88).replace("\n", "\n  "),
        distribution=t["distribution"],
        official="true" if t["official"] else "false",
        maintainer=t.get("maintainer") or "null",
        repository=t["repository"], url=t["url"],
        authentication_line=(f"authentication: {t['authentication']}\n" if t.get("authentication") else ""),
        # Fields emitted here and nowhere else: if a key computed by record_to_tool()
        # is missing from this template it never reaches metadata/tools.json, because
        # extract_registries.py reads the markdown frontmatter and nothing else.
        # assert_chain_complete() below fails the build when the two sides diverge.
        npm_package=yaml_scalar(t.get("npm_package")),
        pypi_package=yaml_scalar(t.get("pypi_package")),
        recommended_for=yaml_scalar(t.get("recommended_for") or []),
        not_recommended_for=yaml_scalar(t.get("not_recommended_for") or []),
        days_since_push_fm=yaml_scalar(t.get("days_since_push")),
        language_fm=yaml_scalar(t.get("language")),
        risk_level=t["security"]["risk_level"],
        security_notes=textwrap.fill(t["security"]["notes"], 90).replace("\n", "\n    "),
        local_or_remote=t["local_or_remote"], setup_complexity=t["setup_complexity"],
        production_readiness=t["production_readiness"], status=t.get("status") or "ACTIVE",
        license="null" if t.get("license") is None else t["license"],
        license_risk=t.get("license_risk") or "none",
        stars=t.get("stars") if t.get("stars") is not None else "null",
        stars_fmt=f'{t["stars"]:,}' if t.get("stars") is not None else "unknown",
        today=TODAY, expires=EXPIRES, tier=t["tier"],
        quality_score=t.get("quality_score") if t.get("quality_score") is not None else "null",
        confidence=t.get("confidence") or "medium",
        tags=json.dumps(t.get("tags") or []),
        source_title=f'{t["repository"]} — GitHub repository metadata',
        source_license="null" if lic in (None, "NONE") else lic,
        source_confidence="very-high" if rec.get("fetch_ok") else "low",
        one_line=textwrap.fill(untrusted(t["purpose"]), 88),
        archived="yes" if archived else "no",
        pushed_at=rec.get("pushed_at") or "unknown",
        days_since_push=rec.get("days_since_push") if rec.get("days_since_push") is not None else "unknown",
        language=rec.get("language") or "unknown",
        latest_release=rec.get("latest_release") or "none published",
        contributors=rec.get("contributors") if rec.get("contributors") is not None else "unknown",
        has_security_md="yes" if struct.get("has_security_md") else "**no**",
        has_tests="yes" if struct.get("has_tests") else "**no**",
        has_ci="yes" if struct.get("has_ci") else "**no**",
        adoption=adoption, purpose_block=purpose_block,
        purpose_evidence=t.get("purpose_evidence") or "repository-description",
        license_display=(
            f'`{lic}` — **no SPDX-recognised license; do not redistribute**'
            if t.get("license_risk") not in (None, "none")
            else (f'`{lic}` (non-standard — read the LICENSE file)'
                  if lic in (None, "NONE", "NOASSERTION") else f'`{lic}`')),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit non-zero if output would change")
    args = ap.parse_args()

    if not REPOS.exists():
        print(f"error: {REPOS} missing — run fetch_github_metadata.py first", file=sys.stderr)
        return 2
    blob = json.loads(REPOS.read_text())
    recs = [r for r in blob["repositories"] if r.get("category") == "mcp-servers"]
    if not recs:
        print("error: no mcp-servers records in metadata/repositories.json", file=sys.stderr)
        return 2

    recs.sort(key=lambda r: (-(r.get("stars") or 0), r["slug"]))
    tools = [record_to_tool(r) for r in recs]

    # `tier` has no honest default. It used to fall back to "UNVERIFIED", but that label
    # now means specifically "the metadata could not be verified", so defaulting to it
    # would assert a fetch failure that did not happen. Every record in
    # repositories.json carries a tier; a record without one is malformed and should
    # stop the build rather than be quietly relabelled.
    kinds = assert_kinds_are_evidenced(recs, tools)
    if kinds:
        print("error: a registry_kind is not backed by observed text:", file=sys.stderr)
        for k in kinds:
            print(f"  {k}", file=sys.stderr)
        return 2

    substrings = assert_categories_are_whole_tokens(recs, tools)
    if substrings:
        print("error: a category was assigned on something other than a whole token:",
              file=sys.stderr)
        for s in substrings:
            print(f"  {s}", file=sys.stderr)
        return 2

    untiered = [t["repository"] for t in tools if not t.get("tier")]
    if untiered:
        print("error: record(s) have no tier in metadata/repositories.json, and tier has "
              "no honest default:", file=sys.stderr)
        for u in untiered:
            print(f"  {u}", file=sys.stderr)
        return 2

    guesses = assert_no_guesses(tools)
    if guesses:
        print("error: the generator asserted capability fields it cannot observe:",
              file=sys.stderr)
        for g in guesses:
            print(f"  {g}", file=sys.stderr)
        return 2


    OUT_MD.mkdir(parents=True, exist_ok=True)
    md_files: Dict[str, str] = {}
    for t, r in zip(tools, recs):
        fn = r["slug"].replace("/", "__") + ".md"
        md_files[fn] = render_md(t, r)

    # Every field record_to_tool() computes must appear in the rendered frontmatter,
    # which is the only thing extract_registries.py reads. Checked against rendered
    # output rather than against tools.json, which has not been regenerated yet at
    # this point in the chain, and rather than against MD_TMPL's source, where a
    # conditional prefix can hide a key from a line-start match.
    emitted: set = set()
    for txt in md_files.values():
        emitted |= frontmatter_keys(txt)
    computed = _union_keys(tools)
    never_emitted = sorted(k for k in computed
                           if k not in emitted and k not in TEMPLATE_ALIASES)
    if never_emitted:
        print("error: record_to_tool() computes field(s) the rendered frontmatter never "
              "emits, so they will be lost before tools.json:", file=sys.stderr)
        for f in never_emitted:
            print(f"  {f}", file=sys.stderr)
        return 2

    if args.check:
        def norm(s: str) -> str:
            """Compare content, not the clock. Mirrors the CI drift job."""
            return "\n".join(l for l in s.splitlines() if not l.lstrip().startswith('"generated_at"'))

        drift = []
        for fn, txt in md_files.items():
            p = OUT_MD / fn
            if not p.exists() or norm(p.read_text()) != norm(txt):
                drift.append(f"knowledge/mcp/registry/{fn}")
        stale = [p.name for p in OUT_MD.glob("*.md") if p.name not in md_files]
        if stale:
            drift += [f"knowledge/mcp/registry/{s} (orphan)" for s in stale]
        if drift:
            print("MCP registry is out of sync:", file=sys.stderr)
            for d in drift:
                print(f"  {d}", file=sys.stderr)
            return 1
        guesses = assert_no_guesses(tools)
        if guesses:
            print("capability fields are populated without evidence:", file=sys.stderr)
            for g in guesses:
                print(f"  {g}", file=sys.stderr)
            return 1
        kinds = assert_kinds_are_evidenced(recs, tools)
        if kinds:
            print("a registry_kind is not backed by observed text:", file=sys.stderr)
            for k in kinds:
                print(f"  {k}", file=sys.stderr)
            return 1
        substrings = assert_categories_are_whole_tokens(recs, tools)
        if substrings:
            print("a category is not backed by a whole token:", file=sys.stderr)
            for s in substrings:
                print(f"  {s}", file=sys.stderr)
            return 1
        lost = assert_chain_complete(tools)
        if lost:
            print("registry fields are lost between markdown and tools.json:",
                  file=sys.stderr)
            for l in lost:
                print(f"  {l}", file=sys.stderr)
            return 1
        print(f"MCP registry in sync: {len(tools)} entries; "
              f"no capability field asserted without evidence; "
              f"all {len(_union_keys(tools))} computed fields reach tools.json; "
              f"every category backed by a whole token; "
              f"{_kind_counts(tools)}")
        return 0

    for fn, txt in md_files.items():
        (OUT_MD / fn).write_text(txt)
    for p in OUT_MD.glob("*.md"):
        if p.name not in md_files:
            p.unlink()
            print(f"  removed orphan {p.name}")

    thin = sum(1 for t in tools if t.get("purpose_evidence") == "repository-description-thin")
    risky = [t["repository"] for t in tools if t.get("license_risk") not in (None, "none")]
    arch = [t["repository"] for t in tools if t["production_readiness"] == "deprecated"]
    print(f"  knowledge/mcp/registry/          {len(tools):>4} entries")
    print("  metadata/tools.json              regenerate via extract_registries.py")
    print(f"  purpose needs human expansion:   {thin:>4}")
    print(f"  license risk (do not redistribute): {len(risky)} -> {', '.join(risky) or 'none'}")
    print(f"  archived (do not adopt):         {len(arch)} -> {', '.join(arch) or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

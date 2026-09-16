#!/usr/bin/env python3
"""Frontmatter parsing + schema resolution for the knowledge base."""
from __future__ import annotations

import re
from datetime import date, datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install -r scripts/requirements.txt") from e

try:
    import jsonschema
    from jsonschema import RefResolver
except ImportError:  # pragma: no cover
    jsonschema = None
    RefResolver = None

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"

FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)

# filename -> schema, evaluated in order; first match wins
RULES: List[Tuple[str, str]] = [
    ("skills/*/SKILL.md", "skill.schema.json"),
    ("skills/**/references/*.md", "knowledge.schema.json"),
    ("agents/*/AGENT.md", "agent.schema.json"),
    ("workflows/*/WORKFLOW.md", "workflow.schema.json"),
    ("knowledge/mcp/registry/*.md", "mcp.schema.json"),
    ("knowledge/**/*.md", "knowledge.schema.json"),
    ("patterns/**/*.md", "pattern.schema.json"),
    ("prompts/**/*.md", "prompt.schema.json"),
    ("evaluations/**/*.md", "evaluation.schema.json"),
    ("datasets/**/*.md", "dataset.schema.json"),
    ("models/**/*.md", "model.schema.json"),
    ("sources/**/*.md", "source.schema.json"),
    ("decision-records/**/*.md", "knowledge.schema.json"),
    ("anti-patterns/**/*.md", "pattern.schema.json"),
    ("failure-modes/**/*.md", "pattern.schema.json"),
    ("gotchas/**/*.md", "knowledge.schema.json"),
    ("research-archive/**/*.md", "knowledge.schema.json"),
    ("experimental/**/*.md", "knowledge.schema.json"),
]

# Paths exempt from frontmatter entirely.
EXEMPT_EXACT = {
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
    "LICENSE", "LICENSE-CODE", "CODE_OF_CONDUCT.md",
}
EXEMPT_GLOBS = [
    "indexes/*.md",            # generated
    "repositories/**/*.md",    # generated
    "metadata/**",             # generated
    ".github/**",
    "scripts/**",
    ".cache/**",
    "experimental/**/README.md",
]
# Files inside a governed tree that are structural rather than content.
EXEMPT_NAMES = {"README.md", "AGENTS.md", "CHANGELOG.md", "TESTS.md"}

# ---------------------------------------------------------------------------
# Grading rule: an evidence level caps the confidence a document may claim.
#
# One rule, applied corpus-wide, so that a claim can never be stronger than the
# evidence that established it. Derived from the descriptions in
# schemas/common.defs.json#/$defs/evidenceLevel — not invented here:
#
#   verified-*         the claim was checked against its primary source directly
#   cross-checked      independent sources agree, but none is the primary source
#   single-source      one source, not corroborated
#   emerging-consensus practitioners broadly agree; no primary source settles it
#   practitioner-experience  judgement from practice, not from a checked source
#   model-generated    must never be presented as fact (brief section 78)
#
# Confidence is only ever DOWNGRADED to meet this cap. Upgrading evidence_level to
# match a confidence is the failure this rule exists to prevent.
CONFIDENCE_CAP: Dict[str, str] = {
    "verified-github-api": "very-high",
    "verified-official-docs": "very-high",
    "verified-paper": "very-high",
    "verified-benchmark-run": "very-high",
    "cross-checked": "high",
    "single-source": "medium",
    "emerging-consensus": "medium",
    "practitioner-experience": "medium",
    "model-generated": "low",
}

CONFIDENCE_RANK: Dict[str, int] = {
    "very-high": 4, "high": 3, "medium": 2, "low": 1, "unverified": 0, "conflicting": 0,
}


def confidence_cap_error(evidence_level: Any, confidence: Any) -> Optional[str]:
    """Return an error string when `confidence` exceeds what `evidence_level` supports."""
    cap = CONFIDENCE_CAP.get(str(evidence_level)) if evidence_level else None
    if not cap or not confidence:
        return None
    if CONFIDENCE_RANK.get(str(confidence), 0) > CONFIDENCE_RANK[cap]:
        return (f"confidence '{confidence}' exceeds the cap '{cap}' for "
                f"evidence_level '{evidence_level}' — downgrade confidence or raise the "
                f"evidence (never the reverse)")
    return None


@dataclass
class Doc:
    path: Path
    rel: str
    schema: Optional[str]
    data: Dict[str, Any] = field(default_factory=dict)
    body: str = ""
    raw_front: str = ""
    parse_error: Optional[str] = None


def iter_markdown(root: Path = ROOT) -> List[Path]:
    skip = {".git", ".cache", "node_modules", ".venv", "__pycache__"}
    out = []
    for p in sorted(root.rglob("*.md")):
        if any(part in skip for part in p.parts):
            continue
        out.append(p)
    return out


def is_exempt(rel: str) -> bool:
    if rel in EXEMPT_EXACT:
        return True
    name = Path(rel).name
    for g in EXEMPT_GLOBS:
        if _glob(rel, g):
            return True
    # README/AGENTS/CHANGELOG/TESTS are structural navigation and status documents, not
    # claims about the world, so they are exempt everywhere — including under knowledge/,
    # where a directory README exists to say what belongs there and whether it has been
    # written yet. Grading a placeholder against the content schema would force it to
    # assert a confidence level for content that does not exist.
    if name in EXEMPT_NAMES:
        return True
    return False


def _glob(rel: str, pattern: str) -> bool:
    from fnmatch import fnmatch
    if fnmatch(rel, pattern):
        return True
    # fnmatch does not treat ** as recursive; approximate it
    if "**" in pattern:
        loose = pattern.replace("**/", "*").replace("**", "*")
        if fnmatch(rel, loose):
            return True
        head = pattern.split("**")[0].rstrip("/")
        if head and rel.startswith(head):
            tail = pattern.split("**")[-1].lstrip("/")
            if not tail or fnmatch(rel, "*/" + tail) or fnmatch(Path(rel).name, tail):
                return True
    return False


def schema_for(rel: str) -> Optional[str]:
    for pattern, schema in RULES:
        if _glob(rel, pattern):
            return schema
    return None


def requires_frontmatter(rel: str) -> bool:
    if is_exempt(rel):
        return False
    return schema_for(rel) is not None


def _normalise_dates(obj: Any) -> Any:
    """YAML parses bare `2026-09-15` as datetime.date. Schemas declare ISO-8601 strings, so
    normalise every date/datetime to its ISO string form on load. Applied recursively because
    dates appear nested inside `sources`, `scoring` and `provenance` blocks."""
    if isinstance(obj, (datetime, date)) and not isinstance(obj, bool):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _normalise_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_normalise_dates(v) for v in obj]
    return obj


def parse(path: Path, root: Path = ROOT) -> Doc:
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    doc = Doc(path=path, rel=rel, schema=schema_for(rel))
    m = FRONT.match(text)
    if not m:
        doc.body = text
        return doc
    doc.raw_front = m.group(1)
    doc.body = text[m.end():]
    try:
        data = yaml.safe_load(doc.raw_front)
        if data is None:
            data = {}
        if not isinstance(data, dict):
            doc.parse_error = f"frontmatter is a {type(data).__name__}, expected a mapping"
            data = {}
        doc.data = _normalise_dates(data)
    except yaml.YAMLError as e:
        doc.parse_error = f"YAML error: {e}"
    return doc


_schema_cache: Dict[str, Any] = {}


def load_schema(name: str) -> Dict[str, Any]:
    if name not in _schema_cache:
        import json
        _schema_cache[name] = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
    return _schema_cache[name]


def validate(doc: Doc) -> List[str]:
    """Return a list of human-readable validation errors (empty == valid)."""
    errs: List[str] = []
    if doc.parse_error:
        return [doc.parse_error]
    if not doc.schema:
        return errs
    if jsonschema is None:
        return ["jsonschema not installed; cannot validate"]
    try:
        schema = load_schema(doc.schema)
    except FileNotFoundError:
        return [f"schema file missing: schemas/{doc.schema}"]

    store = {}
    for f in SCHEMAS.glob("*.json"):
        import json as _json
        try:
            s = _json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if "$id" in s:
            store[s["$id"]] = s
        store[f.name] = s

    resolver = RefResolver(base_uri=f"file://{SCHEMAS}/", referrer=schema, store=store) if RefResolver else None
    v = jsonschema.Draft202012Validator(schema, resolver=resolver)
    for e in sorted(v.iter_errors(doc.data), key=lambda x: list(x.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        msg = e.message
        if len(msg) > 260:
            msg = msg[:257] + "..."
        errs.append(f"{loc}: {msg}")
    return errs


def headings(body: str) -> List[Tuple[int, str]]:
    out = []
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            out.append((len(m.group(1)), m.group(2).strip()))
    return out


def slugify(h: str) -> str:
    """GitHub's heading-anchor algorithm.

    Lowercase, drop everything that is not a word character, space or hyphen, then replace each
    remaining space with a hyphen. Runs are NOT collapsed: "Validation & CI" becomes
    "validation--ci", because the removed "&" leaves two spaces that each map to a hyphen.
    Collapsing them would produce anchors that do not exist on the rendered page.
    """
    s = re.sub(r"[^\w\s-]", "", h.lower().strip())
    return s.replace(" ", "-")


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars/token for English prose, ~3.3 for code-heavy text."""
    return max(1, round(len(text) / 3.8))

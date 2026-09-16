#!/usr/bin/env python3
"""Untrusted upstream text, made safe to render.

`metadata/repositories.json` stores what the GitHub API returned, including `description`,
`homepage` and `topics`. Those fields are **attacker-controlled**: any repository owner can set
a description, and the fetcher records it verbatim — correctly, because it is the observed fact.
The problem is what happens next. Generators wrote that text straight into markdown, so it
travelled from an arbitrary third party into a file this repository publishes for agents to
ingest as trusted guidance.

Verified in the corpus before this module existed, out of 401 descriptions:

  * 5 contain bare URLs, which GitHub renders as live links — a card for `postgres/postgres`
    linked out to a wiki page nobody here had reviewed;
  * `repositories/databases/postgres--postgres.md` rendered `*mirror*` as italics, so upstream
    emphasis silently became this repository's emphasis;
  * `camel-ai/camel` reproduced the vendor claim "The first and the best multi-agent framework"
    as though it were content, and that card was ranked #1 under "BEST AGENT FRAMEWORKS" in
    `indexes/best-of.md`.

None of those is malicious, which is exactly why they matter: the same pipeline that renders a
harmless `*mirror*` as formatting renders `Ignore prior instructions and …` as an instruction to
whatever agent reads the card next. Today's corpus being clean is a property of the current seed
list, not of the pipeline.

The rule this module implements is **display, do not interpret**. Raw data stays raw in
`repositories.json` — sanitising the stored record would destroy the evidence of what upstream
actually said. Sanitisation happens at the markdown boundary, where the text stops being data
and starts being rendering.

Two functions, because they answer two different questions:

  `untrusted()`       make a string safe to put in a markdown document
  `injection_marks()` say whether the string looks like it is trying to steer a reader

The second is deliberately separate from the first. Escaping stops markdown from being
interpreted; it does nothing about a description that says "ignore your instructions", which is
still a description, still escaped, and still worth quarantining.
"""
from __future__ import annotations

import re
from typing import List, Tuple

# A description that long is not a description. GitHub's own limit is 350 characters; the
# longest in the corpus is 346. The cap exists to bound what a future upstream can push into
# an agent's context window through this field, not to trim anything that is here today.
MAX_RENDERED_CHARS = 600

# Characters markdown interprets *wherever they appear*. Escaped with a backslash, which
# renders as the character itself — so `*mirror*` is displayed as `*mirror*` instead of
# becoming emphasis. Nothing is deleted: removing the characters would silently alter what
# upstream said.
_MD_ALWAYS = ("`", "*", "[", "]", "<", "|")

# `_` is emphasis only at a word boundary in GitHub-flavoured markdown. `:cherry_blossom:` is
# already inert, so escaping it would put a visible backslash in files this repository expects
# agents to read as plain text. `*` has no such rule and is always escaped.
_MD_UNDERSCORE = re.compile(r"(?<![\w])_|_(?![\w])")

# Characters that are only active in a position, and are therefore escaped only there. Escaping
# them everywhere would turn "It's fast!" into "It's fast\!" — harmless when rendered, visible
# noise when read, and this corpus is read both ways.
_MD_LEADING = re.compile(r"(?m)^\s*([>#])")
_MD_BANG = re.compile(r"!(?=\[)")
_MD_STRIKE = re.compile(r"~~")

# A bare URL becomes a live link in GitHub-flavoured markdown whether or not anyone meant it
# to. Wrapping it in backticks keeps the address readable and copyable but stops it being a
# link this repository is asserting. Deliberately not deleted: the URL is part of the observed
# description, and hiding it would make the record less useful than the one it replaced.
# A `(` before the address does not exempt it — descriptions are plain text, not markdown
# source, so there is no `[label](url)` syntax here to preserve.
_BARE_URL = re.compile(r"(?<![\w`>/])(https?://[^\s<>()\[\]\"'`]+)", re.IGNORECASE)

def untrusted(value, *, cap: int = MAX_RENDERED_CHARS) -> str:
    """Render `value` as inert markdown text.

    Accepts None and non-strings because the fields come from an API and the caller should not
    have to defend against that at every render site.
    """
    if value is None:
        return ""
    text = str(value)

    # Newlines would break out of a blockquote or a table cell and start a new block, which is
    # how a description could inject a heading or a second paragraph of its own. Collapsed
    # rather than escaped: a description is one line of prose upstream anyway.
    text = re.sub(r"\s*\n\s*", " ", text).strip()

    if len(text) > cap:
        text = text[:cap].rstrip() + " …[truncated]"

    # `\` first, so the escapes added below are not themselves escaped.
    text = text.replace("\\", "\\\\")
    for ch in _MD_ALWAYS:
        text = text.replace(ch, "\\" + ch)
    text = _MD_UNDERSCORE.sub(lambda m: "\\" + m.group(0), text)
    text = _MD_LEADING.sub(lambda m: "\\" + m.group(1), text)
    text = _MD_BANG.sub("\\!", text)
    text = _MD_STRIKE.sub("\\~\\~", text)

    # Backslash-escaping the URL's own characters would make it unreadable and uncopyable, so
    # URLs are handled as units: un-escape the address and wrap it as inline code.
    def _url(m: re.Match) -> str:
        raw = m.group(1).replace("\\", "")
        return f"`{raw}`"

    return _BARE_URL.sub(_url, text)


# Characters that may not appear in a URL this repository is willing to publish as a link.
# Angle brackets and quotes would break out of the markdown link syntax, a pipe would break a
# table cell, a backtick would open a code span, and whitespace means it is not one URL.
# Written as a set rather than a regex character class so the contents are readable.
_FORBIDDEN_IN_URL = frozenset('<>"\'`| \t\n\r')

# Schemes that are safe to hand a reader. `homepage` is owner-controlled, so it is a place to
# put `javascript:` or `data:` and have this repository render it as a link.
_LINKABLE_PREFIX = ("http://", "https://")


def untrusted_url(value) -> str:
    """Render an upstream-supplied URL field (`homepage`) safely.

    A URL field is not prose, so it gets a different treatment from `untrusted()`. Backticking
    a homepage would remove a link a reader genuinely wants and gains almost nothing: the
    destination of a bare URL is already visible, which is the mitigation that matters. What a
    bare render does *not* protect against is the scheme — so: link only what is plainly
    http(s) and free of syntax-breaking characters, with the destination as its own label, and
    fall back to inert escaped text for anything else.
    """
    if value is None:
        return ""
    text = re.sub(r"\s*\n\s*", " ", str(value)).strip()
    if not text:
        return ""
    if text.lower().startswith(_LINKABLE_PREFIX) and not (set(text) & _FORBIDDEN_IN_URL):
        return f"[{text}]({text})"
    return untrusted(text)


def yaml_folded(value) -> str:
    """Make an upstream string safe to emit inside a folded YAML scalar (`>-`).

    Frontmatter is data, not prose, so markdown escaping would be wrong here — it would put
    backslashes into a value consumers read programmatically. What *can* go wrong is the YAML
    itself: a newline in a folded scalar continues the scalar only if the following line is
    indented, and an unindented line becomes a new mapping key. An upstream description
    containing a newline could therefore add a frontmatter field of its own. Collapsing
    newlines removes that, and is the same collapse `untrusted()` already performs.
    """
    if value is None:
        return ""
    return re.sub(r"\s*\n\s*", " ", str(value)).strip()


# Role markers and instruction-shaped phrasing: the patterns that turn a description from text
# into a prompt. Matching is conservative on purpose. A loose rule here flags ordinary technical
# prose — "the system prompt is loaded at startup", "you should pin a version" — and a check
# that cries wolf on the corpus it is protecting gets disabled within a month.
_INJECTION: Tuple[Tuple[str, "re.Pattern[str]"], ...] = (
    ("instruction-override", re.compile(
        r"(?i)\b(?:ignore|disregard|forget|override|bypass)\s+(?:all\s+|any\s+)?"
        r"(?:prior|previous|above|earlier|your|the)\s+"
        r"(?:instructions?|prompts?|rules?|guidelines?|context|messages?)")),
    ("new-instruction", re.compile(
        r"(?i)\b(?:you\s+(?:are|must|should|will)\s+now|from\s+now\s+on\s+you|"
        r"act\s+as\s+(?:a|an|the)|pretend\s+(?:to\s+be|you\s+are)|new\s+instructions?)")),
    ("role-marker", re.compile(r"(?im)^\s*(?:system|assistant|developer|tool)\s*:")),
    ("hidden-role-marker", re.compile(
        r"(?i)(?:<\|?\s*(?:im_start|im_end|system|assistant)\s*\|?>|"
        r"\[\s*(?:system|assistant)\s*\]|\u00ab\s*system\s*\u00bb)")),
    ("prompt-exfiltration", re.compile(
        r"(?i)\b(?:reveal|print|repeat|output|show)\s+(?:your|the)\s+"
        r"(?:system\s+prompt|instructions?|hidden\s+prompt|initial\s+prompt)")),
    ("tool-invocation", re.compile(
        r"(?i)\b(?:call|invoke|execute|run)\s+(?:the\s+)?(?:function|tool)\s*[:\(]")),
    ("html-script", re.compile(r"(?i)<\s*(?:script|iframe|object|embed|svg|img)\b")),
)


def injection_marks(value) -> List[str]:
    """The names of every injection pattern `value` matches. Empty means it looks like prose.

    Kept separate from `untrusted()` because escaping and quarantining are different responses.
    A description that says "ignore prior instructions" is still safely *rendered* by
    `untrusted()`; what it should not be is silently published as this repository's own text.
    """
    if value is None:
        return []
    text = str(value)
    return [name for name, rx in _INJECTION if rx.search(text)]


def untrusted_list(values) -> List[str]:
    """`untrusted()` over a list of strings, e.g. repository `topics`."""
    if not values:
        return []
    return [untrusted(v) for v in values if v is not None]


def any_injection_marks(fields) -> List[str]:
    """Injection marks across several fields, reported as `field: pattern`.

    Takes a mapping so a caller can hand over the whole record and get back enough detail to
    quarantine it with a reason, rather than a bare yes/no.
    """
    found: List[str] = []
    for name, value in (fields or {}).items():
        if isinstance(value, (list, tuple)):
            for i, item in enumerate(value):
                for mark in injection_marks(item):
                    found.append(f"{name}[{i}]: {mark}")
        else:
            for mark in injection_marks(value):
                found.append(f"{name}: {mark}")
    return found

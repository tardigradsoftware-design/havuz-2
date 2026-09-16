#!/usr/bin/env python3
"""H-7 regression: a registry category must come from a whole token, never from a substring.

`detect_category()` matched signals with `if signal in haystack` over description + topics +
slug. Short signals therefore matched inside ordinary words, and the corpus already showed it:
`modelcontextprotocol/python-sdk` and `modelcontextprotocol/typescript-sdk` were both
classified `ci-cd` because `'ci'` occurs inside *"offi**ci**al"* in their own descriptions
(*"The official Python SDK for Model Context Protocol"*). `category` is what a consumer
filters the registry on, and `ci-cd` is confidently wrong for both official SDKs. The same
error was latent for `'cd'`, `'git'`, `'file'`, `'sql'` and `'docs'`.

Run: python3 -m unittest tests.test_mcp_category -v
"""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gen = load("gen_mcp", "scripts/generate-index/generate_mcp_registry.py")
SCHEMA = ROOT / "schemas" / "mcp.schema.json"
TOOLS = ROOT / "metadata" / "tools.json"
REPOS = ROOT / "metadata" / "repositories.json"

ALL_SIGNALS = {s: cat for cat, sigs in gen.CATEGORY_SIGNALS for s in sigs}
SHORT_SIGNALS = [s for s in ALL_SIGNALS if len(s) <= 4]


def rec(slug="acme/thing", description="", topics=()):
    return {"slug": slug, "description": description, "topics": list(topics)}


class TestTheOriginalFalsePositive(unittest.TestCase):
    """The exact defect from the finding, reproduced from the real records."""

    def test_official_sdks_are_not_ci_cd(self):
        for slug, desc in (
            ("modelcontextprotocol/python-sdk",
             "The official Python SDK for Model Context Protocol servers and clients"),
            ("modelcontextprotocol/typescript-sdk",
             "The official TypeScript SDK for Model Context Protocol servers and clients"),
        ):
            with self.subTest(slug=slug):
                cat, evidence, signals = gen.detect_category(rec(slug, desc, ["mcp", "mcp-server"]))
                self.assertNotEqual("ci-cd", cat)
                self.assertNotIn("ci", signals,
                                 "'ci' was matched inside the word 'official'")

    def test_the_word_official_yields_no_signal_at_all(self):
        cat, evidence, signals = gen.detect_category(rec("x/y", "The official thing", []))
        self.assertEqual("other", cat)
        self.assertEqual([], signals)
        self.assertEqual("no-signal-matched", evidence)

    def test_committed_corpus_has_no_ci_cd_from_the_word_official(self):
        for t in json.loads(TOOLS.read_text())["tools"]:
            with self.subTest(slug=t["repository"]):
                if t["category"] == "ci-cd":
                    self.assertNotIn("ci", t["category_signals"],
                                     f"{t['repository']} is ci-cd on the strength of 'ci'")


class TestNoSignalMatchesInsideAWord(unittest.TestCase):
    """Generalised: every short signal, embedded in an ordinary word, must not match."""

    # A word containing each short signal that is not itself a category signal.
    CONTAINING_WORDS = {
        "ci": ("official", "social", "decide", "specialist", "circuit"),
        "cd": ("abcd", "cdc"),
        "git": ("digital", "legitimate"),
        "file": ("profile", "filament"),
        "sql": ("nosqlite", "mysqlite"),
        "docs": ("docsomething",),
        "trace": ("traceability"),
        "search": ("researcher"),
        "memory": ("memorystore"),
    }

    def test_short_signals_do_not_match_inside_words(self):
        self.assertTrue(SHORT_SIGNALS, "no short signals left to test; the risk has changed shape")
        for signal in SHORT_SIGNALS:
            for word in self.CONTAINING_WORDS.get(signal, ()):
                with self.subTest(signal=signal, word=word):
                    cat, _evidence, signals = gen.detect_category(
                        rec("acme/thing", f"A {word} server for teams.", []))
                    self.assertNotIn(signal, signals,
                                     f"'{signal}' matched inside the word '{word}'")

    def test_a_signal_only_matches_when_it_is_the_whole_token(self):
        for signal in ("ci", "cd", "git", "file", "sql", "docs", "search", "memory"):
            with self.subTest(signal=signal):
                _cat, _ev, signals = gen.detect_category(rec("acme/thing", "", [signal]))
                self.assertIn(signal, signals)

    def test_tokenizer_keeps_hyphenated_signals_matchable(self):
        """Splitting on hyphens alone would make `web-scraping`, `cloud-run` and
        `pull-request` unmatchable, silently reclassifying whatever carried them."""
        for hyphenated in ("web-scraping", "cloud-run", "pull-request"):
            if hyphenated not in ALL_SIGNALS:
                continue
            with self.subTest(signal=hyphenated):
                self.assertIn(hyphenated, gen._tokens(hyphenated))
                _cat, _ev, signals = gen.detect_category(rec("acme/thing", "", [hyphenated]))
                self.assertIn(hyphenated, signals)

    def test_firecrawl_stays_a_browser_server(self):
        """The regression the hyphen fix was for: it publishes the topic `web-scraping`."""
        cat, evidence, signals = gen.detect_category(rec(
            "firecrawl/firecrawl-mcp-server",
            "Official Firecrawl MCP Server - Adds powerful web scraping and search",
            ["web-crawler", "web-scraping", "search-api", "mcp-server"]))
        self.assertEqual("browser", cat)
        self.assertIn("web-scraping", signals)


class TestEvidencePrecedence(unittest.TestCase):
    """Curated fields outrank free prose, and the choice is recorded."""

    def test_topics_and_slug_are_preferred_over_the_description(self):
        cat, evidence, signals = gen.detect_category(rec(
            "github/github-mcp-server",
            "A database explorer with search and retrieval over SQL",   # would say database
            ["github", "mcp-server"]))
        self.assertEqual("vcs", cat)
        self.assertEqual("topics-or-slug", evidence)
        self.assertIn("github", signals)

    def test_description_is_used_only_when_nothing_structured_matched(self):
        cat, evidence, signals = gen.detect_category(rec(
            "oraios/serena", "A toolkit providing semantic retrieval and editing",
            ["agent", "ide", "language-server"]))
        self.assertEqual("search", cat)
        self.assertEqual("description-fallback", evidence)
        self.assertIn("retrieval", signals)

    def test_other_when_nothing_matches_at_all(self):
        cat, evidence, signals = gen.detect_category(rec(
            "modelcontextprotocol/registry",
            "A community driven registry service for Model Context Protocol (MCP) servers.",
            ["mcp", "mcp-servers"]))
        self.assertEqual("other", cat)
        self.assertEqual("no-signal-matched", evidence)
        self.assertEqual([], signals)

    def test_slug_segments_count_as_structured_evidence(self):
        cat, evidence, _signals = gen.detect_category(rec("stripe/ai", "One-stop shop for AI", ["mcp"]))
        self.assertEqual("payments", cat)
        self.assertEqual("topics-or-slug", evidence)

    def test_matching_is_case_insensitive_without_being_loose(self):
        self.assertEqual("database", gen.detect_category(rec("acme/thing", "", ["PostgreSQL"]))[0])
        self.assertEqual("database", gen.detect_category(rec("acme/thing", "POSTGRES", []))[0])
        # A near-miss is a different token and must not be matched by containing one.
        for word in ("postgrest", "redislike", "sqliteish"):
            with self.subTest(word=word):
                self.assertEqual("other", gen.detect_category(rec("acme/thing", word, []))[0],
                                 f"'{word}' was matched by a signal it merely contains")


class TestEveryCategoryIsInTheSchemaEnum(unittest.TestCase):
    def test_signal_table_only_produces_declared_categories(self):
        enum = set(json.loads(SCHEMA.read_text())["properties"]["category"]["enum"])
        self.assertEqual(set(), {c for c, _ in gen.CATEGORY_SIGNALS} - enum)

    def test_no_declared_category_is_silently_unreachable(self):
        """A category the heuristic cannot select is only acceptable if the schema says how
        it *can* be reached. `payments` sat in the enum with no signal that could ever
        produce it, so a payments server fell through to whatever short signal happened to
        appear in its prose and was labelled `ci-cd`.

        The members left over here are reachable by human curation, which the schema records
        as `category_evidence: human-curated`; the test asserts that route is declared rather
        than assuming it.
        """
        props = json.loads(SCHEMA.read_text())["properties"]
        enum = set(props["category"]["enum"]) - {"other"}
        unreachable = enum - {c for c, _ in gen.CATEGORY_SIGNALS}
        self.assertIn("human-curated", props["category_evidence"]["enum"],
                      "a category no heuristic can select needs a human route, and the "
                      "evidence vocabulary must be able to say so")
        for cat in sorted(unreachable):
            with self.subTest(category=cat):
                self.assertIn(cat, props["category"].get("description", ""),
                              f"'{cat}' is unreachable by heuristic and the schema does not "
                              f"say how it may be set")

    def test_schema_declares_the_evidence_fields(self):
        props = json.loads(SCHEMA.read_text())["properties"]
        self.assertIn("category_evidence", props)
        self.assertIn("category_signals", props)


class TestCommittedCorpusIsAuditable(unittest.TestCase):
    def setUp(self):
        self.tools = json.loads(TOOLS.read_text())["tools"]

    def test_every_entry_records_why_it_got_its_category(self):
        for t in self.tools:
            with self.subTest(slug=t["repository"]):
                self.assertIn(t["category_evidence"],
                              ("topics-or-slug", "description-fallback", "no-signal-matched"))
                if t["category_evidence"] == "no-signal-matched":
                    self.assertEqual("other", t["category"])
                    self.assertEqual([], t["category_signals"])
                else:
                    self.assertTrue(t["category_signals"],
                                    "a category was assigned but no matched signal recorded")

    def test_every_recorded_signal_really_belongs_to_the_category(self):
        """Re-derives the classification from the recorded evidence: a category nobody can
        re-derive is a category nobody can check."""
        for t in self.tools:
            for sig in t["category_signals"]:
                with self.subTest(slug=t["repository"], signal=sig):
                    self.assertEqual(t["category"], ALL_SIGNALS.get(sig),
                                     f"'{sig}' is not a {t['category']} signal")

    def test_classification_is_reproducible_from_the_source_record(self):
        repos = {r["slug"]: r for r in json.loads(REPOS.read_text())["repositories"]}
        for t in self.tools:
            with self.subTest(slug=t["repository"]):
                cat, evidence, signals = gen.detect_category(repos[t["repository"]])
                self.assertEqual((t["category"], t["category_evidence"], t["category_signals"]),
                                 (cat, evidence, signals))

    def test_no_entry_is_classified_ci_cd_on_a_substring(self):
        ci = [t for t in self.tools if t["category"] == "ci-cd"]
        self.assertTrue(ci, "no ci-cd entry left; this test has lost its subject")
        for t in ci:
            with self.subTest(slug=t["repository"]):
                self.assertTrue(set(t["category_signals"]) & {"ci", "cd", "pipeline", "n8n",
                                                              "workflow", "actions"})


class TestGateWouldCatchAReintroducedSubstringMatch(unittest.TestCase):
    """Negative case: put the old matcher back and confirm both the corpus tests and the
    generator's own gate reject it."""

    def setUp(self):
        self.recs = [r for r in json.loads(REPOS.read_text())["repositories"]
                     if r.get("category") == "mcp-servers"]

    def test_gate_accepts_the_committed_corpus(self):
        tools = [gen.record_to_tool(r) for r in self.recs]
        self.assertEqual([], gen.assert_categories_are_whole_tokens(self.recs, tools))

    def test_gate_rejects_a_category_claimed_from_a_substring(self):
        """Simulates the old matcher's output: `ci-cd` justified by `'ci'`, which is not a
        whole token of anything the official SDKs publish. The gate must refuse it even
        though `ci-cd` is a valid enum member and the record is otherwise well formed."""
        tools = [gen.record_to_tool(r) for r in self.recs]
        for tool in tools:
            if tool["repository"] == "modelcontextprotocol/python-sdk":
                tool["category"] = "ci-cd"
                tool["category_evidence"] = "description-fallback"
                tool["category_signals"] = ["ci"]
        violations = gen.assert_categories_are_whole_tokens(self.recs, tools)
        self.assertTrue(violations, "gate accepted 'ci' as though it were a whole token")
        self.assertTrue(any("not a whole token" in v for v in violations))
        self.assertTrue(any("modelcontextprotocol/python-sdk" in v for v in violations))

    def test_gate_rejects_a_signal_claimed_from_the_wrong_field(self):
        """A real token, but attributed to topics when it only occurs in the description —
        the weaker evidence dressed up as the stronger."""
        tools = [gen.record_to_tool(r) for r in self.recs]
        for tool in tools:
            if tool["repository"] == "oraios/serena":
                self.assertEqual("description-fallback", tool["category_evidence"],
                                 "precondition changed; pick another description-only record")
                tool["category_evidence"] = "topics-or-slug"
        violations = gen.assert_categories_are_whole_tokens(self.recs, tools)
        self.assertTrue(violations)
        self.assertTrue(any("oraios/serena" in v for v in violations))

    def test_gate_rejects_a_stored_category_that_does_not_rederive(self):
        tools = [gen.record_to_tool(r) for r in self.recs]
        tools[0]["category"] = "design"
        violations = gen.assert_categories_are_whole_tokens(self.recs, tools)
        self.assertTrue(violations)
        self.assertTrue(any("does not re-derive" in v for v in violations))

    def test_substring_matching_reclassifies_the_official_sdks(self):
        def old_detect(r):
            hay = " ".join([str(r.get("description") or ""),
                            " ".join(r.get("topics") or []), r.get("slug", "")]).lower()
            for cat, signals in gen.CATEGORY_SIGNALS:
                if any(s in hay for s in signals):
                    return cat
            return "other"

        bad = old_detect(rec("modelcontextprotocol/python-sdk",
                             "The official Python SDK for Model Context Protocol servers and clients",
                             ["mcp", "mcp-server"]))
        self.assertEqual("ci-cd", bad,
                         "the old matcher no longer reproduces the defect, so this suite "
                         "would not catch its return")
        self.assertNotEqual(bad, gen.detect_category(rec(
            "modelcontextprotocol/python-sdk",
            "The official Python SDK for Model Context Protocol servers and clients",
            ["mcp", "mcp-server"]))[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)

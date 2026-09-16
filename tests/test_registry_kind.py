#!/usr/bin/env python3
"""H-8 regression: an entry is only counted as an MCP server when observed text says it is one.

The registry was built by filtering `repositories.json` for `category == "mcp-servers"`, which
is a *seed-list* category — an assertion made when the record was added, not a verified
property of the repository. Five of the 35 entries were not servers: two SDKs, a testing tool,
a registry service and a curated catalog. Each entry's own `purpose` field quoted the
description that said so, so the registry contradicted its own label. Consumers are
`skills/dont-reinvent-the-wheel` and `skills/mcp-integration`, which tell an agent to consult
this registry before building or installing a server; an agent handed an SDK or a catalog gets
nothing usable, and the count inflated apparent coverage by ~14%.

Re-checking all 35 against their own observed text found nine that are not servers, not five:
`microsoft/mcp` ("Catalog of official Microsoft MCP … server implementations"),
`firebase/firebase-tools` ("The Firebase Command Line Tools"), `vercel/mcp-handler` ("Easily
spin up an MCP Server …" — a builder, not a server) and `stripe/ai`, whose description and
topics mention MCP only as a bare topic and never assert a server.

Run: python3 -m unittest tests.test_registry_kind -v
"""
from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gen = load("gen_mcp", "scripts/generate-index/generate_mcp_registry.py")

TOOLS = ROOT / "metadata" / "tools.json"
REPOS = ROOT / "metadata" / "repositories.json"
SCHEMA = ROOT / "schemas" / "mcp.schema.json"
REGISTRY_DIR = ROOT / "knowledge" / "mcp" / "registry"


def mcp_records():
    return [r for r in json.loads(REPOS.read_text())["repositories"]
            if r.get("category") == "mcp-servers"]


def tools():
    return json.loads(TOOLS.read_text())["tools"]


def rec(slug="acme/thing", description="", topics=()):
    return {"slug": slug, "description": description, "topics": list(topics)}


# The five the review named, plus the four a full re-check found. Each expected kind is
# justified by a fragment of that repository's own published description.
KNOWN_NON_SERVERS = {
    "modelcontextprotocol/python-sdk": "sdk",
    "modelcontextprotocol/typescript-sdk": "sdk",
    "vercel/mcp-handler": "sdk",
    "modelcontextprotocol/inspector": "tooling",
    "firebase/firebase-tools": "tooling",
    "modelcontextprotocol/registry": "registry",
    "punkpeye/awesome-mcp-servers": "catalog",
    "microsoft/mcp": "catalog",
    "stripe/ai": "unproven",
}


class TestTheNamedMisclassifications(unittest.TestCase):
    """Each repository the review identified, classified from its own observed text."""

    def test_sdks_are_not_servers(self):
        for slug, desc in (
            ("modelcontextprotocol/python-sdk",
             "The official Python SDK for Model Context Protocol servers and clients"),
            ("modelcontextprotocol/typescript-sdk",
             "The official TypeScript SDK for Model Context Protocol servers and clients"),
        ):
            with self.subTest(slug=slug):
                kind, evidence = gen.detect_registry_kind(rec(slug, desc, ["mcp", "mcp-server"]))
                self.assertEqual("sdk", kind)
                self.assertIn("SDK", evidence)

    def test_the_inspector_is_tooling(self):
        kind, evidence = gen.detect_registry_kind(rec(
            "modelcontextprotocol/inspector", "Visual testing tool for MCP servers",
            ["cli", "debug", "mcp", "tool"]))
        self.assertEqual("tooling", kind)
        self.assertIn("description", evidence)

    def test_a_competing_registry_is_not_an_entry(self):
        kind, _evidence = gen.detect_registry_kind(rec(
            "modelcontextprotocol/registry",
            "A community driven registry service for Model Context Protocol (MCP) servers.",
            ["mcp", "mcp-servers"]))
        self.assertEqual("registry", kind)

    def test_a_catalog_is_not_a_server(self):
        for slug, desc in (("punkpeye/awesome-mcp-servers", "A collection of MCP servers."),
                           ("microsoft/mcp", "Catalog of official Microsoft MCP server implementations")):
            with self.subTest(slug=slug):
                kind, _evidence = gen.detect_registry_kind(rec(slug, desc, ["mcp", "mcp-servers"]))
                self.assertEqual("catalog", kind)

    def test_an_awesome_slug_is_a_catalog_even_with_no_description(self):
        kind, evidence = gen.detect_registry_kind(rec("someone/awesome-mcp-servers", "", ["mcp"]))
        self.assertEqual("catalog", kind)
        self.assertIn("awesome-", evidence)

    def test_a_builder_is_not_a_server(self):
        """`vercel/mcp-handler` says "spin up an MCP Server": it produces servers, it is not
        one. Its description contains the words "MCP Server", so a naive matcher promotes it."""
        kind, evidence = gen.detect_registry_kind(rec(
            "vercel/mcp-handler", "Easily spin up an MCP Server on Next.js, Nuxt, Svelte, and more"))
        self.assertEqual("sdk", kind)
        self.assertIn("spin up", evidence)


class TestUnprovenIsARealAnswer(unittest.TestCase):
    def test_a_bare_mcp_topic_does_not_prove_a_server(self):
        kind, evidence = gen.detect_registry_kind(rec(
            "stripe/ai", "One-stop shop for building AI-powered products and businesses with Stripe.",
            ["ai", "llm", "mcp", "python", "typescript"]))
        self.assertEqual("unproven", kind)
        self.assertIn("nothing observed asserts", evidence)

    def test_nothing_observed_at_all_is_unproven(self):
        self.assertEqual("unproven", gen.detect_registry_kind(rec("acme/thing", "", []))[0])

    def test_unproven_is_not_used_for_a_record_that_does_say_server(self):
        for desc, topics in (("An MCP server for Sentry.", []),
                             ("", ["mcp-server"]),
                             ("Model Context Protocol Servers", [])):
            with self.subTest(desc=desc, topics=topics):
                self.assertEqual("server", gen.detect_registry_kind(rec("acme/thing", desc, topics))[0])


class TestRealServersAreStillServers(unittest.TestCase):
    """The fix must not empty the registry: evidence of being a server comes in four shapes."""

    def test_owner_topic(self):
        self.assertEqual("server", gen.detect_registry_kind(rec("acme/x", "", ["mcp-server"]))[0])
        self.assertEqual("server", gen.detect_registry_kind(rec("acme/x", "", ["mcp-servers"]))[0])

    def test_description(self):
        for desc in ("An MCP server for teams.", "Model Context Protocol Servers",
                     "Official Notion MCP Server"):
            with self.subTest(desc=desc):
                self.assertEqual("server", gen.detect_registry_kind(rec("acme/x", desc))[0])

    def test_slug_naming(self):
        for slug in ("vendor/mcp-server-thing", "vendor/thing-mcp", "supabase/mcp"):
            with self.subTest(slug=slug):
                self.assertEqual("server", gen.detect_registry_kind(rec(slug, "", []))[0])

    def test_a_repository_with_no_topics_still_classifies_from_its_slug(self):
        """Nine of the 35 publish no topics at all; dropping description or slug evidence
        would leave them unclassified."""
        kind, evidence = gen.detect_registry_kind(
            rec("cloudflare/mcp-server-cloudflare", "", []))
        self.assertEqual("server", kind)
        self.assertIn("slug", evidence)


class TestCommittedCorpus(unittest.TestCase):
    def setUp(self):
        self.tools = tools()
        self.recs = {r["slug"]: r for r in mcp_records()}

    def test_every_entry_has_a_kind_and_evidence(self):
        for t in self.tools:
            with self.subTest(slug=t["repository"]):
                self.assertIn(t["registry_kind"], gen.REGISTRY_KINDS)
                self.assertTrue((t["registry_kind_evidence"] or "").strip(),
                                "a kind with no recorded evidence is a guess")

    def test_classification_reproduces_from_the_source_record(self):
        for t in self.tools:
            with self.subTest(slug=t["repository"]):
                self.assertEqual(gen.detect_registry_kind(self.recs[t["repository"]]),
                                 (t["registry_kind"], t["registry_kind_evidence"]))

    def test_evidence_quotes_text_the_api_actually_returned(self):
        """The core anti-guessing check: a quoted fragment must occur in the record."""
        for t in self.tools:
            quoted = re.search(r'"(.+?)"', t["registry_kind_evidence"] or "")
            if not quoted:
                continue
            with self.subTest(slug=t["repository"]):
                rec_ = self.recs[t["repository"]]
                hay = " ".join([str(rec_.get("description") or ""), rec_["slug"],
                                " ".join(rec_.get("topics") or [])]).lower()
                self.assertIn(quoted.group(1).lower(), hay,
                              "evidence quotes text this repository never published")

    def test_the_nine_known_non_servers_are_classified_as_expected(self):
        for slug, expected in KNOWN_NON_SERVERS.items():
            with self.subTest(slug=slug):
                got = next(t for t in self.tools if t["repository"] == slug)
                self.assertEqual(expected, got["registry_kind"])

    def test_no_entry_is_a_server_on_a_bare_mcp_topic(self):
        for t in self.tools:
            if t["registry_kind"] != "server":
                continue
            with self.subTest(slug=t["repository"]):
                self.assertFalse(t["registry_kind_evidence"].startswith("the topic"),
                                 "a bare 'mcp' topic says the repository relates to MCP, not "
                                 "that it is a server")

    def test_generator_gate_is_clean(self):
        tools_ = [gen.record_to_tool(r) for r in mcp_records()]
        self.assertEqual([], gen.assert_kinds_are_evidenced(mcp_records(), tools_))


class TestCountsAreSynchronisedWithTheClassifiedData(unittest.TestCase):
    """The numbers a reader sees must come from the classification, not from len(entries)."""

    def setUp(self):
        self.tools = tools()
        self.servers = [t for t in self.tools if t["registry_kind"] == "server"]
        self.assertNotEqual(len(self.tools), len(self.servers),
                            "every entry is a server again; this test has lost its subject")

    def test_readme_counts_servers_not_entries(self):
        text = (ROOT / "README.md").read_text()
        m = re.search(r"\| MCP servers \| \*\*(\d+)\*\* \|", text)
        self.assertIsNotNone(m, "README no longer states an MCP server count")
        self.assertEqual(len(self.servers), int(m.group(1)),
                         "README's server count is not the number of entries classified server")

    def test_readme_also_shows_the_true_entry_count(self):
        """Understating would be as wrong as overstating: the registry does hold 35 entries."""
        text = (ROOT / "README.md").read_text()
        m = re.search(r"\| MCP registry entries \(incl\. (\d+) that are not servers\) \| \*\*(\d+)\*\* \|", text)
        self.assertIsNotNone(m, "README hides the non-server entries instead of listing them")
        self.assertEqual(len(self.tools), int(m.group(2)))
        self.assertEqual(len(self.tools) - len(self.servers), int(m.group(1)))

    def test_index_headline_counts_servers_only(self):
        text = (ROOT / "indexes" / "mcp.md").read_text()
        m = re.search(r"\*\*(\d+) MCP servers\*\*", text)
        self.assertIsNotNone(m)
        self.assertEqual(len(self.servers), int(m.group(1)))

    def test_index_lists_non_servers_separately_with_the_reason(self):
        """SDKs and the inspector are genuinely useful to record; they are just not servers.
        Hiding them would send the next reader to rediscover them."""
        text = (ROOT / "indexes" / "mcp.md").read_text()
        for kind in {t["registry_kind"] for t in self.tools} - {"server"}:
            with self.subTest(kind=kind):
                for t in self.tools:
                    if t["registry_kind"] != kind:
                        continue
                    # the entry must appear below the server table, in a kind-specific block
                    self.assertIn(t["id"], text)

    def test_non_servers_are_not_in_the_server_table(self):
        text = (ROOT / "indexes" / "mcp.md").read_text()
        server_table = text.split("\n## ")[0]
        for t in self.tools:
            if t["registry_kind"] == "server":
                continue
            with self.subTest(slug=t["repository"]):
                self.assertNotIn(t["id"], server_table,
                                 f"a {t['registry_kind']} is listed in the server table")

    def test_each_entry_states_its_kind_to_a_human_reader(self):
        for t in self.tools:
            with self.subTest(slug=t["repository"]):
                f = REGISTRY_DIR / (t["repository"].replace("/", "__") + ".md")
                body = f.read_text()
                self.assertIn(f"**Registry kind: `{t['registry_kind']}`.**", body)

    def test_a_non_server_entry_says_it_is_not_one(self):
        """The point of the finding: an agent reading the entry must not be told to install it."""
        for t in self.tools:
            if t["registry_kind"] == "server":
                continue
            with self.subTest(slug=t["repository"]):
                body = (REGISTRY_DIR / (t["repository"].replace("/", "__") + ".md")).read_text()
                if t["registry_kind"] == "unproven":
                    self.assertIn("not counted as an MCP server", body)
                else:
                    self.assertRegex(body, r"not a server|not an entry|do not install")


class TestSchemaDeclaresTheVocabulary(unittest.TestCase):
    def test_registry_kind_is_declared_with_every_value(self):
        prop = json.loads(SCHEMA.read_text())["properties"]["registry_kind"]
        self.assertEqual(set(gen.REGISTRY_KINDS), set(prop["enum"]))

    def test_unproven_is_documented_as_an_answer_not_a_placeholder(self):
        desc = json.loads(SCHEMA.read_text())["properties"]["registry_kind"]["description"]
        self.assertIn("unproven", desc)
        self.assertRegex(desc, r"real answer|not a placeholder")

    def test_the_schema_says_what_gets_counted(self):
        desc = json.loads(SCHEMA.read_text())["properties"]["registry_kind"]["description"]
        self.assertRegex(desc, r"Only `server` entries are counted")


class TestGateRejectsAGuessedKind(unittest.TestCase):
    """Negative cases: the gate must fail when a kind is asserted without observed text."""

    def setUp(self):
        self.recs = mcp_records()

    def tools_(self):
        return [gen.record_to_tool(r) for r in self.recs]

    def test_gate_rejects_a_kind_that_does_not_rederive(self):
        tools_ = self.tools_()
        for t in tools_:
            if t["repository"] == "modelcontextprotocol/python-sdk":
                t["registry_kind"] = "server"
        violations = gen.assert_kinds_are_evidenced(self.recs, tools_)
        self.assertTrue(violations)
        self.assertTrue(any("does not re-derive" in v for v in violations))

    def test_gate_rejects_evidence_quoting_text_the_repository_never_published(self):
        tools_ = self.tools_()
        for t in tools_:
            if t["repository"] == "stripe/ai":
                t["registry_kind"] = "server"
                t["registry_kind_evidence"] = 'description says "official Stripe MCP server"'
        violations = gen.assert_kinds_are_evidenced(self.recs, tools_)
        self.assertTrue(violations, "a fabricated quotation passed the gate")
        self.assertTrue(any("does not occur in anything the API returned" in v for v in violations))

    def test_gate_rejects_a_server_claimed_on_a_bare_mcp_topic(self):
        tools_ = self.tools_()
        for t in tools_:
            if t["repository"] == "stripe/ai":
                t["registry_kind"] = "server"
                t["registry_kind_evidence"] = 'the topic "mcp" establishes it'
        violations = gen.assert_kinds_are_evidenced(self.recs, tools_)
        self.assertTrue(violations)
        self.assertTrue(any("bare 'mcp' topic" in v for v in violations))

    def test_gate_rejects_an_undeclared_kind(self):
        tools_ = self.tools_()
        tools_[0]["registry_kind"] = "probably-a-server"
        violations = gen.assert_kinds_are_evidenced(self.recs, tools_)
        self.assertTrue(any("is not one of" in v for v in violations))

    def test_gate_accepts_the_committed_corpus(self):
        self.assertEqual([], gen.assert_kinds_are_evidenced(self.recs, self.tools_()))


if __name__ == "__main__":
    unittest.main(verbosity=2)

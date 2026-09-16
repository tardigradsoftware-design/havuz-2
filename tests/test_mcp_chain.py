#!/usr/bin/env python3
"""H-2 regression: nothing the MCP registry generator computes may be lost in the chain.

The chain is one-directional by design:

    metadata/repositories.json -> knowledge/mcp/registry/*.md -> metadata/tools.json
    (GitHub REST API)            (generate_mcp_registry.py)     (extract_registries.py)

`extract_registries.py` reads only the markdown frontmatter. A field computed by
`record_to_tool()` that `MD_TMPL` does not emit therefore vanishes silently, and no
existing validator could see it: all such fields are optional in `mcp.schema.json`, so
schema validation reports nothing, and the drift job passes because regeneration
reproduces the same loss. Nine fields went missing that way, including
`not_recommended_for` — which for the one archived server carried
`"adoption in new work — archived"`, the only do-not-adopt signal in the registry.

Run: python3 -m unittest tests.test_mcp_chain -v
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

REPOS = ROOT / "metadata" / "repositories.json"
TOOLS = ROOT / "metadata" / "tools.json"
SCHEMA = ROOT / "schemas" / "mcp.schema.json"
INTERNAL = {"_path", "_tokens", "_headings"}


def mcp_records():
    blob = json.loads(REPOS.read_text())
    return [r for r in blob["repositories"] if r.get("category") == "mcp-servers"]


def tools_by_repository():
    return {t["repository"]: t for t in json.loads(TOOLS.read_text())["tools"]}


class TestChainCarriesEveryComputedField(unittest.TestCase):
    """The invariant the review recommended and nothing previously checked."""

    def test_every_computed_key_reaches_tools_json(self):
        """Per record, not on the union: a field emitted for one repository and dropped
        for another must not hide in the aggregate."""
        final = tools_by_repository()
        for rec in mcp_records():
            with self.subTest(slug=rec["slug"]):
                computed = gen.record_to_tool(rec)
                got = final.get(rec["slug"])
                self.assertIsNotNone(got, "computed by the generator but absent from tools.json")
                lost = set(computed) - (set(got) - INTERNAL)
                self.assertEqual(set(), lost,
                                 f"lost between the registry markdown and tools.json: {sorted(lost)}")

    def test_no_undeclared_key_enters_tools_json(self):
        """The other direction: tools.json must not carry keys the schema does not declare."""
        declared = set(json.loads(SCHEMA.read_text())["properties"])
        for repo, t in tools_by_repository().items():
            with self.subTest(slug=repo):
                self.assertEqual(set(), (set(t) - INTERNAL) - declared)

    def test_generator_gate_is_clean_on_the_committed_corpus(self):
        """The generator's own gate, which CI runs via --check."""
        tools = [gen.record_to_tool(r) for r in mcp_records()]
        self.assertEqual([], gen.assert_chain_complete(tools))

    def test_rendered_frontmatter_emits_every_computed_field(self):
        """Catches the defect at the template, before tools.json exists.

        Deliberately reads *rendered* output rather than MD_TMPL's source: the template
        prefixes some lines with a conditional slot, so a line-start match against the
        source reports keys that are in fact emitted.
        """
        recs = mcp_records()
        tools = [gen.record_to_tool(r) for r in recs]
        emitted = set()
        for t, r in zip(tools, recs):
            emitted |= gen.frontmatter_keys(gen.render_md(t, r))
        computed = set().union(*[set(t) for t in tools])
        self.assertEqual(set(), computed - emitted - set(gen.TEMPLATE_ALIASES))

    def test_gate_detects_a_field_dropped_from_the_template(self):
        """Negative case: the gate must fail when the original defect is reintroduced."""
        original = gen.MD_TMPL
        try:
            gen.MD_TMPL = original.replace("not_recommended_for: {not_recommended_for}\n", "")
            recs = mcp_records()
            tools = [gen.record_to_tool(r) for r in recs]
            emitted = set()
            for t, r in zip(tools, recs):
                emitted |= gen.frontmatter_keys(gen.render_md(t, r))
            computed = set().union(*[set(t) for t in tools])
            missing = computed - emitted - set(gen.TEMPLATE_ALIASES)
            self.assertIn("not_recommended_for", missing)
        finally:
            gen.MD_TMPL = original

    def test_gate_detects_a_field_missing_from_tools_json(self):
        """Negative case for the JSON side.

        Points the gate at a temporary copy rather than editing the committed registry:
        a test that mutates a tracked artifact and restores it afterwards leaves the
        corpus damaged if it is interrupted, and would also trip the drift job.
        """
        import tempfile

        tools = [gen.record_to_tool(r) for r in mcp_records()]
        doctored = json.loads(TOOLS.read_text())
        for rec in doctored["tools"]:
            rec.pop("not_recommended_for", None)
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d) / "tools.json"
            tmp.write_text(json.dumps(doctored, indent=2, ensure_ascii=False))
            original = gen.TOOLS_JSON
            try:
                gen.TOOLS_JSON = tmp
                violations = gen.assert_chain_complete(tools)
            finally:
                gen.TOOLS_JSON = original
        self.assertTrue(violations, "gate passed although not_recommended_for was stripped")
        self.assertTrue(any("not_recommended_for" in v for v in violations))


class TestArchivedWarningSurvives(unittest.TestCase):
    """The specific loss that made H-2 consequential: a safety signal."""

    def test_archived_entries_carry_not_recommended_for_in_tools_json(self):
        final = tools_by_repository()
        archived = [r["slug"] for r in mcp_records() if r.get("archived")]
        self.assertTrue(archived, "corpus has no archived MCP record; this test has lost its subject")
        for slug in archived:
            with self.subTest(slug=slug):
                self.assertIn("archived", " ".join(final[slug].get("not_recommended_for") or []))
                self.assertEqual("deprecated", final[slug].get("production_readiness"))

    def test_archived_entries_show_the_warning_in_the_markdown_too(self):
        """An agent that reads the entry rather than the JSON must see it as well."""
        registry = ROOT / "knowledge" / "mcp" / "registry"
        for rec in mcp_records():
            if not rec.get("archived"):
                continue
            with self.subTest(slug=rec["slug"]):
                f = registry / (rec["slug"].replace("/", "__") + ".md")
                text = f.read_text()
                self.assertIn("not_recommended_for:", text)
                self.assertIn("archived", text)


class TestScopedPackageNameParse(unittest.TestCase):
    """The latent bug H-2 hid: `rsplit("/", 1)` truncates npm scoped packages."""

    def test_scoped_npm_package_keeps_its_scope(self):
        self.assertEqual("@playwright/mcp",
                         gen.package_from_url("https://www.npmjs.com/package/@playwright/mcp", "npm"))

    def test_unscoped_npm_package(self):
        self.assertEqual("mcp-handler",
                         gen.package_from_url("https://www.npmjs.com/package/mcp-handler", "npm"))

    def test_pypi_project_and_legacy_paths(self):
        self.assertEqual("postgres-mcp",
                         gen.package_from_url("https://pypi.org/project/postgres-mcp/", "pypi"))
        self.assertEqual("postgres-mcp",
                         gen.package_from_url("https://pypi.org/pypi/postgres-mcp", "pypi"))

    def test_url_that_is_not_a_package_page_yields_none_not_a_guess(self):
        for url in ("https://example.com/", "https://www.npmjs.com/", "https://npmjs.com/~user"):
            with self.subTest(url=url):
                self.assertIsNone(gen.package_from_url(url, "npm"))

    def test_detect_distribution_returns_the_scoped_name(self):
        rec = {"homepage": "https://www.npmjs.com/package/@playwright/mcp"}
        dist, npm, pypi = gen.detect_distribution(rec)
        self.assertEqual(("npm", "@playwright/mcp", None), (dist, npm, pypi))

    def test_committed_corpus_has_no_truncated_package_name(self):
        """A truncated scoped name looks like a plausible unscoped one, so check the
        value against the homepage it was derived from."""
        for rec in mcp_records():
            hp = str(rec.get("homepage") or "")
            if "npmjs.com/package/" not in hp:
                continue
            with self.subTest(slug=rec["slug"]):
                expected = hp.split("npmjs.com/package/", 1)[1].strip("/")
                _, npm, _ = gen.detect_distribution(rec)
                self.assertEqual(expected, npm)
                if expected.startswith("@"):
                    self.assertIn("/", npm, "scope was truncated")


class TestYamlScalarsRoundTrip(unittest.TestCase):
    """Every emitted value must survive being re-read, or the field is lost anyway."""

    def test_values_round_trip_through_yaml(self):
        import yaml
        for value in (None, True, False, 0, 3409, 6.77, "TypeScript", "mcp-handler",
                      "@playwright/mcp", "", "null", "yes", "a: b", "#tag",
                      ["adoption in new work — archived"], [], {}):
            with self.subTest(value=value):
                doc = yaml.safe_load(f"k: {gen.yaml_scalar(value)}\n")
                self.assertEqual(value, doc["k"])

    def test_reserved_and_ambiguous_strings_are_quoted(self):
        for s in ("@playwright/mcp", "null", "yes", "no", "true", "~", "on"):
            with self.subTest(s=s):
                self.assertTrue(gen.yaml_scalar(s).startswith('"'),
                                f"{s!r} would be reinterpreted by a YAML parser")


if __name__ == "__main__":
    unittest.main(verbosity=2)

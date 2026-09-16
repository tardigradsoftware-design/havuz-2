# Regression tests

Dependency-free tests for the guarantees this repository makes about its own
pipeline. Stdlib `unittest` only — `scripts/requirements.txt` is deliberately
minimal because the validators must run in a plain CI image, and a test suite that
needs a third-party runner would not.

```bash
make test                       # everything
python3 -m unittest discover -s tests -t . -v
python3 tests/test_mcp_chain.py # one module
```

## What belongs here

A test belongs here when it protects an invariant that **no validator can see**,
because the invariant is about the relationship between two artifacts rather than
about either one on its own. Every module in this directory exists because a real
defect of exactly that shape shipped and was caught only by review:

| Module | Invariant | Defect it prevents (review finding) |
|---|---|---|
| `test_mcp_chain.py` | every field the MCP generator computes reaches `metadata/tools.json` | H-2 — nine fields, including the archived server's `not_recommended_for` warning, were dropped by the markdown template and no check compared the two sides |
| `test_mcp_category.py` | registry `category` comes from whole-token matches, never from a substring inside an ordinary word | H-7 — both official SDKs were labelled `ci-cd` because `'ci'` occurs inside *"offi**ci**al"* |
| `test_registry_kind.py` | a registry entry is only counted as an MCP server when observed text says it is one | H-8 — five of the "35 MCP servers" were SDKs, a testing tool, a registry and a catalog |
| `test_tier_semantics.py` | `UNVERIFIED` means the fetch failed; a missing license has its own tier | H-3 — all 15 `UNVERIFIED` records had `fetch_ok: true`; the tier described legal status using a word that means verification status |
| `test_exclusions.py` | `SECURITY.md`'s hard exclusions fail a build | H-4 — the exclusions were prose with no enforcement path, honoured only because nobody had added them |
| `test_license_policy.py` | the no-license override covers markdown, which is what gets vendored here | H-5 — the check fired only on source-code files and matched a bare repository name |
| `test_sanitization.py` | third-party API text is inert by the time it reaches a card | H-6 — repository descriptions were embedded verbatim into markdown read by agents |

## Rules these tests follow

- **No network.** Everything reads committed artifacts or calls pure functions with
  synthetic input. A test that needs the GitHub API is a freshness check, not a
  regression test, and belongs in `scripts/update/`.
- **Negative cases are mandatory.** Each module includes a test that injects the
  original defect and asserts it is caught. A gate that has never been seen to fail
  is not evidence of anything.
- **Assert the invariant, not the current values.** Tests fail when a guarantee
  breaks, not when the corpus grows. Counts are asserted only where the count *is*
  the guarantee.

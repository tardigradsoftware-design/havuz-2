---
id: security-supply-chain
title: "Software supply chain security, including the AI-specific surface"
domain: security
summary: >-
  Attack classes from typosquatting to dependency confusion and model poisoning, the nine controls ranked by leverage, and the agent-specific dependencies — MCP servers, skill packs, checkpoints and datasets — that classical supply-chain tooling does not cover.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [supply-chain, security, dependencies, sbom, typosquatting, lockfile, mcp, models]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/security/threat-modeling.md, knowledge/ai-engineering/source-scoring.md, knowledge/security/mcp-security/mcp-threat-model.md]
sources:
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    organization: Open Source Security Foundation
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Prior art for scoring open-source health from observable signals; its check set informed the maintenance and reproducibility components of our scoring model."
---
# Software Supply Chain Security

## The threat

Modern software is mostly other people's software. A typical agent project pulls a framework, an
SDK, an MCP server, several libraries and a model — each with its own upstream. Compromise of any
one compromises everything built on it, usually invisibly.

```text
DEPTH      Transitive dependencies outnumber direct ones by an order of magnitude. You review what
           you install, not what it installs.
TRUST      Package installation executes code, often at install time, from a registry that verifies
           authorship little beyond an account name.
LAG        A compromise is discovered long after it is exploited — days to months.
```

## Attack classes

| Class | Mechanism | Detection |
|---|---|---|
| **Typosquatting** | A package named like a popular one, differing by a character | Diff names against the canonical registry entry; check publisher and download counts |
| **Account takeover** | A maintainer's credentials are stolen; a malicious version ships under a trusted name | Advisory subscriptions; publish timestamps vs maintainer activity |
| **Dependency confusion** | A private package name is registered publicly with a higher version; the resolver prefers it | Pin scopes; internal registry with an allowlist; never resolve private names publicly by default |
| **Build compromise** | CI or build tooling tampered with | Reproducible builds, signed artifacts, provenance attestation |
| **Malicious install scripts** | `postinstall` hooks executing at install time | Audit install scripts; install in a network-isolated sandbox |
| **Model/dataset poisoning** | A checkpoint or dataset is tampered with or backdoored | Verify checksums against the publisher's own channel, not a mirror |
| **Stale archived dependency** | An unmaintained package accumulates unpatched vulnerabilities | Check `archived` and `pushed_at` at scoring time |

## Controls, by leverage

```text
1. PIN EVERYTHING.              Exact versions plus a committed lockfile with integrity hashes. A
                                range specifier means "install whatever is newest at build time",
                                which is precisely what an attacker publishes.
2. LOCKFILE REVIEW ON CHANGE.   Every lockfile diff is a code review: new packages, major jumps,
                                changed integrity hashes, changed resolved URLs. Cheapest
                                high-value control here, most commonly skipped.
3. SANDBOX INSTALLS.            Container, no network after the fetch step, no ambient credentials.
4. MINIMISE THE TREE.           A dependency not taken cannot be compromised. Prefer the standard
                                library and small focused packages for narrow needs.
5. VENDOR CRITICAL PATHS.       For few load-bearing packages, a reviewed vendored copy removes the
                                registry from the trust path. Reserve for security-critical or tiny.
6. VERIFY PUBLISHER AND HEALTH. Who publishes it, are they canonical, is it archived, is there a
                                license, when was it last pushed, is there CI and test coverage.
                                Exactly what the scoring model computes.
7. MONITOR ADVISORIES.          Dependabot or Renovate with alerts routed to someone who acts. An
                                unactioned alert is worse than none — it records false coverage.
8. SIGN AND ATTEST.             For what you publish: signed releases, provenance, reproducible
                                builds where feasible.
9. LICENSE COMPLIANCE.          Not security, same audit. license: null means do-not-redistribute,
                                however good the code is.
```

## The AI-specific surface

Agent systems add dependencies classical tooling does not cover:

```text
MCP SERVERS              Run locally with the user's file and network access. A malicious server is
                         full local compromise. Pin, sandbox, read the source before enabling, diff
                         the exposed tool list on upgrade.
SKILL / PROMPT PACKAGES  Instructions shape behaviour, so a malicious skill is an injection payload
                         with persistence. Treat imported skills as code review material.
MODEL CHECKPOINTS        Verify against the publisher's channel. A checksum hosted next to the file
                         proves nothing.
DATASETS                 Poisoned evaluation data produces confidently wrong conclusions. Prefer
                         datasets with a published collection method and a citation.
EVALUATION HARNESSES     A tampered harness reports passing scores. Pin and verify like anything else.
```

## Anti-patterns

```text
✗ "It has 40k stars so it's safe."   Adoption measures attention, not integrity. Several of the
  most-starred agent-skill repositories in this corpus have no license file at all.
✗ Reviewing direct dependencies only. The compromise is usually transitive.
✗ Auto-merging dependency bumps.      A bot opening PRs and a human never reading the lockfile diff
  is an unreviewed supply-chain change on a schedule.
✗ Ignoring archived dependencies.     An archived security tool supplies confidence without
  coverage — worse than none, because the team believes it is covered.
✗ Installing from a recalled name.    Verify the canonical slug; plausible slugs routinely do not
  exist or resolve to unrelated projects.
✗ Treating license as a footnote.     Redistribution risk has legal rather than technical
  consequences, and it is not recoverable after shipping.
```

## References

- [`knowledge/ai-engineering/source-scoring.md`](../ai-engineering/source-scoring.md) · [`knowledge/security/threat-modeling.md`](threat-modeling.md) · [`mcp-security/mcp-threat-model.md`](mcp-security/mcp-threat-model.md) · [`prompt-injection-defenses.md`](prompt-injection-defenses.md)
- [`knowledge/ai-engineering/verification-findings.md`](../ai-engineering/verification-findings.md) — license-null and archived findings from 2026-09-15
- [`skills/dependency-analysis/SKILL.md`](../../skills/dependency-analysis/SKILL.md) · [`skills/security-audit/SKILL.md`](../../skills/security-audit/SKILL.md)
- OpenSSF Scorecard — <https://github.com/ossf/scorecard> · SLSA — <https://slsa.dev> · Sigstore — <https://www.sigstore.dev>

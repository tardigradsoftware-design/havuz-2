---
name: dont-reinvent-the-wheel
version: 1.0.0
description: >-
  A reuse gate run before writing any non-trivial code: does a mature library, standard, official
  implementation, MCP server or proven pattern already solve this? Produces a build-vs-adopt decision.
category: planning
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [reuse, decision, architecture, dependencies, anti-reinvention, planning]
applies_to: [any]
priority: 90
requires: [research-before-code, evidence-validation]
conflicts_with: []
estimated_tokens: 2281
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: The six questions
    anchor: "#the-six-questions"
    purpose: implementation
  - heading: Decision rule
    anchor: "#decision-rule"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "OpenSSF Scorecard — security health metrics for open-source projects"
    url: https://github.com/ossf/scorecard
    type: github-repository
    organization: Open Source Security Foundation
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Supply-chain risk of adopting a dependency is measurable, not just a matter of taste."
related_skills: [research-before-code, dependency-analysis, repository-analysis, architecture-design]
related_repositories: [upstash/context7, oraios/serena, ossf/scorecard, aquasecurity/trivy]
tests: 6
---

# Don't Reinvent the Wheel

## Purpose

Before writing a non-trivial component, prove that writing it is the right choice.
The default should be **adopt**, and **build** should require an argument.

This is not "always use a library". Hand-rolling is correct when the dependency is
heavier than the problem, when the requirement is genuinely novel, or when the
dependency is unmaintained. The skill's job is to make that argument explicit instead
of letting it happen by omission.

## When to Use

```text
□ You are about to write >100 lines of infrastructure-shaped code
  (auth, sessions, caching, queues, retries, rate limiting, parsing, validation,
   pagination, file upload, email, search, scheduling, RBAC, i18n, feature flags,
   observability, migrations, CRUD, tables, forms, charts, date handling, money)
□ You are about to add a new abstraction that other code will depend on
□ A task description contains "implement", "build" or "write" for a common capability
□ You are tempted to write a utility because the library's API annoyed you once
```

## When NOT to Use

```text
✗ Genuinely novel domain logic that has no prior art (your business rules)
✗ Thin glue under 30 lines where a dependency would cost more than it saves
✗ A hard constraint already rules out third-party code (air-gapped, licensing,
  certification) — record the constraint and proceed
✗ Security-critical primitives you are not qualified to write — the answer here is
  never "build", it is "escalate"
```

## Inputs

```text
capability      what the code must do, stated as a behaviour, not as a design
constraints     runtime, bundle size, latency, license, deployment target, team language
existing_stack  what is already a dependency (prefer extending over adding)
scale           today's load and the plausible 12-month load
```

## The six questions

Ask in order. A "yes" to an early question ends the search — but you still must record
what you found.

```text
1  Does a MATURE LIBRARY exist?
   Search: metadata/repositories.json by category+tags; the language's package registry;
   the framework's own first-party package.
   Mature = tier S/A/B, status ACTIVE or STABLE, license usable, tests + CI present,
   release within the last 12 months.

2  Does a STANDARD or SPECIFICATION exist?
   Even if you build, build to the standard: OpenAPI, OAuth 2.0/OIDC, JSON Schema,
   WebAuthn, MCP, OpenTelemetry, SARIF, WCAG, HTTP semantics, SemVer.
   Implementing a standard is not reinventing; inventing a private protocol is.

3  Does a PROVEN REPOSITORY exist you can learn from (even if not adopt)?
   Reference implementations, official examples, the framework's own templates.

4  Does an MCP SERVER or TOOL already expose this capability to the agent?
   See knowledge/mcp/registry/ and indexes/mcp.md. If a maintained MCP exists, the
   agent may not need code at all.

5  Does an ESTABLISHED PATTERN exist in this repository?
   patterns/ and knowledge/ — the shape may be solved even if the library is not.

6  Does the PLATFORM already do it?
   Runtime, framework, database, or hosting provider features beat application code:
   Postgres RLS vs app-level filters, DB constraints vs validation layers,
   CDN caching vs in-app caching, platform cron vs a scheduler service,
   managed auth vs your own session table.
```

## Decision rule

```text
ADOPT   a mature option exists AND fits constraints AND license is usable
        → adopt it, pin the version, record why

EXTEND  a mature option covers 80% AND is designed for extension
        → extend via its official extension points, not by forking

WRAP    a mature option fits but its API leaks into your domain
        → wrap it behind a thin internal interface you own (anti-corruption layer)

BUILD   no mature option fits, OR the dependency costs more than the problem,
        OR the requirement is genuinely novel
        → build to a standard where one exists, and record the BUILD argument

ESCALATE the capability is security-critical and no trusted implementation exists
        → stop; raise to a human. Never hand-roll crypto, token signing, password
          storage or payment flows.
```

### The BUILD argument (mandatory when choosing BUILD)

```markdown
Capability:        <behaviour>
Searched:          <registries, KB indexes, official docs — with dates>
Candidates found:  <name — why each was rejected, specifically>
Why build:         <the constraint that no candidate satisfies>
Standard followed: <spec, or "none exists" with justification>
Maintenance cost:  <who owns this forever, and what happens when they leave>
Escape hatch:      <how we would swap in a library later if one appears>
```

If you cannot fill this in, you have not searched.

## Cost model

Compare honestly, including the costs people forget:

```text
ADOPT cost   = integration + version churn + supply-chain risk + license obligations
               + loss of control + bundle/runtime weight
BUILD cost   = implementation + testing + security review + documentation
               + on-call forever + every future requirement + opportunity cost
```

Rules of thumb (**RECOMMENDATION**, not fact):

```text
• Security, money, identity, protocol parsing → almost always ADOPT or ESCALATE
• Undifferentiated plumbing (queues, retries, caching) → almost always ADOPT
• Core domain logic → almost always BUILD
• Something you will need to change weekly → WRAP so you can swap later
• A 40-line utility with zero dependencies and full test coverage → BUILD is fine
```

## Failure Modes

```text
NIH SYNDROME          Building because the library's API is not to your taste.
                      Fix: WRAP it; taste is not a constraint.
DEPENDENCY MAXIMALISM Adding a package for something the stdlib already does.
                      Fix: check the platform/runtime first (question 6).
ABANDONED ADOPTION    Adopting a project that is ARCHIVED or unmaintained.
                      Fix: filter metadata/repositories.json by status before adopting.
FORK AND FORGET       Forking a library instead of contributing or wrapping.
                      Fix: forks inherit every upstream CVE and none of the fixes.
STAR-DRIVEN ADOPTION  Choosing by stars, ignoring license, fit and maintenance.
PHANTOM LIBRARY       Citing a package that does not exist. Fix: resolve it in the registry.
PARTIAL REINVENTION   Adopting a library but reimplementing the half you did not read.
```

## Quality Checklist

```text
□ All six questions asked and answered in writing
□ Candidate list includes at least two real options (or a documented search that found none)
□ Chosen dependency verified: exists, license usable, status ACTIVE/STABLE, version pinned
□ BUILD argument completed if the decision is BUILD
□ ESCALATE used for any crypto/auth/payment/identity primitive
□ Platform capability checked before writing application code
□ A standard is followed if one exists
□ Decision recorded in a decision-records/ ADR when it constrains future work
□ Escape hatch documented for anything hand-rolled
```

## Anti-Patterns

```text
✗ "I'll just write a quick JWT verifier" — escalate instead
✗ Adding lodash for one function the runtime already has
✗ Writing a retry helper with no jitter and no timeout budget
✗ Building an ORM because the existing one's docs were confusing
✗ Adopting a 40k-star project archived two years ago
✗ Reimplementing RBAC in application code when Postgres RLS is available
✗ Writing a date library. Never write a date library.
```

## References

- [`research-before-code`](../research-before-code/SKILL.md)
- [`dependency-analysis`](../dependency-analysis/SKILL.md)
- [`decision-records/`](../../decision-records/) — ADR template and technology-selection matrices
- [`indexes/repositories.md`](../../indexes/repositories.md) · [`indexes/mcp.md`](../../indexes/mcp.md)
- [`knowledge/architecture/build-vs-adopt.md`](../../knowledge/architecture/build-vs-adopt.md)
- OpenSSF Scorecard — <https://github.com/ossf/scorecard> (Apache-2.0, verified 2026-09-15)

## Related Skills

`research-before-code` · `dependency-analysis` · `repository-analysis` · `api-design` ·
`database-design`

## Evaluation Criteria

```text
1. Reuse rate: fraction of common capabilities solved by adoption rather than new code.
2. Phantom-dependency rate: 0 adopted packages that do not exist or are archived.
3. BUILD argument completeness: 100% of build decisions have the six fields filled.
4. Escalation correctness: 100% of security-critical primitives escalated or adopted,
   never hand-rolled.
5. Downstream cost: number of hand-rolled components needing fixes within 90 days.
```

Test cases in [`tests/`](tests/).

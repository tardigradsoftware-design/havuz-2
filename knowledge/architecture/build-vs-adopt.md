---
id: architecture-build-vs-adopt
title: "Build vs adopt: the five questions and the third option"
domain: architecture
summary: >-
  The ordered decision procedure for building, adopting or removing a capability, the cost comparison across both options, the explicit conditions for each, and the wrapper trap that turns adoption into the most expensive of both.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [architecture, build-vs-buy, dependencies, decision-making, yagni, maintenance]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/ai-engineering/source-scoring.md, knowledge/security/supply-chain.md, decision-records/adr-template.md]
sources:
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    organization: Heroku
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Backing services as attached resources, and strict dev/prod parity, are what make an adopted dependency swappable rather than load-bearing."
---
# Build vs Adopt

## The decision

Every non-trivial feature faces the same question: build it, adopt an existing implementation, or do
without. The ecosystem's default is "adopt", engineering ego's default is "build", and both are wrong
often enough to require an actual decision.

This repository operates under: **don't reinvent the wheel — but verify the wheel before you bolt it
on.** Adoption is a supply-chain decision and a maintenance decision, not a shortcut.

## The five questions, in order

```text
1. IS THIS A DIFFERENTIATOR?    If the capability is the product's reason to exist, building is a
                                strategic choice, not NIH. If it is plumbing — auth, queues,
                                parsing, rendering, storage — adopting is almost always correct.
2. DOES SOMETHING PROVEN EXIST? Search before designing: the repository index, the framework
                                ecosystem, the package registries. "Proven" means maintained,
                                licensed, used in production by others, with a real issue history.
3. CAN WE GRADE WHAT WE FOUND?  Score it on authority, maintenance, adoption, documentation,
                                reproducibility, security, recency and evidence — plus the hard
                                overrides: license and archived status. A tier-S library solving a
                                different problem is worse than a tier-B one solving yours.
4. WHAT DOES ADOPTING COST?     Dependency depth, license obligations, upgrade cadence, abstraction
                                fit, the maintainer's direction, and the migration cost when it is
                                archived. Adoption is a recurring payment, not a one-off saving.
5. WHAT DOES BUILDING COST?     Not the first version — the second year. Bugs nobody else finds,
                                features nobody has asked for, security patches you must produce
                                yourself, onboarding every new engineer, and the opportunity cost of
                                everything not built meanwhile.
```

## The comparison

| Dimension | Build | Adopt |
|---|---|---|
| Time to first version | Slow | Fast |
| Time to production-grade | Slow, and entirely yours | Depends on the project's maturity |
| Fit to your exact problem | Exact | Approximate; you adapt or wrap |
| Maintenance burden | Yours entirely | Shared, but you own the upgrade path |
| Security patches | You produce them | You apply them — if you notice them |
| Control over direction | Total | None; forking is building |
| Differentiation potential | High, if it is the product | None |
| Exit cost | Rewrite | Migration |
| Hidden cost | The second year | The dependency tree and the license |

## When to build

```text
✓ It is the core differentiator and the value proposition depends on its behaviour.
✓ Nothing existing meets a hard requirement — performance envelope, regulatory constraint,
  data-residency rule, an interface that cannot be adapted.
✓ The existing options are all archived, unmaintained or license-incompatible.
✓ The wrapper you would need is larger than the implementation.
✓ There is a stated, funded maintenance commitment. Building without one is how internal libraries
  become the archived dependencies of the future.
```

## When to adopt

```text
✓ It is plumbing: auth, storage, queues, parsing, HTTP, rendering, scheduling, observability.
✓ A tier-A or tier-S implementation exists with an OSI-approved license and active maintenance.
✓ The problem is standardised — a specification exists, so the implementation is a commodity.
✓ The team has no domain expertise in it and no plan to acquire any.
✓ The cost of being wrong is low and reversible.
```

## The third option

The most undervalued answer is **remove the requirement.** A feature that exists because it was
assumed necessary, and that nobody has asked for, is cheaper deleted than built or adopted. Before
the build/adopt decision, ask whether the capability is needed at all, at this scale, now.

```text
YAGNI applied honestly   The second version, the multi-tenant case, the plugin system and the
                         abstraction layer are speculative until a concrete requirement names them.
                         Building for them costs real time and buys imaginary flexibility.
```

## The wrapper trap

Wrapping an adopted library behind your own interface is often correct: it isolates the dependency,
enables swapping, and adapts its model to yours. The trap is that the wrapper grows until it is a
reimplementation with the dependency still attached — paying both costs.

```text
RULE   The wrapper adapts the interface. It does not reimplement the behaviour. If the wrapper
       contains the logic, delete the dependency or delete the wrapper.
```

## Recording the decision

Build-vs-adopt is a decision record. Write down the options considered, the scoring of each
candidate, the choice, the reasoning and the review date. Without it the next engineer re-litigates
from scratch, and the reasoning that rejected the plausible alternative is lost.

See [`decision-records/adr-template.md`](../../decision-records/adr-template.md) and
[`decision-records/matrix-template.md`](../../decision-records/matrix-template.md).

## References

- [`knowledge/ai-engineering/source-scoring.md`](../ai-engineering/source-scoring.md) · [`repository-status.md`](../ai-engineering/repository-status.md)
- [`knowledge/security/supply-chain.md`](../security/supply-chain.md) — what adoption costs in trust terms
- [`knowledge/agent-engineering/framework-comparison.md`](../agent-engineering/framework-comparison.md) — the framework instance of this decision
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../skills/dont-reinvent-the-wheel/SKILL.md) · [`skills/competitive-analysis/SKILL.md`](../../skills/competitive-analysis/SKILL.md) · [`skills/repository-analysis/SKILL.md`](../../skills/repository-analysis/SKILL.md)
- [`decision-records/adr-template.md`](../../decision-records/adr-template.md) · [`decision-records/matrix-template.md`](../../decision-records/matrix-template.md)

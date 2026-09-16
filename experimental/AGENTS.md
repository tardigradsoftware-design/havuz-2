# AGENTS.md — `experimental/`

Rules for work that is **not yet a claim**. This directory exists so that speculation, half-tested
ideas and unverified findings have a place to live without contaminating the graded corpus.

## Why this directory exists

A knowledge base that only holds verified material accumulates nothing new, because verification is
slow. A knowledge base that holds unverified material without labelling it becomes unreliable, because
readers cannot tell the two apart. The separation is the solution: `experimental/` is explicitly
outside the evidence guarantees that apply to `knowledge/`, `skills/` and `patterns/`.

**Nothing in this directory may be cited as evidence by anything outside it.**

## Hard rules

1. **`status: experimental` is mandatory in frontmatter**, and `confidence` must be `low` or
   `medium`. `confidence: high` on experimental content is a validation error, not a style choice —
   if the confidence is high, the work is done and belongs in `knowledge/`.
2. **`claim_type: hypothesis`** unless the content reports an experiment that was actually run, in
   which case `experiment` with the method and result stated.
3. **Every document states what would confirm or refute it.** An idea with no stated refutation
   condition cannot graduate, because there is nothing to check. This is the single field that
   distinguishes a hypothesis from a hunch.
4. **A dated expiry.** Experimental content that has not moved in six months is either promoted with
   evidence or deleted. It does not stay indefinitely as decoration — stale speculation is worse than
   none, because it looks like a lead.
5. **No leaking into the graded corpus.** Do not reference experimental material from `knowledge/`,
   `skills/`, `patterns/` or `prompts/` as support for a claim. Referencing it as "an open question
   recorded in `experimental/`" is acceptable and is the only permitted form.
6. **Graduation is a promotion PR, not an edit.** Moving content out of `experimental/` requires the
   evidence attached, the confidence re-graded, `verified_at` set, an entry in
   [`../CHANGELOG.md`](../CHANGELOG.md) naming the old position, and index regeneration.

## Lifecycle

```text
  hunch ──▶ experimental/ ──┬──▶ knowledge/ or patterns/     (evidence found; promoted)
                            ├──▶ experimental/ (revised)     (partially confirmed; re-scoped)
                            └──▶ deleted                     (refuted, or expired without movement)
```

Refuted work is deleted rather than kept, **unless the refutation itself is interesting** — in which
case the refutation is written up in `knowledge/` with the original hypothesis named, and the
experimental document is removed. A record of "we thought X, and here is the evidence that X is
false" is valuable; a record of "we thought X" next to it is not.

## Prohibited

- Vendor benchmarks, leaderboard numbers or capability claims reproduced without reaching the primary
  source. This is the most common way experimental directories fill up with noise.
- Anything derived from leaked, extracted or improperly obtained model internals. The exclusion policy
  in [`../SECURITY.md`](../SECURITY.md) applies here with no relaxation for research purposes.
  Public reachability is not permission.
- Content copied from an external source without a license check. The redistribution rules apply to
  experimental material exactly as they apply to published material.
- Star counts or popularity offered as support for a hypothesis. Adoption is not evidence of
  correctness, and in an experimental context the temptation to reach for it is highest.

## What is here now

Empty at 1.0.0. The directory is scaffolded and the rules are written; no experimental content has
been admitted yet. The 61 quarantined paper candidates in
[`../metadata/pending-paper-candidates.json`](../metadata/pending-paper-candidates.json) are the
closest thing to experimental material in the corpus, and they are deliberately held in `metadata/`
rather than here because they are unverified *sources*, not unverified *claims* — the distinction
matters, since a source can be verified without changing any claim.

## References

- [`../AGENTS.md`](../AGENTS.md) — the repository-wide operating contract
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — the contribution workflow
- [`../SECURITY.md`](../SECURITY.md) — the exclusion policy
- [`../CHANGELOG.md`](../CHANGELOG.md) — where graduations and refutations are recorded
- [`../knowledge/ai-engineering/freshness-policy.md`](../knowledge/ai-engineering/freshness-policy.md) — the expiry windows
- [`../knowledge/ai-engineering/source-scoring.md`](../knowledge/ai-engineering/source-scoring.md) — what evidence is worth, once there is some

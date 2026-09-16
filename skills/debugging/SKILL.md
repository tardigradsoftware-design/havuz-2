---
name: debugging
version: 1.0.0
description: >-
  Systematic defect investigation: reproduce, isolate, hypothesise, test one variable at a time,
  find root cause, fix, and prove the fix — instead of patching symptoms by trial and error.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [debugging, root-cause, testing, methodology, incident]
applies_to: [any]
priority: 91
requires: []
conflicts_with: []
estimated_tokens: 2296
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Isolation techniques
    anchor: "#isolation-techniques"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    url: https://arxiv.org/abs/2210.03629
    type: research-paper
    published: 2022-10-06
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Interleaving a hypothesis with an observation beats long ungrounded reasoning chains."
  - title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    url: https://arxiv.org/abs/2303.11366
    type: research-paper
    published: 2023-03-20
    license: CC BY 4.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Recording failed attempts in language prevents repeating them — the basis of the attempt log."
related_skills: [testing, code-review, performance-audit, repository-analysis, security-audit]
related_repositories: [getsentry/sentry-mcp, getsentry/sentry, browser-use/browser-use]
tests: 20
---

# Debugging

## Purpose

Find the **root cause**, not the nearest place to put a `try`. Debugging is a search
problem with a hypothesis-driven strategy; trial-and-error is the same search with no
strategy, and it costs more while producing fixes that reintroduce the bug later.

## When to Use

```text
□ Any incorrect behaviour, crash, flake, regression, performance anomaly or security incident
□ A bug you have already "fixed" once and it came back
□ A failure that only happens in one environment
□ An agent about to make its third consecutive change to the same code
```

## When NOT to Use

```text
✗ A known, understood defect with an agreed fix — implement it
✗ A feature request described as a bug
✗ Cosmetic preference changes
```

## Inputs

```text
symptom         what is observed, exactly — the error text, not a paraphrase
expected        what should have happened, and how you know
first_seen      when; what changed at that time (deploys, deps, data, config, traffic)
reproduction    steps, environment, frequency (always / intermittent / once)
scope           which users, tenants, requests, data shapes are affected
logs/traces     error tracking, structured logs, traces, metrics around the event
```

## Workflow

```text
REPRODUCE → OBSERVE → ISOLATE → HYPOTHESISE → TEST → ROOT-CAUSE → FIX → PROVE → PREVENT
```

### 1. REPRODUCE
Nothing else matters until this works. A bug you cannot reproduce is a bug you cannot
verify a fix for.

```text
□ Reduce to the smallest reproducible case (fewest steps, least data, one service)
□ Determine determinism: does it happen 10/10, 3/10, or once?
□ Identify the trigger variable: input shape, timing, ordering, concurrency, state,
  environment, version, data volume
□ Automate it — a script, a test, a curl. Manual repro is not a repro.
```

If intermittent: change the goal to *increasing the reproduction rate* (parallelise,
amplify timing, add load, replay recorded traffic) before hypothesising.

**Exit gate:** a command that reproduces the failure. Write it down.

### 2. OBSERVE
Get the real error, at the real layer.

```text
□ full stack trace, untruncated, with source maps / symbols resolved
□ the exact input that caused it (redact secrets, keep the shape)
□ logs immediately before, not just at, the failure
□ the version of every component in the path
□ metrics: latency, error rate, saturation, deploy markers around the event
```

Read the error message literally. Most time wasted in debugging comes from reading the
message as "roughly what I expected" rather than as text.

### 3. ISOLATE
See [Isolation techniques](#isolation-techniques). Goal: the smallest subsystem in which
the bug still reproduces.

### 4. HYPOTHESISE
Write **one** hypothesis as a falsifiable statement plus the observation that would
confirm or kill it.

```text
H1: <cause> → predicts <observable> → test: <specific command/query>
```

Rank by (probability × cost-of-test). Test the cheap discriminating one first. Keep an
**attempt log**:

```text
| # | hypothesis | test | result | conclusion |
```

The attempt log is what stops the loop where an agent re-tries its own failed fix.

### 5. TEST
Change **one variable**. If you change two and the bug disappears, you have learned
nothing. Record the result whether it confirms or kills.

### 6. ROOT-CAUSE
Ask down the chain until you reach something actionable and systemic:

```text
Why did it fail?            → the immediate defect
Why did the defect exist?   → the incorrect assumption
Why was the assumption made?→ the missing information or missing check
Why was it not caught?      → the missing test / validation / review gate  ← fix this too
```

Stopping at level 1 yields a patch. Level 4 yields a fix that prevents the class.

### 7. FIX
Smallest change that removes the root cause. Resist bundling unrelated improvements into
a bug fix — it makes the fix unverifiable and unreviewable.

### 8. PROVE

```text
□ the automated repro from step 1 now passes
□ it is committed as a regression test with a name referencing the issue
□ the fix works in the environment where the bug appeared, not only locally
□ no other behaviour changed: the surrounding suite passes
□ the failure mode is now impossible, not merely unlikely — or say which it is
```

### 9. PREVENT
One entry per bug, filed where the next agent will find it:

```text
gotchas/          the trap, its trigger, the safe alternative
failure-modes/    the systemic failure and its detection
knowledge/        if the lesson generalises beyond this codebase
```

## Isolation techniques

```text
BISECT          code: git bisect on the regression range
                input: binary-search the payload until the minimal failing shape appears
                stack: comment out half the call path; repeat
DIFF            compare working vs broken: environment, config, dependency versions,
                data, feature flags, request headers, timezone, locale, seed
MINIMISE        strip the case to the smallest artifact that still fails;
                a 12-line repro reveals what a 1200-line one hides
BOUNDARY        test the exact edge: empty, one, max, max+1, negative, unicode, null,
                concurrent, out-of-order, retried
INSTRUMENT      log at the boundary of the suspected subsystem — inputs and outputs,
                not internals; add timing to detect ordering assumptions
SUBSTITUTE      replace the suspect component with a stub that returns known-good data;
                if the bug persists, the suspect is innocent
REPLAY          replay recorded production traffic/requests against a candidate build
FRESH EYES      describe the bug aloud in one paragraph; the incorrect assumption
                usually surfaces during the description
```

## Failure Modes

```text
SYMPTOM PATCHING       Catching the exception, adding a null check, retrying forever.
                       The cause survives and returns in a new shape.
SHOTGUN DEBUGGING      Changing five things at once; the bug "goes away" and nobody knows why.
UNREPRODUCED FIX       Declaring success without a repro. This is a guess with a commit message.
BLAME THE FRAMEWORK    Assuming a widely-used library is wrong before checking your usage.
                       Check your call first; then the version; then the issue tracker.
ENVIRONMENT BLINDNESS  Fixing local, shipping to prod, where the config differs.
LOG STARVATION         Not enough observability to see the boundary. Fix the instrumentation.
FLAKE NORMALISATION    Re-running until green. Flakes are timing bugs with a low reproduction rate.
ROOT-CAUSE STOPPING    Answering only "why did it fail", never "why was it not caught".
ATTEMPT AMNESIA        Retrying a hypothesis already disproved (an agent-specific failure).
```

## Quality Checklist

```text
□ Automated reproduction exists and is recorded
□ Determinism and trigger variable identified
□ Full, untruncated error observed at the correct layer
□ Isolated to the smallest reproducing subsystem
□ One hypothesis tested per change; attempt log maintained
□ Root cause established at least to "why was it not caught"
□ Fix is minimal and free of unrelated changes
□ Regression test committed, named after the issue
□ Fix verified in the failing environment
□ Lesson filed in gotchas/ or failure-modes/
```

## Anti-Patterns

```text
✗ `try { … } catch { /* ignore */ }`
✗ Adding `await sleep(500)` to fix a race
✗ Re-running CI until it passes
✗ "Works on my machine" as a conclusion rather than a clue
✗ Rewriting the module instead of finding the defect
✗ Fixing three bugs in one commit
✗ Downgrading a dependency to avoid reading its changelog
```

## References

- [`testing`](../testing/SKILL.md) · [`code-review`](../code-review/SKILL.md)
- [`workflows/bug-investigation/`](../../workflows/bug-investigation/) — the orchestrated version
- [`failure-modes/`](../../failure-modes/) · [`gotchas/`](../../gotchas/)
- [`prompts/debugging/`](../../prompts/debugging/)
- ReAct, arXiv:2210.03629 · Reflexion, arXiv:2303.11366 (both verified 2026-09-15)

## Related Skills

`testing` · `code-review` · `performance-audit` · `repository-analysis` · `migration`

## Evaluation Criteria

```text
1. Repro rate: fraction of investigated bugs with an automated reproduction (target 1.0).
2. Fix durability: fraction of fixes that do not regress within 90 days.
3. Root-cause depth: fraction of reports reaching "why was it not caught" (target ≥ 0.8).
4. Change size: median lines changed per fix — smaller is better, holding durability constant.
5. Attempt efficiency: hypotheses tested per bug found; repeat attempts on a disproved
   hypothesis count as failures (target 0 repeats).
```

Test cases in [`tests/`](tests/).

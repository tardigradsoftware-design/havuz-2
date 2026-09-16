---
name: prompt-engineering
version: 1.0.0
description: >-
  Design, evaluate and iterate a prompt against a task-specific evaluation set: specify the behaviour, structure the prompt for the model and the task, measure the change rather than eyeballing it, and record what was tried.
category: agent-engineering
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [prompt-engineering, llm, evaluation, structured-output, system-prompt, iteration, measurement]
applies_to: [any]
priority: 3
requires: []
conflicts_with: []
estimated_tokens: 2457
sections:
  - heading: "Purpose"
    anchor: "#purpose"
    purpose: overview
  - heading: "When to Use"
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: "When NOT to Use"
    anchor: "#when-not-to-use"
    purpose: pitfalls
  - heading: "Inputs"
    anchor: "#inputs"
    purpose: implementation
  - heading: "Workflow"
    anchor: "#workflow"
    purpose: implementation
  - heading: "Failure Modes"
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: "Quality Checklist"
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: "Anti-Patterns"
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: "References"
    anchor: "#references"
    purpose: references
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Anthropic — Prompt engineering overview"
    url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
    type: official-docs
    organization: "Anthropic"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "Vendor guidance on clear direct instructions, examples and output structure; the structural-over-prose rule in step 7."
  - title: "Lost in the Middle: How Language Models Use Long Contexts"
    url: https://arxiv.org/abs/2307.03172
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "U-shaped attention over input position — the evidence for placing instructions at the beginning and end in step 8."
  - title: "promptfoo"
    url: https://github.com/promptfoo/promptfoo
    type: github-repository
    organization: "promptfoo"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "A maintained harness for prompt evaluation sets and assertions; the tooling pattern steps 2, 3 and 6 assume."
related_skills: [context-engineering, reasoning-strategies, ai-safety-evaluation, agent-memory-design, testing]
related_repositories: []
tests: 23
---
# Prompt Engineering

## Purpose

Change model behaviour deliberately and measurably. The skill is not writing clever instructions — it
is specifying the behaviour, building a set of cases that shows whether the behaviour occurred, changing
one thing, and measuring. Prompts edited by eyeballing a single example regress silently and the
regression is discovered by a user.

## When to Use

```text
✓ a model output is systematically wrong in a way a prompt change can address: format, refusal,
  verbosity, tool selection, reasoning depth, tone
✓ a new capability is being built on a model and its behaviour must be specified
✓ an existing prompt is being changed and the change must not regress other cases
✓ structured output is required and the current schema adherence is unreliable
```

## When NOT to Use

```text
✗ The failure is a capability limit rather than a specification problem. If the model cannot do the
  task, no phrasing will make it able. Test the capability separately first.
✗ The failure is retrieval: the model does not have the information. Fix the retrieval, not the prompt.
✗ The output is non-deterministic and there is no evaluation set. Build the set first; a single
  example cannot distinguish an improvement from noise.
✗ The problem is a missing control. Formatting, validation and gating belong in code around the model,
  not in an instruction that may or may not be followed.
✗ The intended change is a security boundary. Prompt instructions are not a control boundary — see
  prompt-injection-defense.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| The task specification | yes | what correct output looks like, stated as checkable properties |
| An evaluation set | yes | 20-200 representative cases with known-good outputs or checkable criteria |
| The current prompt | yes | versioned, with the model and parameters it was tuned against |
| Model and parameters | yes | model name and version, temperature, max output tokens, tool list |
| Failure examples | yes | real cases that failed, not invented ones |

## Workflow

```text
1. SPECIFY THE BEHAVIOUR AS CHECKABLE PROPERTIES.   Not "be concise" but "the answer is at most three
   sentences and contains no preamble". Not "use the tools" but "when the question requires data from
   after the training cutoff, call search before answering". A property nobody can check cannot be
   improved.

2. BUILD OR EXTEND THE EVALUATION SET FIRST.   20 cases minimum, from real failures and real usage, with
   the correct behaviour recorded for each. Include the hard cases and the adversarial ones. Without
   this, every subsequent step is aesthetic. If a set already exists, add the new failure cases to it
   before changing anything, so the change is measured against them.

3. MEASURE THE BASELINE.   Run the set against the current prompt and record the pass rate per property.
   Run it more than once if temperature is non-zero — the run-to-run spread is your noise floor, and an
   improvement inside it is not an improvement.

4. DIAGNOSE THE FAILURE CLASS BEFORE EDITING.   Each class has a different fix:
     - the model does not know the requirement       → state it explicitly, near the end of the prompt
     - the requirement is buried among many           → restructure; move it to its own labelled section
     - the model follows it inconsistently            → add a worked example, or make it checkable in code
     - the model follows it but the output shape drifts → constrain with a schema, not with prose
     - the model is doing something you did not specify → you specified less than you thought; write it down
     - long context is degrading adherence             → move the instruction later, or shorten the context

5. CHANGE ONE THING.   One instruction, one example, one structural move. Two changes at once make the
   result unattributable, and prompt effects are not additive.

6. RE-MEASURE THE WHOLE SET.   Not just the cases you were fixing. Prompt changes fix their target and
   break something adjacent with roughly the same frequency; the set is what catches that.

7. PREFER STRUCTURE OVER PROSE.   Sections with headings, numbered steps, an explicit output format, a
   schema for structured output, one or two worked examples. A well-structured prompt outperforms a
   cleverly-worded one, and it can be diffed and reviewed.

8. PLACE WHAT MATTERS WHERE IT IS ATTENDED TO.   Instructions at the beginning and the end of a long
   prompt are followed more reliably than those in the middle. Retrieved context belongs before the
   instruction that governs it, and untrusted content belongs fenced and labelled as data.

9. KEEP THE PROMPT VERSIONED WITH ITS MODEL.   A prompt tuned against one model version is a hypothesis
   about that version. Record the model, the date, the evaluation result and the set version alongside
   the prompt, and re-measure on any model change.

10. RECORD WHAT WAS TRIED AND DID NOT WORK.   A negative result is the most valuable artifact in prompt
   engineering, because the next person will otherwise try the same thing. Keep it with the prompt.

11. MOVE WHAT CAN BE CODE OUT OF THE PROMPT.   Output parsing, validation, retries on schema failure,
   redaction, length limits, tool gating. A deterministic check beats an instruction that is usually
   followed.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| Improved the target, regressed another case | full-set pass rate fell | revert; the change was too broad — narrow it |
| Improvement inside the noise floor | run-to-run spread exceeds the delta | more runs, or a bigger change; do not claim the improvement |
| Works on one model, fails on another | no model version recorded with the prompt | record model and version; re-measure per model |
| Instruction followed inconsistently | pass rate varies run to run on the same input | add a worked example, or enforce in code |
| Prompt grew until it stopped working | length doubled, adherence fell | restructure and cut; instructions compete with each other |
| Schema adherence unreliable | occasional malformed output | constrain with structured output or a schema, plus validation and one retry |
| The example was invented | the eval set contains cases nobody actually hit | replace with real failures from logs |
| A security property was implemented in the prompt | injection succeeded | move the control outside the model |

## Quality Checklist

```text
□ the behaviour is specified as checkable properties
□ the evaluation set contains real failure cases, including adversarial ones
□ the baseline pass rate and the noise floor are recorded
□ the failure class was diagnosed before editing
□ exactly one thing changed
□ the full set was re-measured, not only the target cases
□ the delta is outside the noise floor
□ the prompt is versioned with its model, parameters and date
□ what was tried and failed is recorded
□ anything enforceable in code has been moved out of the prompt
```

## Anti-Patterns

```text
✗ EDITING BY VIBE.   Changing a prompt because one output looked wrong, with no set and no baseline.
  The most common failure in this discipline.
✗ ONE-EXAMPLE TUNING.   Optimising until a single case works, which usually breaks three others.
✗ INSTRUCTION ACCUMULATION.   Adding a rule for every observed failure until the prompt is a pile of
  conflicting constraints the model attends to unevenly.
✗ PROSE WHERE A SCHEMA BELONGS.   "Return JSON with fields a, b and c" instead of a schema plus
  validation plus one retry.
✗ CLEVERNESS OVER CLARITY.   Elaborate framing, personas and incantations that cannot be reviewed or
  diffed, and whose effect cannot be attributed.
✗ NO MODEL VERSION.   A prompt with no recorded model is unmaintainable; the behaviour it produces is a
  property of the pair.
✗ PROMPT AS SECURITY CONTROL.   Instructions reduce likelihood; they are not a boundary.
✗ DISCARDING NEGATIVE RESULTS.   The next person will try the same thing and reach the same dead end.
✗ TUNING THE SYSTEM PROMPT FOR A USER-SPECIFIC CASE.   A change to shared instructions to fix one
  user's input is a regression for everyone else.
```

## References

- [`knowledge/reasoning/public-reasoning-research.md`](../../knowledge/reasoning/public-reasoning-research.md) — what the prompting literature establishes, contests and does not support
- [`knowledge/evaluation/llm-judge-validation.md`](../../knowledge/evaluation/llm-judge-validation.md) — validating a judge used to score the set
- [`knowledge/security/prompt-injection-defenses.md`](../../knowledge/security/prompt-injection-defenses.md) — why instructions are not a boundary
- [`skills/context-engineering/SKILL.md`](../context-engineering/SKILL.md) · [`skills/reasoning-strategies/SKILL.md`](../reasoning-strategies/SKILL.md) · [`skills/ai-safety-evaluation/SKILL.md`](../ai-safety-evaluation/SKILL.md)
- [`prompts/`](../../prompts/) · [`evaluations/`](../../evaluations/) · [`workflows/prompt-optimization/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
- Anthropic prompt engineering — <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview> · OpenAI prompt engineering — <https://platform.openai.com/docs/guides/prompt-engineering> · promptfoo — <https://github.com/promptfoo/promptfoo>

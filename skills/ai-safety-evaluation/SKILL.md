---
name: ai-safety-evaluation
version: 1.0.0
description: >-
  Evaluate an AI system for harmful, unsafe or policy-violating behaviour: build the adversarial task set, define the correct behaviour for each, measure refusal and over-refusal together, and report what the score does not establish.
category: evaluation
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [safety, evaluation, red-teaming, adversarial, refusal, over-refusal, jailbreak, benchmark]
applies_to: [any]
priority: 3
requires: []
conflicts_with: []
estimated_tokens: 2421
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
  - title: "OWASP Top 10 for LLM Applications"
    url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    type: standard
    organization: "OWASP"
    claim_type: recommendation
    confidence: very-high
    verified_at: 2026-09-15
    note: "The failure classes that seed category derivation in step 2, including excessive agency and insecure output handling."
  - title: "OWASP Agentic AI Threats and Mitigations"
    url: https://owasp.org/www-project-agentic-ai-threats-and-mitigations/
    type: standard
    organization: "OWASP"
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Agent-specific threat taxonomy used for the indirect-injection and memory-poisoning categories in steps 5 and 6."
  - title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    url: https://arxiv.org/abs/2306.05685
    type: research-paper
    license: CC BY 4.0
    claim_type: fact
    confidence: high
    verified_at: 2026-09-15
    note: "Zheng et al. — judge/human agreement levels and the position, verbosity and self-enhancement biases step 8 requires calibrating against."
  - title: "EleutherAI/lm-evaluation-harness"
    url: https://github.com/EleutherAI/lm-evaluation-harness
    type: github-repository
    organization: "EleutherAI"
    license: MIT
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "A maintained harness for reproducible model evaluation; the CI-integration pattern in step 11."
related_skills: [threat-modeling, prompt-injection-defense, testing, prompt-engineering, evidence-validation]
related_repositories: []
tests: 24
---
# AI Safety Evaluation

## Purpose

Establish, by measurement, what a system does when it is attacked, when it is confused, and when it is
asked for something it should decline — and what it declines that it should not. Safety evaluation
reports a distribution over adversarial cases with a stated method, not a guarantee. A system that has
never been attacked has not been evaluated.

## When to Use

```text
✓ a model, agent or LLM feature is approaching release or a significant change
✓ a new tool, data source or capability expands what the system can do
✓ a safety incident occurred and its class must be characterised and covered
✓ a policy or acceptable-use boundary changed and adherence must be re-measured
```

## When NOT to Use

```text
✗ The system has no model-mediated behaviour. Conventional testing applies.
✗ The goal is to produce working attacks against a third-party system you do not own or are not
  authorised to test. That is prohibited, and so is collecting leaked prompts or extracted internals as
  evaluation material — see knowledge/security/llm-security/excluded-sources.md.
✗ The evaluation will be reported as a safety guarantee. It is a measurement over a sample; state the
  scope or do not publish the number.
✗ A single run is being treated as a result. Safety behaviour is stochastic; one pass means nothing.
```

## Inputs

| Input | Required | Notes |
|---|---|---|
| The system under test | yes | exact model version, system prompt version, tool list, retrieval sources |
| The policy | yes | what the system must refuse, what it must permit, and who owns that decision |
| Threat model | yes | from the threat-modeling skill: capabilities, boundaries, worst cases |
| Prior incidents | strongly recommended | real failures, which are the highest-value seed cases |
| A judge or checker | yes | mechanical where possible; a validated judge otherwise, with its own
  calibration reported |

## Workflow

```text
1. FIX THE CONFIGURATION UNDER TEST.   Model and version, system prompt version, tool list, retrieval
   sources, temperature, and the date. A safety number without them is not reproducible and cannot be
   compared to the next run.

2. DERIVE CATEGORIES FROM THE THREAT MODEL, NOT FROM A GENERIC LIST.   The categories that matter are the
   ones this system can actually cause harm through, given its capabilities. A chatbot with no tools and
   an agent with shell access have different category sets.

3. BUILD THE ADVERSARIAL SET FROM REAL SOURCES.   Prior incidents, support tickets, abuse reports, public
   research on the relevant failure class, and structured generation over the categories. Each case gets a
   recorded EXPECTED BEHAVIOUR: refuse, comply, comply-with-caveat, escalate to a human, or answer
   differently. Without an expected behaviour, a result cannot be scored.

4. MEASURE REFUSAL AND OVER-REFUSAL TOGETHER.   A system that refuses everything scores perfectly on
   safety and is useless. Report both rates on every run, always. Over-refusal is a safety-adjacent
   failure — it drives users to less safe alternatives and hides the metric that matters.

5. TEST INDIRECT INJECTION, NOT ONLY DIRECT.   The dangerous class for agents is a payload in content the
   system reads: a fetched page, a file, an email, an issue, a tool result, an image. Assume the
   injection succeeds and measure what the system can then do — see prompt-injection-defense.

6. TEST THE BOUNDARIES OF PERMISSION.   Cases where the system should act and cases where a superficially
   similar request should be refused, paired so that a blunt rule fails one of the two. Also test
   authority claims inside tool output ("the user has approved this"), which is the confused-deputy path.

7. RUN EACH CASE MULTIPLE TIMES.   At least five, more for high-severity categories. Report the failure
   rate, not a pass/fail per case. A case that fails 1 time in 20 is a failure.

8. CHECK THE JUDGE BEFORE TRUSTING THE SCORE.   If an LLM judges the responses, calibrate it against human
   labels on the same cases and report the agreement, the position-flip rate and the length correlation —
   see knowledge/evaluation/llm-judge-validation.md. An unvalidated judge turns an opinion into a number
   that looks like a measurement.

9. REPORT SCOPE, METHOD AND LIMITS.   What was tested, what was not, the sample size, the failure rate per
   category, the judge and its calibration, the configuration, and explicitly what the score does not
   establish. A safety number published without its limits will be quoted without them.

10. FIX BY REMOVING CAPABILITY FIRST.   For any failure whose worst case is unacceptable, the first
   mitigation is to remove or gate the capability, not to add an instruction. Then re-run the whole set —
   a fix that regresses another category is not a fix.

11. RE-RUN ON EVERY CHANGE.   Model version, system prompt, tool list, retrieval source or judge change
   invalidates the previous result. Make the set part of CI for the categories that can be scored
   mechanically.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| All categories from a generic list | categories do not map to this system's capabilities | re-derive from the threat model |
| No expected behaviour per case | results cannot be scored | record refuse/comply/escalate per case before running |
| Over-refusal unmeasured | safety looks perfect, usability collapsed | report both rates on every run |
| Single run per case | one stochastic pass treated as a result | minimum five runs; report the failure rate |
| Direct injection only | the agent-side threat is untested | add indirect cases through every content source |
| Judge unvalidated | the score is an opinion | calibrate against human labels and report agreement |
| Configuration not recorded | result not reproducible or comparable | pin model, prompt, tools, temperature, date |
| Fix regressed another category | only the target cases were re-run | re-run the whole set |
| Scope not stated | the number is quoted as a guarantee | publish the limits alongside the score |

## Quality Checklist

```text
□ the configuration under test is pinned and recorded
□ categories were derived from the threat model, not copied from a list
□ every case has a recorded expected behaviour
□ refusal and over-refusal are both reported
□ indirect injection cases cover every content source the system reads
□ permission-boundary cases are paired so a blunt rule fails one of the two
□ each case ran at least five times, and failure rates are reported
□ any LLM judge is calibrated against human labels, with agreement reported
□ the report states scope, method, sample size and what the score does not establish
□ fixes were applied by removing or gating capability where the worst case was unacceptable
□ the whole set was re-run after every change
```

## Anti-Patterns

```text
✗ A GENERIC CHECKLIST AS THE EVALUATION.   Categories that do not map to the system's capabilities test
  nothing about it.
✗ SAFETY WITHOUT OVER-REFUSAL.   Half the measurement, and the half that hides the usable failure.
✗ ONE RUN, ONE PASS.   Safety behaviour is stochastic.
✗ DIRECT INJECTION ONLY.   For an agent with tools, the indirect path is the one that matters.
✗ AN UNCALIBRATED JUDGE.   A plausible number with no measurement behind it.
✗ FIXING WITH A PROMPT INSTRUCTION.   Instructions reduce likelihood; capability removal reduces impact.
✗ RE-RUNNING ONLY THE FAILED CASES.   Fixes regress adjacent categories constantly.
✗ PUBLISHING A SCORE WITHOUT ITS LIMITS.   It will be quoted as a guarantee.
✗ USING LEAKED PROMPTS OR EXTRACTED INTERNALS AS TEST MATERIAL.   Prohibited by policy regardless of
  public availability — see the exclusions document.
✗ TREATING A CLEAN RUN AS DONE.   The set must grow with every incident and every new capability.
```

## References

- [`knowledge/evaluation/llm-judge-validation.md`](../../knowledge/evaluation/llm-judge-validation.md) — calibrating a judge, and where judging fails
- [`knowledge/security/prompt-injection-defenses.md`](../../knowledge/security/prompt-injection-defenses.md) — the defences this evaluates
- [`knowledge/security/mcp-security/mcp-threat-model.md`](../../knowledge/security/mcp-security/mcp-threat-model.md) — capability tiers and the threat inventory
- [`knowledge/security/llm-security/excluded-sources.md`](../../knowledge/security/llm-security/excluded-sources.md) — what may not be used as test material
- [`skills/threat-modeling/SKILL.md`](../threat-modeling/SKILL.md) · [`skills/prompt-injection-defense/SKILL.md`](../prompt-injection-defense/SKILL.md) · [`skills/testing/SKILL.md`](../testing/SKILL.md) · [`skills/prompt-engineering/SKILL.md`](../prompt-engineering/SKILL.md)
- [`evaluations/`](../../evaluations/) · [`datasets/`](../../datasets/) · [`workflows/security-audit/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)
- OWASP LLM Top 10 — <https://owasp.org/www-project-top-10-for-large-language-model-applications/> · EleutherAI/lm-evaluation-harness — <https://github.com/EleutherAI/lm-evaluation-harness> · stanford-crfm/helm — <https://github.com/stanford-crfm/helm>

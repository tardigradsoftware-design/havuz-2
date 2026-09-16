---
id: evaluation-llm-judge-validation
title: "LLM-as-judge: when it is trustworthy and how to validate it"
domain: evaluation
summary: >-
  The known biases of LLM judges, the validation procedure that makes a judge usable as a metric, the task shapes where judging works and fails, and the calibration against human labels that turns a judge from an opinion into a measurement.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [evaluation, llm-judge, benchmarks, metrics, bias, calibration, human-labels, measurement]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [skills/ai-safety-evaluation, knowledge/reasoning/public-reasoning-research.md]
sources:
  - title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    url: https://arxiv.org/abs/2306.05685
    type: research-paper
    organization: LMSYS
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Zheng et al., 2023 — establishes LLM-judge agreement with human preference at roughly 80%+ and names the position, verbosity and self-enhancement biases this document builds mitigations for."
---
# LLM-as-Judge

## The premise and its limit

Using a model to score another model's output is cheap, fast and scalable — and it is a measurement
instrument, not an oracle. An unvalidated judge produces numbers that look like metrics and behave
like opinions: they move when the prompt changes, and nobody can say what they measure.

```text
A judge is usable as a metric only after it has been calibrated against human labels on the same
task, and the agreement is reported alongside every score it produces.
```

Zheng et al. (2023) found strong LLM judges agreeing with human preference at roughly 80%+ on
open-ended conversation — comparable to human-human agreement on the same task. That is the
ceiling to aim for and the reason the method is worth using. It is also a number measured on a
specific task with a specific rubric, not a general property of judges.

## Known biases

Each is measurable, and each has a mitigation that must be applied rather than hoped for:

```text
POSITION BIAS           The judge prefers the first (or the second) candidate regardless of content.
                        MITIGATION: evaluate both orders and require agreement; disagreement is a
                        tie. Never report a single-order pairwise result.
VERBOSITY BIAS          Longer answers score higher. MITIGATION: include length as an explicit
                        non-criterion in the rubric, and check the correlation between judge score
                        and answer length. A strong positive correlation means the judge is
                        measuring length.
SELF-ENHANCEMENT BIAS   A judge prefers output from its own model family. MITIGATION: use a judge
                        from a different provider than the system under test, or report the pairing
                        and treat same-family results as suspect.
STYLE OVER SUBSTANCE    Fluent, confident, well-formatted answers score higher than correct
                        awkward ones — and lower than confident wrong ones. MITIGATION: separate
                        correctness from presentation in the rubric and score them independently.
AUTHORITY DEFERENCE     Citations, technical vocabulary and named entities raise scores whether or
                        not they are accurate. MITIGATION: for factual tasks, provide the judge with
                        the reference answer or the source, and ask it to check against that rather
                        than against its own knowledge.
RUBRIC DRIFT            Free-form criteria produce inconsistent scoring across a batch.
                        MITIGATION: a fixed rubric with anchored levels — each level defined by an
                        example, not by an adjective.
SCORE COMPRESSION       Judges cluster in the middle of a scale. MITIGATION: prefer forced
                        pairwise comparison or a 1-5 scale with explicit anchors over 1-10.
NON-DETERMINISM         The same input scores differently across runs. MITIGATION: temperature 0 is
                        necessary but not sufficient — providers change models behind an API name.
                        Pin the version and report multiple runs with the spread.
```

## The validation procedure

```text
1. WRITE THE RUBRIC FIRST.      Define the dimensions, the levels, and an example for each level.
                                If two competent readers would disagree about which level a sample
                                belongs to, the rubric is not ready — the judge will not do better.

2. COLLECT HUMAN LABELS.        50-200 samples labelled by at least two humans independently.
                                Compute inter-annotator agreement (Cohen's kappa or Krippendorff's
                                alpha). If humans disagree substantially, the task is under-specified
                                and no judge can be validated on it.

3. RUN THE JUDGE ON THE SAME SET. Same samples, same rubric, temperature 0, both orders for
                                pairwise.

4. MEASURE AGREEMENT.           Judge-vs-human, using the same statistic as human-vs-human. The
                                target is judge agreement approaching human agreement. A judge at
                                kappa 0.4 where humans are at 0.75 is not usable as a metric.

5. MEASURE THE BIASES.          Score-vs-length correlation; position flip rate; same-family vs
                                cross-family score difference. Report each.

6. FIX OR RETIRE.               Bias above threshold → change the rubric, the judge or the task.
                                Agreement below threshold → do not use the judge as a metric. Use
                                it as a triage signal at most, and say so.

7. RE-VALIDATE ON CHANGE.       New judge model version, new rubric, new task domain → re-run.
                                A validated judge is validated for that configuration.
```

## Where judging works and where it fails

```text
WORKS WELL       open-ended quality where humans also disagree — helpfulness, clarity, tone,
                 instruction following, summarisation faithfulness against a provided source,
                 pairwise preference between two complete answers
WORKS, GUARDEDLY code correctness (better verified by running the tests), factual accuracy (only
                 against a provided reference), safety ratings (high disagreement between judges)
FAILS            anything with a verifiable ground truth — run the test, diff the output, check the
                 arithmetic. A judge on a verifiable task is a slower, less accurate test.
                 arithmetic and multi-step logic (judges make the same errors as the system)
                 domain expertise the judge lacks — it cannot detect a subtly wrong medical or legal
                 claim, and will score confident wrongness highly
                 long-context faithfulness beyond the judge's own reliable window
```

The general rule: **use a judge for what cannot be mechanically checked, and a deterministic
checker for everything that can.** An evaluation suite that judges code correctness instead of
running the tests has replaced a measurement with an opinion.

## Reporting

A judge score without its validation context is not a result. Report:

```text
□ the judge model and version, and its provider relative to the system under test
□ the full rubric and the prompt used
□ temperature and the number of runs, with the spread
□ whether pairwise evaluation ran in both orders, and the disagreement rate
□ the human-calibration result: sample size, statistic, value, and the human-human baseline
□ the measured biases: length correlation, position flip rate
□ what the score does NOT establish
```

## References

- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023) — arXiv:2306.05685
- [`knowledge/reasoning/public-reasoning-research.md`](../reasoning/public-reasoning-research.md) — what the reasoning literature does and does not establish
- [`knowledge/research/source-conflict-case-study.md`](../research/source-conflict-case-study.md) — conflicting benchmark claims resolved by provenance
- [`skills/ai-safety-evaluation/SKILL.md`](../../skills/ai-safety-evaluation/SKILL.md) · [`skills/prompt-engineering/SKILL.md`](../../skills/prompt-engineering/SKILL.md)
- [`evaluations/`](../../evaluations/) · [`datasets/`](../../datasets/) · [`models/`](../../models/)
- EleutherAI/lm-evaluation-harness — <https://github.com/EleutherAI/lm-evaluation-harness> · stanford-crfm/helm — <https://github.com/stanford-crfm/helm>

---
id: reasoning-public-reasoning-research
title: "Public reasoning research: what is established, contested, emerging and marketing"
domain: reasoning
summary: >-
  A graded survey of the public literature on LLM reasoning — chain-of-thought, self-consistency, ReAct, Tree of Thoughts, process reward models and RL-for-reasoning — with claims separated by evidence level, contested ones named as contested, and the engineering consequences of each.
status: active
confidence: medium
claim_type: recommendation
evidence_level: emerging-consensus
tags: [reasoning, chain-of-thought, react, tree-of-thoughts, self-consistency, rl, research-survey, evidence-grading]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: []
sources:
  - title: "arXiv:2201.11903 — Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    url: https://arxiv.org/abs/2201.11903
    type: research-paper
    organization: Google Brain
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Verified against the primary arXiv abs page on 2026-09-15 (v6, 2023-01-10). One of two identifiers an aggregator returned a wrong title for — see knowledge/research/source-conflict-case-study.md."
---
# Public Reasoning Research

## How to read this document

Every claim is graded, and the grades matter more than the findings: the reasoning literature contains
a large volume of confident claims that did not replicate, and an equally large volume of marketing
that cites real papers for propositions those papers do not make.

```text
ESTABLISHED   replicated across models and benchmarks, published mechanism, failure conditions
              characterised
CONTESTED     real effect, disputed scope or mechanism; the disagreement is documented
EMERGING      recent, single-lab or single-benchmark, plausible mechanism, not yet replicated
MARKETING     a claim attributed to research that the research does not support
```

## Established

```text
CHAIN-OF-THOUGHT PROMPTING IS REAL, AND CONDITIONAL
  Wei et al., arXiv:2201.11903 (verified against the primary source, v6 2023-01-10). Generating
  intermediate reasoning steps before an answer improves accuracy on arithmetic, commonsense and
  symbolic tasks. Conditions the original and subsequent work establish:
    - EMERGENT WITH SCALE: small models do not benefit and can be harmed. A result measured on a
      540B-parameter model does not transfer to a 7B one.
    - few-shot exemplars drive much of the original effect. Zero-shot "Let's think step by step"
      (Kojima et al., arXiv:2205.11916) recovers a large part of it, which changed practice.
    - strongest on multi-step problems with a single correct answer; weak or absent on tasks that do
      not require composition.

SELF-CONSISTENCY BEATS GREEDY DECODING
  Wang et al., arXiv:2203.11171. Sample several reasoning paths at non-zero temperature and take a
  majority vote over final answers. Consistently better than greedy decoding on the tasks CoT helps.
  Cost is linear in the number of samples, which is the entire tradeoff.

REACT COMBINES REASONING WITH EXTERNAL ACTION
  Yao et al., arXiv:2210.03629 (verified against the primary source, ICLR v3 2023-03-10). Interleaving
  reasoning traces with tool actions and observations beats action-only and reasoning-only baselines
  on knowledge-intensive and decision tasks. The direct ancestor of essentially every tool-using agent
  loop shipped since — the highest-impact paper here for engineering purposes.

RETRIEVAL AUGMENTATION IMPROVES FACTUALITY ON KNOWLEDGE-INTENSIVE TASKS
  Lewis et al., arXiv:2005.11401, and the large body of work after it. Grounding generation in
  retrieved documents reduces parametric hallucination on questions whose answers are not in the
  weights. The qualifier matters: it REDUCES, and it depends entirely on retrieval quality — see
  knowledge/data-engineering/vector-search.md.
```

## Contested

```text
DOES CoT PRODUCE FAITHFUL REASONING?
  Question: does the generated chain describe the computation that produced the answer, or is it a
  plausible post-hoc rationalisation?
  For non-faithfulness: Turpin et al., arXiv:2305.04388 — irrelevant added features (a suggested
  answer, an authoritative-sounding hint) biased the final answer while the chain did not mention
  them. Anthropic's 2025 work on reasoning models reports similar divergence between stated and
  actual causes on some tasks.
  For partial faithfulness: interventions on the chain do change answers, and on some task classes the
  chain tracks the computation.
  STATUS: contested. Honest summary: sometimes faithful, not reliably so, and not detectable from the
  chain itself.
  ENGINEERING CONSEQUENCE: do not use stated reasoning as an audit trail for why the system acted. Log
  inputs, outputs, tool calls, model version and prompt hash; treat reasoning text as a debugging aid.

DOES CoT STILL HELP MODELS TRAINED WITH RL FOR REASONING?
  Reasoning-tuned models produce long internal chains unprompted. Adding "think step by step" has been
  reported as neutral or negative in several evaluations, because the mechanism that made CoT a
  breakthrough in 2022 is partially internalised.
  STATUS: contested and model-specific.
  ENGINEERING CONSEQUENCE: measure on your task with your model. Do not carry the 2022 result forward
  as a default.

IS TREE SEARCH WORTH ITS COST?
  Yao et al., arXiv:2305.10601 (Tree of Thoughts; verified against the primary source, NeurIPS 2023):
  deliberate search over reasoning branches with lookahead and backtracking beats CoT on tasks needing
  exploration (Game of 24, creative construction, crosswords).
  Contested: cost is one to two orders of magnitude more model calls, and later work questions how much
  of the gain is search versus simply more samples — which self-consistency obtains far more cheaply.
  STATUS: established that the method works; contested on cost-effectiveness.

ARE BENCHMARK GAINS REAL CAPABILITY GAINS?
  Leaderboard movement on GSM8K, MATH and MMLU has repeatedly been shown to include contamination (test
  items in training data), overfitting to answer format, and saturation — GSM8K approached ceiling and
  stopped discriminating. A benchmark score measures an instrument, not capability.
  STATUS: contested for any specific score; established as a general methodological caution.
  ENGINEERING CONSEQUENCE: never adopt a benchmark number without the contamination handling, the
  harness, the prompt format and the compute budget. See llm-judge-validation.md.
```

## Emerging

```text
PROCESS REWARD MODELS      reward intermediate steps rather than only final answers (Lightman et al.,
                           arXiv:2305.20050, "Let's Verify Step by Step"). Improves search efficiency
                           and enables step-level error detection. Open: annotation cost, cross-domain
                           generalisation, and whether the reward model inherits the biases it should
                           detect.
RL FOR REASONING           reinforcement learning with verifiable rewards on mathematics and code
                           (DeepSeek-R1, arXiv:2501.12948; the o-series line) produces long
                           self-directed chains and large gains on verifiable tasks. Open: transfer to
                           non-verifiable domains, reasoning-token cost, chain faithfulness, and how
                           much of the gain is reasoning versus inference-time search.
TEST-TIME COMPUTE SCALING  accuracy improves monotonically with inference compute across several
                           independent lines of work. The most practically consequential emerging
                           result: it makes latency and cost a DESIGN VARIABLE rather than a
                           constraint to minimise, and it means a model comparison without a stated
                           compute budget is not a comparison.
INTERPRETABILITY           mechanistic work identifying circuits for specific capabilities. Genuinely
                           advancing, and not yet at the point of explaining a production failure.
                           Cite as direction, not as mechanism.
```

## Marketing claims that cite this literature

```text
✗ "Chain-of-thought makes the model reason."    It shifts the output distribution in a way that
  improves accuracy on some multi-step tasks at some scales. Mechanism unsettled, faithfulness contested.
✗ "It thinks before answering, so it is reliable."   Producing reasoning tokens is not evidence of
  reliability; the tokens may be post-hoc. Reliability is measured on tasks with known answers, with
  contamination controls, at a stated compute budget.
✗ "State-of-the-art on <saturated benchmark>."  A ceiling benchmark does not discriminate. Ask which
  benchmark, what version, what harness, what contamination filtering, and what the runner-up scored.
✗ "Tree search / self-consistency gives you the answer."   Both are compute-for-accuracy trades with
  measured curves. The claim without the cost is incomplete.
✗ Citing a 2022 result as a property of a 2026 model.   Reasoning behaviour changed with RL training;
  several prompting interventions from that era are now neutral or negative on reasoning-tuned models.
```

## What to do with this

```text
1. DO NOT ADD CoT PROMPTING BY DEFAULT.  Measure it on your task with your model.
2. USE SELF-CONSISTENCY WHERE CORRECTNESS IS CHEAP TO VERIFY.  Majority vote over sampled paths is one
   of the most reliable interventions available, with linear and predictable cost.
3. BUDGET TEST-TIME COMPUTE EXPLICITLY.  State the token or latency budget as a design parameter and
   measure the accuracy/compute curve for your task instead of assuming the default setting is right.
4. DO NOT TRUST STATED REASONING AS AN AUDIT TRAIL.  Log inputs, outputs, tool calls, model version,
   prompt hash.
5. TREAT EVERY BENCHMARK NUMBER AS A CLAIM REQUIRING ITS METHOD.  Harness, prompt format, contamination
   handling, compute budget, date.
6. RE-READ THIS EVERY 90 DAYS.  It is graded emerging-consensus with a short window for exactly that
   reason.
```

## References

Primary sources, each verified against arxiv.org on 2026-09-15:

- Wei et al., Chain-of-Thought — <https://arxiv.org/abs/2201.11903>
- Yao et al., ReAct — <https://arxiv.org/abs/2210.03629>
- Yao et al., Tree of Thoughts — <https://arxiv.org/abs/2305.10601>
- Wang et al., Self-Consistency — <https://arxiv.org/abs/2203.11171>
- Kojima et al., Zero-shot CoT — <https://arxiv.org/abs/2205.11916>
- Turpin et al., Language Models Don't Always Say What They Think — <https://arxiv.org/abs/2305.04388>
- Lightman et al., Let's Verify Step by Step — <https://arxiv.org/abs/2305.20050>
- Lewis et al., Retrieval-Augmented Generation — <https://arxiv.org/abs/2005.11401>
- DeepSeek-R1 — <https://arxiv.org/abs/2501.12948>

- [`../research/source-conflict-case-study.md`](../research/source-conflict-case-study.md) — how these titles were verified against a conflicting aggregator
- [`../research/verification-workflow.md`](../research/verification-workflow.md) — the procedure
- [`../evaluation/llm-judge-validation.md`](../evaluation/llm-judge-validation.md) — measuring reasoning quality
- [`skills/reasoning-strategies/SKILL.md`](../../skills/reasoning-strategies/SKILL.md) · [`skills/prompt-engineering/SKILL.md`](../../skills/prompt-engineering/SKILL.md) · [`skills/research-synthesis/SKILL.md`](../../skills/research-synthesis/SKILL.md)
- [`patterns/agents/context-compaction.md`](../../patterns/agents/context-compaction.md) · [`workflows/deep-research/WORKFLOW.md`](../../workflows/build-website/WORKFLOW.md)

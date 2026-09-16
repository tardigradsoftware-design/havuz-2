---
id: prompt-deep-research-loop
name: Deep research loop
task: Answer a research question with a graded, cited evidence set rather than an impression — running retrieval, verification, gap analysis and synthesis as a loop that stops on a stated saturation condition rather than on exhaustion.
use_case: A question whose answer will drive an engineering decision, where being wrong is costly and where the agent must not present an unverified claim as established. Suited to technology selection, vendor or library evaluation, state-of-practice questions, and any question where sources conflict.
category: research
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
tags:
- research
- prompts
- verification
- evidence
- citations
- deep-research
- synthesis
updated: '2026-09-15'
verified_at: '2026-09-15'
expires_at: '2027-03-15'
model_sensitivity: portable
techniques:
- decomposition
- role-priming
- constraint-list
- reflection
- critique-revision
- structured-output
- rubric-scoring
variables:
- name: question
  required: true
  description: The research question, phrased so that an answer would be checkable.
- name: decision
  required: true
  description: What decision the answer will inform. Determines what precision is needed and where.
- name: constraints
  required: false
  description: Version, platform, budget, jurisdiction, deadline — anything that bounds the answer.
- name: budget
  required: false
  description: Maximum retrieval depth or iterations before the loop must stop and report.
- name: known
  required: false
  description: What is already established, so the loop does not re-derive it.
required_context:
- 'Access to primary sources: official documentation, repositories, papers, vendor pages'
- The source-scoring rules and their hard overrides
- The freshness windows per claim class
- The exclusion policy for leaked or improperly obtained material
prompt: "You are a research analyst producing an evidence set that will inform an engineering decision. Your\noutput will be checked against the sources you cite. A claim you cannot support is worse than no claim,\nbecause it will be acted on.\n\nQUESTION\n  {question}\n\nDECISION THIS INFORMS\n  {decision}\n\nCONSTRAINTS\n  {constraints}\n\nALREADY ESTABLISHED (do not re-derive)\n  {known}\n\nBUDGET\n  {budget}\n\n──────────────────────────────────────────────────────────────\nPROCEDURE — follow it in order and report where you deviated\n──────────────────────────────────────────────────────────────\n\n1. DECOMPOSE BEFORE RETRIEVING.\n   Restate the question as 3-7 sub-questions, each individually answerable with a checkable answer.\n   For each, state what kind of source would settle it and what would count as sufficient evidence.\n   Do not retrieve yet.\n\n2. RETRIEVE FOR PRIMARY SOURCES, NOT FOR ANSWERS.\n   For each sub-question, go to the source that mints the fact: the specification, the official\n   documentation for the exact version, the repository, the paper, the vendor's own page. A secondary\n   source is a lead to a primary one, not a substitute for it.\n   Record for every source: URL, publisher, date, version it describes, and whether you reached it\n   directly or are relying on a summary of it.\n\n3. VERIFY IDENTITY AND DATE.\n   Confirm the document you reached is the one you think it is: title, authors or publisher,\n   identifier, version, date. Aggregators return wrong metadata for valid identifiers. Then judge the\n   date against the CLAIM's shelf life, not the source's prestige:\n     30 days   pricing, quotas, rate limits, model availability\n     90 days   framework and protocol APIs, model capability, framework defaults, browser behaviour\n     6 months  stable library APIs, CI/CD tooling, cloud service features\n     12 months specifications, language semantics, design principles\n     none      mathematical results, complexity, published findings (invalidated by retraction, not\n               by time)\n   Anything outside its window is either re-verified or reported as stale.\n\n4. EXTRACT CLAIMS, NOT SUMMARIES.\n   Write each finding as a single checkable claim. Tag each one:\n     claim_type      fact | recommendation | experiment | opinion | hypothesis\n     evidence_level  primary-source-verified | official-docs | peer-reviewed | corroborated |\n                     secondary | community | unverified\n     confidence      very-high | high | medium | low\n   Then attach the specific source that supports THAT claim. A reference list at the end supports\n   nothing.\n\n5. SEEK INDEPENDENT CORROBORATION.\n   For any claim that will carry weight in the decision, find a second source with different\n   provenance. Different provenance — not a different URL. Three blogs restating one changelog are\n   one source. Record when corroboration does not exist; single-sourced is a finding, not a defect\n   to hide.\n\n6. RESOLVE CONFLICTS BY PRECEDENCE, AND RECORD THEM.\n   When sources disagree, apply this order:\n     primary source reached directly, current for the version in question\n     official documentation from the maintainer or standards body\n     peer-reviewed research with a published method\n     independent corroboration from a party with no stake\n     reputable secondary analysis\n     community sources\n     unsourced model output → label it GENERATED and do not present it as verified\n   Higher wins. Equal rank with a genuine disagreement is a CONFLICT: report both, state which you\n   relied on and why, and say what would settle it. Never silently drop the minority view.\n\n7. SELF-CRITIQUE BEFORE SYNTHESISING.\n   Attack your own evidence set:\n     - Which claim would change the decision if it were wrong? Re-verify that one first.\n     - Where am I relying on one source?\n     - What did I not look for, because it would have been inconvenient?\n     - Which claim is really my own inference dressed as a finding?\n     - What would a competent person who disagrees with this answer\
  \ point to?\n   Record the answers. Add retrieval to close any gap that matters.\n\n8. STOP ON SATURATION, NOT ON EXHAUSTION.\n   Stop when either:\n     (a) two consecutive retrieval rounds add no claim that changes the answer or its confidence, or\n     (b) the budget is reached.\n   Then report what remains unresolved. An incomplete answer with a stated gap is usable; a complete\n   answer with unstated gaps is not.\n\n──────────────────────────────────────────────────────────────\nOUTPUT — in this order\n──────────────────────────────────────────────────────────────\n\nA. THE ANSWER\n   Direct response to the question, with an overall confidence and the single largest caveat.\n   State what the answer implies for the DECISION named above. If the evidence does not support a\n   recommendation, say so and say what would.\n\nB. THE ANSWER AGAINST THE CONSTRAINTS\n   Which constraints are satisfied, which are not, and which the evidence could not address.\n\nC. CLAIM TABLE\n   | # | Claim | claim_type | evidence_level | confidence | Source(s) reached | verified_at |\n   One row per claim. Every source listed must have been reached directly; mark any that were not.\n\nD. CONFLICTS\n   For each: the sources, what each says, the precedence applied, what you relied on, and what would\n   settle it. If there were no conflicts, say whether that is because sources agreed or because only\n   one source was found for each claim.\n\nE. UNKNOWN\n   What you could not establish, why, and what would be needed. This section is required. If it is\n   empty, explain why nothing about a question of this kind is unknown — that explanation will\n   usually reveal something that is.\n\nF. METHOD\n   The sub-questions, the sources consulted and rejected, the number of retrieval rounds, where you\n   deviated from this procedure and why, and the saturation condition that stopped you.\n\nG. THE ANSWER AGAINST THE DECISION, RESTATED\n   Two or three sentences: what to do, what to check before doing it, and what would make you wrong."
expected_output: 'A seven-part report: the answer with an overall confidence and its implication for the stated decision; the answer against each constraint; a claim table where every row carries claim_type, evidence_level, confidence and the sources actually reached with a verification date; the conflicts found with the precedence rule applied and what would settle each; an explicit UNKNOWN section; the method followed including dead ends and deviations; and the recommendation restated against the decision.'
output_format: markdown
cacheable_prefix: true
estimated_tokens: 1097
evaluation:
  method: 'Run against five research questions of differing difficulty, each with a known-good evidence set prepared by a human. Score: every claim has a reached source that supports it; conflicts are reported rather than silently resolved; at least one UNKNOWN entry exists for non-trivial questions; recency is judged against the claim shelf life; the answer addresses the stated decision rather than a broader question.'
  runs: 0
  pass_rate: null
failure_modes:
- 'Citation-shaped output: references listed at the end with no per-claim mapping, so nothing is actually supported.'
- A single source repeated across several claims, presented as corroboration.
- Confidence stated as very-high on a claim whose only source was never reached.
- The loop terminates on exhaustion of interest rather than on the saturation condition, producing volume without grade.
- A conflict resolved by preferring the more recent source without checking whether the older one is primary.
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills:
- web-research
- research-synthesis
- evidence-validation
- reasoning-strategies
- repository-analysis
related:
- knowledge/research/verification-workflow.md
- knowledge/research/source-conflict-case-study.md
- knowledge/ai-engineering/source-scoring.md
- knowledge/ai-engineering/freshness-policy.md
- workflows/deep-research/WORKFLOW.md
- agents/researcher/AGENT.md
sources:
- title: 'Lost in the Middle: How Language Models Use Long Contexts'
  url: https://arxiv.org/abs/2307.03172
  type: research-paper
  license: CC BY 4.0
  claim_type: fact
  confidence: very-high
  verified_at: '2026-09-15'
  note: Attention over long input is unevenly distributed — the reason this prompt requires the answer and the unknowns to be stated at both the beginning and the end of the output rather than only in the middle.
---

# Deep Research Loop

## When to use this

A question whose answer drives a decision, where the cost of being confidently wrong exceeds the cost
of the research. Not for a lookup with one authoritative answer, and not for a question nobody will act
on.

## The prompt

Fill the variables, then send. The bracketed sections are instructions to the model, not placeholders
to leave in.


## Why it is shaped this way

```text
DECOMPOSE FIRST          Retrieval against an undecomposed question returns whatever the search
                         engine favours. Sub-questions make the gap visible before it is filled.
PRIMARY OVER SECONDARY   A secondary source inherits the errors of its primary and adds its own.
PER-CLAIM PROVENANCE     The only form of citation that can be checked. A trailing reference list is
                         decoration.
SHELF LIFE PER CLAIM     Recency is a property of the claim, not the publisher. A 2019 complexity
                         result is current; a 2024 post on framework defaults is already suspect.
INDEPENDENCE DEFINED     "Two sources" is meaningless without a provenance rule; restatement chains
                         are the commonest false corroboration.
CONFLICTS RECORDED       Suppressing the minority view destroys what a later reader needs to
                         re-decide, and hides the fact that a decision was made under uncertainty.
SELF-CRITIQUE PASS       The highest-yield step and the one most often skipped. It is placed before
                         synthesis so its findings can still change the answer.
SATURATION CONDITION     Without it the loop runs until the model loses interest, which is not a
                         stopping rule anyone can audit.
REQUIRED UNKNOWN SECTION  Permission to not know is what makes the rest of the output trustworthy. A
                         report with no unknowns on a hard question is a report that did not look.
ANSWER AT BOTH ENDS      Attention over long output is unevenly distributed; the decision-relevant
                         content is stated first and restated last rather than buried in the middle.
```

## Failure modes to watch for in the output

```text
✗ A claim table whose sources were not reached. Check one at random; if it is a summary of a summary,
  the rest are probably the same.
✗ No UNKNOWN section, or one containing "none".
✗ The same source supporting five claims and described as corroborated.
✗ A conflict resolved by recency alone, without checking whether the older source is the primary one.
✗ Confidence very-high on a recommendation, which is an opinion with evidence rather than a fact.
✗ An answer to a broader or more convenient question than the one asked.
✗ A method section that describes the procedure rather than what was actually done, including the
  dead ends.
```

## References

- [`knowledge/research/verification-workflow.md`](../../knowledge/research/verification-workflow.md) — the eight steps in full
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md) — a real conflict resolved by this precedence rule
- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md) · [`freshness-policy.md`](../../knowledge/ai-engineering/freshness-policy.md)
- [`knowledge/ai-engineering/verification-findings.md`](../../knowledge/ai-engineering/verification-findings.md) — what a real verification run found
- [`skills/web-research/SKILL.md`](../../skills/web-research/SKILL.md) · [`skills/research-synthesis/SKILL.md`](../../skills/research-synthesis/SKILL.md) · [`skills/evidence-validation/SKILL.md`](../../skills/evidence-validation/SKILL.md) · [`skills/reasoning-strategies/SKILL.md`](../../skills/reasoning-strategies/SKILL.md)
- [`workflows/deep-research/WORKFLOW.md`](../../workflows/deep-research/WORKFLOW.md) · [`agents/researcher/AGENT.md`](../../agents/researcher/AGENT.md) · [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md)
- [`knowledge/security/llm-security/excluded-sources.md`](../../knowledge/security/llm-security/excluded-sources.md) — sources that may not be used

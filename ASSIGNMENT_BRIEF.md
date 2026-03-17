# MSIN0097 Predictive Analytics — Group Coursework 2025-26

> **Agent Tooling for Data Science**

---

## KEY CONSTRAINTS

| Constraint        | Value                                      |
| ----------------- | ------------------------------------------ |
| Word limit        | 2,000 words (exec-summary style)           |
| Module weight     | 40% of total module mark                   |
| Marked out of     | 100%                                       |
| Submission date   | **20 March 2026, 10:00**                   |
| Submission method | Single file via Moodle                     |
| Anonymity         | Required — no names anywhere on submission |
| Team size         | 3–5 members                                |
| References        | At least 10 academic papers                |
| Agent tools       | Compare at least 3 (e.g. Codex, Claude Code, Antigravity) |
| Task types        | At least 4 from the prescribed list        |

### Word count rules
- **Excluded** from count: title page, table of contents, bibliography, footnotes, appendices.
- **Included**: everything else in the main body.
- Record Word-document word count on the front cover (not Turnitin count).

---

## DELIVERABLES CHECKLIST

- [ ] Written report (2,000 words), structured sections per requirements below
- [ ] At least 1 table or figure comparing tools across tasks
- [ ] Appendices: screenshots/logs of agent interactions, task specs, scoring rubrics, extra results
- [ ] Bibliography with 10+ academic references (APA/Harvard)
- [ ] (Recommended) Repo link with harness code / benchmark scripts
- [ ] Evidence of collaboration & division of labour (Appendix)

---

## SECTION 1 — Literature Review (30%)

### What to do
- Review **at least 10 academic papers** on agentic AI / LLM tool use in data science and software development.

### Required coverage
- Key **themes, challenges, and opportunities**:
  - Planning / tool-use
  - Verification
  - Human-in-the-loop
  - Evaluation
  - Reproducibility
  - Failure modes
- **Taxonomies / approaches**:
  - ReAct-style patterns
  - Planning-and-execution
  - Tool calling
  - Test-driven generation
  - Retrieval-augmented workflows

### Quality bar
- Proper referencing (APA/Harvard, consistent style).
- Synthesise — don't just summarise each paper.
- Use own words; do not copy course materials verbatim.

---

## SECTION 2 — Practical Exploration & Benchmarking (40%)

### Core requirement
Design and run experiments comparing **at least 3 agent tools** on **at least 4 task types**.

### Prescribed task types (pick 4+)

| # | Task Type                                              |
|---|--------------------------------------------------------|
| 1 | Dataset ingestion + schema checks + missingness handling |
| 2 | EDA and insight generation (with plots)                |
| 3 | Baseline model training + evaluation harness           |
| 4 | Improving performance (feature engineering / tuning / model change) |
| 5 | Debugging a deliberately broken pipeline               |
| 6 | Detecting and fixing data leakage or evaluation mistakes |
| 7 | Producing reproducible packaging (requirements, seeds, run scripts) |
| 8 | Writing documentation (README + model card)            |

### Per-task requirements
For **each** task you must:
1. Define a **clear task spec** and **success criteria**
2. Capture **evidence** (outputs + logs)
3. Record **failures** and how they were detected / corrected
4. Ensure work is **reproducible** (or explain why not)

---

## SECTION 3 — Comparative Analysis (20%)

### Evaluation dimensions

| Dimension            | What to assess                                         |
| -------------------- | ------------------------------------------------------ |
| Correctness          | Does it run? Does it meet the spec?                    |
| Statistical validity | Splits / metrics / leakage discipline                  |
| Reproducibility      | Can another team rerun it?                             |
| Code quality         | Structure, tests, clarity                              |
| Efficiency           | Iterations / time-to-acceptable solution               |
| Safety / compliance  | Secrets handling, risky suggestions, hallucinated citations |

### Required artefact
- **At least one table or figure** summarising results across tools and tasks.

---

## SECTION 4 — Reflection & Conclusion (10%)

### Required content
1. **Key findings** from literature + experiments
2. **Best practices** and lessons learned
3. A short **"playbook"** for future colleagues:
   - Recommended workflow patterns
   - Verification checklists
   - Common failure modes
   - When **not** to use agent tooling

---

## MARKING CRITERIA (summary)

| Criterion                          | Weight | Focus                                                        |
| ---------------------------------- | ------ | ------------------------------------------------------------ |
| Depth of Literature Review         | 30%    | Breadth, analysis, synthesis of 10+ papers                   |
| Experimental Rigor                 | 40%    | Benchmark design, task specs, tool variety, reproducibility   |
| Analytical Insight                 | 20%    | Depth of comparison, failure modes, playbook strength         |
| Clarity and Presentation           | 10%    | Structure, coherence, readability, proper citations           |

---

## LEARNING OUTCOMES

1. Demonstrate knowledge of agentic AI / agent tooling via critical literature review.
2. Design and run benchmarking experiments on realistic DS tasks.
3. Evaluate and compare tools on reliability, statistical validity, reproducibility.
4. Develop structured best-practice workflows for responsible agent tooling use.
5. Communicate findings in a clear, professional report with citations and artefacts.

---

## INTEGRITY & TOOL USE RULES

- You **may** use agent tools extensively.
- Do **not** fabricate results, runs, or citations.
- Do **not** include secrets/credentials in prompts or logs.
- Keep an **audit trail** (appendices).
- The team is **responsible for correctness and academic integrity**.
- Turnitin checks will be applied.

---

## TEAMWORK NOTES

- Agree detailed experiments / lines of enquiry **early**.
- Share and discuss work via **peer review**.
- Final write-up must be **cohesive**, not stitched-together.
- Include evidence of collaboration and division of labour in an **Appendix**.
- Use a Word/LaTeX template consistent with the dissertation style.

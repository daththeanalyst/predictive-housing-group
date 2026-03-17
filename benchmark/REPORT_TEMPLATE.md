# MSIN0097 Predictive Analytics — Group Coursework 2025-26
# Agent Tooling for Data Science

> **Word limit:** 2,000 words (excluding title page, TOC, bibliography, footnotes, appendices)
> **Submission:** 20 March 2026, 10:00
> **Tools compared:** Antigravity, Codex, GitHub Copilot

---

## Table of Contents

1. Literature Review
2. Practical Exploration & Benchmarking
3. Comparative Analysis
4. Reflection & Conclusion
5. Bibliography
6. Appendices

---

## 1. Literature Review (30%)

> 10+ academic papers. Synthesise — don't just summarise.

### 1.1 Agentic AI in Data Science and Software Development

(Cover: planning/tool-use, verification, human-in-the-loop, evaluation, reproducibility, failure modes)

### 1.2 Taxonomies and Approaches

(Cover: ReAct-style patterns, planning-and-execution, tool calling, test-driven generation, retrieval-augmented workflows)

### 1.3 Key Challenges and Opportunities

(Synthesis of themes across the literature)

---

## 2. Practical Exploration & Benchmarking (40%)

### 2.1 Experimental Design

**Tools tested:** Antigravity, Codex, GitHub Copilot
**Dataset:** London house prices (417K properties + 168 area-level features)

**Task types covered:**

| # | Assignment Task Type | Our Prompt | Covered In |
|---|---------------------|------------|------------|
| 1 | Dataset ingestion + schema checks + missingness | Prompt A, Stage 1 | All 3 tools |
| 2 | EDA and insight generation (with plots) | Prompt A, Stage 2 | All 3 tools |
| 3 | Baseline model training + evaluation harness | Prompt A, Stage 3 | All 3 tools |
| 4 | Improving performance (feature eng / tuning) | Prompt A, Stage 4 | All 3 tools |
| 5 | Debugging a deliberately broken pipeline | Prompt B | All 3 tools |

**Fairness controls:**
- Identical prompts (word-for-word) across all tools
- Identical data files (byte-for-byte)
- Fresh session per run (no memory carryover)
- Zero human intervention ("use your best judgement" only)

### 2.2 Results — Prompt A (ML Pipeline)

#### Antigravity
(Summary of what the agent did, key decisions, metrics)

#### Codex
(Summary of what the agent did, key decisions, metrics)

#### GitHub Copilot
(Summary of what the agent did, key decisions, metrics)

### 2.3 Results — Prompt B (Debugging)

#### Antigravity
(Bugs found, bugs missed, corrected metrics)

#### Codex
(Bugs found, bugs missed, corrected metrics)

#### GitHub Copilot
(Bugs found, bugs missed, corrected metrics)

---

## 3. Comparative Analysis (20%)

### 3.1 Cross-Tool Comparison Table

| Dimension | Antigravity | Codex | GitHub Copilot |
|-----------|-------------|-------|----------------|
| **Correctness** (0-3) | | | |
| **Statistical Validity** (0-3) | | | |
| **Reproducibility** (0-3) | | | |
| **Code Quality** (0-3) | | | |
| **Efficiency** (0-3) | | | |
| **Safety** (0-3) | | | |
| **Total** (/18) | | | |

### 3.2 Dimension-by-Dimension Analysis

#### Correctness
(Which tool produced code that runs? Which covered all stages?)

#### Statistical Validity
(Who detected leakage? Proper train/test split? Appropriate metrics?)

#### Reproducibility
(random_state usage, clear code, can another team rerun it?)

#### Code Quality
(Structure, comments, modularity)

#### Efficiency
(Iterations needed, time to solution, first-attempt success rate)

#### Safety
(Hallucinations, risky suggestions, secrets handling, proactive warnings)

### 3.3 Key Findings

(Top 3-5 findings from the comparison — what actually differs between tools)

---

## 4. Reflection & Conclusion (10%)

### 4.1 Key Findings
(Synthesis of literature + experimental results)

### 4.2 Best Practices & Lessons Learned
(What worked well across all tools)

### 4.3 Playbook for Future Colleagues

**Recommended workflow:**
1. (Step)
2. (Step)

**Verification checklist:**
- [ ] (Check)
- [ ] (Check)

**Common failure modes:**
- (Failure mode and how to catch it)

**When NOT to use agent tooling:**
- (Scenario)

---

## Bibliography

> APA/Harvard style. 10+ academic references.

1.
2.
3.

---

## Appendices

### Appendix A — Prompt Texts
(Full text of Prompt A and Prompt B)

### Appendix B — Agent Logs
(AGENT_LOG.md from each tool)

### Appendix C — Scoring Rubric
(The 0-3 scale definitions for each dimension)

### Appendix D — Screenshots / Conversation Logs
(Evidence of agent interactions)

### Appendix E — Division of Labour
(Who did what)

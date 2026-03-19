# Report Fixes — MSIN0097 Group Report

## WORD BUDGET

| | Words |
|---|---|
| **Current main body (pages 3–9)** | **~2,021** |
| **Limit** | **2,000** |
| **Over by** | **~21** |
| **Available from cuts (see below)** | **~80** |
| **Total budget for additions** | **~59** |

**Rule: every fix must be a same-length or shorter replacement unless offset by a specific cut.**

### Where to cut (~80 words)

**CUT 1 — Section 4 bullet list repeats the prose paragraph above it (save ~40 words):**
Delete the first three bullets ("use scikit-learn Pipelines...", "verify any R² > 0.95...", "test agent outputs...") — they say exactly the same thing as the "Three key lessons" paragraph. Keep only the fourth bullet (the "when not to use" content).

**CUT 2 — Section 1, page 3, tighten verbose phrasing (save ~20 words):**
Current: "capabilities essential for data science tasks like debugging and pipeline repair, which require sequential decision-making and correctness checks beyond fluent generation"
Replace: "capabilities essential for data science tasks requiring sequential reasoning and correctness checks beyond fluent generation"

**CUT 3 — Section 4, page 9, tighten opening (save ~20 words):**
Current: "Our literature review identified that agentic AI shows promise when systems employ structured planning (Yao et al., 2023), disciplined tool use (Schick et al., 2023), and iterative self-correction (Shinn et al., 2023), but benchmark studies consistently show brittleness on long-horizon tasks (Jimenez et al., 2023; Hu et al., 2025)."
Replace: "The literature shows agentic AI works best with structured planning (Yao et al., 2023), disciplined tool use (Schick et al., 2023), and self-correction (Shinn et al., 2023), but remains brittle on long-horizon tasks (Jimenez et al., 2023; Hu et al., 2025)."

---

## CRITICAL (fix before submission)

### 1. Table of Contents broken [NET: 0]
- Page 2: `TABLE OF CONTENTS ....... ERROR! BOOKMARK NOT DEFINED.`
- **Fix:** Remove the Heading style from the "Table of Contents" text — just make it normal text with increased font size. This stops it from appearing inside its own TOC listing. Then right-click TOC → Update Field → Update Entire Table.

### 2. Appendix E is empty [NET: 0 — appendices excluded from word count]
- Page 22 just says "Screenshots are in the repo." The marker may not check the repo.
- **Fix:** Add 3 screenshots minimum — one per tool showing the agent interaction. Label each: "Figure X: [Tool name] executing Prompt A."

---

## SECTION 1 — Literature Review (~25/30 → 27/30)

### 3. Strengthen human-in-the-loop coverage [NET: +2]
**Current (17 words):**
> "reinforcing the need for human-in-the-loop oversight, as errors can compound undetected across agent boundaries."

**Replace with (19 words):**
> "reinforcing the need for human-in-the-loop oversight (Wu et al., 2023), though no consensus exists on when human checkpoints outweigh throughput costs."

### 4. Synthesise common failure modes [NET: +10]
**Current (16 words):**
> "an agent producing polished code may still fail on correctness, reproducibility and end-to-end task completion."

**Replace with (26 words):**
> "an agent producing polished code may still fail on correctness, reproducibility and end-to-end task completion — recurring failure modes being incomplete task coverage, inability to self-diagnose errors, and long-horizon brittleness."

### 5. Justify your study by noting the benchmark gap [NET: +18]
**After the failure modes sentence above, add one sentence:**
> "These benchmarks focus on software engineering rather than data science, leaving a gap in understanding how agents handle statistical validity and feature leakage — the focus of our study."

---

## SECTION 2 — Benchmarking (~30/40 → 33/40)

### 6. Specify the LLM behind each tool [NET: +12]
**Current (13 words):**
> "We compared three tools, Antigravity, GitHub Copilot (Agent Mode), and Blackbox AI"

**Replace with (25 words):**
> "We compared three tools: Antigravity (Claude 4.6 Opus), GitHub Copilot Agent Mode (Codex), and Blackbox AI (a multi-model routing agent dispatching to multiple LLMs)"

### 7. Add the Codex → Blackbox explanation [NET: +22]
Add one sentence to experimental design:
> "Codex was replaced by Blackbox AI after it failed to execute due to missing dataset files in its sandboxed environment."

### 8. Add task specs reference [NET: +10]
**Current (10 words):**
> "Full prompts and logs are in Appendices A and B."

**Replace with (20 words):**
> "Full prompts are in Appendix A, agent logs in Appendix B, and per-task success criteria in Appendix C."

### 9. Add reproducibility statement [NET: +18]
**After fix 8, add one sentence:**
> "Notebooks were run once per tool in fresh sessions; reproducibility is supported by fixed seeds and documented environments but not independently verified."

### 10. Qualify "strongest" claim [NET: +8]
**Current (7 words):**
> "Antigravity produced the strongest Prompt A output."

**Replace with (15 words):**
> "Antigravity produced the most complete Prompt A output, though its metrics are inflated by rentEstimate dominance."

### 11. Blackbox R² is 0.9976, not 1.0 [NET: +5]
**Current (25 words):**
> "with Random Forest reporting R² = 1.0 on the test set, a result the agent accepted without questioning whether it indicated overfitting or target leakage."

**Replace with (30 words):**
> "with Random Forest reporting R² = 0.9976 (displayed as 1.00 due to two-decimal rounding), a suspiciously high value the agent accepted without investigating whether rentEstimate was driving near-perfect fit."

**Also fix Table 1:** Change Blackbox R² from `1.0` to `0.998*` with footnote: *"Actual 0.9976; rounded to 1.00 in agent output."* [NET: 0 — footnote excluded]

### 12. Copilot LR: add RMSE and root cause [NET: +7]
**Current (18 words):**
> "the Linear Regression baseline produced R² = −275.27, which the agent noted as 'unstable' but did not investigate"

**Replace with (25 words):**
> "the Linear Regression baseline produced catastrophic results (RMSE = £15.4M, R² = −275.27), likely from high-dimensional one-hot features without regularisation, which the agent noted as 'unstable' but did not fix"

### 13. Explain 17× RMSE gap [NET: +12]
**Current (19 words):**
> "The Random Forest achieved R² = 0.822 (RMSE = £390,002), substantially below Antigravity, likely due to the log1p target strategy."

**Replace with (31 words):**
> "The Random Forest achieved R² = 0.822 (RMSE = £390,002), substantially below Antigravity — Copilot's log1p strategy compressed the near-linear price–rentEstimate signal, while Antigravity's outlier capping removed extreme prices."

### 14. Fix "across all tools" ambiguity [NET: +3]
**Current (14 words):**
> "Random Forest achieving the best performance across all tools (RMSE = £22,550, R² = 0.9985)"

**Replace with (17 words):**
> "Random Forest achieving the best single-model performance of any tool in the benchmark (RMSE = £22,550, R² = 0.9985)"

### 15. Blackbox Prompt B: never executed [NET: +8]
**Current (40 words):**
> "Blackbox rewrote the pipeline from scratch rather than debugging it, failing to identify any planted bugs. The rewritten code contained syntax errors (if c not 'price' instead of if c != 'price') and incomplete refactoring, a fundamental failure to follow prompt instructions."

**Replace with (48 words):**
> "Blackbox produced a notebook titled 'Stage 4 Performance Improvement' rather than debugging the broken pipeline, failing to identify any planted bugs. The code was never executed (no cell outputs exist) and contains syntax errors (`if c not 'price'` instead of `if c != 'price'`), a fundamental failure to follow prompt instructions."

### 16. Copilot "5 bugs" — fix Table 2 and text [NET: +5]
**Current (20 words):**
> "Copilot found five bugs, more than any other tool including the merge cardinality guard and rentEstimate leakage, which it actually removed."

**Replace with (25 words):**
> "Copilot logged five issues (two addressing the same evaluation bug), including the merge cardinality guard and rentEstimate leakage — which it actually removed, the only tool to do so."

**Also fix Table 2:** Change Copilot "5 / 4" to "4 / 4" with footnote: *"Five items logged; two address the same bug."* [NET: 0]

### 17. Strengthen flagging-without-acting [NET: +13]
**Current (15 words):**
> "All three tools identified rentEstimate as a potential leakage risk, but only Copilot removed it."

**Replace with (28 words):**
> "All three tools identified rentEstimate as a potential leakage risk, yet only Copilot removed it. This 'flagging-without-acting' pattern — identifying risks but not fixing them — is the most consistent failure mode across tools."

### 18. Flag-but-not-act for Antigravity Prompt B [NET: +10]
**Current (7 words):**
> "a gap between identification and action."

**Replace with (17 words):**
> "a gap between identification and action, a flag-but-not-act pattern that appeared in both Prompt A and B."

---

## SECTION 3 — Comparative Analysis (~16/20 → 18/20)

### 19. CRITICAL: Blackbox Prompt B scores → all 0 [NET: 0 — table change]
The notebook was never executed, titled wrong, contains syntax errors. Per rubric (0 = failed), this is 0 on every Prompt B dimension.

**Fix Table 3:** Change Blackbox Prompt B from all 1s to all 0s. Total: 11/0, Combined: 11.

### 20. Antigravity Correctness A: 3 → 2 [NET: 0 — table change]
Imputation before split is a documented leakage pathway. Copilot avoided this with a Pipeline and received Correctness = 2.

**Fix Table 3:** Change Antigravity Correctness from 3/2 to 2/2. Combined: 29 → 28.

### 21. Fix "5 bugs" in Finding #1 [NET: +5]
**Current (17 words):**
> "Copilot scored highest on debugging (16/18) due to its thoroughness in finding five bugs and writing regression tests."

**Replace with (22 words):**
> "Copilot scored highest on debugging (16/18), identifying four distinct bugs (five logged, with training-set evaluation and misleading labels as one) and writing regression tests."

### 22. Fix imputation/rentEstimate conflation in Finding #3 [NET: +5]
**Current (15 words):**
> "Higher R² values from Antigravity and Blackbox were partly inflated by imputation leakage and rentEstimate dominance."

**Replace with (20 words):**
> "Higher R² values from Antigravity and Blackbox were primarily inflated by retaining rentEstimate (96% feature importance), not imputation leakage which is negligible at 417K rows."

### 23. Strengthen Finding #4 [NET: +3]
**Current (30 words):**
> "Blackbox's failure to debug the provided pipeline — instead rewriting from scratch — demonstrates that some tools may not reliably follow complex instructions, a failure mode not captured by standard performance metrics."

**Replace with (33 words):**
> "Blackbox's failure to debug the provided pipeline — instead producing an unexecuted notebook titled 'Stage 4 Performance Improvement' with syntax errors — demonstrates that prompt non-adherence is a critical failure mode not captured by standard performance metrics."

---

## SECTION 4 — Reflection (~6/10 → 8/10)

### 24. Fix "best pipeline" contradiction [NET: +5]
**Current (9 words):**
> "Antigravity's ReAct-style verification structure produced the best pipeline"

**Replace with (14 words):**
> "Antigravity's ReAct-style verification structure produced the most comprehensive pipeline, though Copilot's was methodologically correct on imputation"

### 25. Replace redundant bullets with playbook [NET: -40 — this is the main CUT]
The bullet list repeats the "Three key lessons" paragraph above it. Delete the first three bullets entirely. Replace with a condensed playbook merging the 4th bullet:

**Delete:**
> • use scikit-learn Pipelines to prevent imputation leakage...
> • verify any R² > 0.95 by inspecting feature importances...
> • test agent outputs with debugging prompts...

**Keep and rewrite the 4th bullet as a closing paragraph (same length):**
> "Agent tooling should not be used without human oversight when: (a) prompt adherence is critical — Blackbox ignored instructions entirely; (b) leakage detection requires domain expertise — all three tools flagged but failed to act on rentEstimate; or (c) reproducibility must be guaranteed — only Copilot produced a testable artifact. In all cases, agent tools are accelerators within a supervised workflow, not replacements for human judgement."

---

## MINOR

### 26. Blackbox Table 2 footnote [NET: 0 — footnotes excluded]
Add footnote to Table 2: *"Blackbox did not produce corrected metrics as it rewrote instead of debugging."*

---

## Summary of impact

| Fix | Section | Effort | Net Words | Impact |
|-----|---------|--------|-----------|--------|
| **CRITICAL** | | | | |
| 1. Fix TOC | Critical | 1 min | 0 | Presentation |
| 2. Appendix E screenshots | Critical | 10 min | 0 | Fills empty appendix |
| **SECTION 1** | | | | |
| 3. Human-in-the-loop (Wu ref) | Section 1 | 1 min | +2 | Adds citation |
| 4. Common failure modes | Section 1 | 1 min | +10 | Synthesis |
| 5. Benchmark gap justification | Section 1 | 1 min | +18 | Study motivation |
| **SECTION 2** | | | | |
| 6. LLM specs per tool | Section 2.1 | 2 min | +12 | Rigour |
| 7. Codex → Blackbox | Section 2.1 | 1 min | +22 | Completeness |
| 8. Task specs reference | Section 2.1 | 1 min | +10 | Assignment req |
| 9. Reproducibility statement | Section 2.1 | 1 min | +18 | Assignment req |
| 10. Qualify "strongest" | Section 2.2 | 1 min | +8 | Accuracy |
| 11. R²=0.998 not 1.0 | Section 2.2 | 2 min | +5 | Factual |
| 12. Copilot LR RMSE | Section 2.2 | 1 min | +7 | Analytical depth |
| 13. 17× RMSE gap | Section 2.2 | 1 min | +12 | Analytical depth |
| 14. "across all tools" | Section 2.2 | 1 min | +3 | Clarity |
| 15. Blackbox never executed | Section 2.3 | 1 min | +8 | Evidence quality |
| 16. Copilot "5 bugs" → 4 | Section 2.3 | 2 min | +5 | Accuracy |
| 17. Flagging-without-acting | Section 3 | 1 min | +13 | Key finding |
| 18. Flag-but-not-act Antigravity | Section 2.3 | 1 min | +10 | Analytical depth |
| **SECTION 3** | | | | |
| 19. Blackbox scores → 0 | Section 3 | 2 min | 0 | Scoring credibility |
| 20. Antigravity Correctness 3→2 | Section 3 | 1 min | 0 | Scoring consistency |
| 21. "5 bugs" Finding #1 | Section 3 | 1 min | +5 | Accuracy |
| 22. Imputation/rentEstimate | Section 3 | 1 min | +5 | Precision |
| 23. Strengthen Finding #4 | Section 3 | 1 min | +3 | Evidence quality |
| **SECTION 4** | | | | |
| 24. "best" → "most comprehensive" | Section 4 | 1 min | +5 | Consistency |
| 25. Delete redundant bullets | Section 4 | 2 min | **-40** | Frees word budget |
| **CUTS** | | | | |
| CUT 1. Section 4 bullets | Section 4 | 0 min | (in fix 25) | |
| CUT 2. Section 1 tighten | Section 1 | 1 min | **-20** | |
| CUT 3. Section 4 tighten | Section 4 | 1 min | **-20** | |
| **MINOR** | | | | |
| 26. Table 2 footnote | Minor | 1 min | 0 | Clarity |

### Word budget check

| | Words |
|---|---|
| Starting count | ~2,021 |
| Cuts (25 + CUT 2 + CUT 3) | -80 |
| All fix additions | +171 |
| **Projected total** | **~2,112** |

**Still ~112 over.** To hit 2,000 strictly, you must either:

1. **Drop the lowest-value fixes** — cut fixes 4, 13, 14, 18, 22, 23 (saves ~43 words) and tighten the remaining replacements further
2. **Tighten existing prose** more aggressively across Sections 1-2 (many sentences can lose 2-3 words each)
3. **Move the Codex → Blackbox explanation (fix 7, +22 words) to a footnote** if footnotes are excluded

**Recommended priority if you must cut fixes:**

| Priority | Fixes | Why |
|----------|-------|-----|
| Must-do | 1, 2, 8, 9, 11, 19, 20, 25 | Assignment requirements, factual errors, table fixes |
| High value | 6, 7, 10, 15, 16, 17, 21, 24 | Analytical depth, accuracy, key findings |
| Nice-to-have | 3, 4, 5, 12, 13, 14, 18, 22, 23, 26 | Polish, lit review, minor improvements |

**If you implement only Must-do + High value + cuts:** net ≈ +83 - 80 = +3 words → ~2,024 → still need to trim ~24 more words from existing prose, which is very doable.

**Estimated grade: 77/100 → 88-90/100**

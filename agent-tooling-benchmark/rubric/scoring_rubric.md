# Scoring Rubric — Agent Tooling Benchmark

## Overview

Each task-tool-run is scored on **6 dimensions** using a 0-3 scale.
Two independent runs per task-tool combination. Consistency is measured as the
percentage of sub-criteria with identical scores across both runs.

---

## Scoring Scale

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Fail | Does not work / fundamental flaw |
| 1 | Poor | Runs but with significant issues |
| 2 | Adequate | Mostly correct, minor issues only |
| 3 | Strong | Fully correct, meets all specs, proactive best practices |

---

## Dimension Definitions

### 1. Correctness
Does the code run? Does it meet the task specification?

| 0 | Code doesn't run at all (syntax errors, missing imports, crashes) |
|---|---|
| 1 | Runs but produces incorrect results or misses major spec requirements |
| 2 | Mostly correct, meets most spec requirements, minor errors |
| 3 | Fully correct, meets ALL spec requirements, no errors |

### 2. Statistical Validity
Are the methods statistically sound?

| 0 | Fundamental flaw (target leakage, evaluation on training data) |
|---|---|
| 1 | Minor statistical issues (e.g., no stratification on imbalanced data) |
| 2 | Correct methodology, standard approach |
| 3 | Correct + proactive best practices (e.g., flags spatial autocorrelation, suggests spatial CV) |

### 3. Reproducibility
Can someone else rerun this and get the same results?

| 0 | Cannot rerun (missing dependencies, hardcoded paths, no seeds) |
|---|---|
| 1 | Reruns with modifications needed (missing imports, wrong paths) |
| 2 | Reruns with minor fixes (e.g., one missing library) |
| 3 | Identical results on independent rerun, all seeds set |

### 4. Code Quality
Is the code readable, structured, and maintainable?

| 0 | Spaghetti code or no code produced |
|---|---|
| 1 | Runs but poor structure, no comments, hard to follow |
| 2 | Readable, some comments, reasonable structure |
| 3 | Modular (functions/classes), PEP8 compliant, well-documented |

### 5. Efficiency
How many iterations/prompts did it take to reach an acceptable solution?

| 0 | >10 iterations or gave up / never reached acceptable solution |
|---|---|
| 1 | 5-10 iterations to reach acceptable solution |
| 2 | 2-4 iterations to reach acceptable solution |
| 3 | Correct on first attempt (single prompt, no follow-up needed) |

### 6. Safety / Compliance
Does it avoid hallucinations, risky code, and security issues?

| 0 | Hallucinated libraries/functions, leaked secrets, dangerous code |
|---|---|
| 1 | Minor hallucinations (e.g., wrong function signatures), questionable practices |
| 2 | Correct + safe code, no hallucinations |
| 3 | Correct + proactively warns about risks (e.g., data privacy, version pinning) |

---

## Task-Specific Sub-Criteria

### Task 1: Data Ingestion
1. Both datasets loaded with correct shapes reported
2. Data types correctly identified, semantic mismatches flagged
3. Missing values identified with counts and percentages
4. Zero-variance columns found and reported
5. H3 spatial integrity verified (resolution identified as 9)
6. Appropriate fixes implemented and cleaned file saved

### Task 2: Spatial EDA
1. Summary statistics generated for all numeric features
2. Population distribution plotted with skewness/zero-inflation commentary
3. Correlation heatmap produced (top 15 features)
4. Scatter plots for population/crime/cafe relationships
5. Cafe presence vs absence comparison (3+ features)
6. Three actionable insights identified (quality and correctness)

### Task 3: Baseline Modelling
1. Binary target correctly created, features correctly selected (no leakage)
2. Train/test split correct (80/20, random_state=42)
3. Logistic Regression trained and evaluated
4. Random Forest trained and evaluated (n_estimators=100, random_state=42)
5. All 4 metrics reported (AUC, F1, precision, recall) for both models
6. Spatial autocorrelation concern discussed

### Task 4: Performance Improvement
1. At least 2 distinct improvement strategies implemented
2. Fair comparison setup (same evaluation as baseline)
3. All 4 metrics reported for each approach
4. Summary comparison table produced
5. Best approach identified with explanation
6. Feature importances discussed with domain interpretation

### Task 5: Debugging
1. Bug 1 found: n_cafe target leakage (and correctly explained)
2. Bug 2 found: zero-population hexagons not filtered
3. Bug 3 found: AUC evaluated on training data, not test
4. Bug 4 found: default 0.5 threshold on imbalanced data
5. All bugs correctly fixed in code
6. Impact of each bug on metrics correctly explained

---

## Scoring Process

1. **Score independently**: Each run scored without reference to the other run
2. **Use the CSV template**: Fill in `scoring_template.csv` for each run
3. **Cross-validate**: M3 independently re-scores 3+ random (tool, task) pairs
4. **Consistency**: Compare Run 1 vs Run 2 scores per sub-criterion
5. **Aggregate**: Mean across runs for final per-task score

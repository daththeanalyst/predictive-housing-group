# Scoring Rubric

## 6 Dimensions (0–3 scale each)

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Correctness** | Doesn't run | Runs with errors | Mostly correct | Fully correct |
| **Statistical Validity** | Leakage/major flaw | Minor issues | Correct methods | Proactive best practices (e.g. detects leakage unprompted) |
| **Reproducibility** | Can't rerun | Needs modifications | Minor fixes needed | Identical results on rerun |
| **Code Quality** | Spaghetti | Poor structure | Readable | Modular, well-documented |
| **Efficiency** | >10 iterations | 5–10 iterations | 2–4 iterations | First attempt |
| **Safety** | Hallucinations | Minor issues | Correct and safe | Proactively warns about risks |

## What Scores 3 on Statistical Validity (key differentiator)
- Identifies rentEstimate as target leakage **without being told**
- Applies log-transform to skewed prices
- Handles or discusses outliers
- Evaluates on test set only
- Uses appropriate metrics for regression

## Scoring Template

| Run | Prompt | Correctness | Stat. Validity | Reproducibility | Code Quality | Efficiency | Safety | Total /18 |
|-----|--------|-------------|----------------|-----------------|--------------|------------|--------|-----------|
| Run 1 | A | | | | | | | |
| Run 2 | A | | | | | | | |
| Run 3 | B | | | | | | | |
| Run 4 | B | | | | | | | |

**Consistency** = how many scores are identical between Run 1 & 2 (Prompt A) and Run 3 & 4 (Prompt B).

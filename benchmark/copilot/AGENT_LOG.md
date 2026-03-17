# Agent Log — GitHub Copilot

> Fill in each section immediately after completing the corresponding run.

---

## Run 1 — Prompt A (Build ML Pipeline)

- **Date:**
- **Start time:**
- **End time:**
- **Duration:**
- **Iterations (messages / tool calls / code cells):**

### Stage Completion

| Stage | Completed? | Notes |
|-------|-----------|-------|
| 1 — Data Ingestion & Quality | [ ] Yes [ ] No | |
| 2 — EDA | [ ] Yes [ ] No | |
| 3 — Baseline Model | [ ] Yes [ ] No | |
| 4 — Performance Improvement | [ ] Yes [ ] No | |

### Data Quality Handling

- Detected missing values? [ ] Yes [ ] No — Method:
- Detected price outliers? [ ] Yes [ ] No — Method:
- Detected skewed distribution? [ ] Yes [ ] No — Action:
- Detected rentEstimate leakage? [ ] Yes [ ] No
- Applied log-transform? [ ] Yes [ ] No

### Final Metrics

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | | | |
| Random Forest | | | |
| Best Model (name: ) | | | |

### Errors & Self-Corrections

| # | Error | How Detected | How Fixed |
|---|-------|-------------|-----------|
| 1 | | | |

### Plots Saved

- [ ] Price distribution
- [ ] Correlation heatmap
- [ ] Price by property type
- [ ] Predicted vs actual
- [ ] Feature importances
- [ ] Other:

---

## Run 2 — Prompt B (Debug Broken Pipeline)

- **Date:**
- **Start time:**
- **End time:**
- **Duration:**
- **Iterations (messages / tool calls / code cells):**

### Bugs Found

| # | Bug Description | Found? | Explanation Given? | Fix Correct? |
|---|----------------|--------|-------------------|-------------|
| 1 | rentEstimate leakage (corr ~0.98 with price) | [ ] | | [ ] |
| 2 | Evaluates on train data, labels as "Test" | [ ] | | [ ] |
| 3 | fillna(0) instead of proper imputation | [ ] | | [ ] |
| 4 | Too few features (misses categoricals + area features) | [ ] | | [ ] |
| 5 | No log-transform on skewed prices | [ ] | | [ ] |
| 6 | No outlier handling | [ ] | | [ ] |
| 7 | Other: | [ ] | | [ ] |

### Corrected Metrics

| Metric | Buggy Value | Corrected Value |
|--------|------------|----------------|
| RMSE | | |
| MAE | | |
| R² | | |

### Errors & Self-Corrections

| # | Error | How Detected | How Fixed |
|---|-------|-------------|-----------|
| 1 | | | |

---

## Scoring (Complete after group review)

| Dimension | Prompt A (0-3) | Prompt B (0-3) | Notes |
|-----------|---------------|---------------|-------|
| Correctness | | | |
| Statistical Validity | | | |
| Reproducibility | | | |
| Code Quality | | | |
| Efficiency | | | |
| Safety | | | |

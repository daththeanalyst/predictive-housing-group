# Agent Log — GitHub Copilot Agent Mode

> Fill this in as you run the benchmark. This becomes your appendix evidence.

## Run 1 — Prompt A (Build Model)
- **Date:** 2026-03-16
- **Duration:** ~5m 10s (notebook reproduction runtime)
- **Agent turns:** N/A (chat transcript not saved in workspace)

### Key Decisions
| # | What the agent did | Correct? | Notes |
|---|---|---|---|
| 1 | Loaded and merged property + area datasets by outcode | Yes | Merge completed with 417,561 rows and no merge loss |
| 2 | Flagged `rentEstimate` as target leakage and excluded it | Yes | Printed explicit leakage warning before modeling |
| 3 | Trained baseline models on test split | Yes | Linear Regression and RandomForest evaluated on TEST set |
| 4 | Added improved pipeline with price clipping + log1p target | Yes | Produced improved model comparison |
| 5 | Selected RF_Tuned_LogTarget as best model | Yes | Best test RMSE/R2 among compared models |

### Data Quality Handling
- Detected missing values? [x] Yes [ ] No — How: Missing summary table printed for prices; major gaps in `energyRating`, `bathrooms`, `livingRooms`, etc.
- Detected price outliers? [x] Yes [ ] No — How: IQR rule reported 37,210 outliers (8.91%).
- Detected skewed distribution? [x] Yes [ ] No — Action: Used capped target (1st/99th pct) and log1p transform in improved models.
- Detected rentEstimate leakage? [x] Yes [ ] No
- Applied log-transform? [x] Yes [ ] No

### Final Metrics
| Model | RMSE | MAE | R² |
|---|---|---|---|
| RF_Tuned_LogTarget (best) | 269,930.65 | 128,001.44 | 0.8814 |

### Errors & Self-Corrections
| Error | How Detected | How Fixed |
|---|---|---|
| `NameError: plot_dir is not defined` during baseline cell plot save | Notebook traceback after model metrics printed | Added setup cell to define/create `plot_dir`, then reran cell successfully |

---

## Run 2 — Prompt A (Build Model)
- **Date:** N/A (no separate Run 2 artifact saved)
- **Duration:** N/A
- **Agent turns:** N/A

### Key Decisions
| # | What the agent did | Correct? | Notes |
|---|---|---|---|
| 1 | Run evidence unavailable in workspace | N/A | No second chat transcript/notebook/output for Copilot Prompt A Run 2 |

### Data Quality Handling
- Detected missing values? [ ] Yes [ ] No — How: N/A (missing run artifact)
- Detected price outliers? [ ] Yes [ ] No — How: N/A (missing run artifact)
- Detected skewed distribution? [ ] Yes [ ] No — Action: N/A (missing run artifact)
- Detected rentEstimate leakage? [ ] Yes [ ] No
- Applied log-transform? [ ] Yes [ ] No

### Final Metrics
| Model | RMSE | MAE | R² |
|---|---|---|---|
| N/A | N/A | N/A | N/A |

### Errors & Self-Corrections
| Error | How Detected | How Fixed |
|---|---|---|
| N/A | N/A | N/A |

---

## Run 3 — Prompt B (Debug Pipeline)
- **Date:** N/A (no Prompt B run transcript saved)
- **Duration:** N/A
- **Agent turns:** N/A

### Bugs Found
| Bug | Found? | Explanation Given | Fix Correct? |
|---|---|---|---|
| rentEstimate leakage | [ ] | N/A (no run artifact) | [ ] |
| No log-transform | [ ] | N/A (no run artifact) | [ ] |
| No outlier handling | [ ] | N/A (no run artifact) | [ ] |
| Train eval reported as test | [ ] | N/A (no run artifact) | [ ] |

### Corrected Metrics
| Metric | Buggy Value | Corrected Value |
|---|---|---|
| RMSE | £31,870 | N/A |
| MAE | £6,460 | N/A |
| R² | 0.9988 | N/A |

---

## Run 4 — Prompt B (Debug Pipeline)
- **Date:** N/A (no Prompt B run transcript saved)
- **Duration:** N/A
- **Agent turns:** N/A

### Bugs Found
| Bug | Found? | Explanation Given | Fix Correct? |
|---|---|---|---|
| rentEstimate leakage | [ ] | N/A (no run artifact) | [ ] |
| No log-transform | [ ] | N/A (no run artifact) | [ ] |
| No outlier handling | [ ] | N/A (no run artifact) | [ ] |
| Train eval reported as test | [ ] | N/A (no run artifact) | [ ] |

### Corrected Metrics
| Metric | Buggy Value | Corrected Value |
|---|---|---|
| RMSE | £31,870 | N/A |
| MAE | £6,460 | N/A |
| R² | 0.9988 | N/A |

# Agent Log — Claude Code

> Canonical runs for the benchmark comparison. Duplicate runs archived in `extra_runs/`.

## Run 1 — Prompt A (Build Model)
- **Date:** 2026-03-16
- **Duration:** ~5 minutes
- **Iterations (tool calls):** 1 (single notebook execution — first-attempt success)
- **Notebook:** `prompt_a_run1.ipynb`

### Key Decisions
| # | What the agent did | Correct? | Notes |
|---|---|---|---|
| 1 | Loaded both CSVs, printed shapes/dtypes/columns | Yes | Standard ingestion |
| 2 | Computed missing values (count + %) for both datasets | Yes | Identified energyRating (20%), bathrooms (19%), etc. |
| 3 | Detected price outliers via IQR method | Yes | Found heavy right-skew (skewness >5) |
| 4 | Checked rentEstimate correlation with price (0.981) | Yes | Identified as target leakage unprompted |
| 5 | Excluded rentEstimate from all models | Yes | Critical for statistical validity |
| 6 | Applied log-transform to target | Yes | Addressed skewness |
| 7 | Capped outliers at 99th percentile | Yes | Reduced extreme value influence |
| 8 | Used median imputation for missing values | Yes | Better than fillna(0) |
| 9 | Encoded categoricals with LabelEncoder | Yes | Appropriate for tree-based models |
| 10 | Trained LR, RF baselines, then RF+log+cap and XGBoost | Yes | Multiple model comparison |
| 11 | Evaluated all models on TEST set only | Yes | No train-set evaluation |
| 12 | Saved all plots as PNG files | Yes | 7 plots saved |

### Data Quality Handling
- Detected missing values? [x] Yes [ ] No — How: isnull().sum() with percentage reporting
- Detected price outliers? [x] Yes [ ] No — How: IQR method + percentile analysis + skewness
- Detected skewed distribution? [x] Yes [ ] No — Action: Log-transform + outlier capping at 99th pctl
- Detected rentEstimate leakage? [x] Yes [ ] No
- Applied log-transform? [x] Yes [ ] No

### Final Metrics
| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression (baseline) | £560,292 | £278,587 | 0.6335 |
| Random Forest (baseline) | £182,852 | £44,064 | 0.9610 |
| RF (log + outlier cap) | £119,633 | £36,751 | 0.9692 |
| XGBoost (log + outlier cap) | £192,772 | £97,920 | 0.9200 |

### Errors & Self-Corrections
| Error | How Detected | How Fixed |
|---|---|---|
| None — ran successfully on first attempt | N/A | N/A |

---

## Run 2 — Prompt B (Debug Pipeline)
- **Date:** 2026-03-16
- **Duration:** ~3 minutes
- **Iterations:** 1 (single notebook execution)
- **Notebook:** `prompt_b_run1.ipynb`

### Bugs Found
| Bug | Found? | Explanation Given | Fix Correct? |
|---|---|---|---|
| rentEstimate leakage | [x] | Corr=0.981 with price; rent is derived from market value; unavailable at prediction time | [x] |
| No log-transform | [x] | Prices heavily right-skewed (skewness >5); distorts training and inflates RMSE | [x] |
| No outlier handling | [x] | Extreme multi-million values inflate RMSE disproportionately | [x] |
| Train eval reported as test | [x] | model.predict(X_train) + y_train used but printed as "Test" metrics | [x] |
| fillna(0) inappropriate | [x] | 0 bedrooms/0 sqm floor area is nonsensical; replaced with median imputation | [x] |
| Limited feature set (7 features) | [x] | Ignored propertyType, tenure, location, detailed area demographics | [x] |

### Corrected Metrics
| Metric | Buggy Value | Corrected Value |
|---|---|---|
| RMSE | £31,870 | £119,633 |
| MAE | £6,460 | £36,751 |
| R² | 0.9988 | 0.9692 |

---

## Reproducibility Note

A second run of each prompt was performed (archived in `extra_runs/`). Key consistency findings:
- **Prompt A:** Baseline metrics (LR, RF) were identical across both runs. The agent made the same core decisions (leakage detection, log-transform, outlier capping, median imputation) in both runs.
- **Prompt B:** Both runs found the same 6 bugs and produced identical corrected metrics (RMSE=£119,633, R²=0.9692).

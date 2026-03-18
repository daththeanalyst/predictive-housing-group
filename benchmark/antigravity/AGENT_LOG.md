# Agent Log

---

## Run 1 — Prompt A (Build ML Pipeline)

- **Date:** 2026-03-17
- **Start time:** 16:04 (first notebook execution)
- **End time:** 16:18 (final notebook execution complete)
- **Duration:** ~14 minutes (notebook execution); ~45 minutes total including planning and cell authoring
- **Iterations (messages / tool calls / code cells):** 8 user messages, ~50 tool calls, 20 code cells executed across 4 stages

### Stages Completed

| Stage | Completed? | Notes |
|-------|-----------|-------|
| Stage 1: Data Ingestion & Quality Assessment | Yes | Both datasets loaded, merged, cleaned. 8 missing-value columns handled. Price outliers capped. PropertyType consolidated from 19 to 5 groups. |
| Stage 2: Exploratory Data Analysis | Yes | 5 plots saved as PNG. Price distribution, correlation heatmap, property type boxplot, area features scatter, energy rating boxplot. 3 insights documented. |
| Stage 3: Baseline Models | Yes | Linear Regression and Random Forest (n_estimators=100) trained. 80/20 split with random_state=42. Evaluated on test set. Predicted vs actual plots saved. |
| Stage 4: Performance Improvement | Yes | 3 improvement strategies: log-transform target, XGBoost, XGBoost + log target. Summary comparison table. Feature importances plotted. |

### Data Quality Issues Found

| Issue | How Detected | Action Taken |
|-------|-------------|-------------|
| energyRating 20.2% missing (84,288 rows) | `isnull().sum()` report | Mode imputation (D) |
| bathrooms 18.6% missing (77,755 rows) | `isnull().sum()` report | Median imputation (1.0) |
| livingRooms 14.5% missing (60,341 rows) | `isnull().sum()` report | Median imputation (1.0) |
| bedrooms 9.7% missing (40,404 rows) | `isnull().sum()` report | Median imputation (2.0) |
| floorAreaSqM 6.0% missing (25,066 rows) | `isnull().sum()` report | Median imputation (84.0) |
| tenure 2.8% missing (11,494 rows) | `isnull().sum()` report | Mode imputation (Leasehold) |
| propertyType 0.3% missing (1,126 rows) | `isnull().sum()` report | Mode imputation (Purpose Built Flat) |
| rentEstimate 0.3% missing (1,101 rows) | `isnull().sum()` report | Median imputation (2600.0) |
| 19 propertyType variants (noisy) | `nunique()` check | Consolidated to 5 groups: Flat, Terraced, Semi-Detached, Detached, Other |
| Price right-skewed (skewness=5.05) | `describe()` and `skew()` | Capped at Q3 + 3×IQR (£2,598,000); 18,574 properties capped (4.45%) |

### Models Trained

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | £242,674 | £144,173 | 0.8285 |
| Random Forest | £22,550 | £4,598 | 0.9985 |
| Random Forest (Log Target) | £23,938 | £4,662 | 0.9983 |
| XGBoost | £33,982 | £15,534 | 0.9966 |
| XGBoost (Log Target) | £38,176 | £15,971 | 0.9958 |

### Errors During Execution

| Error | How Detected | How Fixed |
|-------|-------------|-----------|
| N/A | N/A | N/A |

### Plots Saved

| Filename | Description |
|----------|------------|
| price_distribution.png | Side-by-side histogram of raw and log-transformed prices |
| correlation_heatmap.png | Lower-triangle annotated heatmap of 13 key features |
| price_by_property_type.png | Boxplot of prices by consolidated property type, ordered by median |
| price_vs_area_features.png | 2×2 scatter: floor area, crime, education %, POI count |
| price_by_energy_rating.png | Boxplot of prices by energy rating A–G |
| predicted_vs_actual_baseline.png | Side-by-side predicted vs actual for Linear Regression and Random Forest |
| predicted_vs_actual_best.png | Predicted vs actual for best model (Random Forest) |
| feature_importances.png | Horizontal bar chart of top 15 feature importances from best model |

### Warnings or Concerns

- **rentEstimate dominance:** rentEstimate accounts for 96% of feature importance in the best model. This feature likely "leaks" market information since rent estimates are derived from property valuations. For causal inference, it should be excluded — but for pure prediction it is legitimate.
- **Random Forest outperformed XGBoost:** Unusual result likely driven by rentEstimate's overwhelming predictive power — when one feature dominates, RF's bagging approach captures the signal just as well as boosting, with less overfitting risk.
- **Imputation before train/test split:** Median/mode imputation was computed on the full dataset before splitting. On 417K rows the train/full statistics are nearly identical, so leakage risk is negligible — but strictly, imputation should be fitted on training data only.
- **Log-transform did not improve RF:** Because prices were already capped at Q3+3×IQR, the remaining skewness was modest (1.69), reducing the benefit of log-transformation.

---

## Run 2 — Prompt B (Debug Broken Pipeline)

- **Date:** 2026-03-17
- **Start time:** 16:30
- **End time:** 16:38
- **Duration:** ~8 minutes
- **Iterations (messages / tool calls / code cells):** 4 user messages, ~15 tool calls, 6 code cells executed

### Bugs Found

| Bug | What Was Wrong | How Fixed |
|-----|---------------|-----------|
| 1. Training-set evaluation | `model.predict(X_train)` and metrics computed against `y_train`, but printed as "Test" metrics. Random Forest memorises training data, giving misleadingly perfect scores. | Changed to `model.predict(X_test)` and evaluated against `y_test`. |
| 2. `fillna(0)` for missing values | Missing bedrooms, bathrooms, floorAreaSqM, livingRooms, and rentEstimate filled with 0. A property with 0 bedrooms or 0 m² floor area is nonsensical; 0 rentEstimate (the dominant predictor) drastically distorts predictions. | Replaced with `fillna(df[feature_cols].median())` — median imputation preserves central tendency. |

### Metrics

| Metric | Before Fix (Buggy) | After Fix (Corrected) |
|--------|-----------|-----------|
| RMSE | £31,870 | £66,194 |
| MAE | £6,460 | £15,087 |
| R² | 0.9988 | 0.9949 |

### Errors During Execution

| Error | How Detected | How Fixed |
|-------|-------------|-----------|
| N/A | N/A | N/A |

### Warnings or Concerns

- **Buggy metrics looked better because they were training metrics:** The "before" RMSE/MAE/R² are not comparable to the "after" metrics in the usual sense — the before numbers were on training data (overfitted), while the after numbers are honest test-set metrics.
- **Imputation computed before train/test split:** Median values are computed on the full dataset before splitting. On 417K rows the difference between full-data and train-only medians is negligible, but strictly, imputation should be fitted on training data only.
- **rentEstimate dominance:** rentEstimate likely leaks market information (rent estimates are derived from property valuations). For causal inference it should be excluded, but for pure prediction it is legitimate.

---

## Scoring (Complete after group review)

| Dimension | Prompt A (0-3) | Prompt B (0-3) | Notes |
|-----------|---------------|---------------|-------|
| Correctness | 3 | 2 | A: All 4 stages, verification gates, no errors. B: Found 2/2 main bugs, missed merge guard and rentEstimate removal. |
| Statistical Validity | 3 | 2 | A: Proper split, test eval, leakage flagged, imputation timing acknowledged. B: Correct train→test fix, but kept rentEstimate. |
| Reproducibility | 3 | 2 | A: RANDOM_STATE constant, decision blocks, verification gates, self-contained. B: Clean and runnable, simpler structure. |
| Code Quality | 3 | 2 | A: Decision blocks, verification gates, helper functions, property type consolidation. B: Clean but simpler, no modular design. |
| Efficiency | 3 | 3 | A: 14 min, no errors, first attempt. B: 8 min, 15 tool calls, fastest Prompt B across all tools. |
| Safety | 3 | 2 | A: 4 proactive warnings (leakage, RF>XGB, imputation, log-transform). B: Good explanations but didn't act on leakage. |

Prompt A (18/18)

Antigravity produced the strongest Prompt A output across all tools. The notebook followed a rigorous structure with explicit decision blocks justifying every methodological choice (outlier capping strategy, imputation method, encoding scheme) and verification gates confirming each stage met the spec. It proactively flagged four concerns, most notably that rentEstimate accounted for 96% of feature importance and likely constitutes target leakage. The best model (Random Forest, R²=0.9985) was the highest-performing across all tools, and the agent transparently discussed why improvement strategies (log-transform, XGBoost) did not outperform the baseline RF.

Prompt B (13/18)

Antigravity correctly identified and fixed both primary bugs (training-set evaluation labelled as test metrics, and fillna(0) replacing missing values with nonsensical zeros), producing corrected test-set metrics of RMSE=£66,194, R²=0.9949. The fix was clean and the explanations were sound. However, it missed the merge cardinality guard (no validate='m:1') and did not remove rentEstimate from the corrected pipeline despite flagging it as a leakage concern, a gap in acting on its own warnings. The run was the most efficient Prompt B across all tools at ~8 minutes with no errors.

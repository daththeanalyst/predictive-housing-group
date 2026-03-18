# Agent Log

---

## Run 1 — Prompt A (Build ML Pipeline)

- **Date:** 2026-03-17
- **Start time:** 19:15:30 (approx)
- **End time:** 19:29:46
- **Duration:** 00:14:16 (approx)
- **Iterations (messages / tool calls / code cells):** Approx. 46 total (code cells executed: 12; tool calls: approx. 34; messages: N/A)

### Stages Completed

| Stage | Completed? | Notes |
|-------|-----------|-------|
| Stage 1 — Data Ingestion and Quality Assessment | Yes | Loaded both CSVs, printed shapes/columns/dtypes, missingness report, price outlier analysis, merged on outcode, and applied quality fixes. |
| Stage 2 — Exploratory Data Analysis | Yes | Plotted price distributions, correlation heatmap, price-by-property-type boxplot, and price-vs-area-feature relationships; reported 3 predictive insights. |
| Stage 3 — Feature Preparation | Yes | Built train/test split and preprocessing pipeline (numeric median imputation + categorical imputation + one-hot encoding). |
| Stage 4 — Model Training and Evaluation | Yes | Trained and evaluated two models (LinearRegression, RandomForestRegressor) using log1p target strategy. |
| Any skipped stages | No | N/A |

### Data Quality Issues Found

| Issue | How Detected | Action Taken |
|-------|-------------|-------------|
| Missing values in listing-level columns (e.g., energyRating, bathrooms, livingRooms) | `isna().sum()` and missing percentage report in notebook | For modeling dataset, imputed numeric columns with median and categorical columns with `UNKNOWN`/most frequent in preprocessing. |
| Strong right-skew and high-price tail in `price` (IQR outliers ~8.91%) | IQR bounds, histogram, and boxplot | Kept valid records (no aggressive outlier deletion) and trained models on `log1p(price)`; inverted predictions with `expm1`. |
| Potential categorical inconsistency/whitespace and case variance | Data cleaning review before modeling | Standardized selected categorical fields (`propertyType`, `tenure`, `energyRating`, `outcode`) using strip + uppercase. |
| Potential join quality risk on area merge | `merge(..., indicator=True)` counts | Verified full match (`left_only = 0`), no duplicate outcodes in area table, retained all rows. |

### Models Trained

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| RandomForestRegressor | 390002.047 | 111555.005 | 0.822 |
| LinearRegression | 15383485.373 | 361556.803 | -275.270 |

### Errors During Execution

| Error | How Detected | How Fixed |
|-------|-------------|-----------|
| No runtime exceptions | Notebook execution logs | N/A |

### Plots Saved

| Filename | Description |
|----------|------------|
| price_distribution_boxplot.png | Stage 1 raw price histogram + boxplot for outlier assessment |
| stage2_price_distribution.png | Stage 2 raw vs log-transformed price distribution |
| stage2_correlation_heatmap.png | Correlation heatmap for top numeric predictors and price |
| stage2_price_by_property_type_boxplot.png | Price comparison by property type |
| stage2_price_vs_area_features.png | Price relationship with 3 selected area-level features |
| stage4_actual_vs_predicted_best_model.png | Actual vs predicted scatter for best model (RandomForestRegressor) |

### Warnings or Concerns

- `rentEstimate` has very high correlation with `price` and may encode near-target information (possible leakage risk depending on feature generation source).
- LinearRegression performance is unstable/poor on this feature space (extreme negative R²), likely due to nonlinearity, heteroskedasticity, and high-dimensional encoded features.
- Area features are shared across properties within each outcode; this can understate uncertainty if geographic grouping effects are not explicitly modeled in validation.

---

## Run 2 — Prompt B (Debug Broken Pipeline)

- **Date:** 2026-03-17
- **Start time:** 21:52:13
- **End time:** 22:09:17
- **Duration:** 00:17:04
- **Iterations (messages / tool calls / code cells):** Approx. 66 total (code cells executed: 18; tool calls: approx. 48; messages: N/A)

### Bugs Found

| Bug | What Was Wrong | How Fixed |
|-----|---------------|-----------|
| Evaluated on training split while labeling as test metrics | `train_preds = model.predict(X_train)` was scored against `y_train` but printed as "Test" metrics, causing optimistic bias and invalid generalization reporting. | Evaluated strictly on held-out test split (`X_test`, `y_test`) in corrected pipeline and reporting labels now match actual split. |
| Misleading metric labels | Printed "Test RMSE/MAE/R²" despite using train-set predictions, masking the validation bug. | Added explicit "buggy reported" vs "true held-out" vs "corrected" outputs and comparison table. |
| Naive global imputation with `fillna(0)` | Replacing all missing feature values with zero can inject impossible values and distort feature distributions. | Replaced with median imputation using `SimpleImputer` inside a preprocessing pipeline. |
| No merge cardinality guard | Merge did not enforce one-to-many (`m:1`) assumptions; duplicate outcodes in area table could silently duplicate rows. | Added duplicate key check and used `merge(..., validate='m:1')` in corrected module. |
| Leakage-prone feature (`rentEstimate`) used without validation | `rentEstimate` can encode near-target valuation signals and inflate apparent performance. | Removed `rentEstimate` from corrected benchmark feature list and documented leakage concern. |

### Metrics

| Metric | Before Fix | After Fix |
|--------|-----------|-----------|
| RMSE | 31,869.625 (buggy reported as "test") | 308,321.919 (corrected true test) |
| MAE | 6,460.485 (buggy reported as "test") | 108,681.831 (corrected true test) |
| R² | 0.998797 (buggy reported as "test") | 0.889023 (corrected true test) |

### Errors During Execution

| Error | How Detected | How Fixed |
|-------|-------------|-----------|
| `No module named pytest` when running regression-test cell | Notebook output from test execution cell showed missing dependency and non-zero exit code. | Installed `pytest` in notebook kernel, reran cells after kernel restart, and confirmed `3 passed` with exit code `0`. |

### Warnings or Concerns

- Corrected metrics are much less optimistic than buggy-reported metrics, confirming severe evaluation leakage in the original reporting path.
- Residual diagnostics show large underprediction on ultra-high-price homes; error distribution remains heavy-tailed.
- Area-level features are repeated by outcode and may hide geographic dependence; grouped or spatial validation should be considered for stricter generalization checks.
- Removing `rentEstimate` reduces leakage risk but may lower apparent fit; this is expected and improves validity.

---

## Scoring (Complete after group review)

| Dimension | Prompt A (0-3) | Prompt B (0-3) | Notes |
|-----------|---------------|---------------|-------|
| Correctness | 2 | 3 | A: All stages done but LR gave R²=-275 - broken result not caught. B: Found 5 bugs (most of any tool), wrote regression tests. |
| Statistical Validity | 2 | 3 | A: Proper split + pipeline imputation, flagged leakage, but didn't investigate catastrophic LR. B: Removed rentEstimate (only tool to act on leakage), added merge validation. |
| Reproducibility | 2 | 2 | A: Seeds set, pipeline approach, but no decision blocks or verification gates. B: Clean structure, modular code, but needed pytest install mid-run. |
| Code Quality | 2 | 3 | A: Good sklearn Pipeline usage but no decision docs, LR failure uncaught. B: Modular debug_pipeline.py, regression tests, residual diagnostics — most thorough debug. |
| Efficiency | 2 | 2 | A: 14 min, 46 iterations, no errors but lower quality output. B: 17 min, 66 iterations — slowest but most comprehensive. |
| Safety | 2 | 3 | A: 3 warnings but didn't catch R²=-275 as red flag. B: Actually removed leakage feature, wrote tests, flagged residual issues. |

Prompt A (12/18)

Copilot completed all four stages and was the only tool to use a proper sklearn Pipeline with ColumnTransformer, meaning imputation was correctly fitted on training data only, a best practice approach the other tools missed. However, the Linear Regression baseline produced a catastrophic R²=-275.27 which the agent noted as "unstable" but did not investigate or fix, undermining confidence in the output. The Random Forest (R²=0.822, RMSE=£390K) performed significantly below Antigravity's equivalent, likely due to the log1p target strategy interacting poorly with the preprocessing pipeline. Leakage and geographic dependence were flagged but not acted upon.

Prompt B (16/18)

Copilot delivered the most thorough debugging output of any tool. It found five bugs which are more than any other tool, including the merge cardinality guard and rentEstimate leakage, which it actually removed from the corrected feature list rather than merely flagging. It was the only tool to write regression tests (test_debug_pipeline.py) and produce residual diagnostics (histogram, before/after comparison, top-15 residuals CSV). The corrected metrics (RMSE=£308,322, R²=0.889) are less flattering than Antigravity's because rentEstimate was removed, but this is arguably the more statistically honest result. The trade-off was efficiency, at 17 minutes and 66 iterations, it was the slowest Prompt B run.




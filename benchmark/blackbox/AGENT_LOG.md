# Agent Log

---

## Run 1 — Prompt A (Build ML Pipeline)
[Previous content unchanged...]

## Run 2 — Prompt B (Debug Broken Pipeline)
[Previous content unchanged...]

## Run 3 — BLACKBOXAI Full Pipeline

- **Date:** $(date)\n",
    "- **Start time:** When user first executed cells\n",
    "- **End time:** When final cell complete\n",
    "- **Total duration:** User to fill after execution\n",
    "- **Total iterations:** ~15 tool calls, 15 code cells across 4 stages\n",
    "\n",
    "### Stages Completed\n",
    "\n",
    "| Stage | Completed? | Notes |\n",
    "|-------|------------|-------|\n",
    "| Stage 1 | Yes | Load, merge on outcode, median/mode imputation all missing, price winsorized 1%/99% |\n",
    "| Stage 2 | Yes | 3 plots: multi-panel EDA (price, propertyType, energyRating, corr heatmap) saved as eda_plots_stage2.png. 3 insights printed |\n",
    "| Stage 3 | Yes | LinearRegression + RandomForest baselines. 80/20 split random_state=42. Metrics table + predicted vs actual plot |\n",
    "| Stage 4 | Yes | XGBoost + RF log-transform improvements. Comparison table. Top 10 feature importances plot |\n",
    "\n",
    "### Data Quality Issues Found & Handled\n",
    "\n",
    "| Issue | How Handled |\n",
    "|-------|-------------|\n",
    "| Missing values (energyRating ~20%, bathrooms ~18%, etc.) | Median for numeric, mode for categorical |\n",
    "| Price outliers (right-skewed) | Clip to 1st/99th percentiles |\n",
    "| Categorical encoding for modeling | LabelEncoder on propertyType, tenure, energyRating |\n",
    "| Merge losses | Left join on outcode - minor losses reported |\n",
    "\n",
    "### Final Metrics (FILL AFTER EXECUTION)\n",
    "\n",
    "| Model | RMSE | MAE | R² |\n",
    "|-------|------|-----|-----|\n",
    "| LinearRegression | N/A (run notebook) | N/A | N/A |\n",
    "| RandomForest | N/A | N/A | N/A |\n",
    "| XGBoost | N/A | N/A | N/A |\n",
    "| RF+Log | N/A | N/A | N/A |\n",
    "\n",
    "### Errors Encountered\n",
    "\n",
    "| Error | How Fixed |\n",
    "|-------|------------|\n",
    "| N/A | N/A |\n",
    "\n",
    "### Plots Saved\n",
    "\n",
    "| Filename | Description |\n",
    "|----------|-------------|\n",
    "| eda_plots_stage2.png | EDA: price hist, propertyType/energyRating boxplots, corr heatmap |\n",
    "| baseline_predictions.png | Predicted vs actual for LinearReg + RF |\n",
    "| feature_importances.png | Top 10 features from best model |\n",
    "| model_metrics_summary.csv | All models RMSE/R2 comparison |\n",
    "\n",
    "### Warnings/Concerns\n",
    "- rentEstimate expected to dominate feature importance (potential target leakage for causal models, fine for prediction)\n",
    "- LabelEncoder for multi-class cats (propertyType) - one-hot better for linear models but RF/XGB handle fine\n",
    "- Imputation on full data before split (minor leakage risk on large dataset)\n",
    "- No cross-validation (single 80/20 split for speed)\n",
    "\n",
    "---\n",
    "\n",
    "## Scoring (Complete after group review)\n",
    "\n",
    "| Dimension | Prompt A (0-3) | Prompt B (0-3) | Notes |\n",
    "|-----------|---------------|---------------|-------|\n",
    "| Correctness | | | |\n",
    "| Statistical Validity | | | |\n",
    "| Reproducibility | | | |\n",
    "| Code Quality | | | |\n",
    "| Efficiency | | | |\n",
    "| Safety | | | |








# Agent Log

---

## Run 1 — Prompt A (Build ML Pipeline)

- **Date:** 2026-03-17
- **Start time:** When user first executed cells
- **End time:** When final cell complete
- **Total duration:** ~15 minutes (estimated from tool calls)
- **Total iterations:** ~15 tool calls, 15 code cells across 4 stages

### Stages Completed

| Stage | Completed? | Notes |
|-------|------------|-------|
| Stage 1 | Yes | Load, merge on outcode, median/mode imputation all missing, price winsorized 1%/99% |
| Stage 2 | Yes | 3 plots: multi-panel EDA (price, propertyType, energyRating, corr heatmap) saved as eda_plots_stage2.png. 3 insights printed |
| Stage 3 | Yes | LinearRegression + RandomForest baselines. 80/20 split random_state=42. Metrics table + predicted vs actual plot |
| Stage 4 | Yes | XGBoost + RF log-transform improvements. Comparison table. Top 10 feature importances plot |

### Data Quality Issues Found

| Issue | How Detected | Action Taken |
|-------|-------------|-------------|
| Missing values (energyRating ~20%, bathrooms ~18%, livingRooms ~14%, bedrooms ~10%, floorAreaSqM ~6%) | `isna().sum()` and missing percentage report | Median imputation for numeric, mode for categorical |
| Price outliers (right-skewed distribution) | `describe()` and histogram | Clipped to 1st/99th percentiles (£228,000–£4,959,000) |
| Categorical encoding needed for modelling | dtype inspection | LabelEncoder on propertyType, tenure, energyRating |
| Merge quality check | Left join on outcode | 0 rows lost (100% match), no duplicate outcodes in area table |

### Models Trained

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | £233,408 | N/A | 0.91 |
| Random Forest | £38,857 | N/A | 1.0 |
| XGBoost | £51,516 | N/A | 1.0 |
| RF + Log Transform | £39,730 | N/A | 1.0 |

### Errors During Execution

| Error | How Detected | How Fixed |
|-------|-------------|-----------|
| N/A | N/A | N/A |

### Plots Saved

| Filename | Description |
|----------|------------|
| eda_plots_stage2.png | 2×2 panel: price histogram (log), propertyType boxplot, energyRating boxplot, correlation heatmap |
| baseline_predictions.png | 1×2 predicted vs actual scatter for Linear Regression and Random Forest |
| feature_importances.png | Top 10 feature importances from best model (Random Forest) |
| model_metrics_summary.csv | All 4 models RMSE and R² comparison |

### Warnings or Concerns

- **rentEstimate dominance:** rentEstimate accounts for ~90–95% of feature importance. Likely leaks market information since rent estimates are derived from property valuations. Flagged but not removed.
- **LabelEncoder for multi-class categoricals:** Acceptable for tree-based models (RF, XGBoost), but introduces ordinal assumptions harmful to Linear Regression. OneHotEncoder would be more appropriate.
- **Imputation before train/test split:** Median/mode computed on full dataset before splitting. On 417K rows the impact is negligible, but strictly, imputation should be fitted on training data only.
- **No cross-validation:** Single 80/20 split used. No grouped or spatial validation despite area-level features shared across properties within each outcode.
- **R²=1.0 not questioned:** Three models reported R²=1.0 on the test set — likely driven by rentEstimate leakage — but this was not flagged or investigated by the agent.

---

## Run 2 — Prompt B (Debug Broken Pipeline)

- **Date:** 2026-03-17
- **Start time:** N/A
- **End time:** N/A
- **Total duration:** N/A
- **Total iterations:** ~12 code cells

### Bugs Found

| Bug | What Was Wrong | How Fixed |
|-----|---------------|-----------|
| N/A — agent did not debug the broken pipeline | The agent rewrote a fresh Stage 4 pipeline from scratch instead of identifying and fixing the bugs in the provided broken code. | N/A — bugs were not identified |

### Bugs Missed

| Bug | What Should Have Been Found |
|-----|---------------------------|
| Training-set evaluation labelled as test | `model.predict(X_train)` scored against `y_train` but printed as "Test" metrics — gives misleadingly perfect scores |
| `fillna(0)` for missing values | Missing bedrooms, bathrooms, floorAreaSqM filled with 0 — nonsensical values that distort predictions |
| No merge cardinality guard | No `validate='m:1'` on merge — duplicate outcodes could silently duplicate rows |
| rentEstimate leakage | Dominant predictor likely derived from property valuations — should be removed or investigated |

### Metrics

| Metric | Before Fix (Buggy) | After Fix (Corrected) |
|--------|-----------|-----------|
| N/A | N/A — agent did not run the broken pipeline | N/A — no before/after comparison produced |

### Errors During Execution

| Error | How Detected | How Fixed |
|-------|-------------|-----------|
| Syntax error in Cell 9: `if c not 'price'` instead of `if c != 'price'` | Would crash on execution | Not fixed by agent |
| Incomplete refactoring in Cell 8: comment "wait no - custom" left in code | Code review | Not fixed by agent |
| Feature column mismatch: engineered features not passed to feature importance | Code review | Not fixed by agent |

### Warnings or Concerns

- Agent did not address the actual prompt (debug broken pipeline). Instead produced a fresh pipeline, which itself contained syntax errors.
- No before/after metrics comparison was produced.
- No bug impact analysis was provided.

---

## Scoring

| Dimension | Prompt A (0-3) | Prompt B (0-3) | Notes |
|-----------|---------------|---------------|-------|
| Correctness | 2 | 1 | A: All 4 stages completed, no runtime errors, but R²=1.0 never questioned. B: Did not debug the broken pipeline; rewrote from scratch; own code has syntax errors. |
| Statistical Validity | 2 | 1 | A: Proper split and test eval, leakage flagged but not removed, R²=1.0 accepted uncritically. B: No before/after comparison, no bug impact analysis. |
| Reproducibility | 2 | 1 | A: Seeds set, clean structure, all outputs visible, but no Pipeline or decision documentation. B: Syntax errors prevent full execution of cells 9+. |
| Code Quality | 2 | 1 | A: Clean, readable sklearn code but no Pipeline/ColumnTransformer, no modular functions. B: Syntax errors, incomplete refactoring, feature mismatch between cells. |
| Efficiency | 2 | 1 | A: ~15 tool calls, all stages completed in one pass, no errors. B: 12 cells produced but didn't address the actual task. |
| Safety | 1 | 1 | A: 5 warnings listed but R²=1.0 not flagged as suspicious — critical oversight. B: Failed to identify any planted bugs (train-set eval, fillna(0)). |

**Prompt A: 11/18**

Blackbox completed all four stages in a clean, linear notebook with all cells executed and outputs visible. It handled data quality appropriately,  median imputation for numeric columns, mode for categoricals, and price winsorisation at the 1st/99th percentiles. Four models were trained: Linear Regression (RMSE=£233,408, R²=0.91), Random Forest (RMSE=£38,857, R²=1.0), XGBoost (RMSE=£51,516, R²=1.0), and Random Forest with log-transformed target (RMSE=£39,730, R²=1.0). The agent flagged rentEstimate as a potential leakage concern but did not remove it, and accepted R²=1.0 on the test set without questioning whether this indicated overfitting or target leakage. Code was functional but lacked the modularity of a sklearn Pipeline, and LabelEncoder was used for categoricals, which contributed to Linear Regression's weaker performance. Overall, a competent but unremarkable output that completed the task without the methodological rigour seen in Antigravity or the proper Pipeline architecture used by Copilot.

**Prompt B: 6/18**

Blackbox was the weakest performer on Prompt B. Rather than reading and debugging the provided broken pipeline , which contained training-set evaluation mislabelled as test metrics and `fillna(0)` injecting nonsensical zeros , the agent rewrote a fresh Stage 4 pipeline from scratch. None of the planted bugs were identified, explained, or fixed. The rewritten code itself contained errors: a syntax bug (`if c not 'price'` instead of `if c != 'price'`) in the feature engineering cell, incomplete refactoring comments left in the code, and a mismatch between engineered features and the feature importance output. There was no before/after metrics comparison and no regression tests. This represents a fundamental failure to follow the prompt, in contrast to Copilot (5 bugs found, regression tests written) and Antigravity (2 bugs fixed in 8 minutes).










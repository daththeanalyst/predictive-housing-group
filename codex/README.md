# Codex Reproducible Housing Workflow

This folder now contains both the original benchmark assets and a reproducible notebook workflow for London house-price modelling.

## Files
- `london_price_analysis.ipynb`: end-to-end notebook for ingestion, schema checks, missing-value handling, EDA, baseline modelling, and improved modelling.
- `london_house_prices.csv`: property-level London housing data.
- `london_area_features.csv`: area-level outcode features joined onto properties.
- `requirements.txt`: pinned Python dependencies for repeatable runs.
- `repro_config.json`: checked-in run configuration for seeds, split ratio, EDA sample size, and tuning sample size.
- `setup_env.ps1`: creates a local virtual environment and installs dependencies.
- `run_notebook.ps1`: executes the notebook with Jupyter `nbconvert`.
- `broken_pipeline.py`, `prompt_a_main.txt`, `prompt_b_debugging.txt`, `AGENT_LOG.md`, `SCORING.md`: original benchmark materials.

## Reproducible Setup
Run these commands from the `codex` folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_env.ps1
powershell -ExecutionPolicy Bypass -File .\run_notebook.ps1
```

To overwrite the notebook in place instead of writing a timestamped output:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_notebook.ps1 -InPlace
```

## Reproducibility Controls
- Default seed: `42`
- Train/test split: `0.2`
- EDA sample cap: `30000`
- Tuning sample cap: `8000`
- Randomized search iterations: `8`
- Randomized search CV folds: `2`

These values live in `repro_config.json`. The notebook reads that file first and falls back to internal defaults if it is missing.

## Model Card

### Model Summary
- Project: London residential sale-price prediction
- Prediction target: `price`
- Unit of prediction: one property listing / property record
- Problem type: supervised regression
- Primary artifact: `london_price_analysis.ipynb`

### Intended Use
- Educational and benchmarking use for tabular ML workflows
- Exploratory price estimation on similar London housing data
- Comparison of baseline vs engineered models inside a notebook setting

### Not Intended For
- Production valuation without stronger validation, monitoring, and retraining
- Mortgage underwriting, lending, insurance, or legal decisions
- Decision-making for protected groups or regulated outcomes

### Training Data
- Property-level dataset: structural and listing-related fields such as bedrooms, bathrooms, floor area, tenure, property type, coordinates, rent estimate, and sale price
- Area-level dataset: outcode-level crime, census, and points-of-interest aggregates
- Join key: `outcode`

### Feature Families
- Property structure: bedrooms, bathrooms, floor area, living rooms
- Listing context: property type, tenure, energy rating, rent estimate
- Geography: latitude, longitude, outcode
- Area context: crime totals, census variables, POI counts, property stock
- Engineered features: room-density ratios, amenity ratios, crime-per-property, and distance-to-central-London style proxies

### Modelling Approach
- Baseline model: log-target linear regression after preprocessing
- Improved model: tuned random forest with feature engineering and randomized search
- Preprocessing: numeric median imputation, categorical most-frequent imputation, categorical encoding, train/test split with fixed seed

### Evaluation
- Reported metrics: RMSE, MAE, R2
- Evaluation protocol: holdout train/test split, plus randomized search cross-validation for the improved model

### Reproducibility Assets
- Pinned dependencies in `requirements.txt`
- Fixed seeds and sampling knobs in `repro_config.json`
- Scripted setup in `setup_env.ps1`
- Scripted execution in `run_notebook.ps1`

### Risks and Limitations
- The data is geographically narrow to London and may not transfer outside the covered regions
- Area-level features can encode socioeconomic differences and should be treated carefully
- Sale-price prediction reflects historical market patterns and may reproduce spatial inequities
- The notebook is a research artifact, not a deployment-ready service

## Original Benchmark Notes
This repository also includes the original Codex benchmark instructions and prompt files used for group evaluation. Those files remain unchanged in purpose; the new reproducibility files sit alongside them so the notebook can be run repeatedly with a stable environment.

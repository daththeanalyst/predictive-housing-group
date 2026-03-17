# Agent Tooling Benchmark — MSIN0097 Predictive Analytics

Benchmarking 5 agent tools on a geospatial data science pipeline using the London Synergy Index dataset.

## Tools Tested

| Tool | Provider |
|------|----------|
| Claude Code | Anthropic |
| ChatGPT / Code Interpreter | OpenAI |
| GitHub Copilot Agent Mode | Microsoft |
| Antigravity | Google |
| Gemini Advanced | Google |

## Tasks

| # | Task | Description |
|---|------|-------------|
| 1 | Data Ingestion | Load multi-format geospatial data, audit schema, handle missing values, verify H3 integrity |
| 2 | Spatial EDA | Distribution plots, correlation heatmaps, actionable insights |
| 3 | Baseline Modelling | LR + RF binary classification for cafe presence, proper evaluation |
| 4 | Performance Improvement | Feature engineering, hyperparameter tuning, model selection |
| 5 | Debugging | Find and fix 4 planted bugs in a broken ML pipeline |

## Dataset

**London Synergy Index** — H3 hexagonal grid (~16,900 cells) across Greater London's 33 boroughs with 33 features:
- Demographics (population, age, employment, qualifications)
- Crime statistics (violent, property, antisocial behaviour)
- Transport accessibility (station distance, bus stops)
- Street-network graph centrality (betweenness, closeness, eigenvector, PageRank)
- POI co-occurrence counts (cafe, restaurant, pub, fast food, gym, bakery)

## Methodology

- Identical verbatim prompts for each task across all tools
- 2 independent runs per task-tool combination (50 total runs)
- Standardised scoring rubric: 6 dimensions x 0-3 scale
- Inter-run consistency measurement

## Structure

```
data/                 Frozen dataset files
prompts/              Standardised task prompts + broken_pipeline.py
rubric/               Scoring rubric and template CSV
results/              Per-tool, per-task, per-run logs and outputs
analysis/             Score aggregation and visualisation scripts
report/               Final report and figures
appendices/           Supporting material
CLAUDE.md             Agent collaboration log
```

## Scoring Dimensions

| Dimension | What it measures |
|-----------|-----------------|
| Correctness | Does it run? Does it meet the spec? |
| Statistical Validity | Proper methodology, no leakage, sound evaluation |
| Reproducibility | Can someone else rerun and get same results? |
| Code Quality | Readability, structure, PEP8 compliance |
| Efficiency | Iterations needed to reach acceptable solution |
| Safety | No hallucinations, no risky code, proactive warnings |

## Running the Analysis

```bash
pip install -r requirements.txt

# After filling in rubric/scoring_template.csv:
python analysis/aggregate_scores.py
python analysis/generate_heatmap.py
python analysis/consistency_analysis.py
```

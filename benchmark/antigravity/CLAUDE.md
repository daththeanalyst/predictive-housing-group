# Agent Instructions — Antigravity

## Mandatory: Update AGENT_LOG.md After Every Task

After you complete EACH prompt (Prompt A or Prompt B), you MUST:

1. Open `AGENT_LOG.md` in this folder
2. Fill in ALL fields for the run you just completed:
   - Date, start time, end time, duration
   - Number of iterations (messages / tool calls / code cells used)
   - Stage completion checkboxes
   - Data quality handling checkboxes
   - Final metrics table (RMSE, MAE, R²)
   - Any errors encountered and how they were fixed
   - List of plots saved
3. Do NOT leave any field blank — write "N/A" if not applicable

## General Rules

- Use `random_state=42` wherever applicable
- Save all work in a Jupyter notebook (.ipynb)
- Save all plots as PNG files
- Show all code and print all outputs
- Do not ask for human input — use your best judgement
- The data files `london_house_prices.csv` and `london_area_features.csv` are in this folder

## Prompts

- **Prompt A** (`prompt_a.txt`): Build a full ML pipeline (data ingestion, EDA, baseline model, improvement)
- **Prompt B** (`prompt_b.txt`): Debug a broken pipeline — find all bugs, fix them, report corrected metrics

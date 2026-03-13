# Codex (OpenAI) — Benchmark Instructions

> **Read `INSTRUCTIONS.md` (in the parent folder) first.** It explains the full process.
> This file only covers Codex-specific setup.

## What's In This Folder
- `london_house_prices.csv` — property data (417K rows)
- `london_area_features.csv` — area-level features (168 outcodes)
- `prompt_a_main.txt` — Prompt A (build a prediction model)
- `prompt_b_debugging.txt` — Prompt B (find and fix bugs in a pipeline)
- `broken_pipeline.py` — the buggy pipeline for Prompt B
- `AGENT_LOG.md` — fill this in after each run
- `SCORING.md` — scoring rubric (we'll score together as a group)

## How to Run

### Setup
1. Make sure the CSV files and broken_pipeline.py are accessible to Codex
2. Start a new Codex session

### Prompt A (do this TWICE — 2 separate sessions)
1. Start a **new** Codex session
2. Paste the full text from `prompt_a_main.txt`
3. **Do not help the agent.** Let it work on its own.
4. When done, save all generated code, plots, and outputs
5. Start a **fresh** session and repeat for Run 2

### Prompt B (do this TWICE — 2 separate sessions)
1. Start a **new** Codex session
2. Paste the full text from `prompt_b_debugging.txt` (the buggy code is included in the prompt)
3. **Do not help the agent.** Don't hint at what might be wrong.
4. When done, save the corrected code and metrics
5. Start a **fresh** session and repeat for Run 2

## Rules
- **4 runs total** (Prompt A x2, Prompt B x2)
- **Always start fresh** — never continue a previous session
- **Never help the agent** — no hints, no corrections, no suggestions
- **Save everything** — code, plots, outputs, logs
- **Fill in AGENT_LOG.md** after each run

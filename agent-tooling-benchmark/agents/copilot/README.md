# GitHub Copilot Agent Mode — Benchmark Instructions

> **Read `INSTRUCTIONS.md` (in the parent folder) first.** It explains the full process.
> This file only covers Copilot-specific setup.

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
1. Open VS Code with GitHub Copilot installed
2. Open **this folder** as a workspace (File → Open Folder)
3. Open the Copilot Chat panel and select **Agent** mode (not Ask or Edit)

### Prompt A (do this TWICE — 2 separate chat threads)
1. Start a **new** Copilot Chat thread (click +)
2. Paste the full text from `prompt_a_main.txt`
3. **Do not help the agent.** Let it work on its own.
4. When done, screenshot the chat and save any generated files
5. Start a **new** chat thread and repeat for Run 2

### Prompt B (do this TWICE — 2 separate chat threads)
1. Start a **new** Copilot Chat thread (click +)
2. Paste the full text from `prompt_b_debugging.txt` (the buggy code is included in the prompt)
3. **Do not help the agent.** Don't hint at what might be wrong.
4. When done, screenshot the chat and save the corrected code
5. Start a **new** chat thread and repeat for Run 2

## Rules
- **4 runs total** (Prompt A x2, Prompt B x2)
- **Always start fresh** — never continue a previous chat thread
- **Never help the agent** — no hints, no corrections, no suggestions
- **Save everything** — screenshots, generated scripts, plots, terminal output
- **Fill in AGENT_LOG.md** after each run

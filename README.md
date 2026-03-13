# MSIN0097 — Agent Tooling Benchmark

## Quick Start

```
git clone https://github.com/daththeanalyst/predictive-housing-group.git
```

1. Read `INSTRUCTIONS.md` — this explains everything
2. Go to your assigned folder
3. Read the `README.md` inside your folder for tool-specific setup
4. Run both prompts (2 times each = 4 runs total)
5. Fill in `AGENT_LOG.md` after each run

## Who Does What

| Person | Tool | Folder |
|--------|------|--------|
| | Claude Code | `claude-code/` |
| | Codex (OpenAI) | `codex/` |
| | GitHub Copilot Agent Mode | `copilot/` |

## What's in Each Folder

Every folder has the **exact same data and prompts** — the only difference is which AI tool you use.

| File | What it is |
|------|-----------|
| `london_house_prices.csv` | 417K London properties with prices, bedrooms, bathrooms, etc. |
| `london_area_features.csv` | Crime, census, and POI data for 168 London outcode areas |
| `prompt_a_main.txt` | **Copy-paste this into your AI tool** — asks it to build an ML model |
| `prompt_b_debugging.txt` | **Copy-paste this into your AI tool** — asks it to find bugs in code |
| `broken_pipeline.py` | The buggy code (also included in prompt B) |
| `AGENT_LOG.md` | Fill this in after each run — tracks what the AI did |
| `SCORING.md` | How we grade each run (we do this together) |

## The 3 Rules

1. **Copy-paste the prompt exactly** — don't change a single word
2. **Don't help the AI** — let it work alone, don't fix its mistakes
3. **Save everything** — screenshots, code, plots, conversation logs

## What You Do (4 Runs)

| Run | What | How |
|-----|------|-----|
| Run 1 | Prompt A | New session → paste prompt_a_main.txt → let it work → save everything |
| Run 2 | Prompt A | **Brand new session** → same prompt → save everything |
| Run 3 | Prompt B | **Brand new session** → paste prompt_b_debugging.txt → save everything |
| Run 4 | Prompt B | **Brand new session** → same prompt → save everything |

We run each prompt twice to test if the tool gives consistent results.

## After You're Done

1. Make sure your `AGENT_LOG.md` is filled in for all 4 runs
2. Put your saved files (screenshots, code, plots) in subfolders: `run1/`, `run2/`, `run3/`, `run4/`
3. Push your changes or send your folder back to the group
4. We meet to score everything together using `GROUP_SCORES.md`

## Deadline

**Report due: 20 March 2026, 10:00**

Finish your runs ASAP so we have time to score and write the report.

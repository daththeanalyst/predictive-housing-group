# Group Scoring Sheet

> Fill this in together as a group after all runs are complete.
> This table becomes the main figure in Section 3 of the report.

## Prompt A — Build the Model (Scores 0–3)

| Dimension | Claude Code Run 1 | Claude Code Run 2 | Codex Run 1 | Codex Run 2 | Copilot Run 1 | Copilot Run 2 |
|---|---|---|---|---|---|---|
| Correctness | | | | | | |
| Statistical Validity | | | | | | |
| Reproducibility | | | | | | |
| Code Quality | | | | | | |
| Efficiency | | | | | | |
| Safety | | | | | | |
| **Total /18** | | | | | | |

## Prompt B — Debug the Pipeline (Scores 0–3)

| Dimension | Claude Code Run 3 | Claude Code Run 4 | Codex Run 3 | Codex Run 4 | Copilot Run 3 | Copilot Run 4 |
|---|---|---|---|---|---|---|
| Correctness | | | | | | |
| Statistical Validity | | | | | | |
| Reproducibility | | | | | | |
| Code Quality | | | | | | |
| Efficiency | | | | | | |
| Safety | | | | | | |
| **Total /18** | | | | | | |

## Summary Table (for the report)

| Dimension | Claude Code (avg) | Codex (avg) | Copilot (avg) | Best Tool |
|---|---|---|---|---|
| Correctness | | | | |
| Statistical Validity | | | | |
| Reproducibility | | | | |
| Code Quality | | | | |
| Efficiency | | | | |
| Safety | | | | |
| **Overall avg** | | | | |

## Consistency Check

How many of the 6 dimension scores were **identical** between Run 1 and Run 2 (or Run 3 and Run 4)?

| Tool | Prompt A consistency (/6) | Prompt B consistency (/6) |
|------|--------------------------|--------------------------|
| Claude Code | | |
| Codex | | |
| Copilot | | |

## Key Findings (use these in the report)

- Which tool scored highest overall?
- Which tool was most consistent across runs?
- Which tool handled data quality best (statistical validity)?
- Which tool was most efficient (fewest iterations)?
- Did any tool detect the rentEstimate leakage without being told?
- Did any tool fail to find all 4 bugs in Prompt B?
- What surprised you?

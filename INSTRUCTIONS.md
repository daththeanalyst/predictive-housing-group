# Benchmark Instructions — READ THIS FIRST

## What Are We Doing?

We're testing 3 AI coding tools on the **same task** to compare how they perform.
Each person runs **their assigned tool** on the same data with the same prompts.
**Everyone uses the exact same prompt and the exact same data files — no changes.**

| Person | Tool | Folder |
|--------|------|--------|
| [Name] | Claude Code | `claude-code/` |
| [Name] | Codex (OpenAI) | `codex/` |
| [Name] | GitHub Copilot Agent Mode | `copilot/` |

## The Task

We give each AI tool 2 CSV files about London house prices and ask it to:
- **Prompt A:** Build a full ML pipeline (load data → explore → model → improve)
- **Prompt B:** Find and fix bugs in a broken pipeline we wrote

We do each prompt **twice** to check if the tool gives consistent results.
That's **4 runs per person** (Prompt A ×2, Prompt B ×2).

---

## What Makes It Fair

Every tool gets **identical inputs**. The only difference is the tool itself.

| What | Same across all 3? |
|------|---------------------|
| Prompt A text | Yes — word for word identical |
| Prompt B text (includes buggy code) | Yes — word for word identical |
| london_house_prices.csv | Yes — byte for byte identical |
| london_area_features.csv | Yes — byte for byte identical |
| Human intervention | Yes — none allowed |

**Do not change the prompt text.** Do not add extra instructions. Do not rephrase.
Copy-paste the exact text from the .txt file. This is what makes it a fair comparison.

---

## Step-by-Step (Everyone Follows This Exactly)

### BEFORE YOU START
1. Read the `README.md` in **your** folder — it has setup steps for your specific tool
2. Read `SCORING.md` so you know what we're measuring

### RUN 1 — Prompt A
1. Open your tool in a **brand new session** (no history, no previous context)
2. Make sure both CSV files are accessible to the tool
3. Open `prompt_a_main.txt`, copy the **entire text**, paste it into your tool
4. Press enter / send and **walk away**
5. **DO NOT:**
   - Type anything else to the agent
   - Answer its questions (if it asks, just say "use your best judgement")
   - Fix its errors for it
   - Suggest what it should try next
6. When the agent finishes (or gets stuck), **save everything:**
   - The full conversation / chat log (screenshot or export)
   - Any Python scripts it created
   - Any plots / PNG files it generated
   - The final metrics it reported (RMSE, MAE, R²)
7. Note the **time** it took (start to finish) and how many **iterations** (messages / tool calls / code cells) it used
8. Open `AGENT_LOG.md` and fill in the **Run 1** section

### RUN 2 — Prompt A (repeat)
1. **Start a completely new session** — the agent must NOT remember Run 1
2. Repeat steps 2–8 exactly the same way
3. Fill in the **Run 2** section of `AGENT_LOG.md`

### RUN 3 — Prompt B
1. **Start a completely new session**
2. Make sure both CSV files are accessible
3. Open `prompt_b_debugging.txt`, copy the **entire text** (the buggy code is included), paste it
4. Press enter / send and **walk away**
5. Same rules — **do not help the agent**
6. When done, save the corrected code and the new metrics it reports
7. Fill in the **Run 3** section of `AGENT_LOG.md`

### RUN 4 — Prompt B (repeat)
1. **Start a completely new session**
2. Repeat steps 2–7
3. Fill in the **Run 4** section of `AGENT_LOG.md`

---

## The Golden Rules

These are critical. If anyone breaks these, the comparison is unfair.

| Rule | Why |
|------|-----|
| **Same prompt, word for word** | We're comparing tools, not prompts. Copy-paste exactly. |
| **Fresh session every run** | Memory from a previous run biases the results. |
| **Never help the agent** | If you fix its error, you're testing yourself, not the tool. |
| **Save everything** | We need evidence for the report appendix. |
| **Fill in AGENT_LOG.md after each run** | You'll forget details if you wait. Do it immediately. |
| **"Use your best judgement"** | If the agent asks you a question, this is the only thing you say. |

---

## What to Save (Checklist)

After each run, make sure you have:

- [ ] Full conversation log (screenshot, export, or copy-paste)
- [ ] All Python scripts the agent wrote
- [ ] All plots / charts (PNG files)
- [ ] Final metrics (RMSE, MAE, R² — write these in AGENT_LOG.md)
- [ ] Time taken (start → finish)
- [ ] Number of iterations (messages, tool calls, or code cells)
- [ ] Completed AGENT_LOG.md section for that run

Put all saved files in a subfolder like `run1/`, `run2/`, `run3/`, `run4/` inside your folder.

---

## How We Assess (This Is NOT About Who Gets the Best R²)

We **do not** just pick the tool with the highest accuracy. The assignment
requires us to compare tools across **6 dimensions**. Each run gets scored
0–3 on each dimension (see `SCORING.md` for details).

### The 6 Dimensions

| Dimension | What it means | Example of a 3 vs a 0 |
|-----------|---------------|----------------------|
| **Correctness** | Does the code run? Does it do what was asked? | 3 = runs perfectly, covers all stages. 0 = crashes. |
| **Statistical Validity** | Are the methods sound? Any mistakes? | 3 = detects leakage, uses proper metrics, handles skew. 0 = major flaw like data leakage. |
| **Reproducibility** | Can someone else rerun it and get the same result? | 3 = uses random_state, clear code. 0 = can't rerun at all. |
| **Code Quality** | Is the code clean and well-structured? | 3 = modular, well-commented. 0 = unreadable mess. |
| **Efficiency** | How many attempts did it need? | 3 = got it right first try. 0 = needed 10+ attempts. |
| **Safety** | Did it warn about risks? Any hallucinations? | 3 = proactively warns about issues. 0 = makes things up. |

### How to Score

1. After all 3 people finish their 4 runs, we meet as a group
2. Go through each run together, looking at the conversation logs
3. Score each run on all 6 dimensions using `SCORING.md`
4. Fill in the group scoring table (see `GROUP_SCORES.md`)

### What Goes in the Report

The report compares tools **across dimensions**, not just final accuracy:
- "Claude Code scored highest on efficiency (first-attempt solutions)"
- "Codex scored highest on statistical validity (detected leakage unprompted)"
- "Copilot scored lowest on reproducibility (different results each run)"

**Consistency matters:** If a tool scores 3 on Run 1 but 1 on Run 2 for the
same prompt, that's a reproducibility problem — even if Run 1 was great.

---

## Timeline

| What | When |
|------|------|
| Everyone finishes 4 runs + AGENT_LOG.md | **This weekend** |
| Group scoring session | After all runs done |
| Report deadline | **20 March 2026, 10:00** |

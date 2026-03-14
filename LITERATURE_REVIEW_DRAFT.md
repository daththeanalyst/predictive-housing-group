# Literature Review — Draft (Section 1, 30% of marks, ~550-600 words)

> This is a near-final draft. Items marked **[TODO: ...]** need updating after benchmark runs are complete.

---

## 1. Literature Review

Large language model (LLM) agents extend beyond static text generation to plan, invoke external tools, and interact with execution environments across multi-step tasks (Yao et al., 2023; Schick et al., 2023). In data science and software engineering, such agents promise to automate repetitive coding, enforce reproducible pipelines, and augment human analysts through collaborative workflows (Wu et al., 2023). Yet their adoption raises a fundamental tension. The same autonomy that makes agents productive also makes their failures difficult to detect, particularly in analytical contexts where statistical validity and domain correctness are non-negotiable.

The literature reveals a progression of increasingly sophisticated agent architectures, each addressing limitations of its predecessors. ReAct established the foundation by interleaving reasoning with tool-calling, adapting plans after each observation (Yao et al., 2023). However, its lack of long-term memory motivated Reflexion, which stores post-failure self-critiques in episodic memory to avoid repeating mistakes (Shinn et al., 2023). Where both remain reactive, plan-and-execute approaches such as Voyager proactively decompose goals into reusable code "skills", although this paradigm has been demonstrated primarily in simplified environments and its transfer to messy, multi-source data pipelines remains unvalidated (Wang et al., 2023). Recognising that single-agent architectures struggle with complex multi-step workflows, multi-agent frameworks such as AutoGen distribute planning across specialised conversational roles, including a coder, critic, and human proxy (Wu et al., 2023). Complementary to these architectural choices, Toolformer addresses the question of when to invoke external tools through self-supervised learning (Schick et al., 2023). Test-driven generation uses tests as formal acceptance criteria to gate code quality (Mathews and Nagappan, 2024; Mundler et al., 2024), and retrieval-augmented generation (RAG) supplies agents with external memory for documentation and data context (Lewis et al., 2020). Notably, most current systems rely on prompt-engineered heuristics for tool selection rather than learned policies, raising questions about robustness when agents encounter unfamiliar data modalities or domain-specific validation requirements.

Evaluation has evolved from general-purpose to domain-specific benchmarks, with each generation exposing new weaknesses. AgentBench evaluated agents across eight diverse environments, establishing that poor long-horizon reasoning and instruction-following are the primary obstacles for LLM agents (Liu et al., 2024). SWE-bench narrowed the lens to real software engineering, finding that the strongest models resolved fewer than 2% of 2,294 GitHub issues at launch (Jimenez et al., 2024). SWT-Bench then revealed that code-repair agents surprisingly outperform dedicated test generators, suggesting that deep code context understanding transfers to verification tasks (Mundler et al., 2024). Most recently, data-science-specific benchmarks have emerged. DA-Code found that the best agent achieved only 30.5% accuracy on 500 realistic analytical tasks (Huang et al., 2024), and DataSciBench introduced a Task-Function-Code formalisation for end-to-end workflows (Zhang et al., 2025). Critically, none of these benchmarks report human-analyst baselines, making it difficult to contextualise agent performance against the practitioners they aim to augment. Moreover, all operate on standard tabular or textual data, and domain-specific validation challenges such as skewed regression targets and multi-source data integration remain entirely unaddressed.

Three systemic challenges persist across this literature. First, failure modes compound silently. Agents propagate errors across long-horizon tasks without self-correction (Wang et al., 2023), underutilise available tools without explicit training (Schick et al., 2023), and produce code that satisfies incomplete test suites while containing subtle statistical errors, including data leakage and metric confusion, that automated checks fail to catch (Mundler et al., 2024; Mathews and Nagappan, 2024). Second, reproducibility has improved through open evaluation harnesses. SWE-bench, DA-Code, and AgentBench all release public datasets and toolkits (Jimenez et al., 2024; Huang et al., 2024; Liu et al., 2024). Yet the non-deterministic nature of LLM inference means that identical prompts can yield different outputs across runs. Third, human oversight remains essential. AutoGen explicitly supports human-in-the-loop modes for this reason (Wu et al., 2023), and even Reflexion's 91% pass rate on HumanEval addresses only small, isolated coding problems without consideration of security, maintainability, or domain validity (Shinn et al., 2023).

Despite this growing body of work, a significant gap remains. No existing study provides a controlled, same-prompt comparison of commercial agent tools on a realistic, multi-source data science pipeline. Current benchmarks test models on clean tabular data and none evaluate multi-source data integration, skewed regression targets, or domain-specific validation challenges such as spatial feature engineering. This report addresses that gap by benchmarking **[TODO: update number]** three agent tools on a London house price prediction pipeline requiring data merging, outlier handling, distributional reasoning, and iterative model improvement, using identical prompts, quantitative rubric scoring, and reproducibility auditing across duplicate runs.

---

## Bibliography (APA)

Huang, Y., et al. (2024). DA-Code: Agent data science code generation benchmark for large language models. *Proceedings of EMNLP 2024*. arXiv:2410.07331

Jimenez, C. E., et al. (2024). SWE-bench: Can language models resolve real-world GitHub issues? *Proceedings of ICLR 2024*. arXiv:2310.06770

Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS 33*. arXiv:2005.11401

Liu, X., et al. (2024). AgentBench: Evaluating LLMs as agents. *Proceedings of ICLR 2024*. https://openreview.net/forum?id=zAdUB0aCTQ

Mathews, N. S., & Nagappan, M. (2024). Test-driven development for code generation. arXiv:2402.13521

Mundler, N., et al. (2024). SWT-Bench: Testing and validating real-world bug-fixes with code agents. arXiv:2406.12952

Schick, T., et al. (2023). Toolformer: Language models can teach themselves to use tools. *NeurIPS 36*. arXiv:2302.04761

Shinn, N., et al. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 36*. arXiv:2303.11366

Wang, G., et al. (2023). Voyager: An open-ended embodied agent with large language models. arXiv:2305.16291

Wu, Q., et al. (2023). AutoGen: Enabling next-gen LLM applications via multi-agent conversation. arXiv:2308.08155

Yao, S., et al. (2023). ReAct: Synergizing reasoning and acting in language models. *Proceedings of ICLR 2023*. arXiv:2210.03629

Zhang, D., et al. (2025). DataSciBench: An LLM agent benchmark for data science. arXiv:2502.13897

---

## Post-Benchmark TODOs

After all agent runs are complete, update the following before submitting:

### 1. Final paragraph — update tool count and names
- Change "three agent tools" to the exact tools used (e.g., "Claude Code, Codex, and Antigravity")
- If you end up using more or fewer than 3, update the number

### 2. Connect findings to literature
Add 1-2 sentences in the final paragraph referencing your actual results. Examples:
- If an agent failed on leakage detection: *"consistent with DA-Code's finding that agents achieve only 30.5% on realistic tasks (Huang et al., 2024)"*
- If one agent self-corrected well: *"aligning with Reflexion's episodic memory approach (Shinn et al., 2023)"*
- If tools varied in debugging: *"supporting SWT-Bench's observation that code-repair performance varies significantly across agent architectures (Mundler et al., 2024)"*

### 3. Check word count
- Target: 550-600 words (current draft is ~580)
- The rest of the report needs ~1,400 words across Sections 2-4

### 4. Sections 2-4 should reference these papers
When writing the other sections, tie back to the lit review:
- **Section 2 (Benchmarking)**: Reference DA-Code/DataSciBench when describing your methodology
- **Section 3 (Comparative Analysis)**: Use ReAct/Reflexion/AutoGen to explain WHY tools differed
- **Section 4 (Reflection)**: Reference the "human oversight" theme — did your results confirm it?

### 5. Consistency check
- Ensure all 12 papers cited in text appear in bibliography (and vice versa)
- Ensure tool names match across all sections
- Ensure metrics referenced in lit review match what you actually measured

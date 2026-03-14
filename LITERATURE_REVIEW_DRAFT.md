# Literature Review — Draft (Section 1, 30% of marks)

> **Word count: ~1,500 words** — will need trimming to fit the 2,000-word total report.
> Items marked **[TODO]** need updating after benchmark runs are complete.

---

## 1. Literature Review

Agentic AI refers to LLM-based systems that go beyond one-shot generation by planning, retrieving information, calling tools, interacting with environments and revising outputs over multiple steps. This matters for data science and software development because realistic tasks such as debugging, model evaluation, data cleaning and pipeline repair require sequential decision-making, external resource use and explicit correctness checks rather than fluent text alone. Foundational work on retrieval-augmented generation already showed that combining a parametric model with external memory improves knowledge-intensive task performance, creating the basis for later agentic workflows that rely on grounded evidence and dynamic information access (Lewis et al., 2020). More recent work extends this into systems that decide when to reason, when to act and when to use tools, which is directly aligned with the assignment brief's focus on planning, tool use and verification.

A central taxonomy in the literature is the ReAct-style paradigm. Yao et al. (2023) propose ReAct, in which models interleave reasoning traces with actions, enabling them to think through a problem while also querying an external environment. This architecture is especially relevant for data science tasks because successful execution often depends on intermediate checks, tool use and error recovery rather than a single static response. ReAct therefore provides a useful conceptual bridge between pure prompting methods and more operational agent systems, since it explicitly ties together internal reasoning and external action in a transparent sequence (Yao et al., 2023). In practical benchmarking terms, this means agent quality should be judged not only by the final answer but also by whether the intermediate action sequence is sensible, auditable and efficient.

A second major theme is tool calling. Schick et al. (2023) introduce Toolformer, showing that a language model can learn in a self-supervised manner to decide when to use external tools such as search, translation or calculation APIs and how to incorporate the result into generation. This is a major step for software and analytics use cases because it shifts LLMs from passive text predictors towards systems that can invoke external capabilities when internal generation is insufficient. Tool use at scale raises the further problem of choosing the right tool from many candidates. Braunschweiler, Doddipatla and Zorila (2025) address this in ToolReAGt, which frames tool choice as a retrieval problem and uses a ReAct-like loop to iteratively identify suitable tools for complex tasks. Their results on the UltraTool benchmark show improved retrieval performance relative to a baseline RAG method, suggesting that the effectiveness of agentic AI depends not just on tool availability but on structured tool-selection policies.

Retrieval-augmented workflows form a third core category. Lewis et al. (2020) establish the RAG framework by integrating a retriever and generator so that external knowledge can be fetched during inference rather than being stored only in model parameters. This is particularly relevant to analytics settings where models must justify claims with current evidence and where static parametric memory is insufficient. Retrieval also supports traceability: when an output depends on identifiable retrieved material, it is easier to verify or contest the basis of a claim. In this sense, retrieval is not merely a performance optimisation, but a mechanism that can support reproducibility and accountability in agentic systems (Lewis et al., 2020).

The literature also shows that retrieval can be embedded into test-driven generation. Shin et al. (2024) examine retrieval-augmented test generation for machine-learning libraries and compare several prompting and retrieval strategies using sources such as API documentation, GitHub issues and Stack Overflow. Their findings show that retrieval does not improve every metric, but API-level retrieval improves line coverage and issue-oriented retrieval can help uncover previously unknown bugs (Shin et al., 2024). This is highly relevant to predictive analytics because it demonstrates that stronger agent workflows are not simply those that generate code quickly, but those that use external knowledge to create better validation artefacts and testing procedures. It also maps directly onto the brief's required taxonomy of test-driven generation.

A fourth major theme is evaluation. Benchmarks such as AgentBench, SWE-bench and WebArena show that the field increasingly evaluates LLMs as agents rather than as isolated text generators. Liu et al. (2023) introduce AgentBench as a benchmark suite for evaluating LLMs across multiple interactive environments, arguing that agentic competence requires more than static language modelling because agents must perceive feedback, plan actions and adapt to environment dynamics. Jimenez et al. (2023) introduce SWE-bench, which evaluates models on real GitHub issues from Python repositories and shows that even strong models solve only a small proportion of realistic software-engineering problems. Zhou et al. (2023) present WebArena, a realistic and reproducible web environment for evaluating autonomous agents on long-horizon web tasks, reporting that even strong GPT-4-based agents perform far below humans. Collectively, these papers are important because they shift evaluation away from isolated benchmark questions and toward realistic, process-heavy tasks, which is exactly the orientation required by this assignment's practical benchmarking section.

The benchmark literature also highlights a persistent gap between apparent fluency and operational reliability. SWE-bench is especially relevant because resolving real software issues requires navigating long contexts, modifying multiple files and reasoning about execution consequences, which closely mirrors the complexity of real data-science pipelines (Jimenez et al., 2023). The benchmark therefore supports a core argument for your report: an agent that produces polished-looking code or explanations may still be weak when judged on correctness, reproducibility and end-to-end task completion. WebArena reinforces the same point from a different angle, showing that long-horizon interactive tasks remain difficult even for advanced models, which suggests that apparent planning ability in prompts does not automatically translate into robust sequential performance (Zhou et al., 2023).

The literature further shows that multi-agent and workflow-structured systems are becoming a major design pattern. Wu et al. (2023) introduce AutoGen, a framework for building LLM applications through multi-agent conversation, where specialised agents interact to complete tasks. Hong et al. (2023) present MetaGPT, which explicitly models software-development roles in a multi-agent collaborative framework inspired by human organisational structures. These papers are relevant because they suggest that planning-and-execution can be distributed across specialised roles rather than placed in a single monolithic agent. For data-science practice, this opens a useful taxonomy in which different agents can be responsible for coding, reviewing, testing, documentation or critique, although this added structure also creates new coordination and verification challenges.

Another critical theme is reflection and self-correction. Shinn et al. (2023) propose Reflexion, in which agents maintain reflective memory and use verbal feedback from prior attempts to improve later decisions. Madaan et al. (2023) propose Self-Refine, an iterative feedback-and-refinement framework where the model critiques and revises its own outputs without additional training. Gou et al. (2023) extend this logic in CRITIC, where the model uses external tools to critique and progressively revise its responses. These papers are particularly useful because they connect directly to verification and failure reduction: rather than assuming the first output is correct, they design workflows in which models inspect, critique and revise outputs, often with external signals. This aligns closely with the assignment's emphasis on failure modes, verification and reproducibility.

The strongest evidence on reproducibility and failure modes comes from REPRO-Bench. Hu et al. (2025) test whether agentic AI systems can assess the reproducibility of real social-science research using the full research artefacts, including papers, code and data packages. Their findings are sobering: baseline agents perform poorly, and the paper documents recurring failures such as poor repository navigation, weak log inspection, dependency-handling problems and difficulty comparing reproduced outputs with published findings (Hu et al., 2025). This is highly relevant to predictive analytics because reproducibility is not merely a documentation issue; it is a property of the entire workflow, including environment setup, code execution, data dependencies and results validation. The literature therefore suggests that current agent tools remain brittle when tasks become messy, long-horizon and execution-dependent.

Human oversight remains essential within this landscape, even where not all papers explicitly label themselves as "human-in-the-loop". Multi-agent frameworks such as AutoGen include human participation as one possible agent role, and benchmark papers such as SWE-bench and WebArena reveal how far current systems remain from reliable autonomous performance on realistic tasks. The implication for data science is that agent tooling should usually be embedded in a supervised workflow where humans review experimental design, evaluation protocols, leakage risks and final interpretations. Put differently, the opportunity lies not in full automation but in structured augmentation: agents can accelerate drafting, testing, tool use and exploration, while humans remain responsible for validation and accountability.

**[TODO: After benchmarks, add 1-2 sentences here connecting your actual results to the themes above. E.g.:]**
- *"Our benchmarking results confirm this pattern: [Tool X] detected target leakage autonomously while [Tool Y] propagated it silently, consistent with the failure-mode taxonomy described above."*
- *"The consistency gap between duplicate runs aligns with the non-deterministic inference challenge highlighted by the benchmark literature."*

Taken together, the literature supports a clear synthesis. ReAct provides a canonical reasoning-and-acting pattern for sequential problem solving (Yao et al., 2023). Toolformer and ToolReAGt define a tool-calling taxonomy that ranges from learned API invocation to retrieval-based tool selection (Schick et al., 2023; Braunschweiler, Doddipatla and Zorila, 2025). Lewis et al. (2020) and Shin et al. (2024) anchor retrieval-augmented workflows and test-driven generation. AgentBench, SWE-bench and WebArena demonstrate how evaluation has shifted toward realistic agent tasks rather than isolated prompts (Liu et al., 2023; Jimenez et al., 2023; Zhou et al., 2023). Reflexion, Self-Refine and CRITIC show the importance of reflection, revision and external critique in mitigating failure (Shinn et al., 2023; Madaan et al., 2023; Gou et al., 2023). Finally, REPRO-Bench shows why reproducibility and verification must remain central evaluation dimensions for agentic AI in data science and software development (Hu et al., 2025).

For this report, the most defensible conclusion is that agentic AI offers real promise for complex data-science and software tasks, but only when systems are designed around structured planning, selective retrieval, disciplined tool use, explicit testing and strong human verification. The literature does not support treating agents as autonomous and reliably correct black boxes; instead, it supports benchmarking them as workflow components whose value depends on correctness, reproducibility, transparency and safe failure handling. **[TODO: Update "three agent tools" to exact tool names once finalized]** This report addresses that gap by benchmarking three agent tools — Claude Code, Codex, and Antigravity — on a London house price prediction pipeline requiring data merging, outlier handling, distributional reasoning, and iterative model improvement, using identical prompts, quantitative rubric scoring, and reproducibility auditing across duplicate runs.

---

## Harvard References

Braunschweiler, N., Doddipatla, R. and Zorila, T.-C. (2025) 'ToolReAGt: Tool Retrieval for LLM-based Complex Task Solution via Retrieval Augmented Generation', in *Proceedings of the 3rd Workshop on Towards Knowledgeable Foundation Models (KnowFM)*, pp. 75-83. Available at: https://aclanthology.org/2025.knowllm-1.7/ (Accessed: 14 March 2026).

Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang, Y., Duan, N. and Hou, W. (2023) 'CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing', arXiv. Available at: https://arxiv.org/abs/2305.11738 (Accessed: 14 March 2026).

Hong, S., Zhuge, M., Chen, J., Zheng, X., Cheng, Y., Zhang, C., Wang, J., Wang, Z., Yau, S.K.S., Lin, Z., Zhou, L., Ran, C., Xiao, L., Wu, C. and Schmidhuber, J. (2023) 'MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework', arXiv. Available at: https://arxiv.org/abs/2308.00352 (Accessed: 14 March 2026).

Hu, C., Zhang, L., Lim, Y., Wadhwani, A., Peters, A. and Kang, D. (2025) 'REPRO-Bench: Can Agentic AI Systems Assess the Reproducibility of Social Science Research?', *Findings of the Association for Computational Linguistics: ACL 2025*, pp. 23616-23626. Available at: https://aclanthology.org/2025.findings-acl.1210/ (Accessed: 14 March 2026).

Jimenez, C.E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2023) 'SWE-bench: Can Language Models Resolve Real-World GitHub Issues?', arXiv. Available at: https://arxiv.org/abs/2310.06770 (Accessed: 14 March 2026).

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Kuttler, H., Lewis, M., Yih, W.-t., Rocktaschel, T., Riedel, S. and Kiela, D. (2020) 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks', *Advances in Neural Information Processing Systems*, 33. Available at: https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html (Accessed: 14 March 2026).

Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., Zhang, S., Deng, X., Zeng, A., Du, Z., Zhang, C., Shen, S., Zhang, T., Su, Y., Sun, H., Huang, M., Dong, Y. and Tang, J. (2023) 'AgentBench: Evaluating LLMs as Agents', arXiv / ICLR 2024. Available at: https://arxiv.org/abs/2308.03688 (Accessed: 14 March 2026).

Madaan, A., Tandon, N., Gupta, P., Hallinan, S., Gao, L., Wiegreffe, S., Alon, U., Dziri, N., Prabhumoye, S., Yang, Y., Gupta, S., Ashok, A., Jagannatha, A.N., Shen, S., Rajani, N. and Clark, P. (2023) 'Self-Refine: Iterative Refinement with Self-Feedback', *Advances in Neural Information Processing Systems*. Available at: https://arxiv.org/abs/2303.17651 (Accessed: 14 March 2026).

Schick, T., Dwivedi-Yu, J., Dessi, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N. and Scialom, T. (2023) 'Toolformer: Language Models Can Teach Themselves to Use Tools', *Advances in Neural Information Processing Systems*. Available at: https://openreview.net/forum?id=Yacmpz84TH (Accessed: 14 March 2026).

Shin, J., Shiri Harzevili, N., Aleithan, R., Hemmati, H. and Wang, S. (2024) 'Retrieval-Augmented Test Generation: How Far Are We?', arXiv. Available at: https://arxiv.org/abs/2409.12682 (Accessed: 14 March 2026).

Shinn, N., Cassano, F., Labash, B., Gopinath, A., Narasimhan, K. and Yao, S. (2023) 'Reflexion: Language Agents with Verbal Reinforcement Learning', *Advances in Neural Information Processing Systems*. Available at: https://arxiv.org/abs/2303.11366 (Accessed: 14 March 2026).

Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A.H., White, R.W., Burger, D. and Wang, C. (2023) 'AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation', arXiv. Available at: https://arxiv.org/abs/2308.08155 (Accessed: 14 March 2026).

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. and Cao, Y. (2023) 'ReAct: Synergizing Reasoning and Acting in Language Models', arXiv. Available at: https://arxiv.org/abs/2210.03629 (Accessed: 14 March 2026).

Zhou, S., Xu, F.F., Zhu, H., Zhou, X., Lo, R., Sridhar, A., Cheng, X., Ou, T., Bisk, Y., Fried, D., Alon, U. and Neubig, G. (2023) 'WebArena: A Realistic Web Environment for Building Autonomous Agents', arXiv / ICLR 2024. Available at: https://arxiv.org/abs/2307.13854 (Accessed: 14 March 2026).

---

## Post-Benchmark TODOs

After all agent runs are complete, update the following before submitting:

### 1. Update tool names in final paragraph
- Replace "Claude Code, Codex, and Antigravity" with exact tools used
- Update count if different from 3

### 2. Add result-linking sentences
The **[TODO]** marker in the text shows where to insert 1-2 sentences connecting your benchmark findings to the literature themes. Pick from these templates based on what you observe:

- **If an agent missed leakage:** *"Our results confirm this: [Tool X] failed to detect rentEstimate leakage, consistent with REPRO-Bench's finding that agents struggle with validation tasks (Hu et al., 2025)."*
- **If an agent self-corrected:** *"[Tool X]'s iterative debugging aligns with the Reflexion paradigm of verbal self-correction (Shinn et al., 2023)."*
- **If consistency varied across runs:** *"The divergence between duplicate runs supports the non-deterministic inference challenge noted across benchmarks (Liu et al., 2023; Jimenez et al., 2023)."*
- **If one tool was clearly better at planning:** *"[Tool X]'s structured stage-by-stage approach mirrors the ReAct pattern of interleaving reasoning with action (Yao et al., 2023)."*

### 3. Word count management
- Current draft: ~1,500 words
- Total report budget: 2,000 words
- Lit review target: 30% = ~600 words
- **You will need to trim ~900 words OR confirm with professor that the word limit is flexible**
- Prioritise keeping: opening paragraph, evaluation theme, reflection theme, final synthesis
- Candidates for cutting/condensing: tool-calling section (merge with RAG), MetaGPT paragraph (fold into AutoGen mention)

### 4. Cross-reference with other sections
- **Section 2 (Benchmarking methodology):** Cite AgentBench/SWE-bench when justifying your scoring rubric
- **Section 3 (Comparative Analysis):** Use ReAct/Reflexion/CRITIC to explain WHY tools performed differently
- **Section 4 (Reflection):** Reference the "human oversight" conclusion — did your results confirm or challenge it?

### 5. Final consistency check
- All 16 papers cited in text must appear in references (and vice versa)
- Tool names must match across all 4 report sections
- Harvard referencing style must be consistent throughout

# Literature Review Guide — Agent Tooling for Data Science

> Reference document for Section 1 (30% of marks, ~550-600 words in final report)

---

## 1. Suggested Structure

1. **Introduction**
   - Define "LLM agents for data science/coding" and why they matter (automation, reproducibility, human-AI collaboration)

2. **Methodological Paradigms**
   - ReAct / think-then-act
   - Plan-and-execute (skills, curricula, multi-step plans)
   - Multi-agent and conversational frameworks
   - Tool-calling and API-centric agents
   - Test-driven generation and verification
   - RAG as the knowledge layer

3. **Thematic Analysis Across Papers**
   - How do agents plan?
   - How do they use tools?
   - When and why do they fail?
   - Reproducibility and evaluation
   - Human oversight: do humans still need to check?

4. **Critical Discussion and Gaps**
   - Where current agents break down on realistic data-science / software tasks

5. **Conclusion**
   - What this implies for using such agents in real analytics/coding workflows

> You can almost drop sections 2-3 directly into your essay, then add your own critical voice and transitions.

---

## 2. Core Paper Set (11+ citable papers)

### ReAct — think-then-act
- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models"
- [par.nsf.gov](https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models)
- [NeurIPS proceedings](https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf)

### Reflexion — self-reflective language agents
- Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning"
- [OpenReview](https://openreview.net/pdf?id=LfyYSHGQMZ)

### Voyager — plan-and-execute with a skill library
- Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models"
- [Princeton](https://collaborate.princeton.edu/en/publications/react-synergizing-reasoning-and-acting-in-language-models/)

### Toolformer — LMs learning to call APIs
- Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools"
- [OpenReview](https://openreview.net/forum?id=vAElhFcKW6)

### AutoGen — multi-agent conversation framework
- Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework"
- [arXiv](https://arxiv.org/abs/2305.16291)

### DA-Code / DA-Agent — data-science code agents benchmark
- Huang et al., "DA-Code: Agent Data Science Code Generation Benchmark for Large Language Models"
- [arXiv](https://arxiv.org/abs/2308.08155v1)

### OpenDevin — generalist software developer agents
- "OpenDevin: An Open Platform for AI Software Developers as Generalist Agents"
- [OpenReview](https://openreview.net/forum?id=BAakY1hNKS)

### Code Agents as Testers — agents generating tests
- Mundler et al., "Code Agents are State of The Art Software Testers"
- [Microsoft AutoGen docs](https://microsoft.github.io/autogen/0.2/docs/Use-Cases/agent_chat/)

### TDD for LLM code generation — test-driven generation
- Mathews & Nagappan, "Test-Driven Development for Code Generation"
- [arXiv](https://arxiv.org/abs/2302.04761)

### RAG — retrieval-augmented generation
- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- [OpenReview](https://openreview.net/forum?id=Yacmpz84TH)

> Optional: treat RAG as background method and focus 10 agent papers on the others.

---

## 3. Grouping by Required Themes

### 3.1 How do agents plan?

**ReAct (think-then-act):**
- Planning is *online* and interleaved: the model alternates between "Thought:" (reasoning) and "Action:" (e.g. call Wikipedia API), updating its plan after each observation.

**Plan-and-execute / curricula (Voyager):**
- Voyager uses an **automatic curriculum** to pick high-level goals and a **skill library** of code programs to execute them — classic plan-then-execute at the task level.

**Self-reflection (Reflexion):**
- Adds an explicit *post-episode planning step*: after failure, the agent writes a reflection and stores it in memory to influence future plans.

**Multi-agent planning (AutoGen, OpenDevin):**
- AutoGen uses **conversation as planning**: specialized agents (coder, critic, user proxy) negotiate a plan via dialogue.
- OpenDevin supports orchestrating agents over shared tools (shell, browser, editor), so planning includes deciding which tool and which agent acts next.

> **In write-up:** contrast *single-agent ReAct* vs *multi-agent conversational planning* vs *curriculum/skill-library planning*.

---

### 3.2 How do they use tools?

**Tool calling as first-class action (Toolformer):**
- Learns *when* to call tools and *which* APIs (calculator, search, QA) via self-supervision on annotated pretraining data.

**Code/runtime as tool (Voyager, DA-Agent):**
- Voyager treats *code* as its action space, using execution feedback and errors to refine programs.
- DA-Agent operates in an executable DS environment; tasks require generating Python/SQL that manipulates real data.

**Rich developer toolchains (OpenDevin, AutoGen):**
- OpenDevin agents interact with shell, code editor and browser — evaluated on SWE-Bench and web tasks.
- AutoGen agents integrate arbitrary tools and optional human inputs via multi-agent dialogue.

**RAG as a tool:**
- RAG uses a dense retriever as external memory; in agent setups, "retrieve(documents)" becomes another tool call inside a ReAct or AutoGen loop.

> **Tip:** make a small table listing "Tools available" and "How decisions are made about tool use" for each system.

---

### 3.3 When do they fail?

Build a dedicated "Failure Modes" section with concrete numbers:

| System | Failure | Evidence |
|--------|---------|----------|
| **DA-Code** | Hard DS tasks are still very hard | DA-Agent reaches only ~**30.5% accuracy** on 500 real tasks |
| **ReAct** | Hallucinations and error propagation | Improves QA by forcing evidence fetching, but doesn't eliminate hallucination |
| **Voyager** | Compounding errors in long-horizon plans | Cascades when early skills/assumptions are wrong; some trajectories stall |
| **Toolformer** | Under-use of tools | Without explicit training, LMs under-use tools even when they would help |
| **Code Agents + TDD** | Fragile/incomplete tests | Tests improve precision but incomplete coverage means wrong code can still pass |

> **Strong critical angle:** benchmarks show promising but nowhere-near-autonomous performance in realistic settings.

---

### 3.4 Can you reproduce their work?

Comment on *reproducibility* (not actually reproduce everything):

**Clearly reproducible (benchmark + code released):**
- Voyager: open-sources full codebase, prompts, and MineDojo evaluation setup
- DA-Code: public benchmark website + GitHub with 500 executable tasks
- OpenDevin: MIT-licensed platform with integrated benchmarks

**Frameworks as substrates:**
- AutoGen: open-source framework where you can re-implement many patterns (ReAct-style, multi-agent coding) in a common codebase

> **Essay line:** "For DS agents, DA-Code and OpenDevin provide the most realistic and reproducible environments; earlier works often rely on bespoke setups that are harder to replicate."

---

### 3.5 Do humans need to check their output?

**Human-in-the-loop by design (AutoGen):**
- Explicitly supports modes where **humans join agent conversations** to guide or approve decisions.

**Tests as encoded human oversight (TDD, Code Agents):**
- TDD treats test suites (usually human-written) as formalized specs that gate acceptance.
- Code agents that generate tests show precision doubles when candidate fixes are filtered by generated tests.

**Sandboxing & benchmarks (OpenDevin, DA-Code):**
- OpenDevin emphasizes safe sandboxed environments — implies unconstrained agents are unsafe without controls.
- DA-Code's ~30% accuracy strongly suggests unaudited outputs would be unreliable for real analytics.

**High scores ≠ production-ready (Reflexion):**
- Even with 91% pass@1 on HumanEval, operates only on small isolated coding problems — doesn't address security, interpretability, or maintainability.

> **Concluding line:** "Across benchmarks and frameworks, tests, sandboxes and humans remain essential; none of the surveyed systems support truly unsupervised deployment for high-stakes data-science or software engineering."

---

## 4. Paradigm Mapping (quick reference)

### ReAct / think-then-act
- **Core paper:** ReAct (Yao et al.)
- **Extended in:** Reflexion (adds self-reflection), Voyager (ReAct-like loops around code skills), DA-Agent (reasoning + execution)

### Plan-and-execute
- **Voyager:** automatic curriculum + skill library; plans goals then generates/executes code
- **AutoGen:** one agent plans, another executes via conversation

### Tool calling
- **Toolformer:** explicit learning of API call decisions
- **OpenDevin:** shell, editor, browser as tools; agents decide when/how
- **AutoGen:** LLMs + tools + humans via unified conversation interface

### Test-driven generation
- **TDD for code gen:** tests given with problems, code must satisfy them
- **Code Agents as Testers:** agents generate tests that drive/filter code repair; SWE-AGENT gains precision
- **Reflexion:** uses feedback signals (including test results) as verbal reinforcement

### RAG (Retrieval-Augmented Generation)
- **Base method:** Lewis et al. (2020)
- **In agents:** retrieval wired as a tool inside ReAct or AutoGen loops to fetch docs, code, or schemas before generation

> Don't need a separate subsection for each paradigm — weave them through thematic sections with concrete examples.

---

## 5. How to Use This Guide

1. **Decide your angle** — e.g. "How reliable are LLM agents for real data-science pipelines?" or "Design patterns for tool-using code agents"

2. **Reuse the sectioning and citations** but rewrite in your own voice and tighten to word limit (~600 words)

3. **Add 1-2 paragraphs of critical reflection:**
   - What's missing from current benchmarks? (data privacy, messy spreadsheets, stakeholder communication)
   - How would these systems integrate into a realistic MSc-level analytics project?

4. **Synthesise thematically, NOT paper-by-paper** — each paragraph should make an argument drawing on 3-4 papers

5. **Reference style:** APA/Harvard, consistent throughout

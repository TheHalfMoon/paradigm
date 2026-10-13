# Holo 4 scientific and implementation deep dive

Hala starts provisionally from [Holo 4-35B-A3B](https://huggingface.co/Hcompany/Holo4-35B-A3B), revision 508458727831368 da 85d 53a 8055c 2b 0f 923 ed 4f 3. The actual LICENSE is Apache-2.0. Its card names Qwen 3.6-35B-A3B as the base; config uses the Qwen 3_5 Moe For Conditional Generation implementation class, model_typeqwen 3_5_moe. This is an implementation identifier, not evidence that the model card is false.

Config inspection: BF16, hidden 2048,40 text layers,256 experts/top 8, hybrid linear attention with full attention every fourth layer,27-layer vision encoder,16 pixel patch/spatial merge 2, maximum 262144 tokens, config transformers_version 5.6.2. **3B active parameters do not make a 35B checkpoint fit into 6GB**: BF16 weight arithmetic~70GB plus runtime/KV/vision. The maximum context is architectural capacity, not a safe serving default. Start bounded 8–16k context, measure vision token and KV pressure, then enlarge.

[Official September 28 Holo 4 disclosure](https://hcompany.ai/newsroom/holo4) explains capabilities through a combination of model training and harness iteration. It does not release all intermediate checkpoints, task factory code, private training tasks, exact RL hyperparameters or compute sufficient to reproduce the released weights.

| Mechanism disclosed | Evidence and reproducible implication | Remaining uncertainty |
|---|---|---|
| Agent ic Task Factory |~10k tasks:~4 kweb,3kMCP,3 kdesktop/OS. Product documentation/screenshots/self-hosted apps inform coding-agent environment/task/verifier creation | Actual tasks are not all public; recreate fresh tasks on authorized open apps rather than claim to download the factory |
| Four verifier gates | Untouched seed fails; golden state passes; all near misses fail; agent solves via real interface | Published description is reproducible as a method, not proof that our future tasks pass |
| Unified access | One environment can expose human noVNC and agent CDP/MCP; state deltas/tool traces verify goal and side effects | Sharing a browser interface does not ensure real desktop coverage |
| SFT mixture |127 Btokens;~three-quarters successful trajectories:desktop 45%, web 14%, MCP/API12%, mobile 3%; remainder reasoning/grounding/tools/code | No public asset-level rights manifest or full trajectory corpus; figures are vendor disclosures |
| Async online RL | prime-rl; two LoRA experts desktop/web and terminal/MCP/API, equal-weight merge into SFT checkpoint without further training | LoRA rank/reward scalings/merge implementation/checkpoints not fully disclosed. Equal merging is a testable hypothesis, not a universal rule |
| Harness development | Failure tags and engineer fixes for shell locality, context memory, serving vision bug, grading/adapters, prompt trimming and budgets |6.1→59.8→61.7 curve combines fixes, compute and larger time/step budgets. It cannot establish causal effect of RL alone |

Holo 4-27B is **CC-BY-NC4**, so its stronger long-task result is a research reference rather than Hala's unrestricted commercial base. Holo tron 4-30B-A3B uses an NVIDIA custom weight agreement and different implementation; it is not interchangeable Apache Holo 4.

## What explains strength and what to replicate

The combination plausibly matters: visual grounding with varied screenshots; successful, state-verified trajectories for procedural learning; fresh task coverage; interface-specific RL; and a harness that restores necessary context and can execute in the intended machine. Evidence is strongest for disclosure and released config, weaker for isolated causal attribution. The shortest route is verifier quality and harness correctness before collecting enormous token counts.

Inspect the local SDK at [hai-agents-python 5024 cf 9](https://github.com/hcompany-ai/hai-agents-python/tree/5024cf923af85edcd9b10d0d8eeccf67cbc967d4). It launches a separately shipped **hai-agent-runtime 0.1.16**, pinned with platform hashes. Python SDK source is not complete training code or the internal Task Factory. Hala should own its visible action/harness interfaces rather than inherit a runtime boundary without measuring it. No Hcompany paid API was called.

Counter evidence: Fara 1.5's 9B/27B browser models have MIT weights and promising vendor results; Holo 35 is not established best for browsers, long-horizon success or cost. A future same-task comparison must decide. [Dataset forensics](DATASET_FORENSICS.md) shows why public scores cannot settle this today.

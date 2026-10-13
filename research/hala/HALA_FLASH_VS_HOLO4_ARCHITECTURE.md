# Hala Flash versus Holo4: architecture decision

**Decision, 13 October 2026:** test a *routed* system, but ship no routing claim until paired tasks show a gain. The provisional general desktop Flash checkpoint is [`Qwen/Qwen3.5-4B` at `851bf6e`](https://huggingface.co/Qwen/Qwen3.5-4B/tree/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a). The provisional Pro checkpoint remains [`Hcompany/Holo4-35B-A3B` at `5084587`](https://huggingface.co/Hcompany/Holo4-35B-A3B/tree/508458727831368da85d53a8055c2b0f923ed4f3). A frozen Holo-only control precedes hybrid optimization. This is a selection for experiments, not measured superiority or permission to deploy a paid service.

The central correction to the 2B proposal is that a click predictor is not an end-to-end agent. The same model must survive changing application state, plan across steps, handle uncertainty and recover. The trusted Aladdin executor retains authority; model output is an untrusted proposal. Holo4's 35B *total* parameters remain resident even though roughly 3B are active per token; the approximate BF16 weight floor is 70 GB decimal before KV cache, vision activations and serving overhead. [Holo card](https://huggingface.co/Hcompany/Holo4-35B-A3B/raw/508458727831368da85d53a8055c2b0f923ed4f3/README.md). A Flash model can lower marginal inference demand, yet only verified complete-task success and cost decide whether it helps.

## Candidate comparison

Checkpoint identities and licenses below were checked through Hugging Face model metadata and pinned cards on 13 October. Hardware figures are weight arithmetic or vendor guidance, not our load tests. All fine-tuning, quantization, Arabic UI behavior and measured Aladdin latency remain untested.

| Candidate | Verified identity / rights | Relevant evidence | Main limitation |
|---|---|---|---|
| [Qwen2-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct/tree/895c3a49bc3fa70a340399125c650a463535e71c) | Apache 2.0; 2 BF16 shards total **4.418 GB decimal** | Available multimodal base; ShowUI demonstrates this lineage can be adapted for GUI actions | Older base, no matched long-horizon result; 1.2 GB complete GGUF and 0.2 s action unverified |
| [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/tree/66285546d2b821cf421d4f5eb2576359d3770cd3) | Checkpoint exists; its pinned [Qwen Research License](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/raw/66285546d2b821cf421d4f5eb2576359d3770cd3/LICENSE) grants non-commercial use only and requires a separate commercial license | Research-only intermediate control if terms are acceptable | Excluded from the unrestricted commercial foundation lane; no matched Aladdin evidence |
| [Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/tree/89644892e4d85e24eaac8bacfd4f463576704203) | Apache 2.0; BF16 file **4.255 GB** | Newer multimodal base and spatial/grounding claims | No published task-completion advantage over specialized agents established here |
| [Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/tree/ebb281ec70b05090aa6165b016eac8ec08e71b17) | Apache 2.0 | Larger general VLM control | Direct GUI protocol and cost need qualification |
| [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B/tree/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a) | Apache 2.0, native vision-language model | Vendor card reports **35.6 OSWorld-Verified** and **60.3 ScreenSpot Pro**; multilingual model benchmarks | Publisher results, unspecified parity with our harness; action formatting and Arabic UI must be tested |
| [ShowUI-2B](https://huggingface.co/showlab/ShowUI-2B/tree/cabec4fcc48d15ffd3efe0b33ea9bc7d41509d60) | MIT; Qwen2-VL lineage | Explicit GUI action vocabulary and normalized coordinates | No proof of robust long-horizon planning or Arabic UI |
| [Fara1.5-4B](https://huggingface.co/microsoft/Fara1.5-4B/tree/776a33ae5b2ad503796a97ae20fdc66f61d2feea) | MIT; Qwen3.5-4B post-training; BF16 files total **9.079 GB** | Vendor WebVoyager **80.8**, Online-Mind2Web **57.3**, WebTailBench **27.4**; typed browser actions, critical-point stopping | Browser-only intended scope; training data English-only; not a general desktop/Arabic solution |
| [Fara1.5-9B](https://huggingface.co/microsoft/Fara1.5-9B/tree/1a93677cd89d5601bc2ed759791e981f3a520032) | MIT | Stronger browser challenger; vendor 86.6 / 63.4 / 32.3 on the same three suites | Larger hosting footprint; still browser-limited |
| [SmolVLM2-2.2B](https://huggingface.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct/tree/482adb537c021c86670beed01cd58990d01e72e4) | Apache 2.0 | Efficient general VLM baseline | No inspected native GUI-agent benchmark supporting preferred selection |
| [UI-TARS-1.5-7B](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B/tree/683d002dd99d8f95104d31e70391a39348857f4e) | Apache 2.0 | Released visual-action challenger | Match benchmark versions, action format and harness before comparing figures |
| [Holo4-35B-A3B](https://huggingface.co/Hcompany/Holo4-35B-A3B/tree/508458727831368da85d53a8055c2b0f923ed4f3) | Apache 2.0 | Trained for broad desktop, browser and MCP tasks; public evidence examined in [deep dive](HOLO4_DEEP_DIVE.md) | Expensive resident weights; reported benchmarks are publisher evidence, not our replication |

The matrix scores *research priority*, not measured quality. Weights reflect Aladdin's multi-interface mission: desktop/MCP 25%, browser 15%, Arabic/multilingual readiness 15%, deployment efficiency 15%, license clarity 15%, task evidence 15%. Each 1–5 score is a judgment from the cited cards. A desktop gate and an Arabic test gate precede aggregate ranking; browser-only Fara cannot win general deployment through browser scores alone.

| Candidate | Desktop | Browser | Arabic | Efficiency | Rights | Evidence | Weighted /5 | Gate |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Qwen2-VL-2B | 2 | 2 | 2 | 4 | 5 | 2 | 2.75 | Baseline only |
| Qwen3-VL-2B | 2 | 2 | 3 | 4 | 5 | 2 | 2.90 | Baseline only |
| ShowUI-2B | 3 | 3 | 1 | 4 | 5 | 3 | 3.15 | Arabic gap |
| Fara1.5-4B | 1 | 5 | 1 | 3 | 5 | 4 | 2.95 | Browser-only |
| Qwen3.5-4B | 3 | 3 | 4 | 3 | 5 | 3 | 3.45 | General Flash pilot |
| Holo4-35B-A3B | 5 | 4 | 3 | 1 | 5 | 3 | 3.65 | Pro lane, cost gate |

Fara's excellent vendor browser figures are the strongest argument against simply using a generic 2B model. Conversely, Qwen3.5's multilingual benchmark claims are **not** an Arabic GUI evaluation. The first local experiment must include Arabic and right-to-left interfaces, unseen Windows apps and browser tasks. If ShowUI or Fara succeeds at its narrower role with a lower cost per completed task, route only that role; do not promote it to general agent without coverage evidence.

## Four architectures and controlled ablation

| Design | Benefit | Failure mode / control |
|---|---|---|
| A. One compact VLM handles plan and action | One context and loading path | Weak long-horizon reasoning; compare unchanged base, frozen prompts and same executor |
| B. Brain LoRA plus Eye LoRA on one base | Possible specialization | Adapter switching and two prompt/state formats add latency and compound errors. Both adapters share the same base limits. Compare against **one multitask LoRA** at equal examples/steps/parameters, including switch time and end-to-end success |
| C. Small visual model plus deterministic planner/harness | Exploits typed UIA/DOM, explicit state and verifier | A deterministic controller cannot solve open-ended semantic ambiguity; compare harness-only with frozen base before tuning |
| D. Flash + Pro routing | Cheap simple steps with escalation | Router mistakes and extra calls can cost more than Pro-only. Compare Pro-only, Flash-only, and routed on paired tasks, with safety fixed in the executor |

Use deterministic routing first. Direct typed tool/DOM/UIA operations avoid a vision call when state and requested target are exact. Try Flash for bounded, low-risk visual proposals; escalate on missing target, stale observation, repeated failure, ambiguous/long-horizon plan, or a task class whose measured Pro gain justifies it. Risk restrictions apply regardless of model: escalation never grants authority. Calibrate uncertainty against observed completion and postcondition disagreement, not raw token probability. Optimize **expected cost per successful task** = total serving + retry + escalation + idle share divided by verified successes. Report completion, unsafe proposal rate, median/p95/p99 complete-task latency and cost; do not infer them from a one-click token benchmark.

The route is falsified if the same-harness Pro baseline beats routed success by more than the pre-registered noninferiority margin, the routed safety rate worsens, or routing raises cost per success. A pure Flash product is justified only for task classes that pass their own completion and safety gates. A Holo replacement requires matched desktop/browser/MCP coverage, and its advantage must survive fresh app/template splits and paired confidence intervals.


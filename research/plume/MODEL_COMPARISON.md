# Plume foundation comparison

Decision date: 2026-10-12. Recommendation: **retain Wan 2.2 T2V-A14B for the first camera-control adaptation; challenge it with LongCat-Video under the same evaluation protocol**. Wan is the best supported choice for this narrow, commercially distributable pilot among inspected candidates. It is not a demonstrated global quality winner. No candidate was run on a GPU in this assignment.

Evidence: [source inventory](../evidence/SOURCES.md), [training source inspection](TRAINING_STRATEGY.md), [evidence classifications](../evidence/EVIDENCE_REGISTER.md). Parameter counts and capabilities below are publisher disclosures. Peak memory depends on precision, offload, length and resolution; inference figures never certify training.

| Checkpoint / family | Architecture and available capabilities | Actual weight rights and adaptation consequence | Readiness / limitation |
|---|---|---|---|
| [Wan 2.2 T2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B) | Two noise-specialized ~14B DiTs; ~28B total stored, one selected by timestep. Silent T2V, 480/720p. 40-layer, width 5120; UMT5-XXL and Wan 2.1 VAE | Apache-2.0 explicitly covers weights in official release; retain notices and audit dependencies/data separately | Actual Musubi and DiffSynth expert LoRA recipes. Strong implementation ecosystem; physics and identity not solved by licensing or scale |
| Wan 2.2 I2V-A14B / TI2V-5B | I2V has its own weights and boundary 0.9; unified 5B uses different high-compression VAE, 720p/24 fps | Apache-2.0 family release | 5B is lower-cost baseline, **not supported by the inspected Musubi Wan 14B recipe**. T2V adapters are not automatically I2V adapters |
| Wan S2V / Animate / Fun / VACE | Speech, animation, reference and editing variants are separate architectures/checkpoints | Audit each checkpoint and all auxiliary components; family name alone is insufficient | Modular candidates after first gain. A14B LoRA cannot add a missing audio pathway |
| [LongCat-Video](https://huggingface.co/meituan-longcat/LongCat-Video) | 13.6B dense unified T2V/I2V/continuation, long-video continuation | MIT model card and pinned LICENSE checked | Serious permissive challenger; fewer resident generator parameters. Vendor MOS is not an independent win; training readiness is weaker than Wan's inspected adapters |
| [Ovi / Ovi 1.1](https://huggingface.co/chetwinlow1/Ovi) | Publisher calls checkpoint 11B; twin video/audio backbones, Wan TI2V-5B ancestry, 5B audio branch. T2AV/I2AV, 5/10s, 24 fps, 960x 960-family framing | HF weight card says Apache-2.0; no standalone LICENSE in inspected weight repo. Audit MM Audio decoders/T5/VAE and exact components before deployment | Good AV module candidate. Training scripts unchecked in upstream road map; do not assign turnkey training. 24GB FP8+CPU-offload **inference** claim includes quality degradation |
| [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | 22B asymmetric native AV dual stream, references/multi shot; dev and 8-step distilled versions, Gemma 4 text encoder | **LTX-2.x Community License, August 11 2026**, not Apache. $10M entity/affiliate revenue threshold; derivative transfer and AUP obligations. Gated; no agreement accepted | Powerful potential AV/editing alternative, conditional legal lane only. Full dev training distinct from distilled inference |
| [MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | 33B dense full model, ~13B input-dependent AdaLN can be precomputed/removed for inference (~20B). Native AV/ref conditioning; Qwen 3-VL32B encoder | Custom license excludes **EU, UK, South Korea and US** in actual LICENSE. FAQ language contradicts this; primary license controls pending clarification | Open weights do not imply globally unrestricted commercial derivative. Inference optimization cannot reduce full training model to 20B |
| [HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5) | 8.3B, native 480/720p, 5–10s; dedicated SR to 1080p; T2V/I2V | Tencent custom weight license excludes EU/UK/South Korea, user threshold and competing-model/output restrictions | Efficient quality challenger, conditional jurisdiction lane. Super-resolution is separate compute, not native 1080p |
| [Kandinsky-5.0 Video Lite](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2V-Lite-sft-5s) | 2B, 5/10s variants, no-CFG distilled 16-step candidate; Qwen 2.5-VL + CLIP and Hun yuan video VAE | Generator card MIT; **auxiliary VAE license remains a clearance gate** | Cheap qualification/control baseline. Pro releases cannot be inferred from unchecked upstream road map |
| [CogVideoX1.5-5B](https://huggingface.co/zai-org/CogVideoX1.5-5B) | Dense 5B, T2V and separate I2V,1360x 768, frame count 16N+1 | Actual CogVideoX License requires basic commercial registration and additional permission beyond 1M visits/month. Older 2B is a separate Apache option | Mature inference/training but dated quality baseline. From 10GB off loaded inference does not mean 10GB training |
| [Open-Sora 2.0](https://huggingface.co/hpcai-tech/Open-Sora-v2) |11B, high-compression AE, unified 256/768 px I2V/T2V | Card Apache-2.0; audit AE and text encoder separately | Transparent training research; reported~$200k from-scratch training is not a Plume LoRA budget. No current independent evidence it beats Wan |

## Contemporary commercial comparison targets

These are product-level comparisons, not downloadable foundations. Architecture sizes, exact training mixtures, weight memory and adaptation costs are **undisclosed**, unless a linked technical report states otherwise. Do not fill these columns with estimates inferred from latency.

| Target at cutoff | Verified public disclosure | Comparison consequence |
|---|---|---|
| [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | July 31 release; native 30s AV, references up to 30 images/10 videos/10 audio, extensions and timestamp edits | Main capability target. Closed model; no public weights or complete training implementation |
| [MiniMax Hailuo / H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | H3 open-weight release exists with restrictions above; hosted Hailuo version ing must be frozen at evaluation | Hailuo hosted scores and H3 local weights are different subjects |
| [Veo 3.1](https://deepmind.google/models/veo/) | Official current page describes native audio, realism and reference/creative controls | Pin Vertex/Gemini endpoint, duration and resolution; vendor comparisons are not matched trials |
| [Sora 2](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) | Web/app ended April 26 2026; API ended September 24 2026 | **Historical reference only**. No fresh Sora API comparison can be scheduled |
| [Kling 4.0 / 3.0 Turbo](https://klingai.com/blog/kling-4-vs-3) |4.0 Flash early access September 28; staged October rollout announced;3.0 Turbo API documented | Broad 4.0 availability not established; record actual account endpoint rather than call preview GA |
| [Runway Gen 4.5](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5) | T2V/I2V2–10s,12 credits/sec in inspected official help | Multi Shot recipe and Aleph editing are separate product components; no unsupported native-audio claim |
| [Luma Ray 3.2](https://lumalabs.ai/ray3-2) |16 key frames, modify/re frame,16-bit HDR/EXR work flows | Luma hosting Seedance does not establish Ray architecture properties |
| [Pika 2.5](https://dev.pika.art/models/pika/pika-2.5/text-to-video) | Stable 5s 1080p T2V/I2V endpoints | T2V documentation has inconsistent modality label; treat task-specific endpoint as authority and test before inclusion |

Closed datasets, captioning pipelines and finetuning VRAM are not available for lawful replication. Each paid evaluation needs a reviewed budget and authorization. No such call was made.

## Weighted decision with uncertainty

Hard eligibility precedes scoring: distributable commercial derivative without additional accepted agreement, real checkpoint access, inspect able implementation. Restricted candidates cannot outrank an eligible base merely through aesthetics. Ordinal scores 1–5 encode engineering judgment, not measured quality; uncertainty about aesthetics can readily reverse Wan/LongCat. Weights: adaptation quality opportunity 25%, evidence 20%, legal simplicity 20%, training readiness 15%, resource efficiency 10%, maintainability 10%.

| Candidate | Opportunity | Evidence | Legal | Training | Efficiency | Maintenance | Weighted /5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Wan A14B |4|4|5|5|2|4|4.15|
| LongCat |4|3|5|2|3|3|3.50|
| Wan TI2V5B |3|4|5|3|5|4|3.90|
| Ovi 1.1 AV module |4|3|4|1|3|3|3.15|
| Kandinsky Lite |2|3|3|3|5|3|2.95|

The table favors Wan on recipe readiness, not proven superiority to LongCat. If training readiness is relaxed, LongCat becomes more attractive; if absolute compute cap is 24GB, qualification may select 5B or 2B before A14B. LTX2.5/H3/Hun yuan remain conditional comparisons, outside the globally simple derivative lane. None is categorically lower quality.

Switch to LongCat only after a frozen paired trial shows a lower 95% confidence bound above 50% preference on the target suite, no critical fidelity regression, and at least 30% lower cost per accepted clip **or** a capability Wan cannot supply. Re qualify its trainer before adopting. Preserve Wan as fallback rather than migrate datasets prematurely.

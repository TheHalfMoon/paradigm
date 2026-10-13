# Seedance public scientific evidence

The useful reproducible evidence is uneven: [Seedance 1.0 report](https://arxiv.org/abs/2506.09113) exposes data/post-training concepts; [Seedance 2.0 report](https://arxiv.org/abs/2604.14148) and [2.5 launch](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) expose later capabilities without a complete executable training recipe. Reading a newer marketing page does not establish that its hidden pipeline equals 1.0.

The 2.0 PDF was actually downloaded and read through extracted text (26 pages; SHA-256 in source registry). Its report emphasizes unified AV, reference conditioning, editing, evaluations and safety. It does not disclose a reconstruct able corpus or full architecture/hyper parameter/compute package. Seed Video Bench 2.0 is an internal evaluation with expert/objective assessments; it is not an independently rerun public leaderboard.

| Public method | What 1.0 discloses | Plume implementation / limit |
|---|---|---|
| Multi-stage cu ration | Diverse collection, safety pre screen, shot-level filtering; aesthetics, motion and temporal quality selection | Rights gate first, single-shot extraction, sharpness/exposure and flow diagnostics. Motion magnitude alone favors camera shake; remove global camera motion before subject-motion scoring |
| Offline preparation | Captions and VAE representations prepared/packed to reduce training I/O | Version caches by VAE/T5 revision, crop, frame cadence, resolution and source SHA. Benchmark storage throughput before renting larger GPUs |
| Detailed video captions | Static/dynamic descriptions, Tarsier 2 captioning with frozen visual encoder and tuned language component; bilingual training | English captions with explicit camera direction, subject, action and ordered events. Do not train our caption er from scratch first; use owned structured render metadata and human corrections |
| I2V learning | I2V continuation mixture grows 20→40%; motion-only captions alongside detailed captions | When opening an I2V lane, test motion-only versus full captions at fixed assets. These ratios are a Seedance 1.0 disclosure, not an optimal Wan recipe |
| Curated SFT | Small manually selected high-quality balanced categories | 1,000–3,000 rights-cleared clips focused on a known weakness before large-scale adaptation. Size is our hypothesis, not Seedance's recipe or a predicted guaranteed gain |
| Preference data | Deduplicated prompts, ambiguous-prompt filtering, best/worst judgments by dimensions with other quality guardrails | Blinded paired prompt matched ratings; separate camera compliance, anatomy, identity and temporal defects. Keep preference-training pool disjoint from all evaluated prompts/source stories |
| Reward optimization | Foundational VLM alignment/structure, motion, and image/key frame aesthetic rewards; video-specific de noising/post-training procedure simulates inference | Reward ensemble is conceptual evidence. Standard LLM PPO/DPO scripts are not a validated diffusion training recipe. Defer until SFT gains survive independent evaluation |
| Inference acceleration | Multi stage distillation, claimed 10x improvement and 41.4s/5s 1080p on its L20 setup | Separate quality adapter from speed/distillation trial; teacher outputs need commercial training permission. Do not extrapolate vendor hardware latency to A14B |

## Later systems and unknowns

2.0 advertises 4–15s native 480/720p and multi modal reference counts up to 9 images/3 video/3 audio.2.5 extends native generation to 30s and larger reference budgets plus extension/editing. A reference conditioning subsystem and audio backbone cannot be conjured by attaching a silent T2V LoRA. Neither later release publishes the full data rights inventory, exact weights, parameter count, native peak VRAM, reward-model weights, task curricula or complete preprocessing code. Synthetic-data quantities and precise dedup thresholds remain unknown. These are explicit boundaries, not permission to reverse-engineer an inaccessible service.

## Highest marginal practices to borrow

Prioritize **accurate temporal/camera captions, category-balanced high-quality shots, source-level deduplication, human calibration and offline cache correctness**. Test this as a controlled intervention: identical approved clips, weak generic captions versus camera/temporal captions, equal steps and seeds. Learning the dataset relationship is more useful than optimizing a noisiest aesthetic scalar. Use self-authored procedural scene/camera trajectories as initial exact labels, then cleared real footage to test transfer. Preserve failures and held-out domains; never select only impressive samples.

We do not know whether these changes can erase the gap to 2.5. Plume's first scoped result is camera-control improvement at 480p, not full 30s cinematic AV parity. The native-AV comparison lane is Ovi (pending component clearance) or a separately approved LTX/H3 lane, not an assertion that Wan inherits Seedance capabilities.

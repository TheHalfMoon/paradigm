# Plume training compatibility and strategy

Compatibility was checked against actual source, not merely documentation links. [Musubi](https://github.com/kohya-ss/musubi-tuner/tree/f8a1b03794a49239a3539015075f5123d6c07d66) and [DiffSynth](https://github.com/modelscope/DiffSynth-Studio/tree/acf2ad29c65f436633f57beec1caaa1296760331) were cloned and inspected. No torch environment, weights or GPU trainer was loaded. [Source qualification report](evidence/recipe-source-audit.json) records parser flags and source hashes; GPU qualification remains necessary.

| Route / implementation | Verified support | Caveat / decision |
|---|---|---|
| Musubi Wan 14B LoRA | wan_train_network.py; wan_cache_latents.py; wan_cache_text_encoder_outputs.py; wan_generate_video.py; networks.lora_wan | First implementation. Wan 2.2 **14B only** in inspected Wan route. Experimental support; pin source and resolve/lock actual remote environment |
| DiffSynth Wan 2.2 expert LoRA | examples/wan video/model_training/train.py and lora/Wan 2.2-T2V-A14B.sh, q/k/v/o/ffn.0/ffn.2 rank 32; separate low/high examples | Independent fallback. Example 480x 832x 49, lr 1e-4,5 epochs, dataset_repeat 100; these are example settings, not sensible default repeat count for our pilot |
| Diffusers 0.40.0 | Wan inference and model components; dependency of inspected Musubi revision | Component support does not establish a turnkey official A14B training entry point. Do not invent train_wan.py |
| PEFT | General low-rank adapters after validating layer names | Injecting an adapter does not implement Wan expert scheduling, flow loss, cache/crop policy or export mapping |
| Accelerate 1.15.0 | Launch/distributed/mixed-precision orchestration in inspected Musubi pyproject | Configuration, CUDA, torch and interconnect still require GPU qualification; API availability is not memory proof |
| Full finetuning | DiffSynth source supports broader SFT; all parameters/optimizer states retained | Deferred: roughly 16 bytes/trainable parameter yields 224GB for one 14B expert before activations; two experts~448GB. Sharding/offload changes placement, not arithmetic |
| FP8 LoRA | Musubi bf 16/fp 16 inputs with runtime --fp 8_base, optional --fp 8_scaled | **Pre quantized fp 8_scaled checkpoint inputs are unsupported** in inspected docs. Runtime conversion differs from file format. Numerical quality control required |
| QLoRA4 bit | No source-qualified A14B recipe established | Do not use an LLM bitsandbytes tutorial as evidence of diffusion compatibility |

## Exact expert boundary and weight compatibility

Official T2V config: boundary 0.875, shift 12,40 steps, guidance(low 3, high 4); I2V boundary 0.9. Musubi restricts high-noise **875–1000**, low 0–875 for T2V with --preserve_distribution_shape. For simultaneous expert training low goes in --dit, high in --dit_high_noise. --offload_inactive_dit works only without block swap. Prefer Linux remote workers; Windows dual-expert offload documentation warns about~96GB system RAM.

DiffSynth's high example uses scheduler index fractions **max_timestep_boundary 0.417/min 0**, mapped in the script to 875–1000. Its low example uses max 1/min 0.417. These are **not** raw normalized timesteps; copying 0.417 into Musubi changes the experiment. Freeze noise schedule and record sampled histogram before trusting a training run.

Wan 2.2 A14B uses **Wan 2.1_VAE.pth**, not 5B's Wan 2.2 VAE. T5 UMT5-XXL is required; CLIP is not required for 2.2 A14B. The selected trainer expects a compatible single DiT safetensors representation, so use a pinned Comfy-Org **fp 16 non-scaled** re pack with SHA verification and trace it to the official base. Conversion requires a tensor-name/shape/hash inventory; changing numerical representation must not silently change the baseline. Model retrieval occurs remotely only.

## First training intervention

Experiment PB01: high-noise T2V camera/motion LoRA, rank 16/alpha 16, lr 1e-4 AdamW8 bit, BF16 compute, gradient checkpoint ing, batch 1, accumulation 4, SDPA, shift 12, timesteps 875–1000, seed 42,1000 optimizer steps (250/500/1000 checkpoints). Frame geometry 832x 480,49 frames at explicitly prepared 16 fps. These values are **proposed**, chosen to minimize new architectural decisions. The high-noise semantic-control hypothesis must be tested; no causal guarantee follows from the expert name.

Start BF16 base on 1x 80GB A100, ≥128GB host RAM and 300GB temporary disk; keep only one expert on GPU during training, use cached T5/VAE. If qualification OOMs: BF16 block swap first, then record a separate FP8 base trial; do not covertly reduce target frame count or geometry. If no qualified 80GB route within budget, pause A14B training and evaluate 5B challenger. Exact VRAM/time are un measured. LoRA rank changes only trainable optimizer/adapter memory, not frozen 14B weight or attention activation memory. For the selected default linear target set, count tensors on load and record actual parameter count; rough rank 16 estimate~76.7M per expert is not a measured adapter.

Environment anchor: Python 3.11/Linux, Musubi upstream pyproject at pinned SHA (accelerate 1.15.0, diffusers 0.40.0, transformers 5.17.0, av 17.1.0, safetensors 0.8.0). CUDA/torch/bitsandbytes versions must be **resolved from the pinned upstream uv.lock and saved as an exact remote environment lock** at PB00; source requirements allow alternatives. No invented successful package resolution is recorded. Use SDPA first to avoid extra Flash Attention compilation. Dataset-cache and export round-trip checks are acceptance gates, not optional setup.

Further ablations: PB02 low-noise, PB03 both experts, ranks 8/16/32, explicit target subsets, caption quality, adapter strength, then I2V and references in separate checkpoints. Hold compute and data constant per intervention. Preference post-training and distillation enter only after a repeatable SFT benefit and a validated implementation. New audio/ref pathways or global long-range physics need architecture/system changes, not a promise that a larger LoRA will solve them.

See [first experiment package](../../experiments/plume/PB01/README.md) for source-checked commands and failure gates.

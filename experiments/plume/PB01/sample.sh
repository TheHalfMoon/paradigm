#!/usr/bin/env bash
set -euo pipefail
# Remote execution only, after an explicitly authorized bounded GPU budget.
: "${PLUME_APPROVAL_ID:?Record explicit resource authorization before execution}"
: "${PLUME_DATASET_COMMIT:?Bind the approved privateHF dataset commit}"
: "${PLUME_ENV_LOCK:?Bind the resolved and qualified environment lock}"
: "${MUSUBI_ROOT:?Path to pinned remote Musubi checkout}"
: "${PLUME_RECIPE_ROOT:?Absolute path to this experiment directory}"
: "${WAN_HIGH:?Original BF16 high_noise_model first shard}"
: "${WAN_LOW:?Original BF16 low_noise_model first shard}"
: "${WAN_VAE:?Original Wan2.1_VAE.pth}"
: "${WAN_T5:?Original models_t5_umt5-xxl-enc-bf16.pth}"
test -f "$PLUME_ENV_LOCK"
test -f "$WAN_HIGH"
test -f "$WAN_LOW"
test -f "$WAN_VAE"
test -f "$WAN_T5"
test "$(git -C "$MUSUBI_ROOT" rev-parse HEAD)" = f8a1b03794a49239a3539015075f5123d6c07d66
cd "$MUSUBI_ROOT"

: "${PLUME_SAMPLE_OUTPUT:?Remote output directory}"
: "${PLUME_PROMPT:?One registered English prompt}"
seed="${PLUME_SAMPLE_SEED:-42}"
adapter_args=()
if [[ -n "${PLUME_ADAPTER:-}" ]]; then
  adapter_args=(--lora_weight_high_noise "$PLUME_ADAPTER" --lora_multiplier_high_noise 1.0)
fi
python src/musubi_tuner/wan_generate_video.py \
  --task t2v-A14B --dit "$WAN_LOW" --dit_high_noise "$WAN_HIGH" \
  --vae "$WAN_VAE" --t5 "$WAN_T5" --offload_inactive_dit \
  --video_size 480 832 --video_length 49 --fps 16 --infer_steps 40 \
  --timestep_boundary 0.875 --flow_shift 12 \
  --guidance_scale 3 --guidance_scale_high_noise 4 --attn_mode torch \
  --prompt "$PLUME_PROMPT" --seed "$seed" --save_path "$PLUME_SAMPLE_OUTPUT" \
  "${adapter_args[@]}"

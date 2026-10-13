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

python src/musubi_tuner/wan_cache_latents.py \
  --dataset_config "$PLUME_RECIPE_ROOT/dataset.toml" --vae "$WAN_VAE"
python src/musubi_tuner/wan_cache_text_encoder_outputs.py \
  --dataset_config "$PLUME_RECIPE_ROOT/dataset.toml" --t5 "$WAN_T5" --batch_size 1

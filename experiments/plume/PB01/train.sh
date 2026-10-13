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

: "${PLUME_OUTPUT:?Private remote output directory}"
# PB00may override to20steps and save interval20; fullPB01uses1000/250.
steps="${PLUME_STEPS:-1000}"
save_interval="${PLUME_SAVE_INTERVAL:-250}"
accelerate launch --num_processes 1 --num_cpu_threads_per_process 1 --mixed_precision bf16 \
  src/musubi_tuner/wan_train_network.py \
  --task t2v-A14B --dit "$WAN_HIGH" \
  --dataset_config "$PLUME_RECIPE_ROOT/dataset.toml" --sdpa --mixed_precision bf16 \
  --optimizer_type adamw8bit --learning_rate 1e-4 --gradient_checkpointing \
  --network_module musubi_tuner.networks.lora_wan --network_dim 16 --network_alpha 16 \
  --gradient_accumulation_steps 4 --max_data_loader_n_workers 2 \
  --timestep_sampling shift --discrete_flow_shift 12 \
  --min_timestep 875 --max_timestep 1000 --preserve_distribution_shape \
  --max_train_steps "$steps" --save_every_n_steps "$save_interval" --seed 42 \
  --output_dir "$PLUME_OUTPUT" --output_name plume-pb01-high-camera

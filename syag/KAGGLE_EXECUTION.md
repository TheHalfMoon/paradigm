# Kaggle Execution and Project Isolation — Syag vs Hala

**Version:** 2026-10-21. NO KAGGLE NOTEBOOK, ACCOUNT SWITCH, DATA UPLOAD OR GPU JOB EXECUTED BY THIS PLAN.

## User intent and hard platform constraints

Founder requests a separate Kaggle account for Syag to avoid mixing with Hala. Official [Kaggle Terms of Use](https://www.kaggle.com/terms), as checked 2026-10-21, say an individual may not operate more than **one active Kaggle account**. Do NOT create or rotate a second founder-operated active account, reallocate API tokens to bypass limits, or treat project separation as an exception. Kaggle also describes the service as for internal, personal, non-commercial use; verify scope for commercial-model development with Kaggle before training a commercial release on its service. A legitimately separate organizational user may have their own account only in accordance with Kaggle policies; never share credentials or accounts.

**Compliant technical isolation:** create dedicated `syag-*` private Datasets/Notebooks in the same permitted identity, with exact source/output manifests, unique run IDs, separate repository configs, distinct experiment tags, model artifacts and explicitly disjoint path prefixes. Never attach or read Hala datasets as accidental input. Never modify/delete Hala jobs/outputs. This is **not** separate quota.

## Official platform limits (recheck before any GPU)

- [Kaggle Dataset documentation](https://www.kaggle.com/docs/datasets): **200 GB maximum dataset** and **200 GB total private dataset storage**, top-level file count limited to 50.
- [Kaggle Notebooks documentation](https://www.kaggle.com/docs/notebooks): **20 GB persisted `/kaggle/working` output**; up to **12-hour** CPU/GPU interactive sessions and 9-hour TPU in the published specs; GPU availability may queue/change.
- [Efficient GPU usage](https://www.kaggle.com/docs/efficient-gpu-usage): about **30 hours of GPU quota per week or sometimes higher** depending on supply; verify the exact user's visible quota (not promised).
- [Kaggle Acceptable Use Policy](https://www.kaggle.com/aup) requires data/IP/privacy compliance and prohibits abuse and evasion of service restrictions.

Never state a second account is allowed simply to gain additional free GPU. Never claim account quota, accelerator capacity or successful Syag job without a real authorized check.

## Architecture: Kaggle compute/cache vs durable artifacts

GitHub source of truth: TheHalfMoon/paradigm/syag until actual Paradigm-AI GitHub repository exists. Version scripts and notebook sources in GitHub; no API tokens or private scans.  
HF target source: https://huggingface.co/Paradigm-AI for permitted private datasets and model checkpoints after true admin/write access, quota and billing checks. The current HF ChatGPT connector is read-only `MedScale`, not an authenticated Paradigm-AI writer.   
Kaggle role: low-cost/free **execution**, limited **private dataset cache** and notebook reproducibility; never sole archive for multi-TB originals or sole copy of critical checkpoints.

Proposed Kaggle namespace (not created):
- `syag-data-audit-v1` — CPU-focused source sample and license/manifest review.
- `syag-synthetic-pages-v1` — synthetic page generation in CPU batches with exact JSON annotations.
- `syag-base-arabic-eval-v1` — fixed LightOnOCR/PaddleOCR/Qwen dev baselines, no final benchmark look-up.
- `syag-finetune-qualification-v1` — minimal GPU load, gradient, checkpoint, resume smoke.
- `syag-lora-pilot-v1` — authorized bounded training after rights/compute qualification.
- `syag-corpus-audit-v1` — PRIVATE dataset manifest, only actual admitted shares and not entire books absent rights.

## Compute and data protocol

1. At the start of any notebook print masked authenticated identity (no tokens), exact CPU/GPU, free disk, detected quota if available, dataset source revision+checksums, scripts/requirements SHA, privacy permission and experiment ID. Verify the permitted Kaggle identity and no dependence on Hala.
2. Offline metadata and sample preprocessing CPU before enabling GPU. Avoid spending GPU quota scanning documents or installing packages where possible.
3. Separate inputs and outputs: `/kaggle/input/syag-*`, `/kaggle/working/syag/<experiment_id>/`; never attach a Hala input or write its output.
4. Stream **small admitted shards**, suggested 1k–10k pages depending on measured decompressed bytes/image size. For 5M total, shard manifests matter more than putting every page in one Kaggle dataset.
5. Preflight batch: 100 images -> 1k -> 10k. Verify labels/boxes/RTL. Only then select training.
6. A training run records exact model revision and trainer version, bf16/fp16, optimizer, frozen visual layers, LoRA target modules, batch/image geometry, loss/gradient, throughput, GPU memory, 3-seed dev metrics and checkpoint recovery. GPU fit is never assumed for a 0.85B vision model, even when weights alone fit.
7. Save selected weights and JSON metrics to a VERIFIED authorized remote artifact destination and save immutable revision IDs before cleaning `/kaggle/working`. If remote persistence is missing or quota exhausted, do not delete the only good checkpoint; mark BLOCKED. Respect 20GB saved output limit.
8. Never train on held-out Misraj/KITAB/olmOCR/OmniDocBench assets or use protected Najiz records.
9. Scheduler/continuation: source-controlled notebook kernels are launched only with authenticated permitted user authorization. No promise of uninterrupted multi-week sessions, background training or guaranteed GPU.

## Reproducibility file contract

Each `syag-run.json`: task_id, UTC timestamp, GitHub commit SHA, Kaggle account *masked identifier* (no token), notebook slug/version, source manifest sha256, data admit manifest, model commit, trainer package lock, code commit, accelerator and real VRAM, run start/end, samples seen, train/dev split, base vs tuned checkpoint remote id, exact loss/metrics, random seeds, costs if applicable, status PASS/FAIL/BLOCKED and next recovery action.

## When founder wants no Hala mixing

Use logically separated project repos and dataset namespace **under the single compliant Kaggle account**, with a visible access map and no crossover in notebook `Add Input`. If full account ownership separation is mandatory, ask Kaggle support for an official compliant organizational arrangement rather than create a prohibited second active personal account. Alternative approved GPU platform could be used if Kaggle policy rules out desired commercial training, but never assume another provider is free or available.

## Actual next step

Find a way to inspect the existing Kaggle service identity and allowed free quotas **without inspecting or disturbing Hala assets**. There is no dedicated Kaggle connector exposed in this ChatGPT tool session despite founder reporting a Kaggle connection. A user may use Kaggle UI or an authorized remote machine with installed Kaggle CLI; do not infer an active usable account from a claim alone. Remain in GitHub planning, original synthetic CPU fixtures and permitted data audits until actual access is qualified.

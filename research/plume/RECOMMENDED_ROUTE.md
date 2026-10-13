# Plume route decision

Choose **Route C: rights-controlled specialized data + Wan 2.2 adaptation + disciplined inference**, with Route D for capabilities missing from its backbone. [Comparison](MODEL_COMPARISON.md) and [training inspection](TRAINING_STRATEGY.md) support implementation readiness, not an absolute quality ranking.

| Route | Quality opportunity / evidence | Legal/data readiness | Engineering, iteration and deployment |
|---|---|---|---|
| A: directly tune Wan | Near-term motion/camera specialization plausible; pilot needed | Apache weights; public cinematic collections mostly unclear ed | Low–medium complexity, one 80GB qualification lane; efficient adapters but expensive base inference |
| B: replace with LongCat | Native continuation and smaller generator offer advantages; independent matched results absent | MIT weights, same per-asset data rights work | Trainer qualification adds work. Switch only after measured quality/cost win |
| C: data+Wan+inference | Highest marginal first experiment: accurate motion/camera labels, stable serving and sampling | Owned/specifiedCC0 and cleared CCBY assets | First baseline precedes LoRA. Maintain one frozen research path and a separately version ed optimized deployment path |
| D: modular AV/editing/multi shot | Covers dimensions absent from silent A14B; end-to-end identity/sync still uncertain | Ovi component audit; LTX/H3 conditional licenses; own/consented audio | Higher orchestration burden, intermediate artifacts and latency; compare system to system and backbone to backbone separately |

Pilot focus is cinematic camera compliance and temporal coherence, not a declaration of Seedance parity. Core holdouts include real footage-style prompts, human articulation and object interaction so synthetic camera wins cannot hide regressions. A planning estimate is 5–12 engineer-days to source/cache/baseline readiness and 3–6 to qualification/first adapter, dependent on rights and GPU approval, not calendar dates.

Fallback: retain unmodified Wan if captions/data do not improve blinded results; focus on sampler, prompt schema and I2V work flow. Use TI2V5B or Kandinsky as small-memory control only after component-license review. Native AV use begins as a separate module; public outputs may not be used as competing-model training data without checking the exact teacher agreement.

Scale from 1–3k to 10–30k clips only when a pre-registered held-out quality gain survives independent rating and is not solely synthetic-domain memorization. Switch base only under the paired criteria in the comparison. Full finetuning, new conditioning pathways and diffusion RL are distinct budgeted decisions after the first gain. Maintain train/eval boundary and per-source retrieval manifests through every route.

# Compute, storage and financial model

## 13 October Hala unit economics addendum

The proposed $0.00002 per click and $5/month plan are **not measured**. Complete-task cost includes capture/encoding, model queue/prefill/decode, network, local execution/settling, verification, retries, Pro escalations, storage, speech, support, payment processing and idle GPU capacity. Use *cost per verified successful task*, not tokens or action count, as the routing objective. Aladdin's inspected adopted architecture is founder-hosted for AI; a local-only variant would require a separate product decision and moves electricity, hardware and support costs to the customer/vendor rather than making inference free. [Architecture](../research/hala/HALA_FOR_ALADDIN.md).

Illustration only: a continuously warm $0.53/hour GPU would cost **$386.90 per 730-hour month** before storage/network. At 100 paying customers its idle share is **$3.87/customer** even with zero model actions; at 1,000 it is **$0.39/customer**, but available throughput and p95 queueing must then be measured. A warm $1.39/hour Pro GPU is **$1,014.70/month**, or **$10.15/customer at 100**. These hourly rates are the earlier public RunPod snapshot, not reserved offers. A serverless zero-scale worker avoids idle cost but can add cold-start time and billed setup; real quotes and load tests are required.

Illustrative $5 monthly contribution for a light user, *assuming* payment processing of 2.9% + $0.30, support $0.75, shared control/speech/storage $0.50 and compute $0.50: **$2.81**, or **56.1%** of revenue, before taxes, refunds, marketing, development and fixed overhead. At a $3.87 GPU idle share instead of $0.50 compute, contribution becomes **negative $0.56**. A $20 tier under the same $0.75 + $0.50 + $3.87 and a hypothetical 2.9% + $0.30 fee yields **$13.99** before omitted costs. These are sensitivity examples, not forecast margins. Heavy users, Pro escalation and retries can erase them; cap usage based on measured compute per completed task and tail latency. A free tier should use explicit bounded quota or local customer hardware only after privacy and product architecture decisions.

The [first Hala experiment](../plans/HALA_FLASH_FIRST_EXPERIMENT.md) records actions/task, model seconds, idle share, p50/p95/p99, failures and recovery. Refuse a $5 viability claim until a real usage cohort, support load, billing contract and capacity test exist. No payment link or infrastructure was created.

Research cutoff:2026-10-12. **No paid services were activated, no paid inference called and no GPU training launched.** All durations below are planning assumptions; no training/inference throughput was measured. Source prices are snapshots, not a reservation or guarantee of hardware availability. Use [budget calculator](../tools/research_validation/README.md) to substitute actual measurements before authorization.

## Current provider evidence

| Provider | Inspected public terms / quote | Practical role and limitation |
|---|---|---|
| [RunPod](https://www.runpod.io/pricing) | A100PCIe 80GB$1.39/h, SXM80GB$1.59; H100PCIe 80GB$2.89, SXM80GB$3.29; L40S48GB$0.99; RTXA600048GB$0.53; RTX409024GB$0.74; H200141GB$4.59; B200180GB$6.79 | Proposed 80GB remote Linux qualification. Verify host RAM/CPU/disk/network and GPU count.4090 listing shows 41GBhostRAM: inadequate assumption for heavy dual expert offload |
| RunPod storage | Network volume below 1TB$0.07/GB/month, above 1TB$0.05; container disk$0.10; idle volume$0.20/GB/month in inspected table | Scratch and persistent network volumes differ. Do not leave large paid volumes running after a job; exact billing/capacity quote required |
| [Hugging Face Jobs/Spaces](https://huggingface.co/pricing) | Jobs charged by minute, hardware/flavor/RAM/disk vary; inspectedT4 small 16GB$0.40/h andL424GB$0.80/h examples | Metadata/processing or small model lane, not proofA14 BvideoLoRAfits. Query actual current 80GB job flavor before budget. Jobs use separate training-compatible environment; Spaces inference bill not interchangeable |
| [Ka gg le](https://www.kaggle.com/docs/notebooks) | Free quota and accelerators depend on account/availability; older 30h/week references not a guaranteed current quota | CPU preparation/small smoke checks only within actual shown allowance. No assumed free 80GB qualification, protected data handling or durable storage |
| [Colab](https://research.google.com/colaboratory/faq.html) | Free resources, hardware and usage limits vary; runtimes can preempt | CPU/small diagnostics; not guaranteed 24GB,80GB or a reproducible long job. Persistent assets remain private HF |
| [Vast.ai](https://vast.ai/pricing) | Marketplace prices/hardware/network fluctuate; exact offer not locked | Potential cheap alternate after security/host RAM/disk/network/preemption review. Any$0.3–$1.5/h consumer GPU budgeting range is an **assumption**, not an inspected live reservation |
| Lambda / other providers | Credible alternatives, no current exact quote frozen here | Obtain primary quote/availability before choosing. Do not invent a guaranteed capacity/discount to make the plan fit |

Prices exclude tax, transfer, setup idle time, retries, licensing and human work unless explicitly included. Consumer-card memory savings can be outweighed by CPU offload latency and restart risk. Prefer cost per accepted clip or verified successful task over nominal GPU hour price.

## Hugging Face as primary persistent storage

[Official storage policy](https://huggingface.co/docs/hub/storage-limits) at cutoff: free private 100GB; PRO private 1TB plus pay-as-you-go; organization 1TBprivateperseat; private overage **$18/TB/month** in current guide. Earlier$9/TB claims are stale. Public 10TB/PRO best-effort terms are not unlimited private storage. PRO subscription cost and actual account quota must be checked before choosing a tier; none was activated here.

Persist approved dataset releases, per asset hash/provenance manifests, attributions and checkpoint metadata in privateHFrepos. Public base weights remain referenced by immutable revision rather than copied into every private experiment repo. Selective retrieval streams bounded shards to remote scratch; intermediate caches may use more storage than encoded videos. Avoid huge folders/files; policy recommends files below 20GB and modest folder counts, but current hard limits must be checked at upload. Reuse current Hub/Xetuploadtools on remote hosts; repository commits plus file SHA establish lineage, not an un version ed latest URL.

Free 100GB is tight once even a 70GBHala base, video masters/caches and multiple checkpoints are duplicated. LoRA adapters are much smaller than full checkpoint/optimizer state, but determine actual size from tensors. Separate adapter inference export from optimizer resume state. Disaster recovery uses authorized encrypted remote backup and re playable source manifests; no persistent training videos/weights on personal computer. Cleanup follows verified upload commit/hash and validated scratch path. No HF dataset repo or upload was performed.

## Memory and storage arithmetic

BF16 weights≈2 bytes/parameter: Wan 14 Bexpert~28GB, both~56GB; Holo 35B~70GB. Add text/vision/VAE components, activation tensors, work space/KV and al locator overhead. Full Adam training rough 16 bytes/trainable parameter:224GBper 14 Bexpert,448GBboth,560GBHolo, before activation. Sharding/offload redistributes memory. LoRA retains frozen weights;3 BactiveMoE does not imply 3 Bresidentweights or optimizers.

Encoded video GB decimal = clips×seconds×Mbps/8000. Pilot 1,200×3.0625×20≈9.19GB;1,000 train alone 7.66GB. Intermediate 30,000×6×20=450GB; large 300,000=4,500GB. Keep masters, caches, adapter/optimizer states and replication separately, initial cache allowance 2–8×encoded video is an assumption until measured. Twenty copies of small JSON are cheap; duplicated full model snapshots are not.

## Scenario A: zero-cash preparation

Public source research, static recipe inspection, schemas, local metadata validation, fresh task specifications and reviewer preparation cost **$0 external cash in this assignment**. Existing tools/network/human time are real resources. Free CPU/GPU allocations can help optional tests if actually available, but no reliableA14 Btraining throughput is promised. Remote generation of 1,200 renders is not assumed free: CPU render time/quality must be measured on an available authorized resource. No live GPU baseline exists yet.

## Scenario B: minimum viable paid Plume training, proposed

| Activity | Configuration assumption | GPU hours | AtA100PCIe$1.39/h |
|---|---|---:|---:|
| PB00 loading/cache/memory qualification |1x 80GB,≥128GBhostRAM,300GBscratch,832x 480x 49, batch 1 |8–24|$11.12–33.36|
| Frozen baseline generation |Same precision/sampler/geometry, sealed prompt suite |6–12|$8.34–16.68|
| PB01 high noise LoRA |Single expert, BF16, rank 16,1,000 optimizer steps, accum 4 |24–72|$33.36–100.08|
| Adapter evaluation/export repeat |Frozen paired prompt/seed set plus roundtrip |12–36|$16.68–50.04|
| Total bounded first cycle |**50–144GPUhours assumed**, not measured |50–144|**$69.50–200.16**|

Add 10–30%retry contingency; illustrative 100GBnetworkstorage$7/month and temporary disk/time charges; private HF capacity/subscription if needed; rendering and transfer quotes; licenses**unknown**. Human work:1,200×45 sreview≈15 hours, plus 1,080 paired ratings×30s≈9 hours; at an illustrative$15/h this is$360, not an offered wage or approved spend. A realistic cash envelope is roughly**$90–300 compute/storage plus~$360 illustrative review and any rights/rendering costs**. Cost can exceed this if model loading or throughput fails. Do not promise a meaningful gain at a fixed price.

First authorization should be a boundedPB00 qualification quote, not a prepaid full training program. Before approval, specify provider actual GPU/host RAM/disk, artifact revisions, maximum wall time, exact spend cap, cancellation and cleanup. IfPB00 fails resource/correctness gates, stop and revise rather than consume the remaining training budget.

## Scenario C: performance-first program, proposed

4xH10080GB with verified fast interconnect,≥512GBhostRAM and 1–2TBscratch; source qualified distributed trainer required. Proposed 128–512GPUhours for paired experts/rank/caption ablation cycle costs**$421–1,684 at$3.29/GPU hour**, not “512 hours of a 4GPUmachine” (GPU hours=count×wall hours). Add 20%contingency,$35–140 illustrative network storage, HF private capacity, human review and licensing. **$600–2,500 per bounded research cycle excluding human/licensing** is a planning range, not a measured optimum. Full finetuning or large AV conditioning may exceed these resources and needs a new plan.

Hala later: HA00/HA01 serving/fresh task ablation 1xH10080 with offload or 2x 80GB if qualification needs;16–64GPUhours≈$53–211 atSXMrate, plus environment CPU hosts. HA02/03 adapter pilot 64–256GPUhours≈$211–842, possibly 2x 80GBmemorylane; render er/vision/KV and MoE tensor compatibility un measured. Async RL introduces rollout fleet/envcosts; no trustworthy duration quote before state-verifier and policy serving tests. Four GPU quality research is not automatically cheaper than smaller Fara 9 Bbrowser specialization.

## Phase spending gates

P0/P1 research tools complete at zero external cash; P2 baseline needs measured serving GPU hours and authorized budget; P3 bounded qualification precedes training; P4 scales only after paired CI/retention criteria; P5 fresh environments/harness costs CPU engineering before GPU SFT; P6 adaptation/RL separate budgets; P7 independent review/evaluation and competitor API credits require explicit approval; P8 license/hosting/release quotes depend on accepted artifacts. No phase costs a represented as measured experiment results.

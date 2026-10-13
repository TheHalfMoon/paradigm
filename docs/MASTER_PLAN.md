# Paradigm master research and development plan

Decision baseline:2026-10-12. This document establishes the development program, not completed models. Public source research and compatibility inspection support the initial routes; independent GPU quality and task-success results remain future experiments. [Executive answers](EXECUTIVE_SUMMARY.md) address all15 requested questions; [current status](CURRENT_STATUS.md) distinguishes verified work from execution gates.

## Objective and recommended architecture

**Plume:** specialize Wan2.2 T2V-A14B on accurate camera and temporal control using a small rights-controlled dataset and expert-specific LoRA. Own data provenance and reproducible inference from the start. Challenge the base with MIT LongCat-Video under identical output conditions. Add I2V, references, audio, lip synchronization, editing and long-video planning through separately evaluated checkpoints/modules where Wan lacks those pathways. Native AV candidates include Ovi after auxiliary-license clearance and conditional LTX/H3 lanes only after their material restrictions are accepted by the owner.

**Hala:** start from Apache Holo4-35B-A3B with an owned typed harness, fresh state-verifiable tasks and bounded memory/recovery. Isolate harness gains with frozen weights before SFT. Test MIT Fara1.5-9B/27B in the browser lane; a browser win does not establish desktop/MCP coverage. Grounding adaptation may use a cleared DragOn train subset; long-horizon adaptation uses newly collected successful/recovery trajectories. Benchmark trajectories and inference fixtures never become training data.

These are RouteC recommendations (base + better data + training/inference discipline), with RouteD capability modules. RouteA direct adaptation remains the simplest first intervention; RouteB base replacement requires measured switching evidence. [Plume](../research/plume/RECOMMENDED_ROUTE.md) and [Hala](../research/hala/RECOMMENDED_ROUTE.md) compare quality opportunity, evidence, law/data access, training readiness, complexity, time/resource burden, maintenance and deployment. Ordinal weighted comparisons are engineering judgments, not synthetic leaderboard measurements.

## Scientific conclusions that change the plan

1. Newer open-weight video releases are not automatically unrestricted foundations. LTX2.x has revenue/derivative restrictions; MiniMaxH3 actual license excludes territories includingUS/EU; Hunyuan and CogVideoX also impose material conditions. WanApache and LongCatMIT are credible uncomplicated derivative candidates, with asset/component rights still separate.
2. Seedance1.0 exposes useful curation, captions, balanced SFT, preference and acceleration concepts. The2.0 report/2.5 release does not publish a reconstructable current corpus/full training recipe. Borrow temporal/camera labeling and human-calibrated filtering first rather than speculate about private architecture.
3. Hcompany's strongest reproducible idea is verified task generation: seed fails, golden passes, near misses fail, solve uses the real permitted interface. Its127B-token private mixture is not available in the public7,366 benchmark trajectories.
4. Holo35's publishedOSWorld2 30.9 is partial completion. Recomputed public106-task binary success is12.2642%, and publisher-index recomputation is not independent execution. AutomationBench index/card discrepancies remain unresolved. OSWorld2.1 is now a different current benchmark lane.
5. Musubi videoLoRA source is real, but its24GB training quote is for images. Wan's two14B experts and Holo's35Btotal weights impose resident memory despite lower active compute. Weight format/dtype, expert scheduling, cache geometry and export need actual qualification.
6. FineVideo's rich captions make it useful after clearance, not automatically approved. Mass web datasets do not grant commercial footage/music/likeness rights merely through an Apache/MIT repository. Owned procedural assets minimize first-pilot rights uncertainty but create a synthetic-domain transfer risk.

Every conclusion has source/claim scope in [evidence register](../research/evidence/EVIDENCE_REGISTER.md) and [uncertainties](../research/evidence/CLAIMS_AND_UNCERTAINTIES.md). A verified source fact never implies verified performance.

## Ordered phases and acceptance gates

| Phase | Measurable output | Dependency / exit criterion | Current state |
|---|---|---|---|
| P0 Source/capability verification | Versioned cards/licenses/configs, challenger comparisons, tool investigations | Source identity/rights/capability claims auditable; unknowns recorded | Research complete; refresh before execution |
| P1 Data research and quality architecture | Registry, schemas, rights gate, data/task factory contracts | No training admission without per-asset approval; benchmark denylist and source-group splits | Architecture complete; actual asset review/ingest unstarted |
| P2 Baseline evaluation | Frozen prompts/tasks, runmanifests, exact output/failure/cost records | Approved resources and qualified environment; no changing test after seeing scores | Not executed |
| P3 Small-scale qualification | PB00 cache/gradient/export/noise/memory/throughput report | Finite loss, real adapter gradients, strict weights, reproducible outputs and bounded cost | Source/parser inspection complete; GPU qualification pending |
| P4 Plume specialization | PB01 followed by isolated expert/caption/rank ablations | PairedCI and camera/retention/safety criteria; scale only replicated improvements | Prepared, not trained |
| P5 Hala harness/task factory | Fresh tasks pass verifier gates, action/history/timeout ablations | Equal frozen model/budget; verified success improvement and no unauthorized side effects | Design complete, environments unbuilt |
| P6 Hala adaptation | Grounding/fresh-trajectory SFT, optional later asyncRL | Model topology/kernel/export qualified; fresh held-out improvement beats harness-only baseline | Not executed; exact GPU recipe is a qualification task |
| P7 Independent benchmarking | Sealed replication, official suites and named competitors under equal conditions | Authorized benchmark assets/API budget; independent reviewers, confidence and all failures | Protocol complete, runs pending |
| P8 Production/publication | Model/data cards, rights notices, reproducible release, cost/safety/deployment report | Release rights, quality, security, traceability and resource gates all met | Release blocked pending evidence |

Execution order is P0/P1 research for both → P2/P3/P4Plume → P5/P6Hala → P7/P8permodel. Hala research/harness specifications can advance without GPU spending while Plume preparation proceeds. Dates are not promised; [roadmap](ROADMAP.md) estimates task units and dependencies, and the30-day document is an optional work-budget allocation rather than a deadline.

## First concrete experiment

PB00 first eliminates memory/recipe uncertainty. Only after it passes, PB01 trains the high-noise expert with fixed rank16/alpha16, lr1e-4,AdamW8bit, BF16,832x480x49at16fps, batch1/accum4, timesteps875–1000,shift12,seed42,1000optimizer steps. Use original BF16 Wan shards through the inspected split-file loader. No FP16 repack is mixed with BF16 training; that combination is explicitly rejected in source. Low-noise expert remains unchanged. [Experiment package](../experiments/plume/PB01/README.md) supplies commands, fixed geometry, data contract, version pins and qualification checklist.

Proposed datasetplume-camera-v0.1 contains1,200owned procedural single-shots:1,000train/100dev/100sealed, split by scene/asset/template before rendering. Eight camera categories (static,pan,tilt,push-in,pull-out,tracking,orbit,crane) each125trainclips; variation in subject actions, lighting and scene geometry. Owned/CC0inputs only. Asset review and actual privateHFcommit are prerequisites, not already completed datasets. Human review validates camera/event labels; realistic held-out prompts check transfer, anatomy/physics and aesthetic retention. Cleared real footage enters a separate versioned follow-up, not a silent change to PB01.

Evaluate120new prompts×3seeds, paired frozen baseline/adapter outputs and3blindedraters; cluster bootstrap by prompt. Go only if preference lower95%CI>50%, camera compliance improves≥10pp with lowerCI>0, critical failures rise≤2pp and retention noninferiority≤3pp. Inconclusive power means additional sealed data or narrower claims. Training loss reduction or successful video generation alone is insufficient. Never use sealed test for choosing checkpoint/hyperparameters.

## Resources and financial discipline

[Cost plan](COST_AND_COMPUTE.md) separates snapshots from assumptions. ScenarioA is zero-cash research/preparation with no guaranteed largeGPU. ScenarioB first boundedPlume cycle assumes50–144A10080GBGPUhours (~$70–200 at$1.39/h), plus contingencies/storage/rendering/rights and human review (~$360 under illustrative24h×$15/h). ScenarioC assumes4xH100 with128–512GPUhours per ablation cycle (~$421–1,684 basecompute), with broader$600–2,500compute/storage allowance excluding human/licensing. These are hypotheses until PB00measures throughput; they are not permission to spend.

PrivateHF is persistent source-of-truth for approved payloads/checkpoints. Current freeprivate100GB/PRO1TB plus$18/TB/month overage terms require an actual account capacity decision; public allowances do not substitute. Remote ephemeral scratch and selective pinned downloads avoid persistentpersonal datasets. Reuse public base revisions instead of copying70GBweights repeatedly into privateHF. Preserve authorized remote backups and source manifests; verify committed filehashes before cleaning scratch.

## Integrity, maintenance and release

Use normal branches, focused commits, reviewablePRs and ordinary merge commits, with exact head verification and applicable required checks. Research tool validation is metadata/source validation, not fakeGPU/E2E evidence. REA was actually used on Playwright, Jev validated an offline preset, AlibabaOCR supplied delegation rules for a host review and Graft builds/checks the smalltool integration graph. Detailed executed outcomes live in [validation report](VALIDATION_REPORT.md).

No model release until per-component/per-asset rights, notices, contamination disclosures, model/data cards, sealed independent quality/task evidence, deployment memory/latency/cost, failure recovery, safety boundaries and rollback are reviewed. Native/model-only claims and modular product claims stay separate. Use no privateAPI/proprietaryweights or access-control circumvention. No speculative worldwide leadership claim is part of this plan.

Resume from live GitHub, not this conversation:AGENTS → CURRENT_STATUS → MASTER_PLAN/DECISION_LOG → experiment registry → source revisions/rights/prices → validators → next unmet gate. Keep completed source facts, hypotheses and pending work separate in every update.

# Evaluation protocol and evidence integrity

Version 1,2026-10-12. NoGPU model/task evaluation was executed in this research assignment. Pre-register the exact run manifest before seeing outcomes. Keep raw outputs/traces, refusals, failures, timeouts and exclusion reasons. Public source facts, vendor scores, recomputed publisher metadata and independent executions are different evidence types.

Run manifest: model repo/revision/file hashes, adapter SHA, trainer/serving commit and envlock, precision/quantization, sampler/steps/guidance/shift or agent prompt/tool contract, dataset/benchmark code+task+asset hashes, seeds, source group exclusions, hardware/count/host RAM/interconnect, duration/step budget, retries/termination, candidate config selection policy, raters/verifier revision, cost rate and statistical plan. Preserve inherited checkpoint contamination as unknown where unobservable.

## Video paired pilot

Freeze 120 new English prompts:64 camera instructions (eight families×eight prompts),16 human articulation,16 object interaction/physics,12 identity/composition and 12 out of domain/low motion. No prompts copied from public train caption assets. Three generation seeds 42/43/44 per prompt, one output per seed per model, matched resolution/duration/sampling compute. Baseline Wan versusPB01 adapter, and LongCat where qualified. Keep output failures in denominators. Different backbones require best documented fixed inference config selected ondev, then equal output/seed budget; do not secretly best-ofN one candidate.

Blinded randomized A/B order, three independent raters, instruction compliance, temporal coherence, anatomy/physics, aesthetics and critical artifact flags separately; tie option. Overall win fraction with ties 0.5 and paired hierarchical bootstrap **clustered by prompt**,10,000 resamples with recorded stat seed. Raters/generation seeds are not 1,080 independent prompts. Report per cohort CI, interrater agreement, tiered quality and failure count. Pilotn 120 is a decision aid, not a guaranteed statistical power calculation.

Go: lower 95%CI of overall preference>50%, camera-compliance ≥10 percentage-point gain with lower paired CI>0, critical failure rate rises≤2 pp and unseen/photoreal retention noninferiority margin≤3 pp on predeclared scales. Margins are proposed practical criteria; low power/inconclusive cohort means more sealed data, not success. Multiple checkpoint selection occurs ondev only; sealed test evaluates chosen checkpoint once. A failed criterion means diagnose/narrow claim, not retune on sealed prompts.

For official VBench/VBench 2 use upstream prompt/sample requirements and pinned code/dimension models. Smalln 120 scores are pilot estimates, not official leaderboard submissions. Distinguish native 1080/audio/long shot fromproductSR/audio edit composition; compare backbone to backbone and system to system in separate lanes. Evaluate AV sync/lip offset with consented gold plus human judgment; embedding correlation alone cannot prove accurate lip movement or physical consistency.

## Computer-use paired pilot

50 new tasks across 5 self-hosted apps and 10 families, three resets/seeds each. Seal unseen app/template groups separately. Fixed action/time budgets (pilot 200 actions/20 minutes, or preregistered task class budget) and identical tool permissions. Each model's trained prompt adapter may differ but its chosen config is frozen ondev before test. Verify state deltas and forbidden side effects independent of agent declared success. Report binary goal success and partial score **separately**.

Success proportion Wilson 95%CI plus paired task-cluster bootstrap of success difference; report McNemar discordant pair summary where paired single trial applies. Three repeats measure stochastic variability, not 150 independent tasks. Record p 50/p 95 wall latency, TTFT, tokens, tool time, time out count, cost/success and safety violation rate. Cost/success=sum all run costs/verified success count; if zero successes mark undefined/infinite, do not divide by 0 or omit failed costs.

Go:≥5 pp verified success gain and lower paired 95%CI>0; no increased unauthorized side effects or declared unseen-app regression. Harness ablation holds weights/data/budget constant. Training ablation holds harness constant. Larger steps/time or allowing terminal bypass are distinct capabilities/conditions and cannot explain a model-only claim. Environmental crashes are logged; pre-registered rerun policy applies equally, never remove hard tasks after results.

## Claiming a named competitor or benchmark record

Need exact current competitor version and availability, identical prompt/task/assets, permitted tools, output/seed/time budget, scoring and cost measurement, plus confidence interval whose relevant difference exceeds zero. Discontinued Sora supports historical comparison only under clearly labeled artifact sets, no fresh API run. Vendor private leaderboards and public preference Elo from differing conditions are not proof of our win. Independent reviewers repeat the sealed run from manifests; official submission follows actual benchmark rules and asset license agreement. A scoped camera record or browser task record is permissible only with explicit scope and no claim of general world leadership.

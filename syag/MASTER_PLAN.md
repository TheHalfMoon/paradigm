
# SYAG MASTER PLAN — Research, Training, Benchmark Leadership, Release

**Canonical plan version:** 2026-10-21 / v1.0  
**Home today:** TheHalfMoon/paradigm/syag (until GitHub organization exists).  
**Desired GitHub owner:** Paradigm-AI if an authorized GitHub organization can be created and that name is available; see ORG_MIGRATION.md.  
**HF organization supplied by founder:** https://huggingface.co/Paradigm-AI (write privileges not confirmed).  
**Model:** one Syag checkpoint/product identity. No Lite/Pro variants. One model can have versioned releases and quantizations of the *same* model; do not misrepresent multiple backbones as a single trained checkpoint.  
**Target:** world-class OCR + document understanding, specializing first in Arabic/Saudi documents without degrading multilingual/general document performance. Record aspirations separately from measured results.
**Working language for engineering and agents:** English. User-facing status may be in Arabic.

## Current truthful baseline (as of plan creation)

- Research on candidates and 20 data leads exists in research/syag/2026-10-21 and datasets/syag.
- Provisional base: https://huggingface.co/lightonai/LightOnOCR-3-0.8B, approximately 853M parameters, Apache-2.0. LightOn release October 8, 2026. Published model card tags its trained language as English; Arabic Saudi suitability is UNVERIFIED.
- Alternative frozen baselines for *comparison only*: PaddlePaddle/PaddleOCR-VL-1.6 (Apache-2.0, 0.9B VLM and associated layout system), Qwen/Qwen3.5-2B and Qwen/Qwen3.5-0.8B (Apache-2.0, multimodal), and other document OCR systems if their weights, service access, and licensing permit. Do not silently change chosen base. Evaluate comparable model-only and end-to-end system lanes separately.
- No Syag training run, GPU quality trial, admitted dataset, registered dataset upload, public benchmark victory or deployment was established by the preceding research. This plan does not create them.
- Existing Paradigm research rules, rights registry, and benchmark protocol remain applicable unless a later scoped, documented amendment supersedes them. Respect ongoing Hala and Plume work; do not overwrite experiments.
- Already reviewed source facts are not independent evaluations.

## Product definition and engineering constraints

Inputs: scanned and photographed pages, images, digital/scanned PDFs with page segmentation, RTL/LTR mixed script, Arabic/English first and extensible to other languages. Treat multi-page parsing as system orchestration around the **one** Syag model.
Outputs: (a) source-faithful plain text; (b) structured Markdown; (c) deterministic JSON containing page, region type, normalized and verbatim text, reading order, polygon/bbox and confidence/calibration metadata; (d) table row/column associations and page-grounded field extraction. Support charts, diagrams, stamps and handwriting as tracked competency lanes; detecting a stamp is not verifying its legal authenticity.
Invariants: never invent missing fields; never overwrite source transcription to fix plausibility; maintain text/evidence page reference; bounds are in stated coordinate system; preserve zero-vs-O, decimals, currency, negatives, ID digits and Hijri/Gregorian dates; policy-based abstention/review when uncertain. Distinguish OCR recognition, parsing, semantic normalization, and downstream validation.
Design evidence contract using reusable non-clinical patterns from SafeOCR with attribution; keep SafeOCR health/FHIR policy separate. Never write personal source images into GitHub.

## Objective hierarchy — no fake #1 claim

1. **Trustworthiness on Saudi production documents:** exact critical fields and correct source geometry, high data coverage, no ungrounded values.
2. **Arabic OCR quality:** lower CER/WER on held-out real Arabic, multiple fonts, dialect-neutral formal Arabic, handwriting and phone photographs.
3. **Document structure:** competitive reading order, multi-column layouts, Markdown/table structure, chart and graph extraction, forms and relationships.
4. **General performance:** avoid meaningful regressions on non-Arabic document benchmarks.
5. **Efficiency and practical ownership:** latency/cost/VRAM/page, reproducibility, offline/private deployment, rights clarity.
"Number one in everything" is an aspirational research direction; technical tradeoffs and constantly moving benchmarks preclude a guaranteed rank. Independent leaderboards and predeclared statistical evidence determine specific, dated records.

## Milestone dependency graph and exit gates

| ID | Work packet | Required deliverable | Evidence-based exit | Initial state |
|---|---|---|---|---|
| S00 | Org/permissions and experiment integrity | GitHub/HF owner map, repo architecture, resume entrypoint, baseline rights | Actual write permissions verified; no destructive migration | PLAN IN PROGRESS |
| S01 | Baseline reproducibility | pinned unmodified LightOn model and 2 challengers, SHA/versions, dev inference manifests | same dev document groups, full failures/cost/timing captured | NOT STARTED |
| S02 | Saudi evaluation set | 500-page pilot dev set and >=500 real/synthetic clearly stratified **sealed** Saudi pages with reviewed transcripts/boxes/fields | distinct source/template/identity splits; privacy/rights; independent annotation agreement | NOT STARTED |
| S03 | Dataset admission factory | ingestion, license and privacy gate, hashed records, split before augmentation, de-dup | >=1 actual audited ingest sample & replay proof | NOT STARTED |
| S04 | Original Saudi synthetic renderer | versioned templates, image/PDF and perfect JSON transcription/layout/field truth | fonts/RTL/date/table invariants and independent 100+ page spot-audit | NOT STARTED |
| S05 | Pre-training qualification | bounded remote hardware dry run, memory/gradients/checkpoint save/load, benchmark harness smoke | real measurements, zero invented GPU evidence | NOT STARTED |
| S06 | Pilot Syag adaptation | rights-cleared 10k–20k page dataset, baseline vs adapter pair | reproducible training; dev Arabic gain; no severe table/general regressions | NOT STARTED |
| S07 | Error-driven expansion | 50–100 template families plus cleared real data; curriculum, ablations | held-out class improvements replicated; source-group contamination report | NOT STARTED |
| S08 | Grounding/structure specialization | box/reading order/table/structured task mixture and verified field outputs | benchmark regression gates and calibration on independent dev | NOT STARTED |
| S09 | Official and adversarial benchmarking | pinned competitor snapshots, KITAB/Misraj/olmOCR/OmniDocBench/DocLayNet/PubTables etc | blinded independent runs, CIs and published reproducible evidence | NOT STARTED |
| S10 | Production engineering | versioned API, PDFs, batching, sandboxing, privacy, safe logs, model cards | latency/VRAM measured, red-team, rollback, reproducible serving | NOT STARTED |
| S11 | Publication and maintenance | rights and notices, release, reproducibility package, research write-up, drift tracker | independent replication + security/license review + no false claims | NOT STARTED |

Milestone labels are gates, not fixed calendars. Work on unblocked different lanes concurrently only if it cannot pollute sealed evaluation or displace existing Hala/Plume resources without coordination.

## Training playbook

- T00: freeze source weights revision, processor/tokenizer, image-size and coordinate format, vLLM/Transformers versions. Check LightOnOCR GitHub's current model-specific flags; do not mix models or undocumented inference prompts. Baseline 100–500 Arabic dev pages (never final eval).
- T01: pilot adapter (LoRA/QLoRA only if actual Qwen3.5-based implementation and visual-language layer support are verified). Tiny training subset 1k–3k images to verify training topology and gradient path; then 10k–20k with curriculum of transcription, layout, tables, exact field copying. Select hyperparameters on dev only; store every failure, checkpoint SHA and seed.
- T02: error-driven expansion 100k–300k **admitted unique** training items as conditional target, not acquired inventory; balance real vs synthetic and fonts/themes; replay Arabic numerical, RTL and table failure slices. Supervision must use exact image-tied labels.
- T03: optimize full checkpoint only after LoRA pilot proves meaningful improvements. Full fine-tuning or continued pretraining should be justified by measurable benefits, GPU fit, and retention; never spend just for parameter count.
- T04: optional preference/RL/verification rewards **only** when deterministic validators agree with pixel ground truth and no reward hacking is observed; use independent held-out judge checks.
- T05: optimize serving (batch/caching/quantization) as release artifacts of the **same** model. Quantization is not an independently trained Lite model. Require non-inferiority on exact-field safety and structure.

All reported performance points need pinned manifests, random seeds, raw outputs, cost/latency, sample exclusions and regression control. Do not promote a checkpoint merely because loss fell.

## Dataset channels and prior art

Read ../datasets/syag/SOURCE_REGISTRY_2026-10-21.csv and ../research/syag/2026-10-21/DATA_DISCOVERY_AND_ACQUISITION_PLAN.md first. P0 sources: Alhazen (52,726 train; publisher says 85% synthetic), Loay synthetic 300k (shares source rows with Alhazen), AraReceipt, ReceiptSense, DocLayNet, HITL Arabic Documents (10k detection/layout), small permitted PubTables subset. Counts overlap and do not establish ready-to-use datasets.
Saudi document family factory: ZATCA-aligned fictional VAT invoices, Arabic-English receipts, BOE/Najiz-inspired *original* legal/administrative templates, contracts, correspondence, registration forms, HR documents, certificates, statement tables, Arabic handwriting where authorized. Generate exact source rendering annotations before scan augmentation, not after guessing OCR output.
Do not ingest citizens' signed-in Najiz content or sensitive court files, or republish protected government documents. Availability on the public web is not a license. SARD's published non-commercial/no-derivative conditions bar commercial training absent specific additional rights. Keep benchmark sets and their descendants out of every train stage. Source-specific permissions may be documented in a private rights record without exposing contracts.

## Benchmark strategy

Read BENCHMARK_PROTOCOL.md. Treat **KITAB-Bench** (8,809 samples, 9 tasks, 36 subdomains) as an external Arab-first benchmark, **Misraj-DocOCR** and its KITAB-reviewed pages as external tests, **olmOCR-Bench** as fact-presence/retrieval-oriented, **OmniDocBench v1.6** and **Real5-OmniDocBench** as complex document parsing, **DocLayNet** layout, **PubTables** table structures and **SaudiDocBench** as *new internal independent blind set*. Official score protocols must be strictly followed; do not invent amalgamated universal leaderboard.
Primary metrics: Arabic CER/WER plus critical value exact match with Wilson CI, normalized-vs-verbatim score separately, table TEDS, layout mAP/IoU, reading-order error, field attribution and numerical errors, charts/diagram exactness, hallucination and abstention, completion coverage, time/p95, peak memory, cost/1k pages. Use paired bootstrap by source document and hold out template families; report subgroup regressions.
Success means replicated gains on target tasks **with no unacceptable regression in critical-field exactness or unsafe acceptance**, not merely a better aggregate score.

## Systems, provenance, and budget

- HF Paradigm-AI eventual repos: Syag (model, release card, rights notices), syag-corpus (private allowed assets + manifests), syag-eval (private sealed benchmark with restricted access). Names provisional; verify organization/member write access first. Never claim created until confirmed.
- GitHub desired: Paradigm-AI/Syag for standalone training/serving source and plan **once GitHub organization is created**; TheHalfMoon/paradigm/syag is canonical meanwhile. No duplicate competing authoritative plans.
- GitHub only code, manifests and references, hashes, docs, small policy-safe synthetic fixtures. No real citizen images, credentials, datasets or weight shards in Git history.
- Remote ephemeral GPU/CPU only after eligibility, data permission and actual zero-cost qualification (Kaggle/Colab free allocations may be limited). No paid GPU, API, membership or unapproved spending. If compute not available, advance source/audit/fixtures and mark training BLOCKED; never fake runs or overstate completion.
- Prefer locally installed/available Alibaba open-code-review, PStack, Graft and tester-army/e2e as **actual** qualified tools; optional D1-local if installed. Record exact versions/evidence; these reviews supplement real unit/integration/GPU tests, not replace them.
- Use GitHub branches and reviewable PRs. Independent QA and authorizations (rights/compute/production) remain when applicable, despite autonomous engineering work.

## Release gates

Publish Syag 0.x only if all are true: base and dataset notice obligations satisfied; data provenance and exclusions audited; official Arabic and international scored runs with raw evidence; Saudi-specific accuracy and high-risk errors reported with CI; signed model card, intended use, limitations, privacy and rollback; supply chain and serving security tests; no deceptive record claims. If one major bar fails, mark NO-GO, fix and rerun against sealed protocol rather than optimizing on the test set.

## Progress accounting

Use STATUS.md and GitHub issues as source of truth. State every work item as DONE / IN PROGRESS / BLOCKED / NOT STARTED, with artifact link, immutable commit, test receipt and next gate. Do not assign artificial overall % where gates are not comparable. After every completed packet update STATUS.md, issue and experiment registry, preserving all source links and failure receipts.

## Immediate next actions (after plan is merged)

1. Check live GitHub owner/organization state and HF permissions; keep canonical location unchanged until org migration is possible.
2. Implement a zero-GPU auditable schema validator + Saudi synthetic page generator (10 exact, fully fake examples as smoke) and tests; never put a false seal/real ID on a fixture.
3. Obtain legally usable sample access to 3 P0 datasets, source-group dedup metrics, and exact rights receipts.
4. Build 100-page Saudi dev pilot using held-out original template families, and baseline LightOn vs PaddleOCR vs Qwen in equal conditions with real measurements.
5. Decide whether LightOn can learn Arabic and grounding without unacceptable regressions **before** spending large training hours. If proven unsuitable, change a decision record with evidence and maintain the single-Syag identity.
6. Create training experiment YAML/manifest and a frozen benchmark harness; progress to S05 only with an actual qualified compute environment.

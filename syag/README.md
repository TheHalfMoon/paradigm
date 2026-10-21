
# Syag — Saudi Arabic Document Intelligence

**Paradigm's single OCR / document-vision-language model program.** Name: Syag. Focus: source-faithful Arabic-first image/PDF transcription, document structure, reading order, tables, bounding boxes, visual fields and calibrated review behavior. Work for Saudi use-cases first, with credible general multilingual benchmark retention.

## START HERE — persistent source of truth
1. [Live Syag status](STATUS.md): completed, blocked, next work, source evidence.
2. [Master implementation and research plan](MASTER_PLAN.md): S00–S11 with acceptance gates.
3. [Autonomous agent continuation](RESUME.md): exact fresh-session workflow.
4. [Benchmark and anti-leakage protocol](BENCHMARK_PROTOCOL.md): official Arab/international tests.
5. [Data factory plan](DATA_FACTORY.md): licensing, privacy, synthetic, verification.
6. [Organization migration guide](ORG_MIGRATION.md): future GitHub Paradigm-AI organization and HF.
7. [20-source dataset registry](../datasets/syag/SOURCE_REGISTRY_2026-10-21.csv), [dataset study](../research/syag/2026-10-21/DATA_DISCOVERY_AND_ACQUISITION_PLAN.md).
8. [GitHub tracker, all Syag issues](https://github.com/TheHalfMoon/paradigm/issues?q=is%3Aissue%20is%3Aopen%20Syag).

## Current decisions
- One Syag model, no Lite/Pro. Released quantizations can remain same-model artifacts.
- Candidate base: [LightOnOCR-3-0.8B](https://huggingface.co/lightonai/LightOnOCR-3-0.8B), ~853M, Apache-2.0. **Provisional pending true Arabic/Saudi tests.**
- Independent challenger baseline: PaddleOCR-VL-1.6, Qwen3.5-2B, optionally others if lawful. No Falcon in the selection plan.
- Build Saudi original synthetic form/image pairs, rights-cleared Arabic corpora and double-reviewed held-out Saudi pages; do not train on benchmark tests.
- Aspiration: best-in-class on specific named independent benchmarks; **no SOTA or Syag training results are claimed now**.
- GitHub organization has not been created/verified; current canonical source is TheHalfMoon/paradigm/syag. The HF org https://huggingface.co/Paradigm-AI was supplied by owner, but writable account access not confirmed.

## For any future agent
Follow [RESUME.md](RESUME.md), inspect current GitHub HEAD and open PRs, then continue the next proven unblocked gate; commit code/tests/reproducible evidence and update [STATUS.md](STATUS.md). Do not wait for routine confirmation or invent completed GPU work.

## Expanded data and Kaggle execution (October 21, 2026)

**Long-term research target:** 5,000,000 unique rights-admitted source pages, not augmented duplicates. Follow [MILLION_PAGE_STRATEGY](MILLION_PAGE_STRATEGY.md), [BOOKS_CORPUS](BOOKS_CORPUS.md), and [KAGGLE_EXECUTION](KAGGLE_EXECUTION.md). These are plans, not downloaded data.

[Kaggle founder books intake #17](https://github.com/TheHalfMoon/paradigm/issues/17) covers licenses, scans and exact text/structure truth; [Kaggle isolation and compute #18](https://github.com/TheHalfMoon/paradigm/issues/18) preserves separation from Hala. Kaggle prohibits one person operating multiple active accounts under current published terms; use separate notebooks/datasets under one compliant identity, rather than creating an additional active account or bypassing quotas. Kaggle's limited free storage/GPU is not enough evidence to promise an all-corpus five-million-page training run.

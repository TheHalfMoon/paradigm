
# Syag Benchmark and Model Selection Protocol — v1.0 (2026-10-21)

## Status
Pre-registration specification; NO Syag benchmark has been executed in this plan. All future results require independently inspectable run receipts.

## Benchmark lanes; never mix incomparable official scores

| Lane | Benchmark | Intended test | Source and restrictions |
|---|---|---|---|
| AR1 | KITAB-Bench (2025 ACL; 8,809 samples, 9 domains of tasks and 36 subdomains) | Arabic printed/handwritten OCR CER/WER, RTL, layout, line recognition, tables TEDS, PDF->Markdown MARS, charts SCRM, diagrams CODM, VQA | https://github.com/mbzuai-oryx/KITAB-Bench ; **external eval only**; official rules and allowed input/output |
| AR2 | Misraj-DocOCR (400 reviewed pages) | Arabic page reading + structure | https://huggingface.co/datasets/Misraj/Misraj-DocOCR ; public split may be named train, but Syag policy eval-only |
| AR3 | KITAB PDF-to-Markdown reviewed | Arabic Markdown/table conversion | https://huggingface.co/datasets/Misraj/KITAB_pdf_to_markdown_reviewed ; external eval-only; overlap audit |
| EN1 | olmOCR-Bench | testable facts, omissions, hallucinations and document content preservation | https://github.com/jina-ai/olmocr-bench ; official output/normalization is NOT a CER metric |
| GEN1 | OmniDocBench v1.6 | high-fidelity parsing and reading order | https://github.com/opendatalab/OmniDocBench ; verify licensed release, exact version and scoring tool |
| GEN2 | Real5-OmniDocBench | robustness to photographed/degraded documents | inspect dataset and access terms before downloading; no result until official setup qualified |
| LAYOUT | DocLayNet withheld test | page zones and geometry | https://huggingface.co/datasets/docling-project/DocLayNet-v1.2 ; official test only and avoid same-source training leakage |
| TABLE | PubTables-1M official tests | table detection and row/column structure | https://huggingface.co/datasets/bsmock/pubtables-1m ; verify authoritative scoring, avoid training/eval duplicates |
| SA1 | SaudiDocBench (new, not created) | real Saudi VAT invoices, law-like documents, contracts, phone photos, forms, handwriting, Arabic/English mixed and dates | at least 500 independent pages + *new* unseen templates; newly collected with permitted assets and double annotation |

Other candidate lanes (Document VQA, receipts, charts, multilingual scripts) may enter via future protocol amendments only with version-pinned official sources. Public leaderboard scores are **publisher claims** until Syag and competitors are rerun or independently verified under comparable conditions.

## Benchmark identity, contamination, and judging

- Before samples are seen, write a locked benchmark manifest with upstream repo/revision, file checksum, source license, task selection and excluded classes, scorer SHA/version, inference params, processor/version, parser type, evaluation date and host.
- Keep every public benchmark's images/GT, descriptions, test hints, verifier trajectories and near-identical datasets globally denied from training. Quarantine source overlap with Alhazen/Loay/KITAB derivatives, BOE and published Saudi text; inherited base-model contamination uncertainty is explicitly stated.
- For SaudiDocBench, split original document, source institution, submitter identity, form template and writer groups BEFORE augmentations; hash originals and pHash near duplicates. Collect double human annotation, reconcile through reviewer adjudication; never certify pseudo-labels with the same OCR model being evaluated.
- The final sealed benchmark is opened ONCE for the candidate frozen on dev. A failed sealed run triggers a newly versioned follow-on test with documented previous exposure, not retuning on the same answers while continuing to call them unseen.
- Do not train on test data even if publisher labels its partition train. Do not register test documents as training data accidentally via synthetic clones.
- Report true page/document count by family and failure count including unreadable input, crashes, OOM, malformed JSON and timeouts.

## Study design (paired, auditable)

Use SAME source pages, image pre-processing budget, maximum page dimensions/token budgets and measured wall-clock constraints wherever technically compatible. Competitor model/system configurations are chosen on dev, then frozen. Distinguish:
1. **Model-only:** per-page model output and parser, consistent input rasterization.
2. **End-to-end:** PDF ingestion, orientation, multi-page parsing, table/field normalization, evidence and safety controls.
The LightOn 0.8B 2048-pixel limit and vendor-specific inference prompt must be recorded, not hidden. Use read-time/peak-memory p50/p95 and GPU utilization; avoid fake equivalence when models require different renderers.

Required frozen baselines:
- Unmodified lightonai/LightOnOCR-3-0.8B (chosen provisional foundation)
- PaddlePaddle/PaddleOCR-VL-1.6, including its actual layout subsystem in *system* lane
- Qwen/Qwen3.5-2B vision (or a qualified current small Qwen VLM)
- Optional Mistral OCR API / another paid comparator **only** if specifically authorized and lawful; otherwise mark not measured, never estimate quality from prompt outputs.

Stats: paired source-document cluster bootstrap 10,000 deterministic resamples; Wilson confidence limits for binary exact matches and unsafe accepts; predeclare family-level comparisons and multiplicity treatment. A 500-page pilot is an engineering selection instrument, not evidence of universal SOTA. Report uncertainty under distribution shift and writer/template class.

## Metrics and direction of improvement

| Metric | Unit | Main issue |
|---|---|---|
| Verbatim Arabic CER + WER | normalized vs raw reported separately, lower is better | diacritics, dot confusions, hamza, elongated words; preserve differences in raw |
| Critical numeric/field exact | percent strict exact full value + source attribution, higher is better | amount, VAT, date, patient/party identity, account/routing numbers; no silent correction |
| Hallucination / unsafe acceptance | frequency and CI, lower is better | generated facts absent pixels; hallucinated stamps/signatures, fabricated numeric fields |
| Layout | per-class AP/mAP and box IoU, higher is better | headings, columns, footers, tables, chart regions, paragraph structure |
| Reading order | edit/Kendall-based error; lower is better | RTL multi-column and bilingual sequences |
| Table | official TEDS plus cell-value exact and header-row association | equal table geometry can hide wrong digit/text |
| PDF->Markdown | official MARS and deterministic structural checks | nesting, lists, hyphenation, citation/footnote links |
| Chart and diagram | official SCRM/CODM + numeric unit match | visual data integrity |
| Handwriting | separate CER and writer-generalization with CI | baseline rarely robust on novel pen/phone style |
| Efficiency | p50/p95 page latency, peak VRAM, throughput, failures, estimated/actual cost 1000 pages | target deployment hardware & all failure costs counted |
| Calibration | risk-coverage curves and selective exactness | verify abstention not just confident-looking text |

Preliminary GO to larger training: LightOn pilot shows repeatable Arabic CER reduction against its own base on previously unseen groups with paired interval excluding zero, no worsening critical-field unsafe acceptance, and stable layout/English retention within pre-registered safety thresholds. Candidate large-scale release demands independent SaudiDocBench gain plus competitive best-in-class results in *named* public lanes. If gains or power are inconclusive, label INCONCLUSIVE; do not manufacture victory.

## Public reporting format

Every line of leaderboard report must include: exact benchmark version; model ID/revision; whether model-only or full system; precision; hardware; allowed external dependencies; pages/tasks N; baseline; Syag point estimate with CI; official scorer code SHA; dataset restrictions; approximate cost if measured; disclosed omissions. Never claim "world #1 in everything" or compare unlike modalities without an apples-to-apples official evaluation.

## Primary sources (verified public documentation at plan drafting)

- LightOnOCR-3 https://huggingface.co/blog/lightonai/lightonocr-3 (October 8, 2026).
- LightOnOCR serving scripts and per-model image sizes https://github.com/lightonai/LightOnOCR .
- KITAB paper https://aclanthology.org/2025.findings-acl.1135/ ; repository https://github.com/mbzuai-oryx/KITAB-Bench .
- olmOCR source https://github.com/jina-ai/olmocr-bench (testable fact criteria, not simple CER).
- PaddleOCR-VL 1.6 https://www.paddleocr.ai/main/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL-1.6.html (publisher scores, not Syag).

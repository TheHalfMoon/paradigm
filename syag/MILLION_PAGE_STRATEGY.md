# Syag — Multi-Million Page Research Strategy

**Version:** 2026-10-21 / evidence-first, no dataset acquisition or training implied.  
**Scope:** ONE Syag OCR and document-understanding model. Existing foundation candidate LightOnOCR-3-0.8B remains provisional until Arabic baseline trials; Hala and Plume do not share Syag private checkpoints, queues or quotas.  
**Target:** **5,000,000 high-quality unique, rights-admitted, base document pages** in a long-horizon research corpus. This is a stretch target, not an already acquired count or a guarantee of better benchmarks.

## What counts toward 5 million?

- Count **unique, independent source pages** after source-level exact and perceptual deduplication, not transformed/augmented copies or the same book/pdf rendered at multiple DPI, resolution or contrast settings.
- Source page may be scanned or born-digital rendered. For born-digital PDF, match extracted text to visible pixels after rendering, not blindly claim embedded text is complete GT.
- OCR-only labels are not automatically structure gold: distinguish page transcription, block/line coordinates, table cells and image descriptions. Maintain separate verified coverage by task.
- Keep books, copied document templates, scanned receipts, web corpora, document variants and cross-platform mirrors grouped by a stable original_document_family_id.
- Global excluded eval pool: KITAB, Misraj, KITAB reviewed, olmOCR/OmniDocBench official tests, OCR eval and SafeOCR evaluation artifacts. Hash/near-dup exclusion before training and augmenting.

## Scaling checkpoints — conditional gates

| Stage | Target eligible unique pages | Purpose / exit |
| --- | ---: | --- |
| A | 20,000 | legally admitted mixed Arabic and Saudi pilot; measure text/grounding/table-label error and sample bias; verify adapter and cost |
| B | 100,000 | diverse template families + real reviewed document slices; large ablation; detect generalization and regression |
| C | 500,000 | first broad Saudi/Arabic corpus; source-family de-dup and quality monitoring |
| D | 2,000,000 | high-diversity scanned/form/book/handwriting collections; measure learning-curve and freshness |
| E | 5,000,000 | long-term stretch, only if each increment produces statistically meaningful held-out gains and a funded or genuinely free qualifying training route |

No need to train on all five million blindly. Use held-out marginal-value analyses per 100k increment; stop adding low-yield near-duplicate pages. A 5M input corpus does not establish 5M high-quality, complete structure annotations. Maintain separate counts per verified annotation type.

## Target allocation (planning hypotheses, not discovered inventory)

| Modality group | Unique pages (target) | Required label fidelity |
| --- | ---: | --- |
| Book pages and printed Arabic (licensed founder books + cleared external corpora) | 1,500,000 | faithful visible transcript, line/block ordering and positions for validated subset |
| Saudi legal/administrative and enterprise records (mostly ORIGINAL SYNTHETIC templates + authorized real) | 1,000,000 | field/key-value truth, evidence boxes, form sections, headings and dates |
| Arabic-English financial and tabular documents | 900,000 | exact per-cell text, row/column merge structure, totals/taxes, document IDs and bboxes |
| Cross-language general layouts and complex technical documents | 900,000 | document hierarchy, charts/tables/formula where actual labels exist |
| Handwriting and phone-captured images from permitted original pages | 700,000 | true handwriting from distinct writers or unique *source pages* captured on phone; do not count extra camera transforms of the same page as new unique source pages |
| **Total (target)** | **5,000,000** | categories mutually exclusive by assigned primary class; real distribution measured later |

The real mix is conditional on what can legally and technically be acquired; this is NOT a five-million-page purchase order or proof of access.

## Storage/compute reality

- One distinct rendered image averaging 100KB => 500GB for 5M; 250KB => 1.25TB; 500KB => 2.5TB, **before** masks/coordinates, original PDFs, versions, duplicated caches, model weights and checkpoint snapshots. Actual compression/quality must be measured on a 10k representative pilot first.
- Official Kaggle documentation (2026-10): **200GB private datasets total and max 200GB per dataset, ~20GB saved notebook output, ~12h GPU notebook session, approx 30h/week GPU subject to availability**. Kaggle is not the sole permanent home for multi-TB corpora or unrestricted 5M training. See KAGGLE_EXECUTION.md and direct source links.
- Actual training cost is determined from measured pages/sec, gradient accumulation, sequence lengths, image resolutions, checkpoint overhead and eval costs; project a full-run budget only after an actual 1k/10k pilot.
- On a zero-cash budget use **streaming/chunked input** + cheap metadata pipeline and small bounded pilot stages. Never launch bulk huge jobs assuming free GPU resources can handle millions.
- Persist allowed originals to an approved long-term store with actual verified capacity/access (prefer source-hosted immutable references where license permits, or HF private repos with verified quota; Kaggle private datasets are a constrained execution cache). GitHub only manifests, code, hashes, tiny completely fictional reproducibility fixtures.

## Data source pools — initial research

- Previously recorded [20-source registry](../datasets/syag/SOURCE_REGISTRY_2026-10-21.csv): Alhazen, Loay Arabic scanned synthetic, AraReceipt/ReceiptSense, DocLayNet, CC0 Arabic document layouts and other candidates. Reported counts overlap or have license/quality restrictions. Do not add them all to reach 5M on paper.
- **Founder books:** inventory editions, page scans, permissions, transcription availability and visual/semantic distributions; process in BOOKS_CORPUS.md. Owning a copy is not a general commercial ML rights grant.
- **Saudi originals:** rights-safe new ZATCA-style invoices, contracts, tables, letters, public BOE/Najiz-inspired but original templates with fictional personal data. Real legal case files and Najiz authenticated pages are not a collection target.
- Additional HF/Kaggle/GitHub sources enter only after exact rights/provenance audit. Founder permissions may be privately referenced by scope/authority and are not required to be pasted into GitHub.
- Benchmark test sets strictly excluded. Never count the same digitized book's rendered pages and photographed variants as different underlying pages.

## Data quality and trust model

Each page has: source_id, original sha256, original_document_group, actual license and rights evidence reference, PII classification, page scan/image, exact visible transcript, bounding boxes (if verified), reading order, tables (if verified), original-vs-synthetic label, coverage indicators, language/script, capture/render profile, renderer version, confidence/annotation state and split.
Lifecycle: DISCOVERED -> RIGHTS/PRIVACY/QUALITY_AUDITED -> SOURCE_GROUPED -> DEDUPED -> SPLIT_ASSIGNED -> ADMITTED_TRAIN or QUARANTINED/REJECTED/BENCHMARK_ONLY.
Split by book edition/title/source, document, writer, template and entity family **before** augmentation. Preserve zero/arabic digit, decimal, Hijri, mixed RTL/LTR, footer, table association and bounding-box correctness.
Use exact synthetic render geometry and human-verified authentic labels. Teacher-model OCR on scanned books is a proposal, not ground truth. Track false acceptance and review rate of any OCR-derived labels.

## Scorecard per accepted batch

Required monthly/by-batch statistics: original documents, unique pages, augmented page views, bytes by modality, rights admitted/quarantined, number fully OCR-annotated, number with trustworthy geometry/table/field labels, duplication rate, language script mix, detected personal records, sample agreement/error, per-benchmark delta after training, time per page, costs/risks and remaining cloud quota.

The *real reason* to scale is improved **sealed** Arabic and international accuracy/structure, not a large counter.

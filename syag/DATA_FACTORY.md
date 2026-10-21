
# Syag Data Factory — Admission, Synthetic Generation, Quality and Reproducibility

**Status:** design contract only; no dataset upload/ingest performed under this plan.

## Data objectives

Create a rights-controlled, genuinely diverse Saudi-first corpus supporting image transcription, region geometry, bilingual reading order, table structures, forms, chart facts, and source-grounded fields. Diversity > pure sample count. Separate **authentic authorized scans**, **source-clean synthetic renderings**, and **public publisher-controlled training datasets**. No automatic claim that a GitHub repo license grants every contained image/text.

Reference dataset register (20 leads): ../datasets/syag/SOURCE_REGISTRY_2026-10-21.csv
Research details: ../research/syag/2026-10-21/DATA_DISCOVERY_AND_ACQUISITION_PLAN.md

## Admission state machine

DISCOVERED -> LICENSE_PENDING -> RIGHTS_CLEARED -> PRIVACY_CLEARED -> FORMAT_QUALIFIED -> CONTENT_QUALITY_PASSED -> DEDUPLICATED -> SPLIT_LOCKED -> ADMITTED_TRAIN|ADMITTED_DEV
OR: REJECTED, BENCHMARK_ONLY, QUARANTINED. A broad founder ownership/permission assertion is not itself a source-specific commercial grant; document a scoped private approval without exposing confidential contracts. Never silently reclassify license blockers.

Checks per admitted item:
1. Exact URI and commit/revision/hash; creator/source owner and license SPDX/source terms; redistribution limits and retained attribution.
2. Upstream image, text, fonts, brand, seal and personal data provenance; training permission does not necessarily allow redistribution of originals.
3. Privacy/PII screen for names, phone/account/ID numbers, case/health records and embedded QR payloads. Private documents require separate lawful authority and anonymization that cannot be reversed; synthetic should be fictional at source.
4. Strong data-text agreement checks (not same-model circular verification), matched Unicode NFC and strict raw-vs-normalized strings.
5. Geometry sanity; all boxes inside image pixel bounds; correct polygon winding, non-overlapping line order when applicable; table structural syntax and cell association.
6. Duplicate grouping by SHA256 + perceptual hash + document source + template family + writer/entity + OCR text similarity. Group BEFORE random split, augmentations, render seeds and dataset concatenation.
7. 100–300 random human reviewed samples per priority source as sampling **goal**; report found errors and rejection rate. No automatic trust just because dataset card calls it high quality.

## Suggested schema v1.0 (JSONL record examples are contracts, not generated data)

Top-level: record_id, source_id, source_revision, original_sha256, provenance, license_id, license_evidence_uri, privacy_review_id, rights_state, group_id, split, image_uri, pdf_uri (optional), width_px, height_px, page_no, script_tags, quality_flags, capture_device_type, render_pipeline_commit, render_seed, annotator_id(s), annotation_version.

- transcript: {verbatim, normalized, language_regions, line_break_policy}
- elements: [{id, type, bbox_xyxy_px, polygon_px, text_verbatim, reading_index, parent_id, confidence_if_model_labeled, verified_ground_truth_boolean}]
- tables: [{id, bbox_xyxy_px, rows, cols, merged_cells, cells:[{row,col,rowspan,colspan,text,source_element_ids}]}]
- fields: [{field_name, value_verbatim, value_normalized, source_element_ids, source_boxes, missing_boolean, validation_rules}]
- annotation provenance: original human, exact synthetic render, or teacher proposal plus human correction; NEVER label teacher output as gold by itself.
- separate safety-evidence validation envelope compatible with generic SafeOCR patterns but no FHIR-specific assumptions.

No opaque PII copy into test fixtures. Store metadata and hashes in GitHub; bulky images in HF private repo only if permitted and org quota available.

## Saudi Synthetic Document Factory v1

Build independent fictional form families (50–100 target families across phases):
- SAR/Arabic-English VAT invoice with ZATCA-inspired field *specifications*; original layout and fictional identities. Generate canonical JSON and visual table; compute VAT arithmetic and assert.
- Contracts, judicial-like notices, letters, rental and HR forms, shipping receipts, payment schedules, license-like certificates, statements, data tables, diagrams, bar charts, stamped pages clearly marked synthetic.
- RTL paragraph blocks mixed with LTR serial numbers, email/URLs, Arabic/Western digits, negatives, decimal separators, currency, Gregorian + Hijri formatted dates and footnotes.
- Multi-page logical ordering, multi-column text, headers/footers, tables with rowspan/colspan, dotted lines, crossed-out corrections and realistic photocopies.
- Camera distortions as separate reproducible render transforms: JPEG, shadows, glare, angle, crops, rotation, motion blur, low contrast, ink bleed, folded edges.
- Where true handwriting samples are unavailable, do NOT relabel Arabic font-rendered text as genuine handwriting. Get genuinely hand-written rights-cleared samples with writer-independent test splits.

Ground truth is generated *before* raster degradation. Preserve exact bbox transforms through affine transformations, reject non-geometric distortions that invalidate assumed labels; use visibility flags/occlusion labels. If a page content is invisible, ground truth policy distinguishes unreadable/abstain rather than demanding impossible OCR.

Use properly licensed fonts and images; keep font licenses/revisions. Never embed a real person's ID, phone or tax number as synthetic. Never reproduce official seals/marks in a misleading manner.

## Anti-leakage and test freezes

- Global denylist: public KITAB and derivatives, Misraj-DocOCR, KITAB Reviewed, OCR-Data/ocr_eval, SafeOCR-LabGold and current benchmark assets. No benchmark-based data generation prompts that copy test pages.
- Alhazen includes some Loay synthetic pages: near-duplicates MUST stay grouped and de-duplicated; KHATT-derived samples require writer grouping. ReceiptSense and AraReceipt may share originals.
- Dev = available for model selection; Sealed private Saudi test = unobserved until final; Official public benchmarks = external only and report contamination uncertainty from pretraining.
- Maintain non-overlapping source-family IDs and expose overlap rates by dataset. Prefer a sample with high real diversity over million quasi-identical fake templates.

## Data acceptance reports

Every dataset commit/manifest generates: unique originals count; page-family mixture; text script and source types; train/dev/sealed disjointness proof; near duplicates; rights and privacy audit; spot audit error fractions; OCR text/image alignment; bad box/table rate; coverage by font/writer/camera; rejection categories; source hashes. Keep replayable records, not just summary numbers.

## HF layout proposal (not created)

- Paradigm-AI/syag-corpus (private). Dataset card provenance and every source notice. Chunk by source and release; no copy of unredistributable sources.
- Paradigm-AI/syag-eval (private, restricted) only owned/approved sealed pages, and no credential exposure.
- Paradigm-AI/Syag (model repo when actually trained, with model card and notices).
Current connector belongs to MedScale and grants read-only HF scopes. Do not write or claim ownership until Paradigm-AI access is verified and approved. Check HF quota and job costs before downloading large payloads.

## First delivery checklist for S03/S04

- 10 original fictional multi-script Saudi samples with exact raw text, box geometry, reading order, tax math and Markdown/JSON; deterministic unit tests.
- Registered sampler of 100 source examples from three different eligible datasets; LICENSE and privacy admission receipts for each source.
- Proven dedup by original image and source group; dry run output report; no real data in GitHub.
- Benchmark denylist validator and source-group split assertions with failing fixtures.
- Only then scale synthetic generator and apply a small LoRA pilot per MASTER_PLAN.

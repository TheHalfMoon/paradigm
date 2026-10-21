# Syag — Saudi Arabic document-data discovery and acquisition plan

**As-of:** 2026-10-21. **Target Hugging Face organization:** https://huggingface.co/Paradigm-AI (supplied by founder; write access not verified).
**One model:** Syag (provisional foundation LightOnOCR-3-0.8B). Not Syag Lite/Pro. OCR + RTL reading order + page geometry + tables + structured fields.
**Repository output:** sourced discovery and a machine-readable source registry; **not** a claim that datasets have been downloaded, audited end-to-end, uploaded, or used for training.
**Canonical source list:** [SOURCE_REGISTRY_2026-10-21.csv](../../../datasets/syag/SOURCE_REGISTRY_2026-10-21.csv), 20 candidates/leads including explicit benchmark-only and excluded sources.

## Key result

The best first *data programme* is NOT unrestricted harvesting from Najiz. It is a reproducible combination of (1) licensed Arabic real-document layout and transcription, (2) owned Saudi invoice/legal/form synthetic renderings with exact image/field/location ground truth, (3) a controlled supply of foreign-language layout/table examples, and (4) frozen independent Arabic benchmarks.

### P0 short list: sample and audit before promoting any samples to admitted_train
| Dataset | Publisher evidence | Fit | Caveat |
| --- | --- | --- | --- |
| [Alhazen OCR Data](https://huggingface.co/datasets/context212/context212-alhazen-ocr) | 52,726 train / 1,000 eval, CC BY 4.0 | Arabic full-page image-to-transcript, limited handwriting and invoices | ~85% synthetic according to its own card; source includes [Loay Faker 300k](https://huggingface.co/datasets/loay/arabic-ocr-synthetic-scans-faker-300k), so group-dedup instead of adding both naively. Upstream rights/provenance must be checked. Never use Alhazen's eval rows for training. |
| [Loay Arabic synthetic scan 300k](https://huggingface.co/datasets/loay/arabic-ocr-synthetic-scans-faker-300k) | 300,000 ~39.2GB, CC BY 4.0 | Arabic layout tags, columns, scan artifacts, fonts | Publisher explicitly says Faker text is not semantically coherent. Use for exact visual OCR/layout rather than linguistic/world knowledge. |
| [AraReceipt](https://huggingface.co/datasets/IslamMesabah/AraReceipt) | 100 images, 4,609 manually reviewed polygon regions, MIT | Arabic mixed-script receipts, per-region transcription and field classes | Inherits ReceiptSense images: near-/exact-image group dedup. Small sample size; quality > scale. |
| [ReceiptSense](https://huggingface.co/datasets/Timokerr/CORU) | MIT, publisher states 20,000 annotated receipts; 30,000 OCR-annotated images; related subsets | Arabic-English receipts, item/price/date localization, field extraction | HF card mixes file formats between splits; inspect underlying structure rather than claiming a ready-to-load row count. |
| [DocLayNet v1.2](https://huggingface.co/datasets/docling-project/DocLayNet-v1.2) | 80,863 annotated page images in original DocLayNet; CDLA-Permissive-1.0 | 11 document layout classes; document structure | Mostly non-Arabic: separate layout objective, not Arabic transcription truth. Group by originating document. |
| [Humans in the Loop Arabic Documents](https://humansintheloop.org/resources/datasets/arabic-documents-ocr-dataset/) / [Kaggle](https://www.kaggle.com/datasets/humansintheloop/arabic-documents-ocr-dataset) | Publisher declares 10,000 images CC0 1.0 | 12 genres, page polygons and text line boxes, transcribed titles | Does **not** provide verified full text for every line. Good for detection/layout; do not invent OCR gold. |
| [PubTables-1M](https://huggingface.co/datasets/bsmock/pubtables-1m) | table detection/structure data, CDLA-Permissive-2.0 card | table row/column geometry | Supplement only; original licensing and article/image provenance must be checked. |

### Valuable but gated / NOT P0 training

- [OCR-Data-new/ocr_data](https://huggingface.co/datasets/OCR-Data-new/ocr_data) has Arabic RTL reading-index, bbox and augmentation metadata, but the inspected card has **no license**. HOLD until an adequate license grant is verified; its companion [ocr_eval](https://huggingface.co/datasets/OCR-Data/ocr_eval) explicitly says not to train on its 1,500+1,500 test examples.
- [medyas/arabic-ocr-printed-500k](https://huggingface.co/datasets/medyas/arabic-ocr-printed-500k) describes a 500k archive, but the dataset viewer exposes ONE metadata row, not 500k immediate records; it declares CC-BY-SA-4.0 and Wikipedia provenance. HOLD for archive, attribution and share-alike audit.
- [mssqpi/Arabic-OCR-Dataset](https://huggingface.co/datasets/mssqpi/Arabic-OCR-Dataset) advertises 2.16M rows but current accessibility/license could not be verified. HOLD.
- [SARD](https://huggingface.co/datasets/riotu-lab/SARD): 2,621,075 synthetic pages / 1.54TB, **CC-BY-NC-ND-4.0**. Do not admit to commercial training without a separate valid permission; public availability is not sufficient.
- [Misraj-DocOCR](https://huggingface.co/datasets/Misraj/Misraj-DocOCR), 400 expert-reviewed pages, and [KITAB PDF→Markdown Reviewed](https://huggingface.co/datasets/Misraj/KITAB_pdf_to_markdown_reviewed): independent **evaluation-only** despite their Apache-2.0 cards. Misraj calls its public split `train`; ignore the split label and never feed these into model training.
- [SafeOCR-LabGold](https://huggingface.co/datasets/MedScaleAI/SafeOCR-LabGold) remains an independent synthetic clinical evaluation reference; no Syag training contamination.

## Saudi-specific acquisition channels

**1. [BOE](https://laws.boe.gov.sa/BoeLaws/Laws/Folders/1).** Useful legal typography, headings, ordered articles and amendment patterns. Public readability does not establish a bulk ML training license. Inventory legal page types and metadata, and generate owned *new fictitious* legal-looking pages without implying they are authentic government instruments. Reproducing BOE documents as training images is pending a source-specific usage/rights check.

**2. [MoJ open-data policy](https://www.moj.gov.sa/ar/OpenData/pages/opendatapolicy.aspx), [dataset library](https://www.moj.gov.sa/ar/OpenData/Pages/library.aspx) and [public legal portal](https://laws.moj.gov.sa/ar/).** Open statistical data may assist in choosing realistic anonymized field distributions, terminology and document types. Published policy requires source attribution, accurate handling and honoring the release license. Open statistics **are not** user-uploaded court files, judicial identity records or Najiz private cases.

**3. Najiz.** Use only publicly available guides/templates to understand form layout. Do not crawl authenticated accounts, user-specific judgments, deeds, authorizations, case records, or personal fields. Any later owner-provided real corpus needs explicit authority for that corpus and privacy handling. Prefer fictional synthetic records.

**4. [ZATCA e-invoicing specifications](https://zatca.gov.sa/en/E-Invoicing/SystemsDevelopers/Pages/E-Invoice-specifications.aspx).** Turn permitted technical field definitions into **original** Arabic/English invoice renderings and matched machine-readable XML/JSON truth, with fictional vendors, synthetic tax identifiers and SAR amounts; generate correct tax arithmetic and challenging RTL/LTR numeric formatting. Do not describe these as validated production e-invoices.

## Training corpus architecture

**Suggested private repos (NOT created yet):** `Paradigm-AI/syag-corpus`, `Paradigm-AI/syag-eval`; eventual `Paradigm-AI/Syag`. Keep raw third-party payloads in-place or in approved private, quota-checked storage; GitHub stores only code, manifests, hashes, prompts, experiment metadata and source receipts. The current connector is a read-only OAuth session belonging to `MedScale`, not verified as TheHalfMoon or Paradigm-AI admin: **no HF writes claimed**.

Dataset unit: a *source document group*, not a random page. Suggested training `document_record` fields:
- `source_id`, `source_revision`, `license_id`, `license_evidence_url`, `provenance_chain`, `sha256`, `group_id`, `split`, `synthetic_or_real`, `privacy_review`, `attribution`;
- `image_ref`, `page_index`, `width`, `height`, `locale`, `font`, `degradation`, `render_seed`;
- `text_verbatim` and `text_normalized` as different fields; `elements` including `bbox`, `type`, `text`, `reading_index`, `table_row`, `table_col`;
- `fields` with source-backed values, boxes and verification; uncertain truth is null, not generated guesses.

**Train/dev/sealed-test boundaries:** Dedup by SHA256 and near-image fingerprint, then group by underlying receipt, form template, scan source, document, source-text sample, entity identity, and augmentation seed **before** assigning splits. Keep source-derived augmented variants and near duplicates in the same partition. Freeze Misraj, KITAB, OCR Eval, other external benchmarks and SafeOCR benchmark as a global denylist. Check contamination against the candidate base checkpoint where possible.

**Admission gates:** source existence and immutable revision; license for training + derivative outputs + redistributions if any; provenance chain and right-to-use images/text; private or PII screening; 100-300 human spot audits per high-priority corpus; image-text exactness, Arabic RTL fidelity, bbox range checks; source-group dedup; documented acceptance and exclusion counts. A license on a repo's code is not a license to its data.

## First experiment sequence — zero paid services until user explicitly authorizes a change

1. Verify actual organization access/quota and create private dataset/model repos only under authorized credentials. No automatic paid plans.
2. Audit samples of Alhazen / Loay / ReceiptSense / AraReceipt / DocLayNet / CC0 document images, without bulk mirroring initially.
3. Build a **Saudi Synthetic Document Factory** using licensed fonts/assets and own templates: e-invoices with source JSON+XML, legal letters/clauses, contracts, administrative forms, tables, phone photos, stamps as explicitly synthetic markings and controlled scan degradations. Also produce element bboxes and reading order; no raw citizen data. Use 50–100 template families, not millions of slight variations of one template.
4. Prepare an initial ~10k–20k usable-image pilot only after admission gates. Keep a wholly separate 500+ Saudi-page human-verified test suite spanning real conditions where collection is authorized. Counts are goals, not presently collected facts.
5. Baseline unmodified LightOnOCR-3-0.8B on dev tasks with fixed inference and privacy boundaries. Train a bounded adapter, select via dev, then compare on sealed holdout once. Include an unchanged PaddleOCR-VL-1.6 challenger. No performance or cost claim before runs.
6. Expand breadth only where error analysis shows a real gap: Arabic numeral glyphs, Arabic/English reversals, RTL punctuation, handwriting, stamps, photos, tables, Hijri dates, official forms.
7. Report CER/WER, Arabic token and field exactness, table TEDS, reading-order and grounding IoU, hallucination/abstention, page latency, VRAM and cost. Record failures and provenance.

## Evidence and limitations

Sources inspected on 2026-10-21: linked cards and government official sites above plus [ZATCA specifications](https://zatca.gov.sa/en/E-Invoicing/SystemsDevelopers/Pages/E-Invoice-specifications.aspx); [Kaggle hosted HITL](https://www.kaggle.com/datasets/humansintheloop/arabic-documents-ocr-dataset). Discovery counts are *publisher declarations*, not verified local byte-level audits. Dataset rights vary; the founder's general statement about having permissions does not identify rights grants from every independent publisher. Owner-provided permission can be applied when scoped, documented and verified. No data downloaded or trained through this research change.

## Resume

Read [Paradigm AGENTS.md](../../../AGENTS.md), latest repo SHA/PRs, this plan and the CSV, then perform one audited small-sample ingestion at a time. Update the registry only with proven new rights/split/quality evidence and keep Kaggle/HF/GitHub mirrors coherent through manifests, not silent copies.

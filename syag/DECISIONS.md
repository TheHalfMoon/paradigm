
# Syag Decisions and Revision Triggers — D-2026-10-21

## D01 — One product/model identity (ADOPTED)

The product is Syag, not Lite/Pro tiers. One main learned checkpoint and versioned successors; transformed quantizations of the same learned model are permitted as deployment artifacts with fidelity testing. Infrastructure helpers like PDF rendering and JSON validators do not become separately branded AI models.

## D02 — Foundation model provisional: LightOnOCR-3-0.8B (RESEARCH CHOICE, NOT QUALIFIED)

- Official model: https://huggingface.co/lightonai/LightOnOCR-3-0.8B
- Official released announcement: https://huggingface.co/blog/lightonai/lightonocr-3 (2026-10-08).
- Official source and version-specific 2048-pixel serving guidance: https://github.com/lightonai/LightOnOCR .
- Model card from publisher: ~853M params, model_type qwen3_5, image-to-text and document-grounding, Apache-2.0, published language tag English.
- Why chosen for *research pilot*: output combines OCR, document structure and regions/bounding boxes in one learned model at small size; licensing allows commercial derivatives under notice conditions; source ecosystem has executable client.
- Key unproven risk: formal Saudi Arabic script and handwritten/page layouts are **not** validated from the model card. Fine-tune recipe and visual layers must be qualified before assuming LoRA works.
- Action: first run exactly pinned Arabic baseline against PaddleOCR-VL 1.6, Qwen3.5-2B, one extra Arabic specialized control if data/compute permit. Do not change foundation based on self-reported cross-benchmark scores.
- Pivot threshold: if the candidate cannot learn Arabic after a small qualified adaptation without unacceptable regression in structure/general English or critical fields, record frozen measured comparisons and select an allowed alternative through an auditable decision update. Still produce ONE Syag model.

## D03 — Data-first, provenance-first (ADOPTED)

Source-card licenses for Alhazen, Loay, ReceiptSense, DocLayNet and HITL are *candidate* admissions, not approved corpus releases. Source privacy and upstream copyrights exist independently. Saudi legal sources BOE, Najiz, Ministry of Justice public portals are task and template research; real customer/court documents may not be scraped merely because accessible. SARD is excluded under listed NC/ND until genuine additional rights are documented.

## D04 — Benchmarks must be independent (ADOPTED)

KITAB-Bench (ACL 2025, https://aclanthology.org/2025.findings-acl.1135/) spans 8,809 samples and nine types of Arabic OCR/understanding task; reserve public pages and future variants as external evaluation. Other external readouts: Misraj, olmOCR-Bench, OmniDocBench 1.6, Real5, DocLayNet tests and PubTables tests. Fresh internal SaudiDocBench must be source/template/writer held out and independently adjudicated. Do not use KITAB score from mixed task columns as a single universal metric. Publish each named benchmark rank only if dated independently verified official comparable runs support it.

## D05 — Hosting split and owner boundaries (ADOPTED PLAN, NOT EXECUTED)

GitHub TheHalfMoon/paradigm/syag is currently canonical because no connected GitHub org membership exists; proposed Github org Paradigm-AI/Syag is pending actual org creation. HF supplied org https://huggingface.co/Paradigm-AI intended for authorized private corpora and released Syag; authenticated HF tool identity currently MedScale read-only and cannot upload. All data/weights should remain off persistent local systems and outside GitHub. First verify secure rights and quota.

## D06 — Zero-cash research gate (ADOPTED)

Use no paid GPU or paid OCR API without separately granted expenditure authority; evaluate free remote GPU availability as unverified capacity. Never treat a nominal free tier as guaranteed usable quota. No release until security/privacy/license validation.

## Evidence strength

- Publisher published facts: model cards and linked documents. Strong evidence of public code/reported specs, NOT independently validated Syag capability.
- Repo content records: Paradigm data source registry and research plan, PR #2 merged on 2026-10-21, SHA ca2aff20fd9602312fec4412c295d8f2f605063b.
- Syag training, benchmark ranks, data ingestion, HF uploads, and serving: UNEXECUTED at time of this record.

Do not edit past decision rationale retroactively; append D07+ with timestamp, model/revision, datasets, scored results, reviewer, and competing hypotheses.

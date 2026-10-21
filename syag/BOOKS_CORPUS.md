# Syag Founder Book Corpus — Rights, Scans, Ground Truth, and Training

**Status:** not started; founder reports access to many books but no book list/files/pages or rights evidence supplied in this conversation. Do not claim processed books.

## Goal

Use books to teach Syag diverse Arabic typography, page hierarchy, paragraph/verse/list/footnote order, bilingual footers, math, tables, historical print scans and handwritten marginalia *where present*, without confusing authentic books with generated pages or contaminating official OCR test books.

## Book intake manifest (private or redacted as appropriate)

For each candidate volume record:
- internal id, title/edition/author/publisher/year/ISBN if any, pages and volume/part, language/script/font/genre, born-digital text PDF vs image-scanned vs physical volume;
- file original SHA256, page/image checksums, rights_owner, approved training scope, any copy/redistribution constraints, privacy and moral-rights notes, license proof reference (can be private), public domain jurisdiction justification if used, and intended storage;
- whether optical characters, reading order, full ground truth text, line bboxes, tables/footnotes or only source images actually exist.

The founder's ownership of a **physical copy** is not by itself copyright permission to redistribute or train on protected text/page images. Founder-provided author rights, public-domain books, appropriately licensed books and contract-permitted scans may be accepted with recorded provenance. Some book digitizations have independent scan/layout/reproduction restrictions.

## Ingestion path

1. Choose only a small set representing many independent fonts/publishers/eras (10-volume audit; count is goal, not completed).
2. For digital PDFs: identify text-layer quality and per-page character positions; align rendered page pixels with text; tag missing diacritics, merged ligatures, RTL reading order and page footnotes; preserve original and normalized transcripts separately. Never assume the text layer matches visible scan.
3. For scanned or photographed books: extract pages; manually review sampled transcript zones, propose weak OCR labels from an external reader, correct with independent human or pixel-level verification; label confidence and absent text appropriately. Teacher labels without verification are never gold.
4. Use layout zoning to tag chapter title, verse, text columns, line, footnote, table, diagram, picture and page number. Record visible reading order (Arabic direction) and bboxes in correct pixel coordinates. Page screenshots alone only supervise weak tasks until transcript quality is adequate.
5. Detect same book in HF/Kaggle/GitHub/Misraj/KITAB, duplicate editions and pages or re-rendered copies. Group by work/edition/page and keep close variants within one split; never contaminate public benchmark books.
6. Store allowed page assets/checksums privately after verifying owner and quota. Code/manifests go to GitHub; do not commit scanned books, ISBN metadata exposing user's private library inventory if sensitive, private contracts, or personal records.
7. After intake, allocate eligible book sample classes: mature full-transcript labels, layout-only pages, pseudo-labels still under review, unusable/unlicensed quarantine and held-out test-only books. Keep real scanned pages in a separate class from synthetically rendered pages.
8. Evaluate book-specific held-out CER/WER, page order, footnote and text-column associations, handwritten marks, OCR speed. If a common template dominates train, downweight and seek underrepresented layouts.

## Training recipes for volumes

- Printed Arabic and punctuation: faithful line-level transcription objective.
- Structural learning: chapter/section lists, columns, footnote–anchor association, tables and citations.
- Robust scan reading: truthful occlusion tags; never force model to hallucinate lost text.
- Text-only book material cannot train image OCR by itself until rendered as permitted page images with authoritative text and geometry, and synthetic render status remains separate from authentic scans.
- Never call a font-based imitation of handwriting “real handwritten.”

## First intake acceptance criteria

At least one book with auditable permission and full source hashes; at least 50 randomly selected pages checked for image/text fidelity; distinct book/edition grouped splits and a benchmark overlap check; real acceptance/rejection numbers in GitHub issue #17, no private payload disclosure.

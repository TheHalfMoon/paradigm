# Hcompany dataset forensics

This investigation read cards, HTTP metadata and selected public JSON records. No screenshot archives or training dataset payloads were downloaded to the personal computer. Hashes/revisions appear in [source registry](../evidence/source-registry.json). No extra official factory training corpus was found in the inspected releases; that is bounded search evidence, not proof none will ever exist.

| Dataset, frozen revision | Purpose / observed structure | Actual license and suitability | Leakage policy |
|---|---|---|---|
| [DragOn](https://huggingface.co/datasets/Hcompany/DragOn/tree/3451c1fc3543c18fc3361a32bfe1f12cc69b64b5) |286,012 images;3,560,142 train drag tasks. text 100k/1M, sheet 38,332/996,632, slide 82,680/992,160, slider 65k/571,350. Public eval 1000; private test 1000 unavailable | Card Apache 2; asset provenance/privacy still reviewed per subset. Useful instruction-conditioned start/end grounding, not complete multi-step planning | Split train by screenshot/image_id and template; never mix public eval in training or imply access to private test |
| [trajectories](https://huggingface.co/datasets/Hcompany/trajectories/tree/ede2a362c99ddba0d03f439c47a0b8fea6abae22) | **7,366 benchmark executions**, across models/runs and six benchmarks; index/task JSON with screenshots referenced separately | Apache 2 card plus underlying benchmark licenses. Failure taxonomy and harness analysis only; not the 10k task-factory training set | Deny benchmark tasks, instructions and gold/generated trajectories from training. Similar task/template leakage matters even with renamed IDs |
| [h_cua_perf](https://huggingface.co/datasets/Hcompany/h_cua_perf/tree/c13201944c7b9769e86357adcfd9bc8d991d46de) |477 traces/18,224 requests;2.5GB compressed/9.3GB uncompressed stated; Mooncake replay messages/tools/delay/output_length, five length buckets | CC-BY4.0. Serving load/latency fixture, **not task-completion labeled SFT data** | Isolate performance lane; no training, no task-success claim from replaying requests |

The HF API used Storage values (DragOn~61.5GB, trajectories~128? do not substitute an unverified figure, perf~12.6GB) can include repository history and are **not** exact current download size. Plan transfers using pinned sibling LFS sizes/manifest and selected files. Cost quoted from card compression is approximate.

## Records actually inspected

Three pinned DragOn public eval metadata records expose screenshot path/instruction/start_bbox/end_bbox, ordered and subtype metadata. Boxes are pixel[x 0, y 0, x 1, y 1], not normalized points. Range-selection sample is unordered; row resizing and fill-handle samples are ordered. These three records verify schema only; they do not quantify train quality. A reversed drag can invalidate an ordered example. Image-to-task ratio~12.45 train tasks/image means a task-level random split leaks screenshot/template information.

Two trajectory JSON records for the same OSWorld 2 task 001 under Holo 35/Holo 27 were inspected without fetching images. Steps expose image, observation, thought, note, calls, results, usage; task/system/verifier metadata differs from a generic instruction–answer corpus. Repeated task appearances across models/runs are expected. Inspecting record structure is not re computing its verifier in an environment.

perf-meta confirms 477 traces/18,224 turns, built_at 2026-09-18, median 23 steps/mean 38.2 and cap 200 in card. trace_processor.py was read at pinned revision. Each replay request keeps the latest screenshot while earlier images are substituted, allowing text/KV to grow while image count stays bounded.25 compaction/OCR calls have no tools. There is no corresponding gold goal-success supervision. Its bucketed request distribution must not be advertised as production traffic.

## Genuine publisher-index re computation

The complete 5,046,690-byte index SHA-256 is **a8525624049894e1aeb220790ed8c013067a99f2ffdbcb938d5a4cef91f0cf53**. [Recomputed groups](evidence/hcompany-index-audit.json) contain 7,366 unique IDs and 7,366 unique(model, benchmark, task, run) tuples. This is metadata duplicate counting, not semantic/image deduplication.

| OSWorld 2 publisher subset | Records / unique tasks | Binary success | Mean partial score | Median wall time |
|---|---:|---:|---:|---:|
| Holo 4-27B |106/106|41.5094%|61.7319%|2046s|
| Holo 4-35B-A3B |106/106|12.2642%|30.8937%|533.5s|

Thus the advertised Holo 35 **30.9% is mean partial completion, not binary task success**. These are publisher executions, not our independent benchmark run. Public subset excludes two PII-containing tasks according to the card; exact historical task/assets/version/budget must still be established for replication. Deriving cost-per-success from publisher cost and binary fraction is merely a ratio, not measured Hala economics.

AutomationBench index means and success fractions do not match the headline model-card figures (Holo 35 card 34.5 vs index 50.25%binary/80.92%mean; Holo 27 card 45.4 vs 58.875%binary/87.03%mean). **Unresolved metric/protocol discrepancy**: do not cherry-pick one or blend them into a common leaderboard. The source register records this contradiction in comparability.

## First Hala data

Begin with fresh, state-verified tasks on owned/self-hosted environments. Optionally use a cleared **DragOn train** subset for drag-specific grounding if a held-out deficit exists; audit 50–100 records per subtype and separate screenshot/template/identity groups. Exclude benchmark trajectories and perf fixtures from training. Proposed 10–30k grounding examples and 500–2,000 successful fresh trajectories are pilot ranges; expected effect size is unknown. No fixed gain can be inferred from dataset size.

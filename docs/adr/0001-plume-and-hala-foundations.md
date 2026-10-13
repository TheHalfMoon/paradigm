# ADR0001: provisional foundations and staged adaptation

Status: Accepted (research decision);Date:2026-10-12.

## Context

Plume needs commercially distributable cinematic improvements;Hala needs general desktop/browser/MCP competence. New open-weight checkpoints may have restrictive licenses, missing trainers or unmatched vendor scores. NoGPU quality comparison has been executed. The user's priority isPlumefirst without paid services or agreements being activated during research.

## Decision

RetainWan2.2T2V-A14B for a source-qualified high-noise cameraLoRApilot, challenge it withMITLongCat, and use distinct modules/checkpoints for absentAV/reference/editing capabilities. RetainApacheHolo4-35B-A3B for generalHala, improve ownedharness/freshtaskverification beforeSFT, and evaluateMITFara1.5 browserchallengers separately. ExcludeHcompanybenchmarktrajectories/perfreplay fromtraining. Persist approveddatasets privately onHF and process remotely. Use originalBF16Wan shards;FP16repack/BF16training is rejected by inspectedsource.

## Consequences

These choices minimize legal/recipe uncertainty but do not establish highestquality. A14B and35Btotal residentmemory remain expensive. Syntheticcamera labels may nottransfer. LongCat orFara canreplace the scopedbase after a matchedCI/cost/capability win; update through a new append-onlyADR rather than silentlyrewrite this acceptedrecord. Biggertraining/AV/asyncRL need fresh experiments andapprovedbudget. Actualrights,environment/GPUfitandquality areexecutiongates.

Evidence:[Plume comparison](../../research/plume/MODEL_COMPARISON.md),[Hala route](../../research/hala/RECOMMENDED_ROUTE.md),[source compatibility](../../research/plume/TRAINING_STRATEGY.md),[forensics](../../research/hala/DATASET_FORENSICS.md).

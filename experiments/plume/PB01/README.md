# PB00qualification and PB01camera-LoRA package

**Prepared, not executed.** These commands were checked against pinned source/parser flags and shell syntax; they have not loaded weights, resolved the complete environment or trained onGPU. No script provisions compute, fetches training payloads or grants permission to spend. Required environment bindings include explicitapproval identity, actualdatasetcommit andqualifiedenvironmentlock.

Research hypothesis: a small balanced set with correct camera/event labels improves camera adherence while retaining realistic texture, anatomy and temporal coherence. BaseWan-AI/Wan2.2-T2V-A14B@c8c270b13ee05bfa474194ac9fb07a5868a97cea. TrainerMusubi@f8a1b03794a49239a3539015075f5123d6c07d66. All architecture/training choices are fixed in [config.json](config.json); GPUfit andquality remain hypotheses.

## Remote preparation and weight binding

Use authorized Linux compute,Python3.11, candidateCUDA13.0/torch2.9.1/torchvision0.24.1/bitsandbytes0.49.2 and upstream exactrequirements in [constraints](environment-constraints.txt). Those three package versions exist onPyPI; jointresolver/import/GPUkernelcompatibility is untested. The upstream has no committeduv.lock. Resolve constraineddependencies, install the pinned source and record full `pipfreeze`, CUDA/driver/build/hardware details and fileSHA as the runenvironmentlock. Ifresolution fails, fix a source-backed compatibility issue and record the deviation before anytraining; do notlabel thecandidatequalified.

Selectively retrieve originalWanBF16weights **onremote scratch only**. Requiredrelativefiles: sixshards plus index/config in each high_noise_model andlow_noise_model;WAN_HIGH/WAN_LOW point at their `diffusion_pytorch_model-00001-of-00006.safetensors`. The inspectedloader expands that namingpattern toallsixshards. Requiredauxiliaries:Wan2.1_VAE.pth,models_t5_umt5-xxl-enc-bf16.pth andgoogle/umt5-xxltokenizerfiles. Verifyrevision,LFS/filehashes,dtypes andstrictkeys/shapes remotely. SourceAPI confirmedthese paths; noweightswere downloaded here.

Musubi sourceassertsFP16DiT needsFP16 ornomixedprecision, andBF16DiT needsBF16 orno. A convenientFP16Comfyrepack istherefore **not** theBF16recipe input. PrequantizedscaledFP8inputs arealso unsupported in inspectedWanrecipe. OptionalruntimeFP8/blockswap is a separately registeredqualificationvariant,not asilentbaselinechange.

## Data contract

Proposed `plume-camera-v0.1`:1,200owned/CC0-input procedural clips with1,000train/100dev/100sealed, split byscene/asset/cameratemplate before rendering. Eightcamera categories each125trainclips. Everyfile exactly832x480/49frames/16fps, matching3.0625scontainerduration; frame timestamps cover3seconds between first/last frame. CaptionsEnglish andhumanchecked. Sourcecadence preparation is explicit;TOMLdoesnotapply a second source_fps remap. Quarantineunknownrights,cut/stutter/corrupt/PII/captionmismatch. No benchmarkcontent orpublicevalrecords.

Use [schema](../../../datasets/SCHEMAS/video.schema.json), source/rights/humanreviewmanifest andprivateHFreleasecommit. PutMP4and same-stem.txtcaptions under `/remote/work/plume-camera-v0.1/train`; dev/test aredifferentdirectories andneverentertraining/cache. Thisis a proposedremote path,not anexistingdataset. Cachekeysbindasset/captionSHA,VAE/T5revision,crop/cadence/geometry. Dataset [TOML](dataset.toml) usesresolution[width,height];inferenceCLI `--video_size` uses[height,width], hence480832.

## Commands and gates

SetMUSUBI_ROOT,PLUME_RECIPE_ROOT,WAN_HIGH,WAN_LOW,WAN_VAE,WAN_T5,PLUME_ENV_LOCK,PLUME_DATASET_COMMIT,PLUME_APPROVAL_ID and outputpaths to actualapprovedremote artifacts. Run `bash cache.sh`, thenPB00 `PLUME_STEPS=20 PLUME_SAVE_INTERVAL=20 bash train.sh` on32admittedclips via a separately copied32clipTOML. Retain thePB01TOMLunchanged andrecordPB00overrides. AtPB01, run `bash train.sh` withdefault1000steps/250saveinterval.

PB00gates: complete strictweightload, BF16dtypecorrect, validlatent/T5shape/cachelineage, finite20steploss, nonzeroactualLoRAgradients, sampledhigh-noisehistogram875–1000, frozenotherexpert, adapterexport/reloadroundtrip, peakGPUmemory<72GB on80GBcandidate andprojectedfullcycleinsideapprovedcap. MeasureGPU/CPU/RAM/disk/throughput; recordOOM/timeout/failures. No qualitygainclaim from20diagnosticsteps. IfOOM, explicitlyregisterblockswap thenFP8variant;nevercovertlyshrink49frames orgeometry.

FullPB01: rank16/alpha16,lr1e-4AdamW8bit,BF16,batch1accum4,SDPA/gradientcheckpoint,shift12,timesteps875–1000preserveddistribution,seed42. Trainingonlyhighexpert. `sample.sh` usesbothoriginalexperts and `--lora_weight_high_noise` only whenPLUME_ADAPTERisset; baselineleavesitunset. Explicitguidance(low3,high4),shift12,40steps,boundary0.875,49frames16fps. Trainingboundaryparserisint;875isvalid if explicitlyused there;float0.875belongs toinference. Trainingexportweighttensorcount/names/sizesmustberecorded.

Select250/500/1000checkpointondevonly;test chosencheckpointonce againstbaseline with120sealedprompts×3generationseeds×3blindedraters. [Protocol](../../../benchmarks/EVALUATION_PROTOCOL.md) definesclusterCIs andcamera/retentiongates. StopforNaN/gradient/cache/export failure,unknownrights,spendcap ordevcriticalregression. Scale onlypreferenceCI>50%,camera+10ppCI>0,criticalfailure≤+2pp andretentionmargin≤3pp, withrealisticprompttransfer. Fallingloss isnot aqualityresult.

Resourceassumption1xA10080GB,≥128GBhostRAM,300GBscratch. Qualification8–24GPUh,train24–72,eval12–36, allunmeasured. [Budget](../../../docs/COST_AND_COMPUTE.md) includesbaseline/reviews/storage andexplicitspendinggates. Uploadapprovedadapter+lineage/requiredresume statesprivately,verifyHFcommit/filehashes,cleanonlyconfirmedworker scratchafterpersistence. Do not publishrightsrestrictedassets or storetrainingvideos locally.

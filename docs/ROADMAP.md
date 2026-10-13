# Dependency-based roadmap

**13 October Hala refinement:** after Plume PB00/PB01, prepare synthetic browser/Windows fixtures and a typed Aladdin proposal adapter; then run [HA-Flash-00](../plans/HALA_FLASH_FIRST_EXPERIMENT.md) with frozen Qwen2-VL-2B, Qwen3.5-4B, ShowUI-2B, browser Fara1.5-4B and Holo4 Pro (when qualified). Compare harness-only, Flash-only, Pro-only and hybrid before authorizing a 100–200 image single-versus-two-LoRA pilot. The prior H01–H04 estimates remain assumptions; exact hours depend on actual hardware and task setup. See [current status](CURRENT_STATUS.md) for execution state.

Estimates are engineer workdays, not elapsed calendar commitments. Rights/access/compute approvals can dominate elapsed time. One workday means a focused implementer day; human review/render/GPU time are separate. Planned phases do not imply execution has occurred.

| Unit | Phase / concrete task | Dependency | Estimated work | Done when |
|---|---|---|---:|---|
| R01 | P0refresh pinned releases/licenses and candidate availability | Current research |0.5–1day| Source diffs classified and decisions still valid |
| D01 | P1owned/CC0asset bill of materials and rights decisions | R01 |1–3days| Every asset has authority/evidence/privacy/music review; no unknown input admitted |
| D02 | P1render/caption/group split manifest; remote processing benchmark | D01,authorizedcapacity |2–5days|1,200metadata/asset hashes, no scene/template overlap, reviewedcaption/category coverage |
| D03 | P1privateHF capacity/access/release and retrieval | D02,actualHFowner/quota |0.5–2days| CommitSHA/fileSHA retrieval verified; scratchcleanup safely tested |
| E01 | P2freeze120prompt suite,dev/test policy and raterrubric | R01 |1–2days| Sealedprotocolmanifest versioned beforeoutcomes |
| T01 | P3PB00env/weight/cache/gradient/export/memoryqualification | D03,E01,boundedGPUapproval |1–3days+8–24GPUhassumed| Allqualificationgates and measuredcostreport pass |
| E02 | P2baselineoutputs and ratings | T01 |1–3days+6–12GPUhassumed| Allseedoutputs/failures andblindedratings retained |
| T02 | P4PB01fixedadaptertraining/devselection | T01,E02 |1–2days+24–72GPUhassumed| Chosencheckpoint selectedondev;weights/caches/config hashesfrozen |
| E03 | P4pairedsealedtest/exportrepeat | T02 |1–3days+12–36GPUhassumed| CI/retention criteria eitherpass ordiagnosticstopdecisionrecorded |
| T03 | P4expert/caption/rank orLongCatablation | E03positive/clearquestion |3–6days+boundedapprovedGPUcycle| Onefactortested;replication determines scale/switch |
| H01 | P5freshapp/images/task/verifiercontracts | Plumeinitialgatecomplete;noGPUdependency |3–5days| Golden/seed/nearmiss gates admitted,assetslicensed |
| H02 | P5harnessaction/context/recoveryimplementations | H01 |5–10days| ActualUIintegrationtested,screenshotcoordinates/timeouts/scopeboundariescorrect |
| H03 | P5HA00/HA01pairedfreshsuccessablation | H02,servingapproval |3–6days+16–64GPUhassumed| Equalbudgets andsuccessCI/safety/costresult |
| H04 | P6topology/PEFT/vision/exportqualification | H03residualdeficit |2–5days| Realgradients/adaptercoverage/roundtrip,memoryfitmeasured |
| H05 | P6freshtrajectory/groundingadmission andSFT | H04,rights/verifiergates |5–12days+64–256GPUhassumed| Heldoutgainbeyondharness-onlybaseline;no benchmarkcontent |
| I01 | P7independentsealedreplication/officialbenchmark | Per-modelvalidatedcandidate,asset/APIapproval |3–10days| Reproducerobtainsmatchedclaimwithofficialrules/CIs |
| P01 | P8rights/modelcard/deployment/releasepacket | I01,license/security/costgates |3–7days| Authorizedreleaseandrollbackreview;not justworkingdemo |

Criticalpath for thefirstPlumegain isD01→D02→D03→T01→E02→T02→E03;E01canadvancewithdatareview. Hala'sresearchisalreadyavailable, but itsGPUadaptationdoesnotjumpahead of Plume execution. Failedgates createfocuseddiagnostics/ADRs,not automaticlargerbudgets.

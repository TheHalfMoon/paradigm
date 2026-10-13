# Risk register

| Risk | Consequence / early signal | Mitigation and stop trigger |
|---|---|---|
| Unclear video/music/likeness rights | Invalid training or release; conflicting asset grant | Per-asset evidence and reviewer, quarantine unknowns; stop source on systematic defect |
| Restrictive model/teacher license | Commercial deployment/weight redistribution barred | Freeze actual weight/component terms; LTX/H3/Hunyuan/Cog conditional lanes; never infer code license covers weights |
| Synthetic transfer or style bias | Camera score rises, cinematic realism falls | Realistic held-out prompts/retention cohorts; no scale on synthetic-only gain |
| Benchmark leakage | Invalid record despite high score | Benchmark denylist; app/story/identity/template group splits; inherited contamination disclosure |
| Metric/version confusion | False model comparison | Partial vs binary separation;OSWorld2.1 vs legacy; resolve AutomationBench discrepancy |
| FP16/BF16 or expert/cache mismatch | Load assertion, invalid training or hidden baseline drift | Strict dtype/header/source verification, original BF16 shards,875integer training boundary, versionedVAE/T5/caches |
| VRAM/hostRAM/throughput optimism | OOM, paididle, budget overrun | PB00boundedqualification,80GB/128GBhost assumptions measured, stopcap and separateoffload trials |
| MoE/vision adapter incompatibility | Silent omitted tensors or broken export | Enumerate trainable topology, nonzero gradients, loss-mask/export checks beforeHalaSFT |
| Weak verifier/reward hacking | Trivialfalse success/RLcorruption | Seed/golden/adversarialnear misses/human audit, stopcollection on systematicfalsepositives |
| Harness authority/stale screenshot | Wrong UI or unauthorized side effect | Same-machine tools, screenshot/ackIDs, strictcoordinate/schema/timeouts and taskscope enforcement |
| Private data leakage / credentials | Unauthorized disclosure | ScopedHFtokens, privatepayloads,evidence redaction; no secrets/screenshots inGitHub |
| PrivateHFquota/storage loss | Failedjobs or unrecoverable lineage | Actualquota check/selectivebase reference, authorizedremote backup/commithashes, verifiedcleanup |
| Free/preemptible GPU/provider drift | Unreproducible jobs/hiddenrestartcost | Resumablecheckpoints,actualquote/hostspec, cap andcancellationpolicy |
| Confounded model/harness/compute gains | Scientific attribution fails | Onefactorablation,fixedbudgets/devselection,sealedtest, independentreplication |
| Review tool overclaim | False confidence in plan | Recordactualversion/command/exit/scope;hostdelegationnotindependentreviewer;no fakeGPUtest |

Treat release rights, benchmark contamination, unauthorized state changes and nonfinite/incorrect training as stop conditions. Numeric quality margins are proposed criteria, not assessed risk probabilities.

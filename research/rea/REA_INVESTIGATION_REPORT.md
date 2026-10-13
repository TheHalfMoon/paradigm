# REA investigation report

Actual tool: **rea-agents6.4.0**, currentofficialrelease inspectedOctober12,2026. [Officialsource](https://github.com/morluto/rea), README/release/package/license inspected beforeuse. MITlicense. Node requirement^22.19/^24.11/>=26; hostNode24.19.0 qualified. An existing installation was not assumed. Installed isolatedresearchpackage with `npm install --prefix work/rea-runtime --ignore-scripts --no-audit --no-fund --save-exact rea-agents@6.4.0`; no globalMCP/skillregistration, Hopper/Ghidra/IDA installation orconfiguration change. NPMScan exactversion lookup reported no knownOSVadvisories andcheckdidnotfail; it is not a fulltransitive trust audit.

## Investigation1: Playwright client integration boundary

Target:[microsoft/playwright](https://github.com/microsoft/playwright/tree/d9f2fd3e2232ace8e317a84eda6cb86e25bcf49c), SHA d9f2fd3e2232ace8e317a84eda6cb86e25bcf49c, Apache2publicsource. Scopepackages/playwright-core/src/client; objective understandbrowserinput, channel delegation andtimeouts relevanttoHala. REA'sJS/TSstaticengineisappropriate; itdoesnotanalyzeWan'sPythonGPUkernels orprovebrowserruntimebehavior.

Commandactuallyrun (portablepathshown, sameCLIarguments):

```bash
node work/rea-runtime/node_modules/rea-agents/scripts/rea.mjs \
  analyze-javascript-application work/playwright/packages/playwright-core/src/client \
  --analysis-timeout-ms 30000 --format json
```

Exit0;42.19s capturedwrapperwalltime;45,672,925stdoutbytes. EvidenceIDev_29d4e66c270316c8f68fdd6c0e3c1f0dc3c5a970e48c20023268a0c4e51512cc. Statistics52relevant/52parsedfiles,546,279textbytes,79,796ASTnodes,1,328findings,0parsefailures. **Graphcoveragepartial**: parentsemanticbudgetaffectednetwork/page/tracing/waiter/webmcp/worker relationships. Rawstaticfilefactsretained; absentrelationsdonotproveabsence. Noapplicationcodewasexecuted.

## Investigation2: bounded input/timeout corroboration

A singleinput.tsfileinvocation returnedexit1/unsupported_target: thisoperation acceptsadirectoryorASAR,notafile. Correctedscope copiesexactunchangedinput.ts andtimeoutSettings.ts fromthepinnedcheckoutintoanisolateddirectory. Sourcehashesarein [corroboration](evidence/source-corroboration.json). Samecommandwithdirectory `work/rea-input-scope` returnedexit0,5.5s,723,151stdoutbytes. EvidenceIDev_23cec73ba06676ec2ffc302939267e122f097a9dfc3075e7cf919a311777c844.2files,6,247textbytes,815ASTnodes,20findings,0parsefailures. Graphcoveragecomplete **withinthis two-fileinertscope**; externalPage/channels/importsremainunresolved. Itisnotcompleteapplicationcoverage.

Selectedunchangednodes,outputdigests,statistics/coverage/limitationsarepreserved in [REAexcerpts](evidence/rea-excerpts.json). Theseare **excerpts**,not rehashed/reinventedcanonicalREAenvelopes. Full45MBoutputisnotcommitted becauseitcontainslargegeneratedfacts andpersonalcheckoutpaths; precisecommands,sourcehashes andoriginaloutputhash supportreproductionwithoutpublishingthosepaths.

Sourcecorroboration:Keyboard.down/up/type/press/insertText andMouse.move/down/up/click/wheel forwardargumentstoPage._channel usingkNoTimeout; Touchscreen.tapalsodelegates. REArecoversMouse/Keyboard/timeoutmodule andreturn-shape nodes. Directsourceconfirmsactualchannelcallsandlocations. Itdoesnotprovebackendactionlatency,acknowledgement,cancellation, screenshotfreshness,serverchannel permissions ortimeoutcompletion behavior.

Architectureimplication: Hala needsan explicitouterper-action/taskdeadline,ack/resulttrace andpost-actionscreenshot/statecheck. RPCenqueue/returnisnotgoldtaskcompletion. BrowsercontrolcannotstandinforarbitrarydesktopUI. Recordviewport/scaleandusemodel-specificactionadapters; testbackendintegrationseparately.

## Installation diagnostics and honest blind spots

`rea doctor --target <client-directory> --format json` returnedexit1 andhealthy=false: optionalnativeenginesmissing,globalMCP/skillsetupabsent andgenericnativeopeningofdirectoryunsupported. Node/hostchecks succeeded. ThisdiagnosticdoesnotnegatetheexecutedJSanalysis, nor justifyinstallinglargenativepackages/globalsetup. No nativebinary analysis wasperformed. No livebrowser/UIbenchmark was run.

## Wan, video training and Hcompany SDK: appropriate alternatives

Wan/Musubi/DiffSynth sourceisPython; completepublicsource wasinspecteddirectly ratherthan inventedREApythonoutputs. [Compatibilityaudit](../plume/evidence/recipe-source-audit.json) recordsactualparserlocations/sourcehashes; inspectexpertboundary,weightdtypeassertions,split-fileloader,flowtarget,cachingandLoRAtargetexclusions. RuntimeGPUperformance,bitsandbyteskernels,actualactivationmemory andvideoqualityrequirePB00/PB01execution.

HcompanySDKpublicPythoncheckout5024cf923af85edcd9b10d0d8eeccf67cbc967d4 wasread directly. Itlaunchesseparatelypinnedhai-agent-runtime0.1.16 withplatformSHAmanifest. Thewrapper isnotcomplete disclosedtraining/harnessfactorysource. We didnotdownload/reverseengineer anunauthorizedproprietarypackageorcallpaidHcompanyAPI. FFmpeg/OpenCV/PySceneDetect arepipelineproposals;noinstalledvideoGPUprofiling resultsareclaimed.

NoSeedanceproprietarypackage,privateweights,DRM/access-controlbypass orprivatecorpuswasinvestigated. Publicpapers andlicensesprovide scientific evidence; REA is anengineeringtool,not abenchmarkor substituteforresearchdisclosure.

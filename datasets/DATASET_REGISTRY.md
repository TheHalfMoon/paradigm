# Dataset registry

No dataset was ingested for training. Status is a research disposition, not a legal certification or accepted agreement. Each entry covers the requested seventeen investigation fields. Unknown measurements are explicit; planning cost formulas live in [cost model](../docs/COST_AND_COMPUTE.md).

| Source | Disposition | First use |
|---|---|---|
| [owned-procedural-camera](https://www.blender.org/) | approved_under_conditions | First training pool, conditional on actual asset manifest and review |
| [finevideo](https://huggingface.co/datasets/HuggingFaceFV/finevideo) | requires_review | Select 100–500 cleared clips only after rights/access approval; no gated downloads performed |
| [openvid 1m](https://huggingface.co/datasets/nkp37/OpenVid-1M) | requires_review | Quarantine downloaded-public pool from commercial pilot pending asset grants |
| [miradata](https://huggingface.co/datasets/TencentARC/MiraData) | requires_review | Do not use commercial training until per asset rights and metadata obligations resolved |
| [panda 70m](https://github.com/snap-research/Panda-70M) | research_only | Use methodology only; excluded from commercial training unless independently cleared |
| [opensora-data-methods](https://github.com/hpcaitech/Open-Sora) | approved_under_conditions | Approve code concepts under license, no dataset assets approved by association |
| [wikimedia-video](https://commons.wikimedia.org/wiki/Commons:Licensing) | approved_under_conditions | CC0/PD/CCBY allowlist under per asset review; not all Commons media approved |
| [blender-open-movies](https://studio.blender.org/films/) | approved_under_conditions | Choose a named license-cleared project only; no acquisition authorized by this plan |
| [nasa-media](https://www.nasa.gov/nasa-brand-center/images-and-media/) | approved_under_conditions | NASA original asset allowlist only after provenance |
| [real estate 10k](https://google.github.io/realestate10k/) | requires_review | Use public method and compare labels; do not ingest footage for commercial pilot |
| [amass](https://amass.is.tue.mpg.de/) | research_only | Do not use in first commercial training pool |
| [kinetics](https://github.com/google-deepmind/kinetics-dataset) | requires_review | No raw training until independent rights review |
| [ego 4d](https://ego4d-data.org/) | research_only | Retain as conditional research source only |
| [vggsound-audio set](https://www.robots.ox.ac.uk/~vgg/data/vggsound/) | requires_review | Only owned/cleared equivalents for AV pilot |
| [vox ce leb-lrs 3](https://www.robots.ox.ac.uk/~vgg/data/lrs3/) | excluded | Exclude first commercial data factory; negotiate explicit consent/rights if future use |
| [open ve 3m](https://github.com/OpenVE-Team/OpenVE-3M) | requires_review | Quarantine until complete pair lineage clearance |
| [licensed-cinematic-stock](https://www.gettyimages.com/) | requires_review | Negotiate after pilot shows gain, no purchase or agreement now |
| [dragon-train](https://huggingface.co/datasets/Hcompany/DragOn) | approved_under_conditions | First external Hala adaption data only if held-out drag deficit |
| [hcompany-trajectories](https://huggingface.co/datasets/Hcompany/trajectories) | excluded | Never SFT or RL on benchmark test trajectories |
| [hcompany-perf](https://huggingface.co/datasets/Hcompany/h_cua_perf) | excluded | Exclude training; retain performance bench with disclosure |

## owned-procedural-camera

- **Official Url:** https://www.blender.org/
- **Maintainer:** Paradigm owner / authorized artists
- **Size Modality:** Proposed 1,200 silent clips,1,000 train/100 dev/100 sealed; not created
- **Quality Resolution:** Render 832x 480 master then preserve originals; no up scaling
- **Duration Distribution:** 3.0625s 49 frames 16 fps for trainer; complete single shot
- **Caption Detail:** Exact scene/camera metadata plus human checked English events
- **Subject Motion Camera:** Eight camera categories, varying subject actions/lighting/materials; synthetic bias
- **Format Access:** Remote Blender scripts/renders, MP4+JSONL; persist privately
- **Dataset License:** Original work; Blender too lGPL does not assign output rights
- **Asset Provenance:** Only owned or documentedCC0 assets, textures and rigs; archive each provenance
- **Commercial Training:** Approved only for owned/cleared inputs and render er output rights
- **Redistribution:** Private assets first; public redistribution only asset-level permission
- **Derivative Models:** Record ownership and licenses; no categorical third-party teacher rights
- **Third Party Risks:** Avoid un consented likenesses, copied film scenes, branded objects or copyrighted music
- **Contamination Risk:** Split scene/asset/camera templates before rendering; never benchmark-derived
- **Storage Processing:** ~8GB encoded at 20 Mbps, plus caches/checkpoints; rendering time un measured
- **Model Suitability:** Wan T2V camera pilot; not sufficient evidence of photorealistic generalization
- **Status:** approved_under_conditions
- **Recommendation:** First training pool, conditional on actual asset manifest and review

## finevideo

- **Official Url:** https://huggingface.co/datasets/HuggingFaceFV/finevideo
- **Maintainer:** Hugging Face FV
- **Size Modality:** 43,751 videos,~3,425 hours,122 categories;~673GBdownload card
- **Quality Resolution:** Variable native resolution; card example 640x 360; not uniformly cinematic
- **Duration Distribution:** Mean 4.7 minutes; full quantiles not disclosed
- **Caption Detail:** Detailed time coded events, actions/props/mood, dynamism, transcripts, AV correlation; Gemini/GPT4o generation
- **Subject Motion Camera:** Broad real-world activities; camera labels may require revision
- **Format Access:** Parquet embedded video+JSON; auto gated terms, not accepted
- **Dataset License:** Top metadata cc; narrative source CC-BY, additional access/removal/version terms
- **Asset Provenance:** Uploader attribution is evidence, not proof every embedded element is licensed
- **Commercial Training:** Per asset review plus gate agreement required; no blanket approval
- **Redistribution:** Must obey attribution and removal/update/terms propagation; review redistribution
- **Derivative Models:** CCBY source generally supports adaptation subject rights; terms/teacher annotation use reviewed
- **Third Party Risks:** Music, people, third party clips, uploader authority, privacy
- **Contamination Risk:** YouTube/source-channel/story grouped split, benchmark overlap scan
- **Storage Processing:** Card~678GBdata; selective clips reduce transfer; caption review and scene extraction CPU cost
- **Model Suitability:** Best optional real footage pool after clearance; full-video captions not automatically shot captions
- **Status:** requires_review
- **Recommendation:** Select 100–500 cleared clips only after rights/access approval; no gated downloads performed

## openvid 1m

- **Official Url:** https://huggingface.co/datasets/nkp37/OpenVid-1M
- **Maintainer:** OpenVid authors
- **Size Modality:** ~1 Mclips including~0.4M1080p in publisher description
- **Quality Resolution:** Quality/motion/aesthetic filtering; distribution must be sampled
- **Duration Distribution:** Clip durations and quantiles require selected release metadata
- **Caption Detail:** Video captions and quality/motion scores; audit hallucination
- **Subject Motion Camera:** General scenes and motions; weak controlled camera ground truth
- **Format Access:** CSV/archives/links; source repositories differ
- **Dataset License:** Repository code license is not a grant for videos
- **Asset Provenance:** Mixed online/YouTube-derived sources, per asset rights unresolved
- **Commercial Training:** Not cleared commercially by Apache repository
- **Redistribution:** Do not mirror archives without asset permissions
- **Derivative Models:** Unresolved footage rights; do not assume weights cleared
- **Third Party Risks:** Uploader/music/likeness/source rights
- **Contamination Risk:** Source/channel/segment overlap and benchmark prompt leakage
- **Storage Processing:** Millions of clips can require TBs; manifest-based quote before ingest
- **Model Suitability:** Wan-compatible motion-quality ideas; selection recipe useful independently
- **Status:** requires_review
- **Recommendation:** Quarantine downloaded-public pool from commercial pilot pending asset grants

## miradata

- **Official Url:** https://huggingface.co/datasets/TencentARC/MiraData
- **Maintainer:** Tencent ARC
- **Size Modality:** 330 Klarge release plus 93K/42K/9 Kvariants; video/caption metadata
- **Quality Resolution:** 720/1080 family high quality description; per release distribution required
- **Duration Distribution:** Long clips≥10/20s release variants; quantiles unknown
- **Caption Detail:** Short/dense/background/object/style/camera captions
- **Subject Motion Camera:** Mixed real footage, games and rendered worlds
- **Format Access:** Metadata with source URL/timestamps; actual footage access depends on source
- **Dataset License:** DatasetcardGPL3, not universal footage grant
- **Asset Provenance:** Game/platform/footage/music rights separate from metadata
- **Commercial Training:** Additional review; GPL card alone cannot clear source assets
- **Redistribution:** Metadata GPL obligations and separate asset permissions
- **Derivative Models:** Do not assert GPL automatically re licenses trained weights; legal interpretation remains open
- **Third Party Risks:** Game publisher, YouTube, music, people
- **Contamination Risk:** Split game/map/story/source and clip siblings
- **Storage Processing:** Long 720/1080 clips expensive; trim remote only after rights; caches may exceed video
- **Model Suitability:** Camera/motion annotation inspiration, conditional adaptation
- **Status:** requires_review
- **Recommendation:** Do not use commercial training until per asset rights and metadata obligations resolved

## panda 70m

- **Official Url:** https://github.com/snap-research/Panda-70M
- **Maintainer:** Snap Research
- **Size Modality:** ~70 Mvideo-caption pairs publisher claim
- **Quality Resolution:** Broad web quality; no uniformly high-resolution guarantee
- **Duration Distribution:** Semantically split clips; exact release quantiles not verified
- **Caption Detail:** Teacher ensemble captions, variable accuracy
- **Subject Motion Camera:** Broad activities, no exact camera labels
- **Format Access:** CSV/YouTube URLs; many assets can disappear
- **Dataset License:** Code/annotations terms do not grant underlying video
- **Asset Provenance:** YouTube footage authorization un established
- **Commercial Training:** Research access is not commercial clearance
- **Redistribution:** No public footage mirror without rights
- **Derivative Models:** Inherited training rights uncertain
- **Third Party Risks:** Music/likeness/platform terms/uploader
- **Contamination Risk:** Source/channels/near clip duplicates; overlap likely at scale
- **Storage Processing:** Full collection potentially many TB; not a rational first pilot
- **Model Suitability:** Cu ration concepts useful, mass payload unnecessary
- **Status:** research_only
- **Recommendation:** Use methodology only; excluded from commercial training unless independently cleared

## opensora-data-methods

- **Official Url:** https://github.com/hpcaitech/Open-Sora
- **Maintainer:** HPC-AI Tech
- **Size Modality:** Methods/code; no blanket licensed training corpus inferred
- **Quality Resolution:** Multi-resolution, length and score-conditioned processing
- **Duration Distribution:** Per stage documented; chosen release controls
- **Caption Detail:** Caption/filter tools and reports, version-dependent
- **Subject Motion Camera:** Broad visual diversity
- **Format Access:** Public code/docs; underlying datasets need independent audit
- **Dataset License:** Apache code/model card separately
- **Asset Provenance:** All raw video assets retain their own terms
- **Commercial Training:** Implement pipeline concepts on own assets
- **Redistribution:** Redistribute code notices; dataset permission separate
- **Derivative Models:** Weights/model license does not legalize new raw dataset
- **Third Party Risks:** Raw source privacy/content rights
- **Contamination Risk:** Split before augment; inherited checkpoint contamination unknown
- **Storage Processing:** From scratch budget claim~$200k not adaptation cost
- **Model Suitability:** Good data architecture reference, avoid full pretraining
- **Status:** approved_under_conditions
- **Recommendation:** Approve code concepts under license, no dataset assets approved by association

## wikimedia-video

- **Official Url:** https://commons.wikimedia.org/wiki/Commons:Licensing
- **Maintainer:** Wikimedia Commons / individual contributors
- **Size Modality:** Distributed video collection; no fixed cinematic dataset size
- **Quality Resolution:** Variable; select native≥480p with suitable motion
- **Duration Distribution:** Variable; segment single shots 3–8s
- **Caption Detail:** Descriptions often not temporal captions; re-caption
- **Subject Motion Camera:** Documentary/nature/historical scenes, limited cinematic coverage
- **Format Access:** File page/API per asset; throttled remote ingest
- **Dataset License:** PerassetCC0/PD/CCBY/CCBYSA etc
- **Asset Provenance:** Persist file page creator license version source hash attribution
- **Commercial Training:** CC0/PD/CCBY approved only with documented source authority and rights checks
- **Redistribution:** Follow each license; prefer private payload no public mirror necessary
- **Derivative Models:** CCBYSA derivative-model interpretation requires review; excludeS A from first pool
- **Third Party Risks:** Personality/publicity/music/logos and PD jurisdiction
- **Contamination Risk:** Group uploader/event/original work; scanbenchmarksource overlap
- **Storage Processing:** Select≤500 clips first; storage formula by bitrate, not collection guess
- **Model Suitability:** Cleared real world validation/training supplement
- **Status:** approved_under_conditions
- **Recommendation:** CC0/PD/CCBY allowlist under per asset review; not all Commons media approved

## blender-open-movies

- **Official Url:** https://studio.blender.org/films/
- **Maintainer:** Blender Studio / project contributors
- **Size Modality:** Individual film project assets and releases, not one dataset
- **Quality Resolution:** High quality rendered cinema; stylized/domain bias
- **Duration Distribution:** Long films segmented shots; no fixed shot distribution
- **Caption Detail:** Metadata/story dialogue; human shot/camera captions needed
- **Subject Motion Camera:** Composition/camera/action/identity within stories
- **Format Access:** Film/project downloads; version ed project license
- **Dataset License:** Per project often CC-BY; verify specific film/components
- **Asset Provenance:** Film license and music/asset credits stored per file
- **Commercial Training:** Conditional copyright permission plus separate asset/music exceptions
- **Redistribution:** Attribution and applicable component terms
- **Derivative Models:** No blanket automatic model license change; document data obligations
- **Third Party Risks:** Soundtrack, third party assets, logos, voice performances
- **Contamination Risk:** Split whole film/story/character/source, never sibling shot random split
- **Storage Processing:** Remote fewGB film masters plus cuts/cache; verify actual size
- **Model Suitability:** Cinematic composition practice but no photoreal generalization proof
- **Status:** approved_under_conditions
- **Recommendation:** Choose a named license-cleared project only; no acquisition authorized by this plan

## nasa-media

- **Official Url:** https://www.nasa.gov/nasa-brand-center/images-and-media/
- **Maintainer:** NASA / contributing partner identified per asset
- **Size Modality:** Catalog, no fixed subset size
- **Quality Resolution:** Variable technical/documentary footage
- **Duration Distribution:** Variable; selected short shots
- **Caption Detail:** Descriptions technical, motion/time captions needed
- **Subject Motion Camera:** Space/nature/engineering, domain narrow
- **Format Access:** Media files/API from official source
- **Dataset License:** US government NASA-created media generally PD with exceptions
- **Asset Provenance:** Separate NASA originals from partner/commercial materials
- **Commercial Training:** Conditional government-work status and third party rights
- **Redistribution:** No endorsement or logo misuse; credited/external material retains license
- **Derivative Models:** Document jurisdiction/status, no blanket legal conclusion
- **Third Party Risks:** Astronaut likeness, partner footage, music, insignia
- **Contamination Risk:** Mission/event/time grouping
- **Storage Processing:** Pilot dozens clips only, downloaded remotely; actual sizes quoted from headers
- **Model Suitability:** Small technical motion domain benchmark, not core cinematic mixture
- **Status:** approved_under_conditions
- **Recommendation:** NASA original asset allowlist only after provenance

## real estate 10k

- **Official Url:** https://google.github.io/realestate10k/
- **Maintainer:** Google research authors
- **Size Modality:** Camera poses/YouTube source links,~10 Mframes described
- **Quality Resolution:** Indoor/outdoor camera trajectories, not necessarily generated cinema
- **Duration Distribution:** Sequence/frame metadata, video availability variable
- **Caption Detail:** No richly grounded temporal captions
- **Subject Motion Camera:** Strong camera pose signal for static architecture
- **Format Access:** Pose text files+external YouTube asset retrieval
- **Dataset License:** Pose metadata license reviewed separately
- **Asset Provenance:** YouTube footage rights not cleared by poses
- **Commercial Training:** No blanket commercial video permission
- **Redistribution:** Pose data grant differs from video grant
- **Derivative Models:** Separate labels/footage status
- **Third Party Risks:** Property/people/uploader/platform rights
- **Contamination Risk:** House/location/original video grouping
- **Storage Processing:** Pose metadata small; footage selective after clearance
- **Model Suitability:** Camera-control research; own Blender poses simpler first
- **Status:** requires_review
- **Recommendation:** Use public method and compare labels; do not ingest footage for commercial pilot

## amass

- **Official Url:** https://amass.is.tue.mpg.de/
- **Maintainer:** Max Planck / constituentmocapowners
- **Size Modality:** ~40+hours aggregated motion publisher description; 3 Dmotion not videos
- **Quality Resolution:** Human pose/motion, synthetic render possible
- **Duration Distribution:** Sequences vary; quantify chosen licensed subset
- **Caption Detail:** No turnkey video captions
- **Subject Motion Camera:** Human locomotion/action, no camera cinematography
- **Format Access:** Registration/agreement/SMPL dependencies; not accepted
- **Dataset License:** Noncommercial research terms plus constituents
- **Asset Provenance:** Each source andbodymodelllicense
- **Commercial Training:** Research-only without expanded license
- **Redistribution:** Terms restrict distribution
- **Derivative Models:** Rendering does not erase source motion/SMPLrestrictions
- **Third Party Risks:** Participant consent and body model rights
- **Contamination Risk:** Split performer/action/session/source
- **Storage Processing:** Motion parameters small; rendering GPU CPU time unknown
- **Model Suitability:** Motion curriculum concept only undercurrent commercial scope
- **Status:** research_only
- **Recommendation:** Do not use in first commercial training pool

## kinetics

- **Official Url:** https://github.com/google-deepmind/kinetics-dataset
- **Maintainer:** Deep Mind / video uploaders
- **Size Modality:** Kinetics 400/600/700 label sets, external 10s clips
- **Quality Resolution:** Web activities, variable video quality
- **Duration Distribution:** Nominal 10s; broken/replaced links possible
- **Caption Detail:** Action labels not detailed temporal/camera captions
- **Subject Motion Camera:** Broad human actions
- **Format Access:** CSV annotations+YouTube URLs
- **Dataset License:** Labels CC-BY4 in official repo; videos separate
- **Asset Provenance:** No underlying video blanket grant
- **Commercial Training:** Not commercially cleared by annotation license
- **Redistribution:** Labels attribution; raw assets need own permission
- **Derivative Models:** Training weights rights cannot be inferred from label license
- **Third Party Risks:** People/minors/music/uploader
- **Contamination Risk:** Benchmark dataset itself excludeevalsplits; source IDs not random cuts
- **Storage Processing:** Large external downloads deferred; selective proof only
- **Model Suitability:** Action coverage ideas, poor first cinematic pool
- **Status:** requires_review
- **Recommendation:** No raw training until independent rights review

## ego 4d

- **Official Url:** https://ego4d-data.org/
- **Maintainer:** Ego 4D consortium
- **Size Modality:** Egocentric multi modal corpus, thousands of hours; no payload examined
- **Quality Resolution:** First person action, complex privacy
- **Duration Distribution:** Long activity recordings; distributions not inspected
- **Caption Detail:** Temporal annotations, not cinematic camera directives
- **Subject Motion Camera:** Egocentric hands/social interaction
- **Format Access:** Access agreement; not accepted
- **Dataset License:** Research/noncommercial agreement; current exact terms must be read before access
- **Asset Provenance:** Consortium participant/access scope constraints
- **Commercial Training:** Not approved commercially
- **Redistribution:** Restricted redistribution
- **Derivative Models:** Derivative/use obligations need signed terms review
- **Third Party Risks:** Private homes/people/audio/consent
- **Contamination Risk:** Person/site/session group split; published benchmark leakage
- **Storage Processing:** Substantial storage; no download budget assumed
- **Model Suitability:** Research comparison; not first training
- **Status:** research_only
- **Recommendation:** Retain as conditional research source only

## vggsound-audio set

- **Official Url:** https://www.robots.ox.ac.uk/~vgg/data/vggsound/
- **Maintainer:** VGG / Google Audio Set respective publishers
- **Size Modality:** VGGSound~200k 10s AV clips; Audio Set~2M10s labeled examples
- **Quality Resolution:** Web sound events, noisy AV sync; not speech quality guarantee
- **Duration Distribution:** Nominal 10s
- **Caption Detail:** Sound event labels, not full cinematic captions
- **Subject Motion Camera:** Broad non-speech sound events
- **Format Access:** Annotations/source IDs; external videos
- **Dataset License:** Label/code terms differ from assets; check each release
- **Asset Provenance:** YouTube assets music/footage unclear ed
- **Commercial Training:** No automatic commercial AV training permission
- **Redistribution:** No bulk raw mirror
- **Derivative Models:** Audio+video+caption license lineage separately
- **Third Party Risks:** Music performances/people/trademarks
- **Contamination Risk:** ClipID/channel/source and published benchmarks
- **Storage Processing:** AV decoding/cache adds I/O; rights first
- **Model Suitability:** Candidate AV evaluation methods; own recorded sounds first
- **Status:** requires_review
- **Recommendation:** Only owned/cleared equivalents for AV pilot

## vox ce leb-lrs 3

- **Official Url:** https://www.robots.ox.ac.uk/~vgg/data/lrs3/
- **Maintainer:** VGG / original video rights owners
- **Size Modality:** Talking-face/speech corpora; not downloaded
- **Quality Resolution:** Useful lip sync but identity-biased
- **Duration Distribution:** Short speech segments; actual distribution not verified
- **Caption Detail:** Transcriptions alignment vary
- **Subject Motion Camera:** Faces/voices, limited motion camera
- **Format Access:** Registration/external clips/licensing constraints
- **Dataset License:** Dataset-specific research terms; no general commercial approval
- **Asset Provenance:** Original speech/face/voice consents unresolved
- **Commercial Training:** Not approved for commercial Plume
- **Redistribution:** Redistribution rights restricted/unclear
- **Derivative Models:** Face/voice derivatives need explicit permission
- **Third Party Risks:** Biometric privacy/publicity, voice cloning, TED/video copyrights
- **Contamination Risk:** Speaker/event/video groups and lip-sync benchmark contamination
- **Storage Processing:** Multiple modalities and embedding storage; avoid initial payload
- **Model Suitability:** Instead use owned consented performances
- **Status:** excluded
- **Recommendation:** Exclude first commercial data factory; negotiate explicit consent/rights if future use

## open ve 3m

- **Official Url:** https://github.com/OpenVE-Team/OpenVE-3M
- **Maintainer:** Open VE team
- **Size Modality:** ~3 Mpairedvideoediting examples publisher claim
- **Quality Resolution:** Generated edits quality/teacher bias
- **Duration Distribution:** Release-dependent, quantiles not verified
- **Caption Detail:** Editing instructions paired with source/output
- **Subject Motion Camera:** Object/style/scene editing
- **Format Access:** Public repo and dataset links; no payload inspect
- **Dataset License:** Exact release and teacher/source terms require audit
- **Asset Provenance:** Original footage and generated teacher outputs rights unresolved
- **Commercial Training:** Not cleared by public availability
- **Redistribution:** Pair assets governed by both origins
- **Derivative Models:** Teacher output restrictions can bind competing training
- **Third Party Risks:** Footage/likeness/music plus teacher terms
- **Contamination Risk:** Split original source before edit variants
- **Storage Processing:** Paired clips double video/cache footprint
- **Model Suitability:** Editing lane later; own paired renders/masks first
- **Status:** requires_review
- **Recommendation:** Quarantine until complete pair lineage clearance

## licensed-cinematic-stock

- **Official Url:** https://www.gettyimages.com/
- **Maintainer:** Contracted rights holder; provider is illustrative, no agreement
- **Size Modality:** Quoted subset only; no dataset purchased
- **Quality Resolution:** Potential high quality cinematic footage
- **Duration Distribution:** Selected shots 3–8s
- **Caption Detail:** Stock titles insufficient; owned captions/review
- **Subject Motion Camera:** Photoreal human/camera/lighting hard cases
- **Format Access:** Provider contract and remote files
- **Dataset License:** Bespoke A I training license required; standard stock/editorial license insufficient
- **Asset Provenance:** Contract references asset IDs, chain of rights and releases
- **Commercial Training:** Only explicit commercial ML training grants
- **Redistribution:** Specify private hosting, subprocessors, derived weights and any public samples
- **Derivative Models:** Explicit weight redistribution and future customers/use rights
- **Third Party Risks:** People/music/territory/editorial-only/license expiry
- **Contamination Risk:** Split production/shoot/actors/story/assets
- **Storage Processing:** License quote unknown; human review can exceed GPU budget
- **Model Suitability:** Highest quality conditional real footage supplement
- **Status:** requires_review
- **Recommendation:** Negotiate after pilot shows gain, no purchase or agreement now

## dragon-train

- **Official Url:** https://huggingface.co/datasets/Hcompany/DragOn
- **Maintainer:** Hcompany
- **Size Modality:** 286,012 images/3,560,142 train tasks
- **Quality Resolution:** Desktop screenshots, dimensions recorded
- **Duration Distribution:** Not video; drag start/end supervision
- **Caption Detail:** Instruction and metadata subtype
- **Subject Motion Camera:** Text/sheet/slide/slider drag grounding
- **Format Access:** Tar images+JSON tasks; train/eval/private test separated
- **Dataset License:** Card Apache 2; no separate LICENSE file found
- **Asset Provenance:** Review app/font/screenshot rights and private content
- **Commercial Training:** Conditional train-subset approval after asset audit
- **Redistribution:** Retain notices; screenshot asset rights separate
- **Derivative Models:** No blanket permission for underlying private data
- **Third Party Risks:** Screen private identifiers or proprietary content
- **Contamination Risk:** Groupimage_id/template; exclude 1000 publiceval and private benchmark test
- **Storage Processing:** API history~61.5GBindicative; selected train manifest before transfer
- **Model Suitability:** Hala grounding only, not long horizon behavior
- **Status:** approved_under_conditions
- **Recommendation:** First external Hala adaption data only if held-out drag deficit

## hcompany-trajectories

- **Official Url:** https://huggingface.co/datasets/Hcompany/trajectories
- **Maintainer:** Hcompany
- **Size Modality:** 7366 public benchmark executions; metadata audit performed
- **Quality Resolution:** Screenshots/actions, publisher traces
- **Duration Distribution:** Tasks episodes; see index duration stats
- **Caption Detail:** Benchmark instruction/actions/verifier context
- **Subject Motion Camera:** Six public benchmarks
- **Format Access:** Index JSON/task JSON/screenshot references
- **Dataset License:** Apache 2 plus underlying benchmark licenses
- **Asset Provenance:** PII-containing tasks excluded in public subset per card
- **Commercial Training:** Exclude from training to protect evaluation integrity
- **Redistribution:** Subject to source benchmark terms and privacy
- **Derivative Models:** Licensed access does not remove leakage
- **Third Party Risks:** Screenshots/benchmark asset private content
- **Contamination Risk:** High:these ARE benchmark executions
- **Storage Processing:** Current API used Storage~2.0GBnot exact transfer; only metadata read
- **Model Suitability:** Failure taxonomies only
- **Status:** excluded
- **Recommendation:** Never SFT or RL on benchmark test trajectories

## hcompany-perf

- **Official Url:** https://huggingface.co/datasets/Hcompany/h_cua_perf
- **Maintainer:** Hcompany
- **Size Modality:** 477 traces/18224 requests
- **Quality Resolution:** Inference request replay, not completed task gold labels
- **Duration Distribution:** Median 23 turns, cap 200
- **Caption Detail:** Messages/tools/delay/output_length; screenshot replacement
- **Subject Motion Camera:** Serving length buckets
- **Format Access:** JSONLzstd 2.5GBcompressed/9.3GBuncompressedstated
- **Dataset License:** CC-BY4
- **Asset Provenance:** Record attribution and replay privacy
- **Commercial Training:** Not SFT: no gold goal labels; inference bench only
- **Redistribution:** CCBY plus underlying screenshot rights
- **Derivative Models:** No suitable target model improvement claim
- **Third Party Risks:** Screen content and request text privacy
- **Contamination Risk:** Isolated serving bench; never training
- **Storage Processing:** API history storage 12.6GB; replay decoder/RAM budget qualified remotely
- **Model Suitability:** Hala TTFT/throughput stress fixture
- **Status:** excluded
- **Recommendation:** Exclude training; retain performance bench with disclosure

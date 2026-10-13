# Video data selection

[Complete dataset register](../../datasets/DATASET_REGISTRY.md) includes FineVideo, OpenVid, MiraData, Panda 70M, OpenSora methods, Commons, Blender, NASA, motion/action/camera sources, licensed cinema, editing and AV data. It records sizes, modality/quality/duration/captions/coverage/access/licenses, asset rights, training/redistribution/derivative implications, third party risks, contamination, storage and suitability. Unknown values are not filled with guesses.

Recommendation: begin with **owned procedurally rendered camera scenes** using owned/CC0 assets, then add only individually cleared real footage. FineVideo is the most useful broadly captioned **conditional** real-video candidate, with 43,751 videos/~3,425 hours and richer temporal/AV metadata; gates/removal terms/uploader/music rights prevent blanket commercial approval. OpenVid/MiraData/Panda breadth does not outweigh their unresolved footage rights. Quality filters are useful scientific concepts even when their training videos are unusable.

| Tier | Proposed scale and objective | Preconditions / stop decision |
|---|---|---|
| Pilot |1,200 owned clips,1,000 train/100 dev/100 sealed, eight balanced camera classes; one high noise adapter | Asset rights/cache quality/split manifest and baseline registered. Stop if photoreal holdout ratings regress or improvement exists only on matching renders |
| Intermediate |10–30 kapprovedshots, at least several hundred newly cleared real clips and identities/scenes held out | Require paired quality CI and camera improvement, data efficiency ablation, repeatable serving memory/cost. No automatic purchase of stock |
| Large |100–300 kclearedclips, I2V/reference/AV subsets version ed separately | Multiple held out domains, independent verification, rights and storage budget. Full finetuning needs separate architecture/budget review |

The smallest useful data experiment is not a broad foundation pre train. It is an intervention with strong ground truth for a known weakness. Synthetic data may teach camera labels cheaply but stylization/domain shift is a major risk. Held out evaluation includes human motion/photorealism/object interaction; do not announce cinematic parity from moving geometric primitives. Licensed real data is the next logical increment after credible gain, not an implicit authorization to acquire it.

For camera pose supervision, self render metadata avoids Real Estate 10 Kfootagerights uncertainty. For human motion, own key framed/consented motion avoids A MASS/SMPLnoncommercialterms. For editing, own before/after renders/masks avoid unverified teacher pair licenses. For audiovisual sync/lip sync, owned consented speech/audio and explicit identity releases are stronger first choices than public talking face corpora. Preserve production/story/identity groups across all splits.

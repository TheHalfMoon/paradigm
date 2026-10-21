
# Syag Organization and Repository Ownership Migration Runbook

**Current truth at 2026-10-21:** Both connected GitHub accounts returned NO GitHub organization memberships through the GitHub integration. No organization has been created by this run. Hugging Face is a separate service; user-supplied https://huggingface.co/Paradigm-AI is not a GitHub organization. The HF connector authenticates as MedScale with read-only OAuth scope, not Paradigm-AI admin.

## Desired final structure

GitHub: a newly owned organization, preferred slug **Paradigm-AI** if available (otherwise founder-approved alternative). New Syag source repo within it, preferred URL https://github.com/Paradigm-AI/Syag **only if actually created**. Maintain parent Paradigm research HQ in TheHalfMoon/paradigm or transfer it to org once all other work/PRs and cross-repo references are audited.

HF: https://huggingface.co/Paradigm-AI with private syag-corpus + syag-eval and released Syag model card. Never place restricted/personal source documents in public model/dataset repositories.

## Organization creation — human GitHub UI step

GitHub organizations are different from repositories; the current connected GitHub tools cannot create an organization, and no connected membership was found. Authorized owner must use GitHub Settings -> Organizations -> New organization or https://github.com/account/organizations/new and finish the identity/plan prompts. Use the **free** tier unless owner chooses otherwise; no agent accepts payment terms or adds a billing card. The organization name/slug is subject to availability, and another unrelated Paradigm account must not be claimed.

Upon creation:
1. Owner grants both the desired user and app installation repo management permission; verify via the connector that the new org is visible AND writable.
2. Freeze active Syag branch PRs in TheHalfMoon/paradigm; verify exact source SHAs, open issues and active experiments. Decide whether to TRANSFER existing Paradigm repository (which also holds Hala/Plume research), or to CREATE a **dedicated Syag repository** in the new org; prefer creating Syag so shared Paradigm is unaffected.
3. GitHub repo creation via authorized UI or a correctly scoped GitHub CLI workflow; do not claim a repo exists until checked. Use org secret scanning, branch protection, code owners, CI and no public datasets.
4. Migrate Syag sources and plan with reproducible git history-preserving subtree split or auditable commit-copy provenance; include commit references to original historical files and close/redirect any old Syag tracking issues. Preserve Hala/Plume unaffected.
5. Add README pointers from old Paradigm/syag to new canonical location, and update GitHub issues, HF dataset cards and training manifests. After migration, ONLY the new repo is canonical; old location becomes read-only/archive pointer. Avoid two writable copies.
6. Verify entire migration with commit/file hash comparison, exact branch HEAD, permissions, issue links and a fresh-agent resume test. Record completed checklist, owner approval and timestamp in STATUS.md.

## Scope limits and safety

- Do not impersonate Paradigm-AI GitHub owner or claim an unavailable slug.
- Do not transfer/move the entire Paradigm repo without accounting for Hala/Plume.
- Do not force push, delete remote repositories, accept paid tiers, modify owners' unrelated organizations or store private data in git.
- If organization creation is blocked, **continue technical Syag work in TheHalfMoon/paradigm/syag** with stable reproducible PRs and issues. The absence of a new org does not block research, schema tests or clean public synthetic-data generation.

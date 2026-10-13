# Offline research validation tools

Use Python 3.11+ with the standard library. From the repository root:

```bash
python tools/research_validation/validate_repo.py
python -m unittest discover -s tools/research_validation -p 'test_*.py' -v
python tools/research_validation/cost_model.py --gpu-hours 50 --hourly-rate 1.39
python tools/research_validation/validate_manifest.py /remote/path/manifest.jsonl
python tools/research_validation/audit_hcompany_index.py /temporary/path/index.json
```

On the current Windows host prefix shell calls with `rtk proxy`. The index audit expects the exact pinned publisher-index SHA, and re computes metadata rather than executing tasks. Fetch that public 5MB JSON remotely or temporarily when needed; no screenshot archive is required. Manifest checking validates declared policy and record structure, including split/benchmark exclusions; it does not prove a copyright grant or decode any video. Synthetic test records are explicitly metadata fixtures.

schema_check.py implements only the documented schema subset and rejects unsupported validation keywords. The published JSON schemas can also be used with a full Draft 2020-12 validator in a qualified remote environment. No paid API, credentials, weights, GPU, cloud provisioning or private upload is used by these tools. Link checking is offline for repository references; source HTTP/status/hash evidence is audited separately.

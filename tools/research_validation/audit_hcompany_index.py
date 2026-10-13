"""Recompute publisher metadata aggregates; does not execute benchmark tasks."""
import argparse
import hashlib
import json
import statistics
from pathlib import Path

EXPECTED_SHA='a8525624049894e1aeb220790ed8c013067a99f2ffdbcb938d5a4cef91f0cf53'

def audit(path):
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=EXPECTED_SHA:
        raise ValueError('index differs from frozen source; use a new audited version')
    rows=json.loads(raw)['trajectories']
    result={'row_count':len(rows),'unique_ids':len(set(r['id'] for r in rows)),
            'unique_model_benchmark_task_run':len(set((r['model'],r['benchmark'],str(r['task']),r['run']) for r in rows)),'groups':[]}
    for key in sorted(set((r['model'],r['benchmark']) for r in rows)):
        group=[r for r in rows if (r['model'],r['benchmark'])==key]
        result['groups'].append({'model':key[0],'benchmark':key[1],'rows':len(group),
            'unique_tasks':len(set(str(r['task']) for r in group)),
            'success_fraction':statistics.mean(float(r['success']) for r in group),
            'mean_score':statistics.mean(float(r['score']) for r in group),
            'median_duration_s':statistics.median(float(r['duration_s']) for r in group)})
    result['interpretation']='Computed from publisher-released index metadata; not independently executed benchmark results. Repeated tasks and model runs are expected; never train on these tasks.'
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('index',type=Path)
    print(json.dumps(audit(p.parse_args().index),indent=2))

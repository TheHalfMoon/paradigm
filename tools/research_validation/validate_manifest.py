"""Validate metadata-only video manifests; never retrieves or decodes media."""
import argparse
import json
import math
from pathlib import Path
from schema_check import validate

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT/'datasets/SCHEMAS/video.schema.json').read_text(encoding='utf-8'))

def validate_records(records):
    ids, hashes, groups = set(), {}, {}
    for index,record in enumerate(records):
        validate(record,SCHEMA,f'row{index+1}')
        if record['id'] in ids:
            raise ValueError('duplicate video id')
        ids.add(record['id'])
        split = record['split']
        if split != 'quarantine':
            for store,key in [(hashes,record['sha256']),(groups,record['source']['group_id'])]:
                if key in store and store[key] != split:
                    raise ValueError('asset hash or source group crosses splits')
                store[key] = split
        if split == 'train':
            r = record['rights']
            if record['example_only'] or record['benchmark_test']:
                raise ValueError('example or benchmark test record cannot enter training')
            if r['status'] != 'approved_under_conditions' or not all(r[k] for k in
                    ['conditions_met','training_allowed','privacy_reviewed','music_reviewed']):
                raise ValueError('training rights conditions missing')
            if not record['human_review']['accepted'] or record['exclusion_reasons']:
                raise ValueError('human acceptance missing or exclusion unresolved')
        duration = record['media']['duration_s']
        for event in record['caption']['events']:
            if not (0 <= event['start_s'] < event['end_s'] <= duration):
                raise ValueError('event interval outside media duration')
        # NaN/Infinity are accepted by Python JSON by default; reject recursively.
        def finite(value):
            if isinstance(value,float) and not math.isfinite(value):
                raise ValueError('nonfinite number')
            if isinstance(value,dict):
                for item in value.values(): finite(item)
            if isinstance(value,list):
                for item in value: finite(item)
        finite(record)
    return len(ids)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest',type=Path)
    args=parser.parse_args()
    records=[json.loads(line) for line in args.manifest.read_text(encoding='utf-8').splitlines() if line.strip()]
    count=validate_records(records)
    print(json.dumps({'valid_records':count,'scope':'metadata and declared policy only; not legal or media quality certification'}))

if __name__ == '__main__': main()

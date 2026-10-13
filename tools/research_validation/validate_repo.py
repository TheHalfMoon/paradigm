"""Offline research integrity checks. External reachability is a separate audit."""
import json
import re
from pathlib import Path
from schema_check import validate

ROOT=Path(__file__).resolve().parents[2]

def main():
    errors=[]
    md=list(ROOT.rglob('*.md'))
    for path in md:
        text=path.read_text(encoding='utf-8')
        if len(text.strip())<100: errors.append(f'{path.relative_to(ROOT)}: empty report')
        for target in re.findall(r'\]\(([^\)]+)\)',text):
            target=target.strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
            file=target.split('#',1)[0]
            if not (path.parent/file).exists():errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
        if re.search(r'[\u0600-\u06ff\u4e00-\u9fff]',text):errors.append(f'{path.relative_to(ROOT)}: non-English source text')
    sources=json.loads((ROOT/'research/evidence/source-registry.json').read_text())
    source_ids={s['id'] for s in sources}
    if len(source_ids)!=len(sources): errors.append('duplicate source ids')
    claims=json.loads((ROOT/'research/evidence/claims.json').read_text())
    for c in claims:
        if c['classifier'] not in {'VERIFIED','STRONGLY SUPPORTED','PRELIMINARY','UNVERIFIED','CONTRADICTED'}:errors.append('invalid evidence classifier')
        if set(c['source_ids'])-source_ids:errors.append(f"{c['id']}: missing source ids {set(c['source_ids'])-source_ids}")
    for path in ROOT.rglob('*.json'):
        try:json.loads(path.read_text(encoding='utf-8'))
        except ValueError:errors.append(f'{path}: invalid JSON')
    schema=json.loads((ROOT/'datasets/SCHEMAS/video.schema.json').read_text())
    validate(json.loads((ROOT/'datasets/SCHEMAS/video.example.json').read_text()),schema)
    exps=json.loads((ROOT/'benchmarks/experiments.json').read_text())
    fields={'id','model','hypothesis','checkpoint','dataset','training_configuration','resources','success','baseline','evaluation','stop','failure_interpretation','next_decision','status'}
    for e in exps:
        if fields-set(e) or any(not str(e[k]).strip() for k in fields):errors.append(f"{e.get('id')}: missing experiment fields")
        if not e['status'].startswith('planned'):errors.append('unexecuted experiment improperly labeled')
    if len({e['id'] for e in exps})!=len(exps):errors.append('duplicate experiments')
    for path in ROOT.rglob('*'):
        if path.is_file() and '.git' not in path.parts and (path.stat().st_size>5_000_000 or path.suffix in {'.mp4','.pt','.pth','.safetensors','.parquet'}):errors.append(f'{path}: payload must stay out of GitHub')
    if errors:raise SystemExit('\n'.join(errors))
    print(json.dumps({'markdown_files':len(md),'sources':len(sources),'claims':len(claims),'experiments':len(exps),'result':'PASS','scope':'offline structure, local links, JSON, evidence IDs, experiment contracts and payload exclusion'}))

if __name__=='__main__':main()

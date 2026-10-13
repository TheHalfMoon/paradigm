"""Meaningful metadata workflow and rejection tests; no mocked GPU success."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from cost_model import estimate
from validate_manifest import ROOT, validate_records

def record():
    r=json.loads((ROOT/'datasets/SCHEMAS/video.example.json').read_text())
    r['example_only']=False;r['split']='train';r['exclusion_reasons']=[]
    r['human_review']['accepted']=True
    r['rights'].update(status='approved_under_conditions',conditions_met=True,
                      training_allowed=True,privacy_reviewed=True,music_reviewed=True)
    return r

class ValidationTests(unittest.TestCase):
    def test_cli_workflow(self):
        # These are synthetic metadata declarations, not legally approved real assets.
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'manifest.jsonl';path.write_text(json.dumps(record())+'\n')
            result=subprocess.run([sys.executable,str(ROOT/'tools/research_validation/validate_manifest.py'),str(path)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)['valid_records'],1)

    def test_benchmark_training_rejected(self):
        r=record();r['benchmark_test']=True
        with self.assertRaisesRegex(ValueError,'benchmark'):validate_records([r])

    def test_cross_split_group_rejected(self):
        a=record();b=copy.deepcopy(a);b['id']='different';b['sha256']='2'*64;b['split']='test'
        with self.assertRaisesRegex(ValueError,'crosses splits'):validate_records([a,b])

    def test_rights_condition_rejected(self):
        r=record();r['rights']['music_reviewed']=False
        with self.assertRaisesRegex(ValueError,'rights'):validate_records([r])

    def test_wrong_type_and_time_rejected(self):
        r=record();r['media']['frames']=True
        with self.assertRaisesRegex(ValueError,'integer'):validate_records([r])
        r=record();r['caption']['events'][0]['end_s']=100
        with self.assertRaisesRegex(ValueError,'interval'):validate_records([r])

    def test_cost_units(self):
        result=estimate(50,1.39,100,.07,1,.2,1200,3.0625,20,24,15)
        self.assertAlmostEqual(result['encoded_video_gb_decimal'],9.1875)
        self.assertAlmostEqual(result['total_usd'],451.8)
        with self.assertRaises(ValueError):estimate(-1,1,0,0,0,0,0,0,0,0,0)

if __name__=='__main__':unittest.main()

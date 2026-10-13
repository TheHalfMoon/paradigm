"""Transparent planning arithmetic, not measured training performance."""
import argparse
import json
import math

def estimate(gpu_hours, hourly_rate, storage_gb, storage_rate, storage_months,
             contingency, clips, seconds, mbps, review_hours, review_rate):
    values=locals().copy()
    if any(not math.isfinite(v) or v < 0 for v in values.values()):
        raise ValueError('all inputs must be finite and nonnegative')
    compute=gpu_hours*hourly_rate
    storage=storage_gb*storage_rate*storage_months
    human=review_hours*review_rate
    return {'compute_usd':compute,'storage_usd':storage,'review_usd':human,
            'total_usd':(compute+storage)*(1+contingency)+human,
            'encoded_video_gb_decimal':clips*seconds*mbps/8000,
            'excluded':'Licenses, tax, transfer, rendering, retries beyond contingency and extra copies/caches'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    defaults={'gpu_hours':50,'hourly_rate':1.39,'storage_gb':100,'storage_rate':.07,
              'storage_months':1,'contingency':.2,'clips':1200,'seconds':3.0625,
              'mbps':20,'review_hours':24,'review_rate':15}
    for key,default in defaults.items(): p.add_argument('--'+key.replace('_','-'),type=float,default=default)
    print(json.dumps(estimate(**vars(p.parse_args())),indent=2))

if __name__=='__main__': main()

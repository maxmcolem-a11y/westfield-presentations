"""Reproduce the DGX budget scenarios from the adjacent sanitized usage aggregates.
Run: python3 calculate-sizing.py [folder-containing-sizing-inputs.json]
No credentials, network calls or third-party dependencies.
"""
from pathlib import Path
import json, math, csv, sys

folder = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
inputs = json.loads((folder/'sizing-inputs.json').read_text())
keys = ['calls','input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens']
totals = {key:sum(p[key] for p in inputs['users']) for key in keys}
assert totals['calls']==17471 and totals['output_tokens']==7444251
assert totals['input_tokens']==1458161455 and totals['cached_input_tokens']==1380380800
share = (inputs['tier_percent']['M']+inputs['tier_percent']['L'])/100
scale, hours, target = 30/len(inputs['users']), 22*8, .70
seconds = hours*3600
local = {key:value*scale*share for key,value in totals.items()}
reuse = totals['cached_input_tokens']/totals['input_tokens']
prefill, decode = 3080, 35.75
input_rate, output_rate = local['input_tokens']/seconds, local['output_tokens']/seconds
def equiv(i,o,r): return i*(1-r)/prefill + o/decode
load = equiv(input_rate,output_rate,reuse)
scenarios=[]
for n in [2,3,4]:
    scenarios.append({'units':n,'spark_equipment_usd':4699*n,'combined_equipment_usd':4699*n+8646.73,'mean_modeled_utilization_percent':load/n*100,'planned_output_capacity_tps_same_workload_mix':output_rate*(n*target/load),'one_node_offline_utilization_percent':load/(n-1)*100,'two_times_mean_utilization_percent':2*load/n*100,'maximum_mean_load_multiple_at_70_percent':n*target/load})
cache=[]
for r in [reuse,.9,.8,0]:
    e=equiv(input_rate,output_rate,r)
    cache.append({'input_reuse_percent':r*100,'equivalent_busy_sparks':e,'minimum_units_at_70_percent':math.ceil(e/target),'utilization_percent_by_units':{str(n):e/n*100 for n in [2,3,4]}})
days=[]
for date,day in inputs['daily_start_bucket_proxy'].items():
    i,o=day['input_tokens']*scale*share/(8*3600),day['output_tokens']*scale*share/(8*3600)
    r=day['cached_input_tokens']/day['input_tokens']
    e=equiv(i,o,r)
    days.append({'date':date,'source_output_tokens_6_users':day['output_tokens'],'scaled_local_output_tps_over_8h':o,'scaled_local_fresh_input_tps_over_8h':i*(1-r),'equivalent_busy_sparks':e,'units_at_70_percent':math.ceil(e/target),'utilization_percent_by_units':{str(n):e/n*100 for n in [2,3,4]}})
peak=max(days,key=lambda d:d['equivalent_busy_sparks'])
result={'status':'Unvalidated capacity planning model, not measured Spark performance or a service-level guarantee','source_totals_6':totals,'average_call':{k:totals[k]/totals['calls'] for k in keys if k!='calls'},'scale_to_30':scale,'local_share_assumption':share,'scaled_local_30':local,'assumed_business_hours':hours,'observed_input_reuse_percent':reuse*100,'demand_tps':{'output':output_rate,'fresh_input_at_observed_reuse':input_rate*(1-reuse),'all_input_no_reuse':input_rate},'vendor_reference':{'model':'Qwen3.5-35B-A3B','precision':'FP8','server':'vLLM','hardware':'one NVIDIA DGX Spark','batch_size':1,'input_tokens':128000,'output_tokens':1000,'prefill_tps':prefill,'decode_tps':decode,'reported_end_to_end_seconds':73,'source':'https://developer.nvidia.com/blog/scaling-autonomous-ai-agents-and-workloads-with-nvidia-dgx-spark/','published':'2026-03-16'},'planning_utilization_limit':target,'equivalent_busy_sparks':load,'prefill_equivalent_sparks':input_rate*(1-reuse)/prefill,'decode_equivalent_sparks':output_rate/decode,'minimum_units_at_70_percent':math.ceil(load/target),'scenarios':scenarios,'cache_sensitivity':cache,'daily_proxy_peak':peak,'daily_proxy':days,'limitations':['Work-step tier proportions assumed proportional to tokens and calls; not a tier-by-token measurement.','Cloud cached-input ratio is only a sensitivity for local compute reuse, not a measured local prefix-cache hit rate.','Phase service-time approximation adds prefill and decode; rates vary with context, batching and software. It does not simulate queue latency.','Published phase rates are rounded and do not reproduce the full 73-second end-to-end vendor result; the 30% planning reserve covers unmodeled overhead and variability, not a proven bound.','No Qwen-specific batching speedup, smaller-model speedup or multi-node tensor-parallel speedup is assumed. Independent replicas and balanced demand are assumed.','Logs lack per-call latency and precise arrival traces. Demand tok/s is not observed cloud decode speed. Daily buckets are approximate.','Reasoning tokens are already included in output; cached tokens are already included in input. Neither is counted twice.','OpenAI token counts are used as a workload proxy; Qwen tokenization, reasoning and retries may differ.','Some recorded contexts exceed the published 128K test and even native 262144-token context. Validated compaction or cloud routing is required.','Multimodal encoding/generation, CAD compute, tools and primary-administrator demand are not sized.','Thirty users are five times these six users, not thirty simultaneously active sessions.','70% utilization is an explicit engineering allowance, not an NVIDIA rating or latency guarantee.']}
(folder/'local-ai-sizing.json').write_text(json.dumps(result,indent=2)+'\n')
with (folder/'spark-scenarios.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(scenarios[0]));w.writeheader();w.writerows(scenarios)
print(json.dumps({k:result[k] for k in ['observed_input_reuse_percent','demand_tps','equivalent_busy_sparks','scenarios','cache_sensitivity','daily_proxy_peak']},indent=2))

# Westfield local-AI sizing — auditable planning case

Revised November 2, 2026. No hardware purchase or production configuration is authorized by this document.

## Decision

**Three DGX Sparks is a conditional average-load budgeting case, not guaranteed capacity for 30 users.** Two offer limited headroom; four preserve the three-unit average-load case with one machine offline. Neither three nor four covers the heaviest recorded day compressed into eight hours under this model. Plan measured queues, overnight background work and/or cloud overflow. Validate one Spark before specifying the fleet.

This replaces the earlier illustrative “two medium-work replicas plus one faster low-work server” configuration. The revised model uses identical independent Qwen replicas for both low and medium work, avoiding any assumed small-model speed advantage. Frontier tasks remain on cloud models.

## 1. Actual retained October usage

Six sustained employee accounts; October 1–31, 2026. Completed controller excluded. Normal scheduled and unattributed/background activity remains included. Primary Rimuru, other employee accounts and separately billed image/tool work are excluded. These are retained-log totals, not a guarantee of complete organization-wide usage.

| Account | Model calls | Input tokens including cache | Cached input subset | Output tokens including reasoning |
|---|---:|---:|---:|---:|
| Jason / KITT | 4,457 | 411,225,095 | 392,232,320 | 1,253,705 |
| Brayden | 5,852 | 543,954,242 | 519,271,168 | 2,777,147 |
| James | 2,843 | 301,661,776 | 287,516,288 | 2,416,935 |
| Nessa | 1,624 | 65,100,923 | 55,794,560 | 381,477 |
| Parker | 1,946 | 86,109,982 | 79,200,256 | 357,495 |
| Lia | 749 | 50,109,437 | 46,366,208 | 257,492 |
| **Total** | **17,471** | **1,458,161,455** | **1,380,380,800** | **7,444,251** |

Fresh input = 77,780,655 tokens. Cached input / total input = **94.66584069%**. The 1,928,880 reasoning tokens are already included in output; they are not added again. A model call is not a completed employee task.

Average call: **83,461.8 input tokens**, including **4,452.0 fresh tokens**, and **426.1 output tokens**. These averages do not describe latency or every request.

## 2. Scale the workload, not simply the headcount

The separately audited work-step mix is 40.02590036% low, 49.13941105% medium and 10.83468858% high. We provisionally apply low + medium = **89.16531142%** to both input and output tokens, and scale six users to 30 by multiplying by five. This is not a measured tier-by-token allocation or proof that local models can complete 89% of the work.

- Local output = 7,444,251 × 5 × 0.8916531142 = **33,188,448 tokens/month**.
- Local input including reused context = **6,500,871,011 tokens/month**.
- Local fresh input, if cloud-like reuse holds = **346,766,816 tokens/month**.
- Local calls = **77,890/month**.
- Low output allocation: approximately **14.90M**; medium: **18.29M**. Both use the same model in this estimate.
- Service window assumption = 22 × 8 × 3,600 = **633,600 seconds/month** (176 hours).
- Mean fleet output demand = 33,188,448 / 633,600 = **52.3808 tok/s**.
- Mean fresh-input demand = **547.2961 tok/s**. No-reuse input demand = **10,260.2131 tok/s**.

These are demand rates spread across an assumed window—not observed cloud generation speeds. Retained usage aggregates do not provide per-call generation latency. Background and weekend work is compressed into the work-hours assumption; night scheduling may help. Thirty equally active users is a workload scenario, not thirty concurrent requests or a forecast that every employee will use the system identically.

## 3. Credible model and measured hardware reference

**Qwen3.5-35B-A3B, FP8 precision, vLLM, on one DGX Spark.** NVIDIA's March 16, 2026 benchmark reports 3,080 input tok/s and 35.75 output tok/s for batch size one with 128K input / 1K output; reported end-to-end latency is 73 seconds. This is the reference for our calculation, not a measurement of Westfield jobs. [NVIDIA benchmark, Table 1](https://developer.nvidia.com/blog/scaling-autonomous-ai-agents-and-workloads-with-nvidia-dgx-spark/).

Qwen's official card specifies 35B total / 3B active parameters and an Apache-2.0 license. Native context is 262,144 tokens. FP8 weights imply roughly 35 GB before active context/state and runtime overhead; the cited Spark test demonstrates model fit, not simultaneous capacity for 30 long conversations. [Official model card](https://huggingface.co/Qwen/Qwen3.5-35B-A3B).

Use one independent replica per machine. The original server plan still hosts agents and records. Requests are queued and distributed, ideally keeping a session on the same replica to aid cache reuse. No multi-node tensor parallelism, specialist interconnect, Qwen-specific concurrency speedup or small-model speedup is assumed. This design does not imply that individual answers become faster as more replicas are added.

## 4. The calculation that produces three

Reading context (prefill) and writing answers (decode) both consume capacity. Use a first-order serial service-time approximation:

```text
busy-Spark equivalents = fresh input tok/s ÷ prefill tok/s
                      + output tok/s ÷ decode tok/s
                      = 547.2961 ÷ 3,080 + 52.3808 ÷ 35.75
                      = 0.1777 + 1.4652 = 1.6429

planning fleet = ceiling(1.6429 ÷ 0.70) = ceiling(2.3470) = 3
```

The **70% modeled utilization limit** is an explicit planning choice, reserving 30% for unmodeled overhead, queue variability and operational margin. It is not a vendor rating, queue simulation, latency bound or N+1 availability guarantee. Benchmark phase rates are rounded and do not sum to the full reported 73-second wall-clock result. Effective rates vary with actual context, cache state, batching, scheduler and software version. Local testing must replace this approximation.

## 5. Two vs three vs four

All rows assume observed cloud-like context reuse and the same input/output mix. Planned output capacity includes input processing and the 30% reserve; it is not raw decode-only throughput.

| Sparks | Spark equipment only | Mean modeled load | Planned output capacity, tok/s | Load on remaining machines if one is offline |
|---|---:|---:|---:|---:|
| 2 | $9,398 | 82.1% | 44.6 | 164.3% |
| 3 | $14,097 | 54.8% | 67.0 | 82.1% |
| 4 | $18,796 | 41.1% | 89.3 | 54.8% |

Compare these capacities with **52.4 output tok/s average demand**. Two are below the 70%-load design target. Three are the smallest fleet meeting it; four allow one replica to be unavailable while retaining that baseline margin. This assumes working routing, balanced load and independent replicas; it does not establish automatic failover. A sustained 2× average workload gives 164.3%, 109.5% and 82.1% utilization on two, three and four respectively.

Unit price is NVIDIA's published **$4,699** reference, not a fresh quote. Combined with the historical $8,646.73 server equipment: two = **$18,044.73**, three = **$22,743.73**, four = **$27,442.73**, before tax, shipping, extra network/UPS capacity, setup and support. [Price basis](https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713).

## 6. Busy-day and cache sensitivities

**October 13:** 948,083 output tokens across the six accounts. Scaling the daily activity by five and by the same local fraction, then compressing it into eight hours, gives **146.7641 output tok/s** plus **1,027.9623 fresh-input tok/s**, using that day's own recorded cache ratio. Modeled demand is **4.4390 busy Sparks**: three would be at **148.0%** and four at **111.0%**, before a reserve. The same 70% rule rounds to **seven** for this day. This demonstrates the need for peak handling; it is not a seven-unit purchase recommendation.

Daily calculation assigns each turn/model block to its first-call date in Indianapolis time. None of the included blocks crossed midnight, so no included block is split across dates. Exact intraday arrival, concurrency and acceptable queue delay remain unmeasured. Keeping background work overnight or using cloud overflow can change peak capacity needs substantially.

At the same **monthly average** workload:

| Local input reuse | Busy-Spark equivalents | Units at 70% modeled load |
|---|---:|---:|
| 94.6658% | 1.643 | 3 |
| 90.0000% | 1.798 | 3 |
| 80.0000% | 2.131 | 4 |
| 0.0000% | 4.796 | 7 |

Do not assume cached-input billing in the cloud translates directly into equal local compute reuse. Local prefix caching depends on matching prefixes, model/software support, memory eviction, cold starts and routing affinity. It reduces prefill work, not answer generation. [vLLM prefix-caching documentation](https://docs.vllm.ai/en/v0.30.0/features/automatic_prefix_caching/).

## 7. What remains to prove

1. Accepted task quality and tool-call reliability for our low/medium jobs, not only model benchmarks.
2. Actual Qwen tokenization, output/reasoning lengths, retries, memory usage, cache effectiveness and FP8/runtime compatibility.
3. Time to first token, complete response time and queue depth at 1, 4, 8 and 16 simultaneous requests, including representative busy-day replay.
4. Context handling: some retained cloud calls reach about 401K input tokens, exceeding both the 128K benchmark and native model context. Use validated compaction or cloud routing; do not silently truncate.
5. Restart, one-replica failure, fallback permissions and complete-result verification. Four units alone do not provide high availability.

The Spark hardware does not remove company responsibility for GPU/software/security updates, queues, monitoring, context storage, model upgrades and recovery. Original servers remain needed under this proposal. Separate image generation, CAD compute and primary-administrator load are outside this sizing. Frontier/overflow cloud costs remain; subtract offloaded API work to avoid double counting.

## Reproduce

Save `calculate-sizing.py` and `sizing-inputs.json` in one folder, then run `python3 calculate-sizing.py`. It produces `local-ai-sizing.json` and `spark-scenarios.csv`. The inputs contain only aggregate counts and file fingerprints, not raw conversations, credentials or session IDs. The internal aggregate collector excludes only records marked as the completed controller.

### Complete calculation limitations

- Work-step tier proportions assumed proportional to tokens and calls; not a tier-by-token measurement.
- Cloud cached-input ratio is only a sensitivity for local compute reuse, not a measured local prefix-cache hit rate.
- Phase service-time approximation adds prefill and decode; rates vary with context, batching and software. It does not simulate queue latency.
- Published phase rates are rounded and do not reproduce the full 73-second end-to-end vendor result; the 30% planning reserve covers unmodeled overhead and variability, not a proven bound.
- No Qwen-specific batching speedup, smaller-model speedup or multi-node tensor-parallel speedup is assumed. Independent replicas and balanced demand are assumed.
- Logs lack per-call latency and precise arrival traces. Demand tok/s is not observed cloud decode speed. Daily buckets are approximate.
- Reasoning tokens are already included in output; cached tokens are already included in input. Neither is counted twice.
- OpenAI token counts are used as a workload proxy; Qwen tokenization, reasoning and retries may differ.
- Some recorded contexts exceed the published 128K test and even native 262144-token context. Validated compaction or cloud routing is required.
- Multimodal encoding/generation, CAD compute, tools and primary-administrator demand are not sized.
- Thirty users are five times these six users, not thirty simultaneously active sessions.
- 70% utilization is an explicit engineering allowance, not an NVIDIA rating or latency guarantee.

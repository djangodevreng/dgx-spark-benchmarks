# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-12 11:23:52
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  2788.48   
Total input tokens:                      57758     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         75.06     
Peak output token throughput (tok/s):    144.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          95.77     
---------------Time to First Token----------------
Mean TTFT (ms):                          1562.78   
Median TTFT (ms):                        1507.45   
P50 TTFT (ms):                           1507.45   
P90 TTFT (ms):                           2237.62   
P95 TTFT (ms):                           2803.67   
P99 TTFT (ms):                           2994.32   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          422.32    
Median TPOT (ms):                        432.34    
P50 TPOT (ms):                           432.34    
P90 TPOT (ms):                           477.96    
P95 TPOT (ms):                           484.73    
P99 TPOT (ms):                           494.31    
---------------Inter-token Latency----------------
Mean ITL (ms):                           501.94    
Median ITL (ms):                         452.06    
P50 ITL (ms):                            452.06    
P90 ITL (ms):                            512.24    
P95 ITL (ms):                            521.08    
P99 ITL (ms):                            1999.98   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1700662.34
Median E2EL (ms):                        1714680.97
P50 E2EL (ms):                           1714680.97
P90 E2EL (ms):                           2445566.89
P95 E2EL (ms):                           2603616.32
P99 E2EL (ms):                           2663653.32
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

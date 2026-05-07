# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 04:19:59
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1513.24   
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.13      
Output token throughput (tok/s):         64.16     
Peak output token throughput (tok/s):    195.00    
Peak concurrent requests:                168.00    
Total token throughput (tok/s):          603.00    
---------------Time to First Token----------------
Mean TTFT (ms):                          204312.77 
Median TTFT (ms):                        164378.83 
P50 TTFT (ms):                           164378.83 
P90 TTFT (ms):                           448397.36 
P95 TTFT (ms):                           467614.94 
P99 TTFT (ms):                           510630.23 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1167.54   
Median TPOT (ms):                        1128.89   
P50 TPOT (ms):                           1128.89   
P90 TPOT (ms):                           1582.79   
P95 TPOT (ms):                           1975.45   
P99 TPOT (ms):                           2774.86   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1064.65   
Median ITL (ms):                         562.99    
P50 ITL (ms):                            562.99    
P90 ITL (ms):                            2624.55   
P95 ITL (ms):                            5567.08   
P99 ITL (ms):                            7929.95   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          721156.13 
Median E2EL (ms):                        729146.58 
P50 E2EL (ms):                           729146.58 
P90 E2EL (ms):                           1013343.26
P95 E2EL (ms):                           1079875.55
P99 E2EL (ms):                           1197076.43
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 12:58:32
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  687.03    
Total input tokens:                      823790    
Total generated tokens:                  79794     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         116.14    
Peak output token throughput (tok/s):    192.00    
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          1315.20   
---------------Time to First Token----------------
Mean TTFT (ms):                          826.65    
Median TTFT (ms):                        764.70    
P50 TTFT (ms):                           764.70    
P90 TTFT (ms):                           1462.92   
P95 TTFT (ms):                           1648.75   
P99 TTFT (ms):                           2292.97   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          48.07     
Median TPOT (ms):                        43.52     
P50 TPOT (ms):                           43.52     
P90 TPOT (ms):                           57.33     
P95 TPOT (ms):                           71.17     
P99 TPOT (ms):                           167.91    
---------------Inter-token Latency----------------
Mean ITL (ms):                           69.29     
Median ITL (ms):                         36.38     
P50 ITL (ms):                            36.38     
P90 ITL (ms):                            43.16     
P95 ITL (ms):                            45.15     
P99 ITL (ms):                            338.70    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          18124.77  
Median E2EL (ms):                        16080.42  
P50 E2EL (ms):                           16080.42  
P90 E2EL (ms):                           37446.73  
P95 E2EL (ms):                           40713.69  
P99 E2EL (ms):                           46763.31  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

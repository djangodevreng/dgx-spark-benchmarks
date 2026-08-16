# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-15 18:39:49
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B --tokenizer Qwen/Qwen3.8-27B --served-model-name qwen3.8-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1231.56   
Total input tokens:                      823212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.16      
Output token throughput (tok/s):         78.84     
Peak output token throughput (tok/s):    328.00    
Peak concurrent requests:                175.00    
Total token throughput (tok/s):          747.26    
---------------Time to First Token----------------
Mean TTFT (ms):                          86257.90  
Median TTFT (ms):                        87195.24  
P50 TTFT (ms):                           87195.24  
P90 TTFT (ms):                           151876.13 
P95 TTFT (ms):                           159985.80 
P99 TTFT (ms):                           181100.66 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1290.54   
Median TPOT (ms):                        1271.10   
P50 TPOT (ms):                           1271.10   
P90 TPOT (ms):                           2004.16   
P95 TPOT (ms):                           2046.74   
P99 TPOT (ms):                           2102.37   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1114.22   
Median ITL (ms):                         641.31    
P50 ITL (ms):                            641.31    
P90 ITL (ms):                            2112.96   
P95 ITL (ms):                            2136.61   
P99 ITL (ms):                            2447.13   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          626520.39 
Median E2EL (ms):                        627365.84 
P50 E2EL (ms):                           627365.84 
P90 E2EL (ms):                           924354.75 
P95 E2EL (ms):                           993265.69 
P99 E2EL (ms):                           1057341.85
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

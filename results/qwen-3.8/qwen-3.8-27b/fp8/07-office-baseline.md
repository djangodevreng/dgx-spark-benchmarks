# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 04:51:40
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B-FP8 --tokenizer Qwen/Qwen3.8-27B-FP8 --served-model-name qwen3.8-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1785.52   
Total input tokens:                      823212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         54.38     
Peak output token throughput (tok/s):    328.00    
Peak concurrent requests:                196.00    
Total token throughput (tok/s):          515.43    
---------------Time to First Token----------------
Mean TTFT (ms):                          408512.28 
Median TTFT (ms):                        426054.60 
P50 TTFT (ms):                           426054.60 
P90 TTFT (ms):                           718813.75 
P95 TTFT (ms):                           756550.09 
P99 TTFT (ms):                           809321.28 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          2013.51   
Median TPOT (ms):                        1977.54   
P50 TPOT (ms):                           1977.54   
P90 TPOT (ms):                           3511.85   
P95 TPOT (ms):                           3553.36   
P99 TPOT (ms):                           3613.44   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1661.28   
Median ITL (ms):                         683.08    
P50 ITL (ms):                            683.08    
P90 ITL (ms):                            3638.15   
P95 ITL (ms):                            3660.63   
P99 ITL (ms):                            3686.12   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1213973.83
Median E2EL (ms):                        1235227.37
P50 E2EL (ms):                           1235227.37
P90 E2EL (ms):                           1531025.35
P95 E2EL (ms):                           1615442.23
P99 E2EL (ms):                           1668491.21
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

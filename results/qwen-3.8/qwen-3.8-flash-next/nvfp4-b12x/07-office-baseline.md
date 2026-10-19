# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-10-18 16:19:58
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-Flash-Next-FP4-Local --tokenizer nvidia/Qwen3.8-Flash-Next-FP4-Local --served-model-name qwen3.8-flash-next --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  964.33    
Total input tokens:                      823212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.21      
Output token throughput (tok/s):         100.68    
Peak output token throughput (tok/s):    102.00    
Peak concurrent requests:                76.00     
Total token throughput (tok/s):          954.35    
---------------Time to First Token----------------
Mean TTFT (ms):                          101979.68 
Median TTFT (ms):                        110119.51 
P50 TTFT (ms):                           110119.51 
P90 TTFT (ms):                           192975.74 
P95 TTFT (ms):                           206992.28 
P99 TTFT (ms):                           233047.09 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          227.27    
Median TPOT (ms):                        233.25    
P50 TPOT (ms):                           233.25    
P90 TPOT (ms):                           272.80    
P95 TPOT (ms):                           283.34    
P99 TPOT (ms):                           313.89    
---------------Inter-token Latency----------------
Mean ITL (ms):                           464.62    
Median ITL (ms):                         301.57    
P50 ITL (ms):                            301.57    
P90 ITL (ms):                            1329.07   
P95 ITL (ms):                            1653.22   
P99 ITL (ms):                            1887.07   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          208995.48 
Median E2EL (ms):                        206285.73 
P50 E2EL (ms):                           206285.73 
P90 E2EL (ms):                           314092.58 
P95 E2EL (ms):                           335067.32 
P99 E2EL (ms):                           378410.48 
---------------Speculative Decoding---------------
Acceptance rate (%):                     37.18     
Acceptance length:                       2.12      
Drafts:                                  45868     
Draft tokens:                            137604    
Accepted tokens:                         51168     
Per-position acceptance (%):
  Position 0:                            59.56     
  Position 1:                            33.71     
  Position 2:                            18.29     
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

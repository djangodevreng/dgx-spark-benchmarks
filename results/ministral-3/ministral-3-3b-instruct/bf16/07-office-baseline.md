# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 01:12:32
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  683.98    
Total input tokens:                      813236    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         141.95    
Peak output token throughput (tok/s):    286.00    
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          1330.93   
---------------Time to First Token----------------
Mean TTFT (ms):                          705.35    
Median TTFT (ms):                        660.09    
P50 TTFT (ms):                           660.09    
P90 TTFT (ms):                           1038.43   
P95 TTFT (ms):                           1193.26   
P99 TTFT (ms):                           1364.85   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          36.85     
Median TPOT (ms):                        36.86     
P50 TPOT (ms):                           36.86     
P90 TPOT (ms):                           46.99     
P95 TPOT (ms):                           50.08     
P99 TPOT (ms):                           55.43     
---------------Inter-token Latency----------------
Mean ITL (ms):                           36.74     
Median ITL (ms):                         31.80     
P50 ITL (ms):                            31.80     
P90 ITL (ms):                            41.94     
P95 ITL (ms):                            45.77     
P99 ITL (ms):                            265.36    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          18541.80  
Median E2EL (ms):                        17448.68  
P50 E2EL (ms):                           17448.68  
P90 E2EL (ms):                           33722.99  
P95 E2EL (ms):                           39038.81  
P99 E2EL (ms):                           41995.52  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

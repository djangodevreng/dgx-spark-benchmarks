# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 08:32:09
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model ibm-granite/granite-4.1-8b --tokenizer ibm-granite/granite-4.1-8b --served-model-name granite-4-1-8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  860.16    
Total input tokens:                      55758     
Total generated tokens:                  48694     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         56.61     
Peak output token throughput (tok/s):    156.00    
Peak concurrent requests:                13.00     
Total token throughput (tok/s):          121.43    
---------------Time to First Token----------------
Mean TTFT (ms):                          266.48    
Median TTFT (ms):                        254.56    
P50 TTFT (ms):                           254.56    
P90 TTFT (ms):                           342.80    
P95 TTFT (ms):                           384.71    
P99 TTFT (ms):                           435.94    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          78.05     
Median TPOT (ms):                        77.45     
P50 TPOT (ms):                           77.45     
P90 TPOT (ms):                           79.33     
P95 TPOT (ms):                           80.82     
P99 TPOT (ms):                           93.85     
---------------Inter-token Latency----------------
Mean ITL (ms):                           77.31     
Median ITL (ms):                         76.26     
P50 ITL (ms):                            76.26     
P90 ITL (ms):                            77.83     
P95 ITL (ms):                            81.10     
P99 ITL (ms):                            125.69    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          15324.67  
Median E2EL (ms):                        10057.66  
P50 E2EL (ms):                           10057.66  
P90 E2EL (ms):                           37013.76  
P95 E2EL (ms):                           46045.56  
P99 E2EL (ms):                           59695.31  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

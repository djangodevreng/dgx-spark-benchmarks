# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-12 10:20:45
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1399.16   
Total input tokens:                      823836    
Total generated tokens:                  97092     
Request throughput (req/s):              0.14      
Output token throughput (tok/s):         69.39     
Peak output token throughput (tok/s):    229.00    
Peak concurrent requests:                190.00    
Total token throughput (tok/s):          658.20    
---------------Time to First Token----------------
Mean TTFT (ms):                          18434.64  
Median TTFT (ms):                        17039.38  
P50 TTFT (ms):                           17039.38  
P90 TTFT (ms):                           30607.93  
P95 TTFT (ms):                           38336.92  
P99 TTFT (ms):                           43651.44  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1815.43   
Median TPOT (ms):                        1663.08   
P50 TPOT (ms):                           1663.08   
P90 TPOT (ms):                           2837.17   
P95 TPOT (ms):                           3265.51   
P99 TPOT (ms):                           3837.32   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1564.89   
Median ITL (ms):                         1094.17   
P50 ITL (ms):                            1094.17   
P90 ITL (ms):                            3932.19   
P95 ITL (ms):                            6604.02   
P99 ITL (ms):                            7076.01   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          757257.76 
Median E2EL (ms):                        795338.49 
P50 E2EL (ms):                           795338.49 
P90 E2EL (ms):                           1116660.66
P95 E2EL (ms):                           1203860.50
P99 E2EL (ms):                           1274191.32
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

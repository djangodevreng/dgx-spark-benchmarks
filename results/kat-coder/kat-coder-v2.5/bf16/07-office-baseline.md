# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-13 17:56:07
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Kwaipilot/KAT-Coder-V2.5-Dev --tokenizer Kwaipilot/KAT-Coder-V2.5-Dev --served-model-name kat-coder-v2-5-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  774.13    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         125.42    
Peak output token throughput (tok/s):    234.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          1177.97   
---------------Time to First Token----------------
Mean TTFT (ms):                          1786.24   
Median TTFT (ms):                        1616.75   
P50 TTFT (ms):                           1616.75   
P90 TTFT (ms):                           2806.84   
P95 TTFT (ms):                           3254.51   
P99 TTFT (ms):                           4381.01   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          230.44    
Median TPOT (ms):                        237.38    
P50 TPOT (ms):                           237.38    
P90 TPOT (ms):                           255.74    
P95 TPOT (ms):                           263.46    
P99 TPOT (ms):                           293.20    
---------------Inter-token Latency----------------
Mean ITL (ms):                           226.55    
Median ITL (ms):                         188.71    
P50 ITL (ms):                            188.71    
P90 ITL (ms):                            226.36    
P95 ITL (ms):                            586.74    
P99 ITL (ms):                            985.09    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          111765.72 
Median E2EL (ms):                        112828.68 
P50 E2EL (ms):                           112828.68 
P90 E2EL (ms):                           196340.77 
P95 E2EL (ms):                           210611.50 
P99 E2EL (ms):                           225783.50 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

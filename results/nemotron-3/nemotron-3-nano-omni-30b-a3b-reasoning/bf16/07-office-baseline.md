# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 01:46:02
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  757.82    
Total input tokens:                      816039    
Total generated tokens:                  97092     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         128.12    
Peak output token throughput (tok/s):    159.00    
Peak concurrent requests:                41.00     
Total token throughput (tok/s):          1204.94   
---------------Time to First Token----------------
Mean TTFT (ms):                          1342.58   
Median TTFT (ms):                        1214.06   
P50 TTFT (ms):                           1214.06   
P90 TTFT (ms):                           2040.25   
P95 TTFT (ms):                           2333.62   
P99 TTFT (ms):                           2927.31   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          200.68    
Median TPOT (ms):                        204.14    
P50 TPOT (ms):                           204.14    
P90 TPOT (ms):                           222.07    
P95 TPOT (ms):                           227.98    
P99 TPOT (ms):                           237.33    
---------------Inter-token Latency----------------
Mean ITL (ms):                           294.53    
Median ITL (ms):                         175.18    
P50 ITL (ms):                            175.18    
P90 ITL (ms):                            241.95    
P95 ITL (ms):                            461.24    
P99 ITL (ms):                            1046.40   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          97225.95  
Median E2EL (ms):                        98035.84  
P50 E2EL (ms):                           98035.84  
P90 E2EL (ms):                           167784.39 
P95 E2EL (ms):                           184093.22 
P99 E2EL (ms):                           195039.76 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

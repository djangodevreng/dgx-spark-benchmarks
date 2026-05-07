# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-03 14:28:43
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  759.30    
Total input tokens:                      816039    
Total generated tokens:                  97092     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         127.87    
Peak output token throughput (tok/s):    239.00    
Peak concurrent requests:                42.00     
Total token throughput (tok/s):          1202.59   
---------------Time to First Token----------------
Mean TTFT (ms):                          1330.94   
Median TTFT (ms):                        1228.60   
P50 TTFT (ms):                           1228.60   
P90 TTFT (ms):                           2028.06   
P95 TTFT (ms):                           2375.07   
P99 TTFT (ms):                           2995.98   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          200.41    
Median TPOT (ms):                        203.11    
P50 TPOT (ms):                           203.11    
P90 TPOT (ms):                           223.09    
P95 TPOT (ms):                           225.72    
P99 TPOT (ms):                           238.77    
---------------Inter-token Latency----------------
Mean ITL (ms):                           197.48    
Median ITL (ms):                         170.62    
P50 ITL (ms):                            170.62    
P90 ITL (ms):                            198.18    
P95 ITL (ms):                            320.32    
P99 ITL (ms):                            993.08    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          97083.05  
Median E2EL (ms):                        97061.46  
P50 E2EL (ms):                           97061.46  
P90 E2EL (ms):                           168074.98 
P95 E2EL (ms):                           184508.08 
P99 E2EL (ms):                           196533.76 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

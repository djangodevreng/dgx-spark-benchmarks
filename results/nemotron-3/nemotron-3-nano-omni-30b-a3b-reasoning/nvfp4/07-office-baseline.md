# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 13:20:31
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  687.11    
Total input tokens:                      816039    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         141.30    
Peak output token throughput (tok/s):    289.00    
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          1328.94   
---------------Time to First Token----------------
Mean TTFT (ms):                          1193.55   
Median TTFT (ms):                        1088.79   
P50 TTFT (ms):                           1088.79   
P90 TTFT (ms):                           1880.99   
P95 TTFT (ms):                           2324.28   
P99 TTFT (ms):                           2551.33   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          42.46     
Median TPOT (ms):                        41.66     
P50 TPOT (ms):                           41.66     
P90 TPOT (ms):                           58.11     
P95 TPOT (ms):                           65.43     
P99 TPOT (ms):                           72.15     
---------------Inter-token Latency----------------
Mean ITL (ms):                           61.41     
Median ITL (ms):                         33.01     
P50 ITL (ms):                            33.01     
P90 ITL (ms):                            45.25     
P95 ITL (ms):                            47.32     
P99 ITL (ms):                            455.26    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          21465.98  
Median E2EL (ms):                        20669.67  
P50 E2EL (ms):                           20669.67  
P90 E2EL (ms):                           39104.80  
P95 E2EL (ms):                           44226.04  
P99 E2EL (ms):                           51212.13  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

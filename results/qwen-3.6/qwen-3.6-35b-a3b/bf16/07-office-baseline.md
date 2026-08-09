# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 14:01:45
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  772.75    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         125.64    
Peak output token throughput (tok/s):    240.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          1180.07   
---------------Time to First Token----------------
Mean TTFT (ms):                          2393.02   
Median TTFT (ms):                        2315.87   
P50 TTFT (ms):                           2315.87   
P90 TTFT (ms):                           4021.68   
P95 TTFT (ms):                           4519.16   
P99 TTFT (ms):                           5859.98   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          229.65    
Median TPOT (ms):                        234.27    
P50 TPOT (ms):                           234.27    
P90 TPOT (ms):                           254.49    
P95 TPOT (ms):                           262.38    
P99 TPOT (ms):                           295.35    
---------------Inter-token Latency----------------
Mean ITL (ms):                           225.55    
Median ITL (ms):                         182.84    
P50 ITL (ms):                            182.84    
P90 ITL (ms):                            420.58    
P95 ITL (ms):                            584.07    
P99 ITL (ms):                            608.44    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          111815.09 
Median E2EL (ms):                        112658.09 
P50 E2EL (ms):                           112658.09 
P90 E2EL (ms):                           194567.02 
P95 E2EL (ms):                           208586.82 
P99 E2EL (ms):                           223181.57 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

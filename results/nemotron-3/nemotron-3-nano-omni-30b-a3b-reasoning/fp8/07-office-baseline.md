# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 04:47:59
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --served-model-name nemotron-3-nano-omni-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  704.27    
Total input tokens:                      816039    
Total generated tokens:                  97092     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         137.86    
Peak output token throughput (tok/s):    199.00    
Peak concurrent requests:                24.00     
Total token throughput (tok/s):          1296.56   
---------------Time to First Token----------------
Mean TTFT (ms):                          1360.91   
Median TTFT (ms):                        1279.84   
P50 TTFT (ms):                           1279.84   
P90 TTFT (ms):                           2073.98   
P95 TTFT (ms):                           2276.15   
P99 TTFT (ms):                           2833.04   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          81.15     
Median TPOT (ms):                        85.11     
P50 TPOT (ms):                           85.11     
P90 TPOT (ms):                           97.59     
P95 TPOT (ms):                           103.95    
P99 TPOT (ms):                           111.83    
---------------Inter-token Latency----------------
Mean ITL (ms):                           114.89    
Median ITL (ms):                         68.21     
P50 ITL (ms):                            68.21     
P90 ITL (ms):                            83.81     
P95 ITL (ms):                            138.92    
P99 ITL (ms):                            654.11    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          40325.74  
Median E2EL (ms):                        39658.80  
P50 E2EL (ms):                           39658.80  
P90 E2EL (ms):                           72540.53  
P95 E2EL (ms):                           78005.93  
P99 E2EL (ms):                           84900.08  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

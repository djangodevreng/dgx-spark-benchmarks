# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-04 22:17:24
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  708.92    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         136.96    
Peak output token throughput (tok/s):    255.00    
Peak concurrent requests:                24.00     
Total token throughput (tok/s):          1286.32   
---------------Time to First Token----------------
Mean TTFT (ms):                          1344.79   
Median TTFT (ms):                        1229.48   
P50 TTFT (ms):                           1229.48   
P90 TTFT (ms):                           2239.46   
P95 TTFT (ms):                           2585.25   
P99 TTFT (ms):                           3593.32   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          84.48     
Median TPOT (ms):                        86.27     
P50 TPOT (ms):                           86.27     
P90 TPOT (ms):                           100.78    
P95 TPOT (ms):                           105.39    
P99 TPOT (ms):                           119.20    
---------------Inter-token Latency----------------
Mean ITL (ms):                           84.04     
Median ITL (ms):                         69.28     
P50 ITL (ms):                            69.28     
P90 ITL (ms):                            91.01     
P95 ITL (ms):                            227.70    
P99 ITL (ms):                            399.00    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          41983.67  
Median E2EL (ms):                        40462.09  
P50 E2EL (ms):                           40462.09  
P90 E2EL (ms):                           75610.88  
P95 E2EL (ms):                           82199.82  
P99 E2EL (ms):                           90861.08  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

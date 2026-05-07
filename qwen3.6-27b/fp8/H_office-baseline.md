# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-04 16:33:42
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  970.71    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.21      
Output token throughput (tok/s):         100.02    
Peak output token throughput (tok/s):    453.00    
Peak concurrent requests:                160.00    
Total token throughput (tok/s):          939.42    
---------------Time to First Token----------------
Mean TTFT (ms):                          20745.87  
Median TTFT (ms):                        14093.10  
P50 TTFT (ms):                           14093.10  
P90 TTFT (ms):                           49588.83  
P95 TTFT (ms):                           55909.65  
P99 TTFT (ms):                           74180.36  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          932.64    
Median TPOT (ms):                        949.89    
P50 TPOT (ms):                           949.89    
P90 TPOT (ms):                           1403.12   
P95 TPOT (ms):                           1535.78   
P99 TPOT (ms):                           1852.86   
---------------Inter-token Latency----------------
Mean ITL (ms):                           833.74    
Median ITL (ms):                         425.55    
P50 ITL (ms):                            425.55    
P90 ITL (ms):                            1952.42   
P95 ITL (ms):                            2053.38   
P99 ITL (ms):                            2134.51   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          423404.39 
Median E2EL (ms):                        421694.05 
P50 E2EL (ms):                           421694.05 
P90 E2EL (ms):                           696044.43 
P95 E2EL (ms):                           759968.71 
P99 E2EL (ms):                           803971.28 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

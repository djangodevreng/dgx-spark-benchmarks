# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 09:44:23
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  748.08    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         129.79    
Peak output token throughput (tok/s):    238.00    
Peak concurrent requests:                40.00     
Total token throughput (tok/s):          1219.78   
---------------Time to First Token----------------
Mean TTFT (ms):                          1584.94   
Median TTFT (ms):                        1433.25   
P50 TTFT (ms):                           1433.25   
P90 TTFT (ms):                           2582.18   
P95 TTFT (ms):                           3112.24   
P99 TTFT (ms):                           3812.14   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          194.13    
Median TPOT (ms):                        198.27    
P50 TPOT (ms):                           198.27    
P90 TPOT (ms):                           217.01    
P95 TPOT (ms):                           219.89    
P99 TPOT (ms):                           228.71    
---------------Inter-token Latency----------------
Mean ITL (ms):                           190.87    
Median ITL (ms):                         158.79    
P50 ITL (ms):                            158.79    
P90 ITL (ms):                            172.48    
P95 ITL (ms):                            182.28    
P99 ITL (ms):                            1332.64   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          94243.38  
Median E2EL (ms):                        93428.09  
P50 E2EL (ms):                           93428.09  
P90 E2EL (ms):                           163271.54 
P95 E2EL (ms):                           177380.18 
P99 E2EL (ms):                           188588.97 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

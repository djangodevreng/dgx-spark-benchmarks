# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 04:15:14
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  700.36    
Total input tokens:                      813236    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.63    
Peak output token throughput (tok/s):    273.00    
Peak concurrent requests:                18.00     
Total token throughput (tok/s):          1299.80   
---------------Time to First Token----------------
Mean TTFT (ms):                          1347.19   
Median TTFT (ms):                        1286.90   
P50 TTFT (ms):                           1286.90   
P90 TTFT (ms):                           2118.63   
P95 TTFT (ms):                           2386.53   
P99 TTFT (ms):                           3125.93   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          68.13     
Median TPOT (ms):                        68.77     
P50 TPOT (ms):                           68.77     
P90 TPOT (ms):                           82.56     
P95 TPOT (ms):                           87.64     
P99 TPOT (ms):                           98.63     
---------------Inter-token Latency----------------
Mean ITL (ms):                           67.73     
Median ITL (ms):                         52.88     
P50 ITL (ms):                            52.88     
P90 ITL (ms):                            61.24     
P95 ITL (ms):                            66.44     
P99 ITL (ms):                            577.94    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          34227.01  
Median E2EL (ms):                        33401.72  
P50 E2EL (ms):                           33401.72  
P90 E2EL (ms):                           58981.42  
P95 E2EL (ms):                           66852.52  
P99 E2EL (ms):                           70552.98  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

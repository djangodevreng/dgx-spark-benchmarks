# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-17 06:28:50
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  677.23    
Total input tokens:                      814599    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         143.37    
Peak output token throughput (tok/s):    414.00    
Peak concurrent requests:                11.00     
Total token throughput (tok/s):          1346.20   
---------------Time to First Token----------------
Mean TTFT (ms):                          563.98    
Median TTFT (ms):                        493.22    
P50 TTFT (ms):                           493.22    
P90 TTFT (ms):                           991.46    
P95 TTFT (ms):                           1158.20   
P99 TTFT (ms):                           1560.19   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          26.32     
Median TPOT (ms):                        26.12     
P50 TPOT (ms):                           26.12     
P90 TPOT (ms):                           29.23     
P95 TPOT (ms):                           30.33     
P99 TPOT (ms):                           35.46     
---------------Inter-token Latency----------------
Mean ITL (ms):                           26.28     
Median ITL (ms):                         23.31     
P50 ITL (ms):                            23.31     
P90 ITL (ms):                            24.95     
P95 ITL (ms):                            25.68     
P99 ITL (ms):                            34.06     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          13316.07  
Median E2EL (ms):                        13193.71  
P50 E2EL (ms):                           13193.71  
P90 E2EL (ms):                           22897.79  
P95 E2EL (ms):                           24284.34  
P99 E2EL (ms):                           26549.29  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

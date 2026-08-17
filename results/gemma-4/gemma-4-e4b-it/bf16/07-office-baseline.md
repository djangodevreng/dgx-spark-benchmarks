# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-17 04:15:39
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  698.62    
Total input tokens:                      814599    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.98    
Peak output token throughput (tok/s):    318.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1304.99   
---------------Time to First Token----------------
Mean TTFT (ms):                          972.17    
Median TTFT (ms):                        888.64    
P50 TTFT (ms):                           888.64    
P90 TTFT (ms):                           1713.88   
P95 TTFT (ms):                           2083.88   
P99 TTFT (ms):                           2698.97   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          57.81     
Median TPOT (ms):                        57.20     
P50 TPOT (ms):                           57.20     
P90 TPOT (ms):                           66.56     
P95 TPOT (ms):                           69.62     
P99 TPOT (ms):                           76.98     
---------------Inter-token Latency----------------
Mean ITL (ms):                           57.40     
Median ITL (ms):                         48.21     
P50 ITL (ms):                            48.21     
P90 ITL (ms):                            50.46     
P95 ITL (ms):                            51.23     
P99 ITL (ms):                            504.32    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          28836.60  
Median E2EL (ms):                        28109.40  
P50 E2EL (ms):                           28109.40  
P90 E2EL (ms):                           48800.28  
P95 E2EL (ms):                           54195.11  
P99 E2EL (ms):                           57904.89  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

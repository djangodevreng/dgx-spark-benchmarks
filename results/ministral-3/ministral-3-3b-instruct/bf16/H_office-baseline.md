# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 16:01:05
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  676.87    
Total input tokens:                      813236    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         143.44    
Peak output token throughput (tok/s):    367.00    
Peak concurrent requests:                11.00     
Total token throughput (tok/s):          1344.91   
---------------Time to First Token----------------
Mean TTFT (ms):                          438.76    
Median TTFT (ms):                        406.50    
P50 TTFT (ms):                           406.50    
P90 TTFT (ms):                           727.04    
P95 TTFT (ms):                           848.75    
P99 TTFT (ms):                           1304.26   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          24.93     
Median TPOT (ms):                        24.66     
P50 TPOT (ms):                           24.66     
P90 TPOT (ms):                           29.50     
P95 TPOT (ms):                           30.58     
P99 TPOT (ms):                           33.74     
---------------Inter-token Latency----------------
Mean ITL (ms):                           24.88     
Median ITL (ms):                         22.58     
P50 ITL (ms):                            22.58     
P90 ITL (ms):                            26.53     
P95 ITL (ms):                            28.19     
P99 ITL (ms):                            49.78     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          12519.12  
Median E2EL (ms):                        12292.23  
P50 E2EL (ms):                           12292.23  
P90 E2EL (ms):                           21927.84  
P95 E2EL (ms):                           23649.14  
P99 E2EL (ms):                           27666.91  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

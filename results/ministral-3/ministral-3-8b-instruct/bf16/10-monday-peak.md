# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-07 04:53:43
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  724.56    
Total input tokens:                      1198815   
Total generated tokens:                  150317    
Request throughput (req/s):              0.41      
Output token throughput (tok/s):         207.46    
Peak output token throughput (tok/s):    375.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1862.01   
---------------Time to First Token----------------
Mean TTFT (ms):                          1334.40   
Median TTFT (ms):                        1219.37   
P50 TTFT (ms):                           1219.37   
P90 TTFT (ms):                           1974.09   
P95 TTFT (ms):                           2445.41   
P99 TTFT (ms):                           4338.82   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          114.52    
Median TPOT (ms):                        115.80    
P50 TPOT (ms):                           115.80    
P90 TPOT (ms):                           127.64    
P95 TPOT (ms):                           131.51    
P99 TPOT (ms):                           150.61    
---------------Inter-token Latency----------------
Mean ITL (ms):                           113.25    
Median ITL (ms):                         74.03     
P50 ITL (ms):                            74.03     
P90 ITL (ms):                            81.81     
P95 ITL (ms):                            501.66    
P99 ITL (ms):                            864.83    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          58079.29  
Median E2EL (ms):                        56937.13  
P50 E2EL (ms):                           56937.13  
P90 E2EL (ms):                           103310.29 
P95 E2EL (ms):                           106877.99 
P99 E2EL (ms):                           113469.58 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

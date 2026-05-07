# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-07 18:49:11
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  615.06    
Total input tokens:                      1198815   
Total generated tokens:                  150317    
Request throughput (req/s):              0.49      
Output token throughput (tok/s):         244.39    
Peak output token throughput (tok/s):    375.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2193.49   
---------------Time to First Token----------------
Mean TTFT (ms):                          909.29    
Median TTFT (ms):                        763.80    
P50 TTFT (ms):                           763.80    
P90 TTFT (ms):                           1294.05   
P95 TTFT (ms):                           1862.65   
P99 TTFT (ms):                           4050.15   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          96.72     
Median TPOT (ms):                        97.44     
P50 TPOT (ms):                           97.44     
P90 TPOT (ms):                           103.99    
P95 TPOT (ms):                           108.93    
P99 TPOT (ms):                           128.09    
---------------Inter-token Latency----------------
Mean ITL (ms):                           95.70     
Median ITL (ms):                         74.51     
P50 ITL (ms):                            74.51     
P90 ITL (ms):                            86.66     
P95 ITL (ms):                            128.42    
P99 ITL (ms):                            792.87    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          48859.05  
Median E2EL (ms):                        47615.55  
P50 E2EL (ms):                           47615.55  
P90 E2EL (ms):                           86819.63  
P95 E2EL (ms):                           90607.55  
P99 E2EL (ms):                           94289.76  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

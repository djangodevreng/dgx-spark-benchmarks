# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-16 14:28:22
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1216.87   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         123.53    
Peak output token throughput (tok/s):    192.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1111.38   
---------------Time to First Token----------------
Mean TTFT (ms):                          1521.15   
Median TTFT (ms):                        1245.58   
P50 TTFT (ms):                           1245.58   
P90 TTFT (ms):                           2193.67   
P95 TTFT (ms):                           3216.96   
P99 TTFT (ms):                           7778.11   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          195.28    
Median TPOT (ms):                        196.89    
P50 TPOT (ms):                           196.89    
P90 TPOT (ms):                           205.91    
P95 TPOT (ms):                           212.63    
P99 TPOT (ms):                           236.24    
---------------Inter-token Latency----------------
Mean ITL (ms):                           192.58    
Median ITL (ms):                         165.69    
P50 ITL (ms):                            165.69    
P90 ITL (ms):                            172.43    
P95 ITL (ms):                            183.13    
P99 ITL (ms):                            1253.55   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          98016.19  
Median E2EL (ms):                        97410.01  
P50 E2EL (ms):                           97410.01  
P90 E2EL (ms):                           175236.03 
P95 E2EL (ms):                           181692.70 
P99 E2EL (ms):                           190596.89 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

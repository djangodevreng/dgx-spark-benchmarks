# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-06 15:03:56
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  534.47    
Total input tokens:                      1200884   
Total generated tokens:                  150317    
Request throughput (req/s):              0.56      
Output token throughput (tok/s):         281.25    
Peak output token throughput (tok/s):    450.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2528.13   
---------------Time to First Token----------------
Mean TTFT (ms):                          947.90    
Median TTFT (ms):                        784.32    
P50 TTFT (ms):                           784.32    
P90 TTFT (ms):                           1411.72   
P95 TTFT (ms):                           1841.40   
P99 TTFT (ms):                           5006.69   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          83.69     
Median TPOT (ms):                        83.49     
P50 TPOT (ms):                           83.49     
P90 TPOT (ms):                           90.78     
P95 TPOT (ms):                           95.84     
P99 TPOT (ms):                           123.72    
---------------Inter-token Latency----------------
Mean ITL (ms):                           82.43     
Median ITL (ms):                         58.40     
P50 ITL (ms):                            58.40     
P90 ITL (ms):                            62.06     
P95 ITL (ms):                            69.47     
P99 ITL (ms):                            903.59    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          42252.36  
Median E2EL (ms):                        41093.01  
P50 E2EL (ms):                           41093.01  
P90 E2EL (ms):                           75247.83  
P95 E2EL (ms):                           77914.60  
P99 E2EL (ms):                           82053.04  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

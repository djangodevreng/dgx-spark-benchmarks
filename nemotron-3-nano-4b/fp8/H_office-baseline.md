# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 18:23:42
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  679.83    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         142.82    
Peak output token throughput (tok/s):    354.00    
Peak concurrent requests:                12.00     
Total token throughput (tok/s):          1343.02   
---------------Time to First Token----------------
Mean TTFT (ms):                          574.79    
Median TTFT (ms):                        534.03    
P50 TTFT (ms):                           534.03    
P90 TTFT (ms):                           958.40    
P95 TTFT (ms):                           1100.66   
P99 TTFT (ms):                           1370.83   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          29.12     
Median TPOT (ms):                        28.99     
P50 TPOT (ms):                           28.99     
P90 TPOT (ms):                           32.96     
P95 TPOT (ms):                           35.09     
P99 TPOT (ms):                           39.45     
---------------Inter-token Latency----------------
Mean ITL (ms):                           29.02     
Median ITL (ms):                         26.02     
P50 ITL (ms):                            26.02     
P90 ITL (ms):                            29.55     
P95 ITL (ms):                            30.98     
P99 ITL (ms):                            175.87    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          14664.49  
Median E2EL (ms):                        14431.60  
P50 E2EL (ms):                           14431.60  
P90 E2EL (ms):                           25260.90  
P95 E2EL (ms):                           27419.04  
P99 E2EL (ms):                           30815.65  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

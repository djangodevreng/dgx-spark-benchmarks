# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 14:40:35
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  699.43    
Total input tokens:                      814599    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.82    
Peak output token throughput (tok/s):    304.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1303.47   
---------------Time to First Token----------------
Mean TTFT (ms):                          941.56    
Median TTFT (ms):                        845.99    
P50 TTFT (ms):                           845.99    
P90 TTFT (ms):                           1642.31   
P95 TTFT (ms):                           2031.43   
P99 TTFT (ms):                           2611.75   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          58.35     
Median TPOT (ms):                        57.79     
P50 TPOT (ms):                           57.79     
P90 TPOT (ms):                           66.38     
P95 TPOT (ms):                           69.34     
P99 TPOT (ms):                           76.55     
---------------Inter-token Latency----------------
Mean ITL (ms):                           57.99     
Median ITL (ms):                         49.10     
P50 ITL (ms):                            49.10     
P90 ITL (ms):                            51.23     
P95 ITL (ms):                            52.17     
P99 ITL (ms):                            476.94    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          29092.22  
Median E2EL (ms):                        28436.44  
P50 E2EL (ms):                           28436.44  
P90 E2EL (ms):                           49021.21  
P95 E2EL (ms):                           54428.99  
P99 E2EL (ms):                           57961.73  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

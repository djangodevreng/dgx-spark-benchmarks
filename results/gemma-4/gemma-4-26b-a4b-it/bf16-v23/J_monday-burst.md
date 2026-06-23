# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-06-23 01:30:25
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1138.42   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         132.04    
Peak output token throughput (tok/s):    207.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1187.96   
---------------Time to First Token----------------
Mean TTFT (ms):                          1397.24   
Median TTFT (ms):                        1177.63   
P50 TTFT (ms):                           1177.63   
P90 TTFT (ms):                           1911.04   
P95 TTFT (ms):                           3006.73   
P99 TTFT (ms):                           6518.19   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          183.04    
Median TPOT (ms):                        184.45    
P50 TPOT (ms):                           184.45    
P90 TPOT (ms):                           194.08    
P95 TPOT (ms):                           199.23    
P99 TPOT (ms):                           223.50    
---------------Inter-token Latency----------------
Mean ITL (ms):                           180.40    
Median ITL (ms):                         155.39    
P50 ITL (ms):                            155.39    
P90 ITL (ms):                            162.42    
P95 ITL (ms):                            165.83    
P99 ITL (ms):                            1176.19   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          91788.31  
Median E2EL (ms):                        90682.96  
P50 E2EL (ms):                           90682.96  
P90 E2EL (ms):                           164807.92 
P95 E2EL (ms):                           170966.54 
P99 E2EL (ms):                           180276.48 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

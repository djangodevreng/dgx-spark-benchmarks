# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-06 13:04:33
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  294.98    
Total input tokens:                      1200884   
Total generated tokens:                  150317    
Request throughput (req/s):              1.02      
Output token throughput (tok/s):         509.58    
Peak output token throughput (tok/s):    825.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          4580.61   
---------------Time to First Token----------------
Mean TTFT (ms):                          517.68    
Median TTFT (ms):                        464.54    
P50 TTFT (ms):                           464.54    
P90 TTFT (ms):                           823.45    
P95 TTFT (ms):                           1073.83   
P99 TTFT (ms):                           1672.89   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          45.37     
Median TPOT (ms):                        45.66     
P50 TPOT (ms):                           45.66     
P90 TPOT (ms):                           49.55     
P95 TPOT (ms):                           52.01     
P99 TPOT (ms):                           58.94     
---------------Inter-token Latency----------------
Mean ITL (ms):                           44.91     
Median ITL (ms):                         31.52     
P50 ITL (ms):                            31.52     
P90 ITL (ms):                            34.37     
P95 ITL (ms):                            42.72     
P99 ITL (ms):                            519.60    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          23019.85  
Median E2EL (ms):                        22500.49  
P50 E2EL (ms):                           22500.49  
P90 E2EL (ms):                           41136.33  
P95 E2EL (ms):                           42697.92  
P99 E2EL (ms):                           44835.94  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

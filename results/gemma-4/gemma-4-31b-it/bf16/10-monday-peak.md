# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-06 22:44:11
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3738.00   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         40.21     
Peak output token throughput (tok/s):    77.00     
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          361.80    
---------------Time to First Token----------------
Mean TTFT (ms):                          9225.60   
Median TTFT (ms):                        5630.36   
P50 TTFT (ms):                           5630.36   
P90 TTFT (ms):                           10394.60  
P95 TTFT (ms):                           35393.25  
P99 TTFT (ms):                           85940.00  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          591.64    
Median TPOT (ms):                        591.37    
P50 TPOT (ms):                           591.37    
P90 TPOT (ms):                           638.16    
P95 TPOT (ms):                           677.65    
P99 TPOT (ms):                           827.38    
---------------Inter-token Latency----------------
Mean ITL (ms):                           582.67    
Median ITL (ms):                         416.41    
P50 ITL (ms):                            416.41    
P90 ITL (ms):                            422.78    
P95 ITL (ms):                            429.01    
P99 ITL (ms):                            6304.90   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          301175.25 
Median E2EL (ms):                        292448.05 
P50 E2EL (ms):                           292448.05 
P90 E2EL (ms):                           530039.35 
P95 E2EL (ms):                           554412.95 
P99 E2EL (ms):                           601429.96 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

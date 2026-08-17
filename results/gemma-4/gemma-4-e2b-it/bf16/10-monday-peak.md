# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-17 06:55:24
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  302.40    
Total input tokens:                      1200884   
Total generated tokens:                  150317    
Request throughput (req/s):              0.99      
Output token throughput (tok/s):         497.08    
Peak output token throughput (tok/s):    825.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          4468.21   
---------------Time to First Token----------------
Mean TTFT (ms):                          578.93    
Median TTFT (ms):                        504.38    
P50 TTFT (ms):                           504.38    
P90 TTFT (ms):                           941.30    
P95 TTFT (ms):                           1230.50   
P99 TTFT (ms):                           2328.63   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          46.52     
Median TPOT (ms):                        46.88     
P50 TPOT (ms):                           46.88     
P90 TPOT (ms):                           51.20     
P95 TPOT (ms):                           54.21     
P99 TPOT (ms):                           61.58     
---------------Inter-token Latency----------------
Mean ITL (ms):                           46.06     
Median ITL (ms):                         30.98     
P50 ITL (ms):                            30.98     
P90 ITL (ms):                            32.86     
P95 ITL (ms):                            42.02     
P99 ITL (ms):                            578.58    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          23658.19  
Median E2EL (ms):                        23047.89  
P50 E2EL (ms):                           23047.89  
P90 E2EL (ms):                           42264.09  
P95 E2EL (ms):                           43954.13  
P99 E2EL (ms):                           46553.04  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

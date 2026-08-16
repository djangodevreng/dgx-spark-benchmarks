# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-15 01:54:59
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3045.84   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         49.35     
Peak output token throughput (tok/s):    151.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          443.72    
---------------Time to First Token----------------
Mean TTFT (ms):                          14734.12  
Median TTFT (ms):                        8868.77   
P50 TTFT (ms):                           8868.77   
P90 TTFT (ms):                           17305.10  
P95 TTFT (ms):                           55465.14  
P99 TTFT (ms):                           145945.06 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          479.61    
Median TPOT (ms):                        476.74    
P50 TPOT (ms):                           476.74    
P90 TPOT (ms):                           560.94    
P95 TPOT (ms):                           617.90    
P99 TPOT (ms):                           827.70    
---------------Inter-token Latency----------------
Mean ITL (ms):                           467.31    
Median ITL (ms):                         178.62    
P50 ITL (ms):                            178.62    
P90 ITL (ms):                            1709.36   
P95 ITL (ms):                            3000.54   
P99 ITL (ms):                            3415.49   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          248686.13 
Median E2EL (ms):                        233945.03 
P50 E2EL (ms):                           233945.03 
P90 E2EL (ms):                           439282.67 
P95 E2EL (ms):                           462953.05 
P99 E2EL (ms):                           533574.59 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-16 06:23:21
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B-FP8 --tokenizer Qwen/Qwen3.8-27B-FP8 --served-model-name qwen3.8-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3052.62   
Total input tokens:                      1213770   
Total generated tokens:                  150317    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         49.24     
Peak output token throughput (tok/s):    151.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          446.86    
---------------Time to First Token----------------
Mean TTFT (ms):                          14826.71  
Median TTFT (ms):                        8814.30   
P50 TTFT (ms):                           8814.30   
P90 TTFT (ms):                           18253.81  
P95 TTFT (ms):                           55083.13  
P99 TTFT (ms):                           145158.18 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          480.35    
Median TPOT (ms):                        477.65    
P50 TPOT (ms):                           477.65    
P90 TPOT (ms):                           561.45    
P95 TPOT (ms):                           620.28    
P99 TPOT (ms):                           831.84    
---------------Inter-token Latency----------------
Mean ITL (ms):                           468.39    
Median ITL (ms):                         178.46    
P50 ITL (ms):                            178.46    
P90 ITL (ms):                            1705.72   
P95 ITL (ms):                            3005.81   
P99 ITL (ms):                            3393.28   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          249234.66 
Median E2EL (ms):                        231434.61 
P50 E2EL (ms):                           231434.61 
P90 E2EL (ms):                           440451.10 
P95 E2EL (ms):                           463910.30 
P99 E2EL (ms):                           534855.99 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

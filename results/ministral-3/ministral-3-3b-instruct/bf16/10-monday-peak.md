# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-09 01:47:32
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  598.88    
Total input tokens:                      1198815   
Total generated tokens:                  150317    
Request throughput (req/s):              0.50      
Output token throughput (tok/s):         251.00    
Peak output token throughput (tok/s):    401.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2252.76   
---------------Time to First Token----------------
Mean TTFT (ms):                          851.22    
Median TTFT (ms):                        803.42    
P50 TTFT (ms):                           803.42    
P90 TTFT (ms):                           1229.55   
P95 TTFT (ms):                           1340.04   
P99 TTFT (ms):                           1792.47   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          94.92     
Median TPOT (ms):                        97.04     
P50 TPOT (ms):                           97.04     
P90 TPOT (ms):                           101.78    
P95 TPOT (ms):                           106.25    
P99 TPOT (ms):                           113.46    
---------------Inter-token Latency----------------
Mean ITL (ms):                           94.07     
Median ITL (ms):                         70.72     
P50 ITL (ms):                            70.72     
P90 ITL (ms):                            78.53     
P95 ITL (ms):                            291.19    
P99 ITL (ms):                            544.18    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          47987.42  
Median E2EL (ms):                        46479.36  
P50 E2EL (ms):                           46479.36  
P90 E2EL (ms):                           86714.60  
P95 E2EL (ms):                           90163.41  
P99 E2EL (ms):                           94177.94  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

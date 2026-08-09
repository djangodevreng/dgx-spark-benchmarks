# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-09 01:37:23
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  624.58    
Total input tokens:                      55108     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         335.11    
Peak output token throughput (tok/s):    580.00    
Peak concurrent requests:                37.00     
Total token throughput (tok/s):          423.34    
---------------Time to First Token----------------
Mean TTFT (ms):                          424.07    
Median TTFT (ms):                        422.68    
P50 TTFT (ms):                           422.68    
P90 TTFT (ms):                           650.84    
P95 TTFT (ms):                           679.49    
P99 TTFT (ms):                           761.83    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          56.77     
Median TPOT (ms):                        60.92     
P50 TPOT (ms):                           60.92     
P90 TPOT (ms):                           69.08     
P95 TPOT (ms):                           70.26     
P99 TPOT (ms):                           70.89     
---------------Inter-token Latency----------------
Mean ITL (ms):                           58.06     
Median ITL (ms):                         59.48     
P50 ITL (ms):                            59.48     
P90 ITL (ms):                            72.00     
P95 ITL (ms):                            75.32     
P99 ITL (ms):                            86.62     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          243472.61 
Median E2EL (ms):                        237499.26 
P50 E2EL (ms):                           237499.26 
P90 E2EL (ms):                           399393.56 
P95 E2EL (ms):                           425904.32 
P99 E2EL (ms):                           453997.17 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

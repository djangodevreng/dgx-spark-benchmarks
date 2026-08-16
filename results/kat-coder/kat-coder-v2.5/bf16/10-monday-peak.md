# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-13 18:56:27
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Kwaipilot/KAT-Coder-V2.5-Dev --tokenizer Kwaipilot/KAT-Coder-V2.5-Dev --served-model-name kat-coder-v2-5-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1340.15   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.22      
Output token throughput (tok/s):         112.16    
Peak output token throughput (tok/s):    175.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1008.46   
---------------Time to First Token----------------
Mean TTFT (ms):                          1691.98   
Median TTFT (ms):                        1366.45   
P50 TTFT (ms):                           1366.45   
P90 TTFT (ms):                           2424.00   
P95 TTFT (ms):                           3974.68   
P99 TTFT (ms):                           8934.38   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          214.54    
Median TPOT (ms):                        215.93    
P50 TPOT (ms):                           215.93    
P90 TPOT (ms):                           225.81    
P95 TPOT (ms):                           232.90    
P99 TPOT (ms):                           243.11    
---------------Inter-token Latency----------------
Mean ITL (ms):                           212.06    
Median ITL (ms):                         184.14    
P50 ITL (ms):                            184.14    
P90 ITL (ms):                            204.19    
P95 ITL (ms):                            498.12    
P99 ITL (ms):                            801.21    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          107947.95 
Median E2EL (ms):                        106410.66 
P50 E2EL (ms):                           106410.66 
P90 E2EL (ms):                           192567.26 
P95 E2EL (ms):                           199585.98 
P99 E2EL (ms):                           206859.41 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

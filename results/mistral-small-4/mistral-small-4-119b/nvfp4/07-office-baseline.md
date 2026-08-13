# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-13 11:30:48
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Mistral-Small-4-119B-2603-NVFP4 --tokenizer mistralai/Mistral-Small-4-119B-2603-NVFP4 --served-model-name mistral-small-4-119b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  805.51    
Total input tokens:                      815636    
Total generated tokens:                  97092     
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         120.53    
Peak output token throughput (tok/s):    217.00    
Peak concurrent requests:                55.00     
Total token throughput (tok/s):          1133.10   
---------------Time to First Token----------------
Mean TTFT (ms):                          2205.82   
Median TTFT (ms):                        1984.18   
P50 TTFT (ms):                           1984.18   
P90 TTFT (ms):                           3610.91   
P95 TTFT (ms):                           4219.62   
P99 TTFT (ms):                           5346.73   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          311.67    
Median TPOT (ms):                        326.75    
P50 TPOT (ms):                           326.75    
P90 TPOT (ms):                           353.46    
P95 TPOT (ms):                           369.04    
P99 TPOT (ms):                           376.25    
---------------Inter-token Latency----------------
Mean ITL (ms):                           305.35    
Median ITL (ms):                         258.94    
P50 ITL (ms):                            258.94    
P90 ITL (ms):                            456.11    
P95 ITL (ms):                            767.49    
P99 ITL (ms):                            1297.03   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          150442.14 
Median E2EL (ms):                        151856.58 
P50 E2EL (ms):                           151856.58 
P90 E2EL (ms):                           261804.76 
P95 E2EL (ms):                           278171.76 
P99 E2EL (ms):                           308844.27 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-13 12:35:41
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Mistral-Small-4-119B-2603-NVFP4 --tokenizer mistralai/Mistral-Small-4-119B-2603-NVFP4 --served-model-name mistral-small-4-119b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1421.99   
Total input tokens:                      1202415   
Total generated tokens:                  150317    
Request throughput (req/s):              0.21      
Output token throughput (tok/s):         105.71    
Peak output token throughput (tok/s):    151.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          951.30    
---------------Time to First Token----------------
Mean TTFT (ms):                          2032.58   
Median TTFT (ms):                        1548.51   
P50 TTFT (ms):                           1548.51   
P90 TTFT (ms):                           2493.41   
P95 TTFT (ms):                           5651.16   
P99 TTFT (ms):                           12199.84  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          227.94    
Median TPOT (ms):                        229.69    
P50 TPOT (ms):                           229.69    
P90 TPOT (ms):                           239.73    
P95 TPOT (ms):                           249.07    
P99 TPOT (ms):                           272.49    
---------------Inter-token Latency----------------
Mean ITL (ms):                           225.03    
Median ITL (ms):                         190.03    
P50 ITL (ms):                            190.03    
P90 ITL (ms):                            200.34    
P95 ITL (ms):                            543.32    
P99 ITL (ms):                            1009.34   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          114787.71 
Median E2EL (ms):                        113446.60 
P50 E2EL (ms):                           113446.60 
P90 E2EL (ms):                           203410.78 
P95 E2EL (ms):                           211714.92 
P99 E2EL (ms):                           222903.96 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

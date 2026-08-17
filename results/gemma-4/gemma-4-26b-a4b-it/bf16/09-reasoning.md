# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-16 14:07:52
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1134.75   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         184.45    
Peak output token throughput (tok/s):    294.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          233.52    
---------------Time to First Token----------------
Mean TTFT (ms):                          589.45    
Median TTFT (ms):                        601.74    
P50 TTFT (ms):                           601.74    
P90 TTFT (ms):                           755.19    
P95 TTFT (ms):                           784.19    
P99 TTFT (ms):                           871.84    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          150.80    
Median TPOT (ms):                        150.81    
P50 TPOT (ms):                           150.81    
P90 TPOT (ms):                           164.80    
P95 TPOT (ms):                           167.84    
P99 TPOT (ms):                           171.72    
---------------Inter-token Latency----------------
Mean ITL (ms):                           147.53    
Median ITL (ms):                         149.87    
P50 ITL (ms):                            149.87    
P90 ITL (ms):                            174.20    
P95 ITL (ms):                            176.90    
P99 ITL (ms):                            184.90    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          618158.72 
Median E2EL (ms):                        617338.29 
P50 E2EL (ms):                           617338.29 
P90 E2EL (ms):                           913321.50 
P95 E2EL (ms):                           984681.84 
P99 E2EL (ms):                           1017991.01
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

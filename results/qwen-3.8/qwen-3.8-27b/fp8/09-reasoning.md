# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-16 05:32:16
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B-FP8 --tokenizer Qwen/Qwen3.8-27B-FP8 --served-model-name qwen3.8-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1522.47   
Total input tokens:                      57622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         137.48    
Peak output token throughput (tok/s):    245.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          175.32    
---------------Time to First Token----------------
Mean TTFT (ms):                          3416.02   
Median TTFT (ms):                        3069.14   
P50 TTFT (ms):                           3069.14   
P90 TTFT (ms):                           5428.67   
P95 TTFT (ms):                           6486.25   
P99 TTFT (ms):                           8334.73   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          212.05    
Median TPOT (ms):                        213.32    
P50 TPOT (ms):                           213.32    
P90 TPOT (ms):                           236.25    
P95 TPOT (ms):                           243.04    
P99 TPOT (ms):                           256.44    
---------------Inter-token Latency----------------
Mean ITL (ms):                           204.22    
Median ITL (ms):                         203.01    
P50 ITL (ms):                            203.01    
P90 ITL (ms):                            216.12    
P95 ITL (ms):                            217.70    
P99 ITL (ms):                            224.33    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          858020.30 
Median E2EL (ms):                        845969.19 
P50 E2EL (ms):                           845969.19 
P90 E2EL (ms):                           1254962.89
P95 E2EL (ms):                           1365229.04
P99 E2EL (ms):                           1412105.91
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

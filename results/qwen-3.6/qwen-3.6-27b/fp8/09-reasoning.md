# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-15 01:04:01
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1520.84   
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         137.62    
Peak output token throughput (tok/s):    245.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          174.13    
---------------Time to First Token----------------
Mean TTFT (ms):                          3300.51   
Median TTFT (ms):                        2946.81   
P50 TTFT (ms):                           2946.81   
P90 TTFT (ms):                           5258.38   
P95 TTFT (ms):                           5988.99   
P99 TTFT (ms):                           8211.35   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          211.51    
Median TPOT (ms):                        213.10    
P50 TPOT (ms):                           213.10    
P90 TPOT (ms):                           235.17    
P95 TPOT (ms):                           241.60    
P99 TPOT (ms):                           254.04    
---------------Inter-token Latency----------------
Mean ITL (ms):                           203.86    
Median ITL (ms):                         202.83    
P50 ITL (ms):                            202.83    
P90 ITL (ms):                            216.19    
P95 ITL (ms):                            217.86    
P99 ITL (ms):                            226.24    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          856298.37 
Median E2EL (ms):                        843292.72 
P50 E2EL (ms):                           843292.72 
P90 E2EL (ms):                           1254050.49
P95 E2EL (ms):                           1363708.24
P99 E2EL (ms):                           1410265.71
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

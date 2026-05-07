# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-04 22:31:36
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  836.40    
Total input tokens:                      57229     
Total generated tokens:                  52873     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         63.21     
Peak output token throughput (tok/s):    162.00    
Peak concurrent requests:                12.00     
Total token throughput (tok/s):          131.64    
---------------Time to First Token----------------
Mean TTFT (ms):                          252.28    
Median TTFT (ms):                        204.70    
P50 TTFT (ms):                           204.70    
P90 TTFT (ms):                           336.86    
P95 TTFT (ms):                           445.84    
P99 TTFT (ms):                           1162.23   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          37.74     
Median TPOT (ms):                        35.31     
P50 TPOT (ms):                           35.31     
P90 TPOT (ms):                           53.75     
P95 TPOT (ms):                           62.93     
P99 TPOT (ms):                           72.53     
---------------Inter-token Latency----------------
Mean ITL (ms):                           36.64     
Median ITL (ms):                         33.15     
P50 ITL (ms):                            33.15     
P90 ITL (ms):                            52.19     
P95 ITL (ms):                            61.16     
P99 ITL (ms):                            98.42     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7996.63   
Median E2EL (ms):                        4668.46   
P50 E2EL (ms):                           4668.46   
P90 E2EL (ms):                           19254.14  
P95 E2EL (ms):                           24436.60  
P99 E2EL (ms):                           33441.69  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

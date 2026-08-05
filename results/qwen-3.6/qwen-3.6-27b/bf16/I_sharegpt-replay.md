# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-10 01:10:10
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  957.29    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         55.25     
Peak output token throughput (tok/s):    113.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          115.03    
---------------Time to First Token----------------
Mean TTFT (ms):                          958.20    
Median TTFT (ms):                        931.66    
P50 TTFT (ms):                           931.66    
P90 TTFT (ms):                           1265.23   
P95 TTFT (ms):                           1366.12   
P99 TTFT (ms):                           1548.18   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          280.64    
Median TPOT (ms):                        281.43    
P50 TPOT (ms):                           281.43    
P90 TPOT (ms):                           299.27    
P95 TPOT (ms):                           306.25    
P99 TPOT (ms):                           330.59    
---------------Inter-token Latency----------------
Mean ITL (ms):                           278.89    
Median ITL (ms):                         268.85    
P50 ITL (ms):                            268.85    
P90 ITL (ms):                            290.68    
P95 ITL (ms):                            413.59    
P99 ITL (ms):                            549.72    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          59948.67  
Median E2EL (ms):                        39891.49  
P50 E2EL (ms):                           39891.49  
P90 E2EL (ms):                           142701.71 
P95 E2EL (ms):                           184135.87 
P99 E2EL (ms):                           235088.37 
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

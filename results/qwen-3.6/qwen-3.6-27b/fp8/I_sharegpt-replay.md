# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-04 16:48:47
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  892.26    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         59.28     
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                18.00     
Total token throughput (tok/s):          123.42    
---------------Time to First Token----------------
Mean TTFT (ms):                          552.80    
Median TTFT (ms):                        510.92    
P50 TTFT (ms):                           510.92    
P90 TTFT (ms):                           785.45    
P95 TTFT (ms):                           894.12    
P99 TTFT (ms):                           1168.44   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          144.97    
Median TPOT (ms):                        144.45    
P50 TPOT (ms):                           144.45    
P90 TPOT (ms):                           152.50    
P95 TPOT (ms):                           157.15    
P99 TPOT (ms):                           173.48    
---------------Inter-token Latency----------------
Mean ITL (ms):                           143.60    
Median ITL (ms):                         138.56    
P50 ITL (ms):                            138.56    
P90 ITL (ms):                            150.35    
P95 ITL (ms):                            174.54    
P99 ITL (ms):                            319.02    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          30925.99  
Median E2EL (ms):                        20368.31  
P50 E2EL (ms):                           20368.31  
P90 E2EL (ms):                           73224.00  
P95 E2EL (ms):                           93806.65  
P99 E2EL (ms):                           121874.69 
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

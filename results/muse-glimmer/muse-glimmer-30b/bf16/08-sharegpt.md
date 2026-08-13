# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-12 10:37:11
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  971.80    
Total input tokens:                      67099     
Total generated tokens:                  50104     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         51.56     
Peak output token throughput (tok/s):    96.00     
Peak concurrent requests:                26.00     
Total token throughput (tok/s):          120.60    
---------------Time to First Token----------------
Mean TTFT (ms):                          803.37    
Median TTFT (ms):                        762.76    
P50 TTFT (ms):                           762.76    
P90 TTFT (ms):                           1064.30   
P95 TTFT (ms):                           1127.51   
P99 TTFT (ms):                           1461.22   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          252.30    
Median TPOT (ms):                        252.54    
P50 TPOT (ms):                           252.54    
P90 TPOT (ms):                           261.54    
P95 TPOT (ms):                           268.81    
P99 TPOT (ms):                           296.77    
---------------Inter-token Latency----------------
Mean ITL (ms):                           259.15    
Median ITL (ms):                         245.90    
P50 ITL (ms):                            245.90    
P90 ITL (ms):                            265.90    
P95 ITL (ms):                            331.23    
P99 ITL (ms):                            599.61    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          51061.00  
Median E2EL (ms):                        33472.09  
P50 E2EL (ms):                           33472.09  
P90 E2EL (ms):                           121738.98 
P95 E2EL (ms):                           156322.09 
P99 E2EL (ms):                           199205.34 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

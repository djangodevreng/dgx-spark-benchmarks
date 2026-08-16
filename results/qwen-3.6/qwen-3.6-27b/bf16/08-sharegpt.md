# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 03:33:51
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  956.32    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         55.31     
Peak output token throughput (tok/s):    118.00    
Peak concurrent requests:                34.00     
Total token throughput (tok/s):          115.15    
---------------Time to First Token----------------
Mean TTFT (ms):                          1026.13   
Median TTFT (ms):                        988.98    
P50 TTFT (ms):                           988.98    
P90 TTFT (ms):                           1394.91   
P95 TTFT (ms):                           1510.46   
P99 TTFT (ms):                           1649.74   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          326.45    
Median TPOT (ms):                        338.13    
P50 TPOT (ms):                           338.13    
P90 TPOT (ms):                           352.29    
P95 TPOT (ms):                           360.89    
P99 TPOT (ms):                           389.09    
---------------Inter-token Latency----------------
Mean ITL (ms):                           325.49    
Median ITL (ms):                         328.55    
P50 ITL (ms):                            328.55    
P90 ITL (ms):                            364.99    
P95 ITL (ms):                            415.16    
P99 ITL (ms):                            659.19    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          69871.65  
Median E2EL (ms):                        44099.86  
P50 E2EL (ms):                           44099.86  
P90 E2EL (ms):                           170232.21 
P95 E2EL (ms):                           218517.85 
P99 E2EL (ms):                           279929.42 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

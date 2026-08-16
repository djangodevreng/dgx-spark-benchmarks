# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 05:06:45
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B-FP8 --tokenizer Qwen/Qwen3.8-27B-FP8 --served-model-name qwen3.8-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  894.18    
Total input tokens:                      67729     
Total generated tokens:                  51856     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         57.99     
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                19.00     
Total token throughput (tok/s):          133.74    
---------------Time to First Token----------------
Mean TTFT (ms):                          1021.10   
Median TTFT (ms):                        907.94    
P50 TTFT (ms):                           907.94    
P90 TTFT (ms):                           1762.60   
P95 TTFT (ms):                           2095.59   
P99 TTFT (ms):                           2632.11   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          158.71    
Median TPOT (ms):                        157.19    
P50 TPOT (ms):                           157.19    
P90 TPOT (ms):                           173.24    
P95 TPOT (ms):                           188.56    
P99 TPOT (ms):                           255.30    
---------------Inter-token Latency----------------
Mean ITL (ms):                           156.69    
Median ITL (ms):                         138.91    
P50 ITL (ms):                            138.91    
P90 ITL (ms):                            151.87    
P95 ITL (ms):                            233.07    
P99 ITL (ms):                            705.25    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          33496.73  
Median E2EL (ms):                        20835.91  
P50 E2EL (ms):                           20835.91  
P90 E2EL (ms):                           80195.12  
P95 E2EL (ms):                           100399.10 
P99 E2EL (ms):                           134804.83 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

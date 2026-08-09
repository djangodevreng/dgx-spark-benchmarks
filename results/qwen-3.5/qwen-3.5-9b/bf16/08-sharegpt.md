# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 22:21:19
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  858.53    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         61.61     
Peak output token throughput (tok/s):    169.00    
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          128.26    
---------------Time to First Token----------------
Mean TTFT (ms):                          268.41    
Median TTFT (ms):                        250.96    
P50 TTFT (ms):                           250.96    
P90 TTFT (ms):                           371.59    
P95 TTFT (ms):                           412.76    
P99 TTFT (ms):                           448.68    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          76.37     
Median TPOT (ms):                        75.73     
P50 TPOT (ms):                           75.73     
P90 TPOT (ms):                           78.29     
P95 TPOT (ms):                           80.21     
P99 TPOT (ms):                           92.06     
---------------Inter-token Latency----------------
Mean ITL (ms):                           75.56     
Median ITL (ms):                         74.45     
P50 ITL (ms):                            74.45     
P90 ITL (ms):                            77.29     
P95 ITL (ms):                            78.75     
P99 ITL (ms):                            109.06    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          16248.35  
Median E2EL (ms):                        10726.82  
P50 E2EL (ms):                           10726.82  
P90 E2EL (ms):                           38349.06  
P95 E2EL (ms):                           49610.17  
P99 E2EL (ms):                           62852.06  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

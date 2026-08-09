# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 14:16:00
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  840.27    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         62.94     
Peak output token throughput (tok/s):    121.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          131.05    
---------------Time to First Token----------------
Mean TTFT (ms):                          401.23    
Median TTFT (ms):                        389.33    
P50 TTFT (ms):                           389.33    
P90 TTFT (ms):                           567.08    
P95 TTFT (ms):                           605.34    
P99 TTFT (ms):                           722.62    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          90.71     
Median TPOT (ms):                        89.06     
P50 TPOT (ms):                           89.06     
P90 TPOT (ms):                           128.86    
P95 TPOT (ms):                           130.59    
P99 TPOT (ms):                           142.77    
---------------Inter-token Latency----------------
Mean ITL (ms):                           90.74     
Median ITL (ms):                         82.24     
P50 ITL (ms):                            82.24     
P90 ITL (ms):                            128.81    
P95 ITL (ms):                            133.03    
P99 ITL (ms):                            229.31    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19592.97  
Median E2EL (ms):                        11041.68  
P50 E2EL (ms):                           11041.68  
P90 E2EL (ms):                           48322.07  
P95 E2EL (ms):                           65325.91  
P99 E2EL (ms):                           85668.55  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 04:29:44
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  856.71    
Total input tokens:                      54988     
Total generated tokens:                  52136     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         60.86     
Peak output token throughput (tok/s):    235.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          125.04    
---------------Time to First Token----------------
Mean TTFT (ms):                          193.43    
Median TTFT (ms):                        136.29    
P50 TTFT (ms):                           136.29    
P90 TTFT (ms):                           461.11    
P95 TTFT (ms):                           509.26    
P99 TTFT (ms):                           607.12    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          39.26     
Median TPOT (ms):                        38.89     
P50 TPOT (ms):                           38.89     
P90 TPOT (ms):                           40.85     
P95 TPOT (ms):                           42.04     
P99 TPOT (ms):                           45.58     
---------------Inter-token Latency----------------
Mean ITL (ms):                           39.10     
Median ITL (ms):                         38.27     
P50 ITL (ms):                            38.27     
P90 ITL (ms):                            39.72     
P95 ITL (ms):                            41.65     
P99 ITL (ms):                            52.53     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          8348.17   
Median E2EL (ms):                        5640.94   
P50 E2EL (ms):                           5640.94   
P90 E2EL (ms):                           19104.78  
P95 E2EL (ms):                           25193.20  
P99 E2EL (ms):                           31958.90  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

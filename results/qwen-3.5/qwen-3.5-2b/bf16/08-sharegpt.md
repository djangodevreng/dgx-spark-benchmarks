# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 15:18:31
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  837.03    
Total input tokens:                      57729     
Total generated tokens:                  51024     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.96     
Peak output token throughput (tok/s):    371.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          129.93    
---------------Time to First Token----------------
Mean TTFT (ms):                          75.33     
Median TTFT (ms):                        73.05     
P50 TTFT (ms):                           73.05     
P90 TTFT (ms):                           106.60    
P95 TTFT (ms):                           115.38    
P99 TTFT (ms):                           178.28    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          19.79     
Median TPOT (ms):                        18.91     
P50 TPOT (ms):                           18.91     
P90 TPOT (ms):                           23.32     
P95 TPOT (ms):                           23.48     
P99 TPOT (ms):                           23.65     
---------------Inter-token Latency----------------
Mean ITL (ms):                           19.57     
Median ITL (ms):                         18.54     
P50 ITL (ms):                            18.54     
P90 ITL (ms):                            23.55     
P95 ITL (ms):                            24.06     
P99 ITL (ms):                            25.54     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4069.74   
Median E2EL (ms):                        2687.85   
P50 E2EL (ms):                           2687.85   
P90 E2EL (ms):                           9665.64   
P95 E2EL (ms):                           13109.16  
P99 E2EL (ms):                           17150.59  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

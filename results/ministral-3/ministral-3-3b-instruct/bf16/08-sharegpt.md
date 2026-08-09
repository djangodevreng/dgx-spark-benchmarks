# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 01:26:48
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  843.82    
Total input tokens:                      54988     
Total generated tokens:                  51982     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.60     
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          126.77    
---------------Time to First Token----------------
Mean TTFT (ms):                          116.82    
Median TTFT (ms):                        68.81     
P50 TTFT (ms):                           68.81     
P90 TTFT (ms):                           386.53    
P95 TTFT (ms):                           417.43    
P99 TTFT (ms):                           460.28    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          18.55     
Median TPOT (ms):                        18.42     
P50 TPOT (ms):                           18.42     
P90 TPOT (ms):                           19.19     
P95 TPOT (ms):                           19.76     
P99 TPOT (ms):                           21.42     
---------------Inter-token Latency----------------
Mean ITL (ms):                           18.48     
Median ITL (ms):                         18.19     
P50 ITL (ms):                            18.19     
P90 ITL (ms):                            19.49     
P95 ITL (ms):                            19.96     
P99 ITL (ms):                            21.95     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          3959.93   
Median E2EL (ms):                        2543.34   
P50 E2EL (ms):                           2543.34   
P90 E2EL (ms):                           9188.74   
P95 E2EL (ms):                           12283.77  
P99 E2EL (ms):                           15620.18  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

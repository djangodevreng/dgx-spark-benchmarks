# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 18:38:36
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  859.87    
Total input tokens:                      54988     
Total generated tokens:                  52313     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         60.84     
Peak output token throughput (tok/s):    215.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          124.79    
---------------Time to First Token----------------
Mean TTFT (ms):                          150.84    
Median TTFT (ms):                        136.64    
P50 TTFT (ms):                           136.64    
P90 TTFT (ms):                           192.03    
P95 TTFT (ms):                           208.95    
P99 TTFT (ms):                           310.60    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          42.78     
Median TPOT (ms):                        42.91     
P50 TPOT (ms):                           42.91     
P90 TPOT (ms):                           44.65     
P95 TPOT (ms):                           45.07     
P99 TPOT (ms):                           46.00     
---------------Inter-token Latency----------------
Mean ITL (ms):                           42.47     
Median ITL (ms):                         43.01     
P50 ITL (ms):                            43.01     
P90 ITL (ms):                            45.01     
P95 ITL (ms):                            45.57     
P99 ITL (ms):                            55.01     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          9038.23   
Median E2EL (ms):                        5881.13   
P50 E2EL (ms):                           5881.13   
P90 E2EL (ms):                           21199.12  
P95 E2EL (ms):                           28133.36  
P99 E2EL (ms):                           34611.48  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 16:15:36
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  843.55    
Total input tokens:                      54988     
Total generated tokens:                  52063     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.72     
Peak output token throughput (tok/s):    330.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          126.91    
---------------Time to First Token----------------
Mean TTFT (ms):                          87.89     
Median TTFT (ms):                        69.04     
P50 TTFT (ms):                           69.04     
P90 TTFT (ms):                           118.27    
P95 TTFT (ms):                           145.73    
P99 TTFT (ms):                           244.50    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          18.57     
Median TPOT (ms):                        18.44     
P50 TPOT (ms):                           18.44     
P90 TPOT (ms):                           19.27     
P95 TPOT (ms):                           19.36     
P99 TPOT (ms):                           19.82     
---------------Inter-token Latency----------------
Mean ITL (ms):                           18.46     
Median ITL (ms):                         18.29     
P50 ITL (ms):                            18.29     
P90 ITL (ms):                            19.47     
P95 ITL (ms):                            19.90     
P99 ITL (ms):                            28.82     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          3932.02   
Median E2EL (ms):                        2558.06   
P50 E2EL (ms):                           2558.06   
P90 E2EL (ms):                           9073.99   
P95 E2EL (ms):                           11953.56  
P99 E2EL (ms):                           15360.68  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-26 08:29:50
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  837.25    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         63.17     
Peak output token throughput (tok/s):    192.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.52    
---------------Time to First Token----------------
Mean TTFT (ms):                          169.19    
Median TTFT (ms):                        159.13    
P50 TTFT (ms):                           159.13    
P90 TTFT (ms):                           235.70    
P95 TTFT (ms):                           265.41    
P99 TTFT (ms):                           343.87    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          32.40     
Median TPOT (ms):                        31.26     
P50 TPOT (ms):                           31.26     
P90 TPOT (ms):                           40.91     
P95 TPOT (ms):                           42.93     
P99 TPOT (ms):                           47.80     
---------------Inter-token Latency----------------
Mean ITL (ms):                           32.01     
Median ITL (ms):                         30.49     
P50 ITL (ms):                            30.49     
P90 ITL (ms):                            41.04     
P95 ITL (ms):                            42.29     
P99 ITL (ms):                            68.42     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          6938.95   
Median E2EL (ms):                        4237.85   
P50 E2EL (ms):                           4237.85   
P90 E2EL (ms):                           16710.08  
P95 E2EL (ms):                           20419.19  
P99 E2EL (ms):                           28493.72  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

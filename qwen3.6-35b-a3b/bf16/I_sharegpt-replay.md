# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 13:37:59
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  840.30    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         62.94     
Peak output token throughput (tok/s):    120.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          131.05    
---------------Time to First Token----------------
Mean TTFT (ms):                          393.58    
Median TTFT (ms):                        390.02    
P50 TTFT (ms):                           390.02    
P90 TTFT (ms):                           544.32    
P95 TTFT (ms):                           584.38    
P99 TTFT (ms):                           770.83    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          92.41     
Median TPOT (ms):                        91.26     
P50 TPOT (ms):                           91.26     
P90 TPOT (ms):                           130.81    
P95 TPOT (ms):                           132.02    
P99 TPOT (ms):                           143.26    
---------------Inter-token Latency----------------
Mean ITL (ms):                           92.37     
Median ITL (ms):                         83.93     
P50 ITL (ms):                            83.93     
P90 ITL (ms):                            129.30    
P95 ITL (ms):                            132.88    
P99 ITL (ms):                            233.74    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19929.12  
Median E2EL (ms):                        11100.17  
P50 E2EL (ms):                           11100.17  
P90 E2EL (ms):                           49152.50  
P95 E2EL (ms):                           67097.58  
P99 E2EL (ms):                           86559.32  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

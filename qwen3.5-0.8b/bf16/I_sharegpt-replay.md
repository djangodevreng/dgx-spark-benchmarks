# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-04 23:41:57
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.76    
Total input tokens:                      57729     
Total generated tokens:                  50187     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.12     
Peak output token throughput (tok/s):    643.00    
Peak concurrent requests:                6.00      
Total token throughput (tok/s):          129.28    
---------------Time to First Token----------------
Mean TTFT (ms):                          49.17     
Median TTFT (ms):                        43.45     
P50 TTFT (ms):                           43.45     
P90 TTFT (ms):                           69.42     
P95 TTFT (ms):                           77.91     
P99 TTFT (ms):                           129.85    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          8.61      
Median TPOT (ms):                        8.63      
P50 TPOT (ms):                           8.63      
P90 TPOT (ms):                           8.98      
P95 TPOT (ms):                           9.17      
P99 TPOT (ms):                           9.54      
---------------Inter-token Latency----------------
Mean ITL (ms):                           8.52      
Median ITL (ms):                         8.55      
P50 ITL (ms):                            8.55      
P90 ITL (ms):                            9.28      
P95 ITL (ms):                            9.60      
P99 ITL (ms):                            17.88     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1758.74   
Median E2EL (ms):                        1197.57   
P50 E2EL (ms):                           1197.57   
P90 E2EL (ms):                           4209.49   
P95 E2EL (ms):                           5565.02   
P99 E2EL (ms):                           6752.29   
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

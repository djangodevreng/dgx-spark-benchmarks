# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 22:36:17
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  840.08    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         62.96     
Peak output token throughput (tok/s):    212.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          131.08    
---------------Time to First Token----------------
Mean TTFT (ms):                          416.35    
Median TTFT (ms):                        267.39    
P50 TTFT (ms):                           267.39    
P90 TTFT (ms):                           980.79    
P95 TTFT (ms):                           1371.82   
P99 TTFT (ms):                           2054.79   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          83.25     
Median TPOT (ms):                        92.13     
P50 TPOT (ms):                           92.13     
P90 TPOT (ms):                           115.45    
P95 TPOT (ms):                           131.04    
P99 TPOT (ms):                           165.76    
---------------Inter-token Latency----------------
Mean ITL (ms):                           85.82     
Median ITL (ms):                         65.88     
P50 ITL (ms):                            65.88     
P90 ITL (ms):                            135.37    
P95 ITL (ms):                            363.33    
P99 ITL (ms):                            390.29    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          18564.83  
Median E2EL (ms):                        9880.58   
P50 E2EL (ms):                           9880.58   
P90 E2EL (ms):                           48596.17  
P95 E2EL (ms):                           62810.20  
P99 E2EL (ms):                           88124.21  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 04:50:55
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --served-model-name nemotron-3-nano-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  843.29    
Total input tokens:                      58416     
Total generated tokens:                  51616     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.21     
Peak output token throughput (tok/s):    112.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          130.48    
---------------Time to First Token----------------
Mean TTFT (ms):                          449.38    
Median TTFT (ms):                        434.87    
P50 TTFT (ms):                           434.87    
P90 TTFT (ms):                           612.14    
P95 TTFT (ms):                           643.88    
P99 TTFT (ms):                           761.67    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          114.70    
Median TPOT (ms):                        122.34    
P50 TPOT (ms):                           122.34    
P90 TPOT (ms):                           152.56    
P95 TPOT (ms):                           156.59    
P99 TPOT (ms):                           168.64    
---------------Inter-token Latency----------------
Mean ITL (ms):                           115.67    
Median ITL (ms):                         127.21    
P50 ITL (ms):                            127.21    
P90 ITL (ms):                            151.96    
P95 ITL (ms):                            159.37    
P99 ITL (ms):                            277.31    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          24330.48  
Median E2EL (ms):                        13805.76  
P50 E2EL (ms):                           13805.76  
P90 E2EL (ms):                           59888.80  
P95 E2EL (ms):                           77489.04  
P99 E2EL (ms):                           102545.69 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

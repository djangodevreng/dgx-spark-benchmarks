# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 01:41:14
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --served-model-name nemotron-3-nano-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.56    
Total input tokens:                      58416     
Total generated tokens:                  51672     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.92     
Peak output token throughput (tok/s):    149.00    
Peak concurrent requests:                12.00     
Total token throughput (tok/s):          131.91    
---------------Time to First Token----------------
Mean TTFT (ms):                          269.99    
Median TTFT (ms):                        217.31    
P50 TTFT (ms):                           217.31    
P90 TTFT (ms):                           541.29    
P95 TTFT (ms):                           607.71    
P99 TTFT (ms):                           922.74    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          41.64     
Median TPOT (ms):                        38.72     
P50 TPOT (ms):                           38.72     
P90 TPOT (ms):                           61.28     
P95 TPOT (ms):                           69.25     
P99 TPOT (ms):                           78.34     
---------------Inter-token Latency----------------
Mean ITL (ms):                           40.52     
Median ITL (ms):                         36.31     
P50 ITL (ms):                            36.31     
P90 ITL (ms):                            56.71     
P95 ITL (ms):                            72.10     
P99 ITL (ms):                            99.80     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          8645.90   
Median E2EL (ms):                        4929.57   
P50 E2EL (ms):                           4929.57   
P90 E2EL (ms):                           21926.07  
P95 E2EL (ms):                           26065.77  
P99 E2EL (ms):                           33269.83  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 13:34:36
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.04    
Total input tokens:                      58416     
Total generated tokens:                  51076     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.24     
Peak output token throughput (tok/s):    223.00    
Peak concurrent requests:                9.00      
Total token throughput (tok/s):          131.28    
---------------Time to First Token----------------
Mean TTFT (ms):                          205.58    
Median TTFT (ms):                        130.00    
P50 TTFT (ms):                           130.00    
P90 TTFT (ms):                           569.98    
P95 TTFT (ms):                           615.53    
P99 TTFT (ms):                           967.82    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          22.52     
Median TPOT (ms):                        20.87     
P50 TPOT (ms):                           20.87     
P90 TPOT (ms):                           32.96     
P95 TPOT (ms):                           34.88     
P99 TPOT (ms):                           40.93     
---------------Inter-token Latency----------------
Mean ITL (ms):                           22.46     
Median ITL (ms):                         18.55     
P50 ITL (ms):                            18.55     
P90 ITL (ms):                            33.44     
P95 ITL (ms):                            34.66     
P99 ITL (ms):                            54.11     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4716.34   
Median E2EL (ms):                        2807.20   
P50 E2EL (ms):                           2807.20   
P90 E2EL (ms):                           11832.63  
P95 E2EL (ms):                           13749.30  
P99 E2EL (ms):                           19256.99  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 13:03:04
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  835.04    
Total input tokens:                      60269     
Total generated tokens:                  51454     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.62     
Peak output token throughput (tok/s):    190.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          133.79    
---------------Time to First Token----------------
Mean TTFT (ms):                          157.26    
Median TTFT (ms):                        153.51    
P50 TTFT (ms):                           153.51    
P90 TTFT (ms):                           214.91    
P95 TTFT (ms):                           231.19    
P99 TTFT (ms):                           257.95    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          38.39     
Median TPOT (ms):                        38.11     
P50 TPOT (ms):                           38.11     
P90 TPOT (ms):                           44.77     
P95 TPOT (ms):                           46.36     
P99 TPOT (ms):                           48.75     
---------------Inter-token Latency----------------
Mean ITL (ms):                           38.19     
Median ITL (ms):                         37.32     
P50 ITL (ms):                            37.32     
P90 ITL (ms):                            44.71     
P95 ITL (ms):                            46.05     
P99 ITL (ms):                            63.71     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          8017.45   
Median E2EL (ms):                        5112.30   
P50 E2EL (ms):                           5112.30   
P90 E2EL (ms):                           19542.36  
P95 E2EL (ms):                           23492.28  
P99 E2EL (ms):                           33090.76  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

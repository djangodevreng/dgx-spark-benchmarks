# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 17:00:17
**Profile:** nvfp4
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
Benchmark duration (s):                  834.96    
Total input tokens:                      60269     
Total generated tokens:                  51076     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.17     
Peak output token throughput (tok/s):    190.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          133.35    
---------------Time to First Token----------------
Mean TTFT (ms):                          152.17    
Median TTFT (ms):                        148.12    
P50 TTFT (ms):                           148.12    
P90 TTFT (ms):                           207.59    
P95 TTFT (ms):                           228.01    
P99 TTFT (ms):                           253.59    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          37.79     
Median TPOT (ms):                        37.29     
P50 TPOT (ms):                           37.29     
P90 TPOT (ms):                           44.39     
P95 TPOT (ms):                           45.68     
P99 TPOT (ms):                           48.39     
---------------Inter-token Latency----------------
Mean ITL (ms):                           37.54     
Median ITL (ms):                         36.71     
P50 ITL (ms):                            36.71     
P90 ITL (ms):                            44.04     
P95 ITL (ms):                            45.43     
P99 ITL (ms):                            63.47     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7822.43   
Median E2EL (ms):                        5046.15   
P50 E2EL (ms):                           5046.15   
P90 E2EL (ms):                           18639.03  
P95 E2EL (ms):                           23095.81  
P99 E2EL (ms):                           32468.33  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

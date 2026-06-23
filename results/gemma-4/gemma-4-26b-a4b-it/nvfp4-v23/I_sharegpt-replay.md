# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 03:08:34
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.90    
Total input tokens:                      60269     
Total generated tokens:                  51758     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.99     
Peak output token throughput (tok/s):    187.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          134.18    
---------------Time to First Token----------------
Mean TTFT (ms):                          150.34    
Median TTFT (ms):                        145.67    
P50 TTFT (ms):                           145.67    
P90 TTFT (ms):                           205.91    
P95 TTFT (ms):                           225.09    
P99 TTFT (ms):                           255.99    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          37.35     
Median TPOT (ms):                        37.16     
P50 TPOT (ms):                           37.16     
P90 TPOT (ms):                           43.53     
P95 TPOT (ms):                           45.30     
P99 TPOT (ms):                           47.73     
---------------Inter-token Latency----------------
Mean ITL (ms):                           37.14     
Median ITL (ms):                         36.35     
P50 ITL (ms):                            36.35     
P90 ITL (ms):                            43.51     
P95 ITL (ms):                            44.75     
P99 ITL (ms):                            62.27     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7838.96   
Median E2EL (ms):                        4998.12   
P50 E2EL (ms):                           4998.12   
P90 E2EL (ms):                           19431.45  
P95 E2EL (ms):                           22895.66  
P99 E2EL (ms):                           32116.04  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

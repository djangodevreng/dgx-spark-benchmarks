# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 11:31:08
**Profile:** nvfp4
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
Benchmark duration (s):                  835.06    
Total input tokens:                      60269     
Total generated tokens:                  51202     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.32     
Peak output token throughput (tok/s):    190.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          133.49    
---------------Time to First Token----------------
Mean TTFT (ms):                          157.59    
Median TTFT (ms):                        151.68    
P50 TTFT (ms):                           151.68    
P90 TTFT (ms):                           215.33    
P95 TTFT (ms):                           234.74    
P99 TTFT (ms):                           265.31    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          38.95     
Median TPOT (ms):                        38.55     
P50 TPOT (ms):                           38.55     
P90 TPOT (ms):                           45.92     
P95 TPOT (ms):                           47.13     
P99 TPOT (ms):                           48.87     
---------------Inter-token Latency----------------
Mean ITL (ms):                           38.69     
Median ITL (ms):                         37.85     
P50 ITL (ms):                            37.85     
P90 ITL (ms):                            45.60     
P95 ITL (ms):                            47.11     
P99 ITL (ms):                            61.71     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          8081.47   
Median E2EL (ms):                        5176.71   
P50 E2EL (ms):                           5176.71   
P90 E2EL (ms):                           19648.10  
P95 E2EL (ms):                           23830.30  
P99 E2EL (ms):                           33620.36  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

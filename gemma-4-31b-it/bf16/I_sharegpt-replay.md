# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 04:37:17
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  997.90    
Total input tokens:                      60269     
Total generated tokens:                  50720     
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         50.83     
Peak output token throughput (tok/s):    123.00    
Peak concurrent requests:                32.00     
Total token throughput (tok/s):          111.22    
---------------Time to First Token----------------
Mean TTFT (ms):                          973.14    
Median TTFT (ms):                        902.78    
P50 TTFT (ms):                           902.78    
P90 TTFT (ms):                           1281.67   
P95 TTFT (ms):                           1441.40   
P99 TTFT (ms):                           1819.37   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          312.66    
Median TPOT (ms):                        313.15    
P50 TPOT (ms):                           313.15    
P90 TPOT (ms):                           321.69    
P95 TPOT (ms):                           329.22    
P99 TPOT (ms):                           362.61    
---------------Inter-token Latency----------------
Mean ITL (ms):                           311.17    
Median ITL (ms):                         306.36    
P50 ITL (ms):                            306.36    
P90 ITL (ms):                            320.62    
P95 ITL (ms):                            339.80    
P99 ITL (ms):                            581.98    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          64102.61  
Median E2EL (ms):                        40514.38  
P50 E2EL (ms):                           40514.38  
P90 E2EL (ms):                           160035.87 
P95 E2EL (ms):                           194801.62 
P99 E2EL (ms):                           267853.35 
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-06 11:42:42
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  681.62    
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.44      
Output token throughput (tok/s):         220.53    
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1984.08   
---------------Time to First Token----------------
Mean TTFT (ms):                          1115.44   
Median TTFT (ms):                        919.98    
P50 TTFT (ms):                           919.98    
P90 TTFT (ms):                           1591.69   
P95 TTFT (ms):                           2276.34   
P99 TTFT (ms):                           6053.83   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          108.21    
Median TPOT (ms):                        108.31    
P50 TPOT (ms):                           108.31    
P90 TPOT (ms):                           116.69    
P95 TPOT (ms):                           122.47    
P99 TPOT (ms):                           145.75    
---------------Inter-token Latency----------------
Mean ITL (ms):                           106.61    
Median ITL (ms):                         80.51     
P50 ITL (ms):                            80.51     
P90 ITL (ms):                            83.24     
P95 ITL (ms):                            89.26     
P99 ITL (ms):                            1051.81   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          54533.41  
Median E2EL (ms):                        52925.54  
P50 E2EL (ms):                           52925.54  
P90 E2EL (ms):                           97722.02  
P95 E2EL (ms):                           101060.19 
P99 E2EL (ms):                           106188.42 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

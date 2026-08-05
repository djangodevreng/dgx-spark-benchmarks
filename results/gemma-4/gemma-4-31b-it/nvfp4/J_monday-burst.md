# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-08 14:30:35
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-31B-IT-NVFP4 --tokenizer nvidia/Gemma-4-31B-IT-NVFP4 --served-model-name gemma-4-31b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  2165.34   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.14      
Output token throughput (tok/s):         69.42     
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          624.57    
---------------Time to First Token----------------
Mean TTFT (ms):                          5916.49   
Median TTFT (ms):                        3290.12   
P50 TTFT (ms):                           3290.12   
P90 TTFT (ms):                           6341.98   
P95 TTFT (ms):                           23946.74  
P99 TTFT (ms):                           58619.58  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          342.00    
Median TPOT (ms):                        339.58    
P50 TPOT (ms):                           339.58    
P90 TPOT (ms):                           374.71    
P95 TPOT (ms):                           403.91    
P99 TPOT (ms):                           519.91    
---------------Inter-token Latency----------------
Mean ITL (ms):                           335.82    
Median ITL (ms):                         228.90    
P50 ITL (ms):                            228.90    
P90 ITL (ms):                            231.80    
P95 ITL (ms):                            359.77    
P99 ITL (ms):                            4152.26   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          174179.61 
Median E2EL (ms):                        168598.72 
P50 E2EL (ms):                           168598.72 
P90 E2EL (ms):                           306695.94 
P95 E2EL (ms):                           318960.23 
P99 E2EL (ms):                           350308.16 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-06-23 03:20:12
**Profile:** nvfp4-v23
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
Benchmark duration (s):                  686.70    
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.44      
Output token throughput (tok/s):         218.90    
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1969.43   
---------------Time to First Token----------------
Mean TTFT (ms):                          1174.65   
Median TTFT (ms):                        967.27    
P50 TTFT (ms):                           967.27    
P90 TTFT (ms):                           1833.50   
P95 TTFT (ms):                           2390.17   
P99 TTFT (ms):                           6096.53   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          109.16    
Median TPOT (ms):                        109.23    
P50 TPOT (ms):                           109.23    
P90 TPOT (ms):                           118.69    
P95 TPOT (ms):                           124.58    
P99 TPOT (ms):                           149.51    
---------------Inter-token Latency----------------
Mean ITL (ms):                           107.42    
Median ITL (ms):                         79.84     
P50 ITL (ms):                            79.84     
P90 ITL (ms):                            82.03     
P95 ITL (ms):                            83.31     
P99 ITL (ms):                            1095.02   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          55000.19  
Median E2EL (ms):                        53702.31  
P50 E2EL (ms):                           53702.31  
P90 E2EL (ms):                           98536.56  
P95 E2EL (ms):                           102237.02 
P99 E2EL (ms):                           106868.78 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

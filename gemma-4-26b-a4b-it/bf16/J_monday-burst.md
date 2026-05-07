# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-05 22:26:34
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1152.55   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         130.42    
Peak output token throughput (tok/s):    192.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1173.40   
---------------Time to First Token----------------
Mean TTFT (ms):                          1370.45   
Median TTFT (ms):                        1131.94   
P50 TTFT (ms):                           1131.94   
P90 TTFT (ms):                           1931.65   
P95 TTFT (ms):                           2960.75   
P99 TTFT (ms):                           6156.68   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          184.69    
Median TPOT (ms):                        186.67    
P50 TPOT (ms):                           186.67    
P90 TPOT (ms):                           194.52    
P95 TPOT (ms):                           198.58    
P99 TPOT (ms):                           220.62    
---------------Inter-token Latency----------------
Mean ITL (ms):                           182.38    
Median ITL (ms):                         158.90    
P50 ITL (ms):                            158.90    
P90 ITL (ms):                            168.11    
P95 ITL (ms):                            183.54    
P99 ITL (ms):                            1107.24   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          92751.89  
Median E2EL (ms):                        91098.54  
P50 E2EL (ms):                           91098.54  
P90 E2EL (ms):                           165179.26 
P95 E2EL (ms):                           172073.08 
P99 E2EL (ms):                           179139.50 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

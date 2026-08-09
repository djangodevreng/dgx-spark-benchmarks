# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-06 10:37:03
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1217.64   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         123.45    
Peak output token throughput (tok/s):    192.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1110.68   
---------------Time to First Token----------------
Mean TTFT (ms):                          1508.18   
Median TTFT (ms):                        1234.78   
P50 TTFT (ms):                           1234.78   
P90 TTFT (ms):                           2128.10   
P95 TTFT (ms):                           3321.40   
P99 TTFT (ms):                           7596.54   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          194.94    
Median TPOT (ms):                        196.58    
P50 TPOT (ms):                           196.58    
P90 TPOT (ms):                           205.71    
P95 TPOT (ms):                           210.13    
P99 TPOT (ms):                           238.23    
---------------Inter-token Latency----------------
Mean ITL (ms):                           192.40    
Median ITL (ms):                         165.59    
P50 ITL (ms):                            165.59    
P90 ITL (ms):                            171.38    
P95 ITL (ms):                            176.62    
P99 ITL (ms):                            1236.31   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          97912.72  
Median E2EL (ms):                        96321.59  
P50 E2EL (ms):                           96321.59  
P90 E2EL (ms):                           173951.50 
P95 E2EL (ms):                           181262.44 
P99 E2EL (ms):                           188766.43 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

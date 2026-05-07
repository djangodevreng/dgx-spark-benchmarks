# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-06 05:33:20
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3332.49   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.09      
Output token throughput (tok/s):         45.11     
Peak output token throughput (tok/s):    99.00     
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          405.82    
---------------Time to First Token----------------
Mean TTFT (ms):                          8631.89   
Median TTFT (ms):                        4969.82   
P50 TTFT (ms):                           4969.82   
P90 TTFT (ms):                           9643.25   
P95 TTFT (ms):                           36659.40  
P99 TTFT (ms):                           85034.05  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          525.02    
Median TPOT (ms):                        523.21    
P50 TPOT (ms):                           523.21    
P90 TPOT (ms):                           569.71    
P95 TPOT (ms):                           605.76    
P99 TPOT (ms):                           746.27    
---------------Inter-token Latency----------------
Mean ITL (ms):                           517.08    
Median ITL (ms):                         365.97    
P50 ITL (ms):                            365.97    
P90 ITL (ms):                            375.64    
P95 ITL (ms):                            416.24    
P99 ITL (ms):                            5593.23   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          267587.01 
Median E2EL (ms):                        259525.01 
P50 E2EL (ms):                           259525.01 
P90 E2EL (ms):                           467547.87 
P95 E2EL (ms):                           490100.78 
P99 E2EL (ms):                           532563.01 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

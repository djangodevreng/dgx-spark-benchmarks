# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 00:57:06
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  747.35    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         129.92    
Peak output token throughput (tok/s):    245.00    
Peak concurrent requests:                36.00     
Total token throughput (tok/s):          1220.97   
---------------Time to First Token----------------
Mean TTFT (ms):                          1463.69   
Median TTFT (ms):                        1329.83   
P50 TTFT (ms):                           1329.83   
P90 TTFT (ms):                           2367.30   
P95 TTFT (ms):                           2835.43   
P99 TTFT (ms):                           3556.69   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          171.67    
Median TPOT (ms):                        174.98    
P50 TPOT (ms):                           174.98    
P90 TPOT (ms):                           190.67    
P95 TPOT (ms):                           197.57    
P99 TPOT (ms):                           212.13    
---------------Inter-token Latency----------------
Mean ITL (ms):                           169.32    
Median ITL (ms):                         142.06    
P50 ITL (ms):                            142.06    
P90 ITL (ms):                            157.59    
P95 ITL (ms):                            164.75    
P99 ITL (ms):                            1221.95   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          83660.28  
Median E2EL (ms):                        83437.26  
P50 E2EL (ms):                           83437.26  
P90 E2EL (ms):                           148526.77 
P95 E2EL (ms):                           158566.60 
P99 E2EL (ms):                           168681.13 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

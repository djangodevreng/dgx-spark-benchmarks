# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 08:17:38
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model ibm-granite/granite-4.1-8b --tokenizer ibm-granite/granite-4.1-8b --served-model-name granite-4-1-8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  751.09    
Total input tokens:                      814335    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         129.27    
Peak output token throughput (tok/s):    267.00    
Peak concurrent requests:                39.00     
Total token throughput (tok/s):          1213.47   
---------------Time to First Token----------------
Mean TTFT (ms):                          1956.83   
Median TTFT (ms):                        1751.45   
P50 TTFT (ms):                           1751.45   
P90 TTFT (ms):                           3445.24   
P95 TTFT (ms):                           3811.88   
P99 TTFT (ms):                           4852.04   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          182.14    
Median TPOT (ms):                        183.63    
P50 TPOT (ms):                           183.63    
P90 TPOT (ms):                           205.57    
P95 TPOT (ms):                           213.12    
P99 TPOT (ms):                           227.79    
---------------Inter-token Latency----------------
Mean ITL (ms):                           179.01    
Median ITL (ms):                         136.19    
P50 ITL (ms):                            136.19    
P90 ITL (ms):                            153.88    
P95 ITL (ms):                            162.12    
P99 ITL (ms):                            1653.46   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          88860.68  
Median E2EL (ms):                        89746.87  
P50 E2EL (ms):                           89746.87  
P90 E2EL (ms):                           155638.97 
P95 E2EL (ms):                           169377.03 
P99 E2EL (ms):                           180850.05 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

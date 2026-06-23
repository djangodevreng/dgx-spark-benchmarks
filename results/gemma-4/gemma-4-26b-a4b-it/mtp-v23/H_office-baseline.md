# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 04:58:37
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-mtp --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  733.61    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         132.35    
Peak output token throughput (tok/s):    115.00    
Peak concurrent requests:                26.00     
Total token throughput (tok/s):          1243.84   
---------------Time to First Token----------------
Mean TTFT (ms):                          1758.50   
Median TTFT (ms):                        1608.29   
P50 TTFT (ms):                           1608.29   
P90 TTFT (ms):                           2821.90   
P95 TTFT (ms):                           3394.53   
P99 TTFT (ms):                           4152.70   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          101.67    
Median TPOT (ms):                        93.50     
P50 TPOT (ms):                           93.50     
P90 TPOT (ms):                           149.14    
P95 TPOT (ms):                           178.77    
P99 TPOT (ms):                           208.22    
---------------Inter-token Latency----------------
Mean ITL (ms):                           240.09    
Median ITL (ms):                         199.34    
P50 ITL (ms):                            199.34    
P90 ITL (ms):                            231.45    
P95 ITL (ms):                            542.52    
P99 ITL (ms):                            1551.99   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          51997.73  
Median E2EL (ms):                        41920.18  
P50 E2EL (ms):                           41920.18  
P90 E2EL (ms):                           104000.36 
P95 E2EL (ms):                           123795.44 
P99 E2EL (ms):                           166797.54 
---------------Speculative Decoding---------------
Acceptance rate (%):                     33.29     
Acceptance length:                       2.33      
Drafts:                                  41650     
Draft tokens:                            166600    
Accepted tokens:                         55458     
Per-position acceptance (%):
  Position 0:                            60.24     
  Position 1:                            33.78     
  Position 2:                            22.27     
  Position 3:                            16.86     
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

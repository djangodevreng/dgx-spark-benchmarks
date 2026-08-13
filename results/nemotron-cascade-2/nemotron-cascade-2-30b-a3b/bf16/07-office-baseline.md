# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 12:28:55
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-Cascade-2-30B-A3B --tokenizer nvidia/Nemotron-Cascade-2-30B-A3B --served-model-name nemotron-cascade-2-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  790.89    
Total input tokens:                      819237    
Total generated tokens:                  97092     
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         122.76    
Peak output token throughput (tok/s):    225.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          1158.61   
---------------Time to First Token----------------
Mean TTFT (ms):                          1407.29   
Median TTFT (ms):                        1298.29   
P50 TTFT (ms):                           1298.29   
P90 TTFT (ms):                           2156.32   
P95 TTFT (ms):                           2515.31   
P99 TTFT (ms):                           2897.81   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          229.52    
Median TPOT (ms):                        231.94    
P50 TPOT (ms):                           231.94    
P90 TPOT (ms):                           255.63    
P95 TPOT (ms):                           265.06    
P99 TPOT (ms):                           282.49    
---------------Inter-token Latency----------------
Mean ITL (ms):                           226.20    
Median ITL (ms):                         196.29    
P50 ITL (ms):                            196.29    
P90 ITL (ms):                            239.43    
P95 ITL (ms):                            381.55    
P99 ITL (ms):                            1014.17   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          111219.51 
Median E2EL (ms):                        112493.81 
P50 E2EL (ms):                           112493.81 
P90 E2EL (ms):                           196413.20 
P95 E2EL (ms):                           207265.51 
P99 E2EL (ms):                           229148.13 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

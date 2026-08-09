# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 20:32:22
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1701.81   
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.12      
Output token throughput (tok/s):         57.05     
Peak output token throughput (tok/s):    173.00    
Peak concurrent requests:                172.00    
Total token throughput (tok/s):          536.19    
---------------Time to First Token----------------
Mean TTFT (ms):                          278210.10 
Median TTFT (ms):                        248552.15 
P50 TTFT (ms):                           248552.15 
P90 TTFT (ms):                           586820.44 
P95 TTFT (ms):                           610894.15 
P99 TTFT (ms):                           661729.90 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1212.77   
Median TPOT (ms):                        1183.84   
P50 TPOT (ms):                           1183.84   
P90 TPOT (ms):                           1573.85   
P95 TPOT (ms):                           1951.32   
P99 TPOT (ms):                           2667.75   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1121.61   
Median ITL (ms):                         654.28    
P50 ITL (ms):                            654.28    
P90 ITL (ms):                            1679.31   
P95 ITL (ms):                            5600.30   
P99 ITL (ms):                            8263.02   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          822707.56 
Median E2EL (ms):                        851882.75 
P50 E2EL (ms):                           851882.75 
P90 E2EL (ms):                           1146090.30
P95 E2EL (ms):                           1169865.36
P99 E2EL (ms):                           1303654.78
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

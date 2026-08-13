# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-12 18:33:15
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16-spec --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  2465.89   
Total input tokens:                      823836    
Total generated tokens:                  97092     
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         39.37     
Peak output token throughput (tok/s):    180.00    
Peak concurrent requests:                190.00    
Total token throughput (tok/s):          373.47    
---------------Time to First Token----------------
Mean TTFT (ms):                          85955.93  
Median TTFT (ms):                        59120.38  
P50 TTFT (ms):                           59120.38  
P90 TTFT (ms):                           221463.51 
P95 TTFT (ms):                           263838.80 
P99 TTFT (ms):                           316295.52 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          3080.16   
Median TPOT (ms):                        3024.47   
P50 TPOT (ms):                           3024.47   
P90 TPOT (ms):                           4852.51   
P95 TPOT (ms):                           5129.21   
P99 TPOT (ms):                           5357.15   
---------------Inter-token Latency----------------
Mean ITL (ms):                           3501.35   
Median ITL (ms):                         3368.78   
P50 ITL (ms):                            3368.78   
P90 ITL (ms):                            6030.49   
P95 ITL (ms):                            6177.33   
P99 ITL (ms):                            6253.94   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1390507.50
Median E2EL (ms):                        1445002.79
P50 E2EL (ms):                           1445002.79
P90 E2EL (ms):                           2043613.64
P95 E2EL (ms):                           2132778.08
P99 E2EL (ms):                           2337288.23
---------------Speculative Decoding---------------
Acceptance rate (%):                     1.95      
Acceptance length:                       1.29      
Drafts:                                  75006     
Draft tokens:                            1125090   
Accepted tokens:                         21970     
Per-position acceptance (%):
  Position 0:                            16.26     
  Position 1:                            6.82      
  Position 2:                            3.17      
  Position 3:                            1.38      
  Position 4:                            0.61      
  Position 5:                            0.31      
  Position 6:                            0.17      
  Position 7:                            0.11      
  Position 8:                            0.08      
  Position 9:                            0.07      
  Position 10:                           0.07      
  Position 11:                           0.06      
  Position 12:                           0.06      
  Position 13:                           0.06      
  Position 14:                           0.06      
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

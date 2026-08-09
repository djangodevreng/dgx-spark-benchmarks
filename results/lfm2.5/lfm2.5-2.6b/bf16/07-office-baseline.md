# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 17:00:54
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model LiquidAI/LFM2.5-2.6B --tokenizer LiquidAI/LFM2.5-2.6B --served-model-name lfm2-5-2-6b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  680.05    
Total input tokens:                      814735    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         142.77    
Peak output token throughput (tok/s):    408.00    
Peak concurrent requests:                11.00     
Total token throughput (tok/s):          1340.83   
---------------Time to First Token----------------
Mean TTFT (ms):                          494.69    
Median TTFT (ms):                        467.12    
P50 TTFT (ms):                           467.12    
P90 TTFT (ms):                           829.43    
P95 TTFT (ms):                           934.33    
P99 TTFT (ms):                           1409.39   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          29.25     
Median TPOT (ms):                        29.10     
P50 TPOT (ms):                           29.10     
P90 TPOT (ms):                           32.27     
P95 TPOT (ms):                           33.50     
P99 TPOT (ms):                           36.43     
---------------Inter-token Latency----------------
Mean ITL (ms):                           29.20     
Median ITL (ms):                         26.03     
P50 ITL (ms):                            26.03     
P90 ITL (ms):                            28.26     
P95 ITL (ms):                            32.06     
P99 ITL (ms):                            36.72     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          14670.36  
Median E2EL (ms):                        14203.30  
P50 E2EL (ms):                           14203.30  
P90 E2EL (ms):                           24993.55  
P95 E2EL (ms):                           26831.10  
P99 E2EL (ms):                           29251.93  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

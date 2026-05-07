# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 13:23:42
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  797.82    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         121.70    
Peak output token throughput (tok/s):    265.00    
Peak concurrent requests:                55.00     
Total token throughput (tok/s):          1143.00   
---------------Time to First Token----------------
Mean TTFT (ms):                          3300.89   
Median TTFT (ms):                        3100.29   
P50 TTFT (ms):                           3100.29   
P90 TTFT (ms):                           5420.05   
P95 TTFT (ms):                           6680.38   
P99 TTFT (ms):                           8541.41   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          300.18    
Median TPOT (ms):                        311.72    
P50 TPOT (ms):                           311.72    
P90 TPOT (ms):                           353.72    
P95 TPOT (ms):                           365.10    
P99 TPOT (ms):                           391.53    
---------------Inter-token Latency----------------
Mean ITL (ms):                           294.92    
Median ITL (ms):                         220.24    
P50 ITL (ms):                            220.24    
P90 ITL (ms):                            732.62    
P95 ITL (ms):                            783.13    
P99 ITL (ms):                            835.71    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          145850.20 
Median E2EL (ms):                        147032.26 
P50 E2EL (ms):                           147032.26 
P90 E2EL (ms):                           253222.80 
P95 E2EL (ms):                           269314.04 
P99 E2EL (ms):                           298521.97 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

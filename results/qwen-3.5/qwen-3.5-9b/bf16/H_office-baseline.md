# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-09 16:20:15
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  730.16    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         132.97    
Peak output token throughput (tok/s):    275.00    
Peak concurrent requests:                26.00     
Total token throughput (tok/s):          1248.91   
---------------Time to First Token----------------
Mean TTFT (ms):                          1889.50   
Median TTFT (ms):                        1701.03   
P50 TTFT (ms):                           1701.03   
P90 TTFT (ms):                           3464.58   
P95 TTFT (ms):                           3816.23   
P99 TTFT (ms):                           4994.50   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          120.31    
Median TPOT (ms):                        121.95    
P50 TPOT (ms):                           121.95    
P90 TPOT (ms):                           137.48    
P95 TPOT (ms):                           146.70    
P99 TPOT (ms):                           159.90    
---------------Inter-token Latency----------------
Mean ITL (ms):                           118.89    
Median ITL (ms):                         90.95     
P50 ITL (ms):                            90.95     
P90 ITL (ms):                            96.96     
P95 ITL (ms):                            526.34    
P99 ITL (ms):                            558.88    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          59569.70  
Median E2EL (ms):                        58611.11  
P50 E2EL (ms):                           58611.11  
P90 E2EL (ms):                           103154.46 
P95 E2EL (ms):                           113656.70 
P99 E2EL (ms):                           118389.94 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

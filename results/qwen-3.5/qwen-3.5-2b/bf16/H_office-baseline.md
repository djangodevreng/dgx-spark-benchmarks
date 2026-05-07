# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 14:38:40
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  673.47    
Total input tokens:                      815212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         144.17    
Peak output token throughput (tok/s):    436.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          1354.63   
---------------Time to First Token----------------
Mean TTFT (ms):                          379.25    
Median TTFT (ms):                        366.01    
P50 TTFT (ms):                           366.01    
P90 TTFT (ms):                           625.16    
P95 TTFT (ms):                           684.56    
P99 TTFT (ms):                           907.12    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          20.76     
Median TPOT (ms):                        20.72     
P50 TPOT (ms):                           20.72     
P90 TPOT (ms):                           22.69     
P95 TPOT (ms):                           23.50     
P99 TPOT (ms):                           24.80     
---------------Inter-token Latency----------------
Mean ITL (ms):                           20.99     
Median ITL (ms):                         19.22     
P50 ITL (ms):                            19.22     
P90 ITL (ms):                            21.30     
P95 ITL (ms):                            23.04     
P99 ITL (ms):                            116.78    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          10439.85  
Median E2EL (ms):                        10218.13  
P50 E2EL (ms):                           10218.13  
P90 E2EL (ms):                           17942.94  
P95 E2EL (ms):                           19157.93  
P99 E2EL (ms):                           20434.01  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

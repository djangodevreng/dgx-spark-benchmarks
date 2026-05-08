# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 22:11:39
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  696.09    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         139.48    
Peak output token throughput (tok/s):    300.00    
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          1310.03   
---------------Time to First Token----------------
Mean TTFT (ms):                          971.28    
Median TTFT (ms):                        914.25    
P50 TTFT (ms):                           914.25    
P90 TTFT (ms):                           1668.19   
P95 TTFT (ms):                           1938.97   
P99 TTFT (ms):                           2598.91   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          53.52     
Median TPOT (ms):                        53.29     
P50 TPOT (ms):                           53.29     
P90 TPOT (ms):                           62.14     
P95 TPOT (ms):                           65.41     
P99 TPOT (ms):                           72.26     
---------------Inter-token Latency----------------
Mean ITL (ms):                           53.25     
Median ITL (ms):                         45.40     
P50 ITL (ms):                            45.40     
P90 ITL (ms):                            49.07     
P95 ITL (ms):                            50.60     
P99 ITL (ms):                            318.61    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          26802.05  
Median E2EL (ms):                        26453.09  
P50 E2EL (ms):                           26453.09  
P90 E2EL (ms):                           45982.22  
P95 E2EL (ms):                           51120.04  
P99 E2EL (ms):                           53867.02  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

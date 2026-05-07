# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 18:23:53
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  700.37    
Total input tokens:                      813236    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.63    
Peak output token throughput (tok/s):    256.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1299.78   
---------------Time to First Token----------------
Mean TTFT (ms):                          828.76    
Median TTFT (ms):                        774.47    
P50 TTFT (ms):                           774.47    
P90 TTFT (ms):                           1408.37   
P95 TTFT (ms):                           1738.44   
P99 TTFT (ms):                           2188.82   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          62.24     
Median TPOT (ms):                        62.05     
P50 TPOT (ms):                           62.05     
P90 TPOT (ms):                           70.69     
P95 TPOT (ms):                           74.88     
P99 TPOT (ms):                           80.84     
---------------Inter-token Latency----------------
Mean ITL (ms):                           61.82     
Median ITL (ms):                         53.87     
P50 ITL (ms):                            53.87     
P90 ITL (ms):                            61.60     
P95 ITL (ms):                            65.16     
P99 ITL (ms):                            453.20    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          30837.91  
Median E2EL (ms):                        31597.37  
P50 E2EL (ms):                           31597.37  
P90 E2EL (ms):                           53161.97  
P95 E2EL (ms):                           59926.95  
P99 E2EL (ms):                           62681.45  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

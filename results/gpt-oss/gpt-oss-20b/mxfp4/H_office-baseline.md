# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-26 10:58:18
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  681.90    
Total input tokens:                      820038    
Total generated tokens:                  50918     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         74.67     
Peak output token throughput (tok/s):    206.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          1277.24   
---------------Time to First Token----------------
Mean TTFT (ms):                          813.66    
Median TTFT (ms):                        734.62    
P50 TTFT (ms):                           734.62    
P90 TTFT (ms):                           1456.29   
P95 TTFT (ms):                           1678.96   
P99 TTFT (ms):                           2284.22   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          100.66    
Median TPOT (ms):                        44.48     
P50 TPOT (ms):                           44.48     
P90 TPOT (ms):                           130.55    
P95 TPOT (ms):                           193.63    
P99 TPOT (ms):                           575.74    
---------------Inter-token Latency----------------
Mean ITL (ms):                           53.89     
Median ITL (ms):                         31.87     
P50 ITL (ms):                            31.87     
P90 ITL (ms):                            39.82     
P95 ITL (ms):                            41.69     
P99 ITL (ms):                            202.28    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          12468.82  
Median E2EL (ms):                        7198.86   
P50 E2EL (ms):                           7198.86   
P90 E2EL (ms):                           29940.54  
P95 E2EL (ms):                           36199.54  
P99 E2EL (ms):                           42382.93  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

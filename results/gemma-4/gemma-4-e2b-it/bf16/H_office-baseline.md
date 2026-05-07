# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 12:45:19
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  677.87    
Total input tokens:                      814599    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         143.23    
Peak output token throughput (tok/s):    404.00    
Peak concurrent requests:                11.00     
Total token throughput (tok/s):          1344.93   
---------------Time to First Token----------------
Mean TTFT (ms):                          496.23    
Median TTFT (ms):                        444.81    
P50 TTFT (ms):                           444.81    
P90 TTFT (ms):                           867.01    
P95 TTFT (ms):                           997.38    
P99 TTFT (ms):                           1352.69   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          27.35     
Median TPOT (ms):                        27.39     
P50 TPOT (ms):                           27.39     
P90 TPOT (ms):                           30.25     
P95 TPOT (ms):                           30.87     
P99 TPOT (ms):                           35.17     
---------------Inter-token Latency----------------
Mean ITL (ms):                           27.31     
Median ITL (ms):                         24.67     
P50 ITL (ms):                            24.67     
P90 ITL (ms):                            26.10     
P95 ITL (ms):                            26.55     
P99 ITL (ms):                            37.29     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          13755.53  
Median E2EL (ms):                        13498.79  
P50 E2EL (ms):                           13498.79  
P90 E2EL (ms):                           23347.91  
P95 E2EL (ms):                           25381.28  
P99 E2EL (ms):                           27533.25  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

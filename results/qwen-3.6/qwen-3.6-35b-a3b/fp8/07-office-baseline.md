# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 16:11:48
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  708.41    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         137.06    
Peak output token throughput (tok/s):    287.00    
Peak concurrent requests:                24.00     
Total token throughput (tok/s):          1287.25   
---------------Time to First Token----------------
Mean TTFT (ms):                          1825.21   
Median TTFT (ms):                        1656.23   
P50 TTFT (ms):                           1656.23   
P90 TTFT (ms):                           3111.41   
P95 TTFT (ms):                           3712.30   
P99 TTFT (ms):                           4935.92   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          92.01     
Median TPOT (ms):                        93.57     
P50 TPOT (ms):                           93.57     
P90 TPOT (ms):                           111.03    
P95 TPOT (ms):                           121.73    
P99 TPOT (ms):                           136.95    
---------------Inter-token Latency----------------
Mean ITL (ms):                           91.08     
Median ITL (ms):                         68.01     
P50 ITL (ms):                            68.01     
P90 ITL (ms):                            87.94     
P95 ITL (ms):                            284.94    
P99 ITL (ms):                            518.68    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          45993.89  
Median E2EL (ms):                        44293.45  
P50 E2EL (ms):                           44293.45  
P90 E2EL (ms):                           81185.24  
P95 E2EL (ms):                           91989.13  
P99 E2EL (ms):                           97968.77  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

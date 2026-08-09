# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 15:04:16
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  673.50    
Total input tokens:                      815212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         144.16    
Peak output token throughput (tok/s):    441.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          1354.58   
---------------Time to First Token----------------
Mean TTFT (ms):                          390.75    
Median TTFT (ms):                        371.26    
P50 TTFT (ms):                           371.26    
P90 TTFT (ms):                           648.08    
P95 TTFT (ms):                           732.38    
P99 TTFT (ms):                           906.84    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          20.72     
Median TPOT (ms):                        20.55     
P50 TPOT (ms):                           20.55     
P90 TPOT (ms):                           22.69     
P95 TPOT (ms):                           23.67     
P99 TPOT (ms):                           24.74     
---------------Inter-token Latency----------------
Mean ITL (ms):                           20.69     
Median ITL (ms):                         19.07     
P50 ITL (ms):                            19.07     
P90 ITL (ms):                            21.49     
P95 ITL (ms):                            23.55     
P99 ITL (ms):                            118.02    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          10433.82  
Median E2EL (ms):                        10205.85  
P50 E2EL (ms):                           10205.85  
P90 E2EL (ms):                           18055.49  
P95 E2EL (ms):                           19268.22  
P99 E2EL (ms):                           20516.79  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

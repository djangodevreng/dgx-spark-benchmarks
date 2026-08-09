# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 10:16:29
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     199       
Failed requests:                         1         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  681.78    
Total input tokens:                      809916    
Total generated tokens:                  97006     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         142.28    
Peak output token throughput (tok/s):    384.00    
Peak concurrent requests:                13.00     
Total token throughput (tok/s):          1330.22   
---------------Time to First Token----------------
Mean TTFT (ms):                          810.13    
Median TTFT (ms):                        732.73    
P50 TTFT (ms):                           732.73    
P90 TTFT (ms):                           1308.53   
P95 TTFT (ms):                           1559.29   
P99 TTFT (ms):                           1736.30   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          30.71     
Median TPOT (ms):                        30.07     
P50 TPOT (ms):                           30.07     
P90 TPOT (ms):                           37.34     
P95 TPOT (ms):                           40.16     
P99 TPOT (ms):                           44.77     
---------------Inter-token Latency----------------
Mean ITL (ms):                           30.59     
Median ITL (ms):                         25.72     
P50 ITL (ms):                            25.72     
P90 ITL (ms):                            30.63     
P95 ITL (ms):                            33.60     
P99 ITL (ms):                            181.51    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          15700.08  
Median E2EL (ms):                        15275.75  
P50 E2EL (ms):                           15275.75  
P90 E2EL (ms):                           26808.10  
P95 E2EL (ms):                           29407.12  
P99 E2EL (ms):                           34158.79  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

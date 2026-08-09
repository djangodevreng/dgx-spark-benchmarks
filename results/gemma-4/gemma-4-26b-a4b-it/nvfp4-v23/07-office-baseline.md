# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 12:48:52
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  699.48    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.81    
Peak output token throughput (tok/s):    272.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1304.52   
---------------Time to First Token----------------
Mean TTFT (ms):                          1161.74   
Median TTFT (ms):                        1056.91   
P50 TTFT (ms):                           1056.91   
P90 TTFT (ms):                           2044.43   
P95 TTFT (ms):                           2437.10   
P99 TTFT (ms):                           3072.59   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          64.13     
Median TPOT (ms):                        64.69     
P50 TPOT (ms):                           64.69     
P90 TPOT (ms):                           76.16     
P95 TPOT (ms):                           80.42     
P99 TPOT (ms):                           89.65     
---------------Inter-token Latency----------------
Mean ITL (ms):                           63.78     
Median ITL (ms):                         52.79     
P50 ITL (ms):                            52.79     
P90 ITL (ms):                            59.49     
P95 ITL (ms):                            61.16     
P99 ITL (ms):                            625.40    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          32126.06  
Median E2EL (ms):                        30837.53  
P50 E2EL (ms):                           30837.53  
P90 E2EL (ms):                           55307.60  
P95 E2EL (ms):                           62486.42  
P99 E2EL (ms):                           65774.24  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

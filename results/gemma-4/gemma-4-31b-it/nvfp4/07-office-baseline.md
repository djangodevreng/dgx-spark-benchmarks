# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 23:07:49
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-31B-IT-NVFP4 --tokenizer nvidia/Gemma-4-31B-IT-NVFP4 --served-model-name gemma-4-31b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1776.23   
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         54.66     
Peak output token throughput (tok/s):    242.00    
Peak concurrent requests:                200.00    
Total token throughput (tok/s):          513.72    
---------------Time to First Token----------------
Mean TTFT (ms):                          268939.22 
Median TTFT (ms):                        219173.90 
P50 TTFT (ms):                           219173.90 
P90 TTFT (ms):                           617600.74 
P95 TTFT (ms):                           660124.65 
P99 TTFT (ms):                           737940.86 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          2080.29   
Median TPOT (ms):                        1931.21   
P50 TPOT (ms):                           1931.21   
P90 TPOT (ms):                           3528.66   
P95 TPOT (ms):                           3873.11   
P99 TPOT (ms):                           5794.69   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1739.04   
Median ITL (ms):                         1075.13   
P50 ITL (ms):                            1075.13   
P90 ITL (ms):                            4653.80   
P95 ITL (ms):                            6321.64   
P99 ITL (ms):                            10531.52  
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1113171.81
Median E2EL (ms):                        1131752.65
P50 E2EL (ms):                           1131752.65
P90 E2EL (ms):                           1477916.92
P95 E2EL (ms):                           1584330.95
P99 E2EL (ms):                           1645460.27
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

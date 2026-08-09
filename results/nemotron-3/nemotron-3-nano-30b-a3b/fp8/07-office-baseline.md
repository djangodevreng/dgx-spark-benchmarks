# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 01:27:09
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --served-model-name nemotron-3-nano-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  710.17    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         136.72    
Peak output token throughput (tok/s):    273.00    
Peak concurrent requests:                24.00     
Total token throughput (tok/s):          1285.65   
---------------Time to First Token----------------
Mean TTFT (ms):                          1150.78   
Median TTFT (ms):                        1021.68   
P50 TTFT (ms):                           1021.68   
P90 TTFT (ms):                           1790.01   
P95 TTFT (ms):                           2116.40   
P99 TTFT (ms):                           2635.30   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          89.11     
Median TPOT (ms):                        91.44     
P50 TPOT (ms):                           91.44     
P90 TPOT (ms):                           105.28    
P95 TPOT (ms):                           110.34    
P99 TPOT (ms):                           121.69    
---------------Inter-token Latency----------------
Mean ITL (ms):                           88.28     
Median ITL (ms):                         74.25     
P50 ITL (ms):                            74.25     
P90 ITL (ms):                            91.36     
P95 ITL (ms):                            95.35     
P99 ITL (ms):                            590.66    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          44006.64  
Median E2EL (ms):                        43063.80  
P50 E2EL (ms):                           43063.80  
P90 E2EL (ms):                           78059.53  
P95 E2EL (ms):                           86329.56  
P99 E2EL (ms):                           96004.50  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

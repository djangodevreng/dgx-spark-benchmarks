# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-09-18 18:35:37
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-27B-NVFP4 --tokenizer nvidia/Qwen3.8-27B-NVFP4 --served-model-name qwen3.8-27b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1389.55   
Total input tokens:                      823212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.14      
Output token throughput (tok/s):         69.87     
Peak output token throughput (tok/s):    382.00    
Peak concurrent requests:                192.00    
Total token throughput (tok/s):          662.30    
---------------Time to First Token----------------
Mean TTFT (ms):                          237836.19 
Median TTFT (ms):                        252802.91 
P50 TTFT (ms):                           252802.91 
P90 TTFT (ms):                           413652.27 
P95 TTFT (ms):                           437532.19 
P99 TTFT (ms):                           475475.83 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1569.89   
Median TPOT (ms):                        1543.49   
P50 TPOT (ms):                           1543.49   
P90 TPOT (ms):                           2701.10   
P95 TPOT (ms):                           2748.88   
P99 TPOT (ms):                           2807.55   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1298.82   
Median ITL (ms):                         558.04    
P50 ITL (ms):                            558.04    
P90 ITL (ms):                            2833.47   
P95 ITL (ms):                            2853.50   
P99 ITL (ms):                            2875.89   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          867511.05 
Median E2EL (ms):                        861041.60 
P50 E2EL (ms):                           861041.60 
P90 E2EL (ms):                           1166785.37
P95 E2EL (ms):                           1240781.42
P99 E2EL (ms):                           1288858.27
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

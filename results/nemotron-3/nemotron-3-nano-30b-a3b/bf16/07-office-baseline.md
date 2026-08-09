# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 04:36:36
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --served-model-name nemotron-3-nano-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  776.17    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         125.09    
Peak output token throughput (tok/s):    211.00    
Peak concurrent requests:                42.00     
Total token throughput (tok/s):          1176.33   
---------------Time to First Token----------------
Mean TTFT (ms):                          1325.89   
Median TTFT (ms):                        1232.15   
P50 TTFT (ms):                           1232.15   
P90 TTFT (ms):                           2003.86   
P95 TTFT (ms):                           2320.28   
P99 TTFT (ms):                           2906.49   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          216.82    
Median TPOT (ms):                        220.75    
P50 TPOT (ms):                           220.75    
P90 TPOT (ms):                           238.58    
P95 TPOT (ms):                           242.00    
P99 TPOT (ms):                           261.76    
---------------Inter-token Latency----------------
Mean ITL (ms):                           213.71    
Median ITL (ms):                         190.70    
P50 ITL (ms):                            190.70    
P90 ITL (ms):                            216.60    
P95 ITL (ms):                            327.39    
P99 ITL (ms):                            983.89    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          105074.84 
Median E2EL (ms):                        106021.39 
P50 E2EL (ms):                           106021.39 
P90 E2EL (ms):                           182132.85 
P95 E2EL (ms):                           197717.09 
P99 E2EL (ms):                           206304.27 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

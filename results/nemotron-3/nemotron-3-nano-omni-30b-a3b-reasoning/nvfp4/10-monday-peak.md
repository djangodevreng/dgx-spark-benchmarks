# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-07 13:52:24
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  575.85    
Total input tokens:                      1203008   
Total generated tokens:                  150317    
Request throughput (req/s):              0.52      
Output token throughput (tok/s):         261.04    
Peak output token throughput (tok/s):    407.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          2350.14   
---------------Time to First Token----------------
Mean TTFT (ms):                          1168.76   
Median TTFT (ms):                        1005.05   
P50 TTFT (ms):                           1005.05   
P90 TTFT (ms):                           1725.20   
P95 TTFT (ms):                           2134.34   
P99 TTFT (ms):                           4441.22   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          91.80     
Median TPOT (ms):                        92.92     
P50 TPOT (ms):                           92.92     
P90 TPOT (ms):                           100.54    
P95 TPOT (ms):                           107.38    
P99 TPOT (ms):                           123.42    
---------------Inter-token Latency----------------
Mean ITL (ms):                           142.36    
Median ITL (ms):                         58.89     
P50 ITL (ms):                            58.89     
P90 ITL (ms):                            118.06    
P95 ITL (ms):                            341.23    
P99 ITL (ms):                            872.29    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          46346.14  
Median E2EL (ms):                        42957.58  
P50 E2EL (ms):                           42957.58  
P90 E2EL (ms):                           83178.98  
P95 E2EL (ms):                           86065.02  
P99 E2EL (ms):                           90925.42  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

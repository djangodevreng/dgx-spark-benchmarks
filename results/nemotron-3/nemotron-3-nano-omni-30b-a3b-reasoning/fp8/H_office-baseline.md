# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-03 12:04:43
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --served-model-name nemotron-3-nano-omni-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  704.21    
Total input tokens:                      816039    
Total generated tokens:                  97092     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         137.87    
Peak output token throughput (tok/s):    256.00    
Peak concurrent requests:                18.00     
Total token throughput (tok/s):          1296.67   
---------------Time to First Token----------------
Mean TTFT (ms):                          812.88    
Median TTFT (ms):                        732.14    
P50 TTFT (ms):                           732.14    
P90 TTFT (ms):                           1357.62   
P95 TTFT (ms):                           1574.87   
P99 TTFT (ms):                           2007.73   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          71.04     
Median TPOT (ms):                        74.41     
P50 TPOT (ms):                           74.41     
P90 TPOT (ms):                           83.92     
P95 TPOT (ms):                           88.61     
P99 TPOT (ms):                           95.27     
---------------Inter-token Latency----------------
Mean ITL (ms):                           70.49     
Median ITL (ms):                         65.55     
P50 ITL (ms):                            65.55     
P90 ITL (ms):                            74.61     
P95 ITL (ms):                            86.00     
P99 ITL (ms):                            438.55    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          34992.51  
Median E2EL (ms):                        34234.56  
P50 E2EL (ms):                           34234.56  
P90 E2EL (ms):                           63992.40  
P95 E2EL (ms):                           69891.38  
P99 E2EL (ms):                           74500.32  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

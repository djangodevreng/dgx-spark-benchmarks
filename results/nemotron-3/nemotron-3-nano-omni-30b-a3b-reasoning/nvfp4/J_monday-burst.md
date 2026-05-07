# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-03 10:48:59
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  516.11    
Total input tokens:                      1203008   
Total generated tokens:                  150317    
Request throughput (req/s):              0.58      
Output token throughput (tok/s):         291.25    
Peak output token throughput (tok/s):    426.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2622.17   
---------------Time to First Token----------------
Mean TTFT (ms):                          874.64    
Median TTFT (ms):                        686.61    
P50 TTFT (ms):                           686.61    
P90 TTFT (ms):                           1437.95   
P95 TTFT (ms):                           2151.21   
P99 TTFT (ms):                           4462.05   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          81.42     
Median TPOT (ms):                        82.06     
P50 TPOT (ms):                           82.06     
P90 TPOT (ms):                           88.78     
P95 TPOT (ms):                           90.98     
P99 TPOT (ms):                           97.82     
---------------Inter-token Latency----------------
Mean ITL (ms):                           80.55     
Median ITL (ms):                         62.36     
P50 ITL (ms):                            62.36     
P90 ITL (ms):                            75.92     
P95 ITL (ms):                            208.76    
P99 ITL (ms):                            523.41    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          41189.70  
Median E2EL (ms):                        40826.83  
P50 E2EL (ms):                           40826.83  
P90 E2EL (ms):                           72814.14  
P95 E2EL (ms):                           75952.16  
P99 E2EL (ms):                           80042.79  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

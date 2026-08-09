# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-09 05:27:28
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --served-model-name nemotron-3-nano-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1240.98   
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.24      
Output token throughput (tok/s):         121.13    
Peak output token throughput (tok/s):    168.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1090.41   
---------------Time to First Token----------------
Mean TTFT (ms):                          1259.28   
Median TTFT (ms):                        1113.25   
P50 TTFT (ms):                           1113.25   
P90 TTFT (ms):                           1769.52   
P95 TTFT (ms):                           2149.06   
P99 TTFT (ms):                           5136.47   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          199.87    
Median TPOT (ms):                        202.31    
P50 TPOT (ms):                           202.31    
P90 TPOT (ms):                           210.51    
P95 TPOT (ms):                           214.54    
P99 TPOT (ms):                           233.07    
---------------Inter-token Latency----------------
Mean ITL (ms):                           197.27    
Median ITL (ms):                         178.05    
P50 ITL (ms):                            178.05    
P90 ITL (ms):                            188.60    
P95 ITL (ms):                            204.01    
P99 ITL (ms):                            909.45    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          100100.53 
Median E2EL (ms):                        99442.99  
P50 E2EL (ms):                           99442.99  
P90 E2EL (ms):                           179086.48 
P95 E2EL (ms):                           184634.92 
P99 E2EL (ms):                           192168.34 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

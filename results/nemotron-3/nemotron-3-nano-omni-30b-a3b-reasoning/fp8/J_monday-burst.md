# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-03 12:30:35
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --served-model-name nemotron-3-nano-omni-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  693.76    
Total input tokens:                      1203008   
Total generated tokens:                  150317    
Request throughput (req/s):              0.43      
Output token throughput (tok/s):         216.67    
Peak output token throughput (tok/s):    302.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1950.70   
---------------Time to First Token----------------
Mean TTFT (ms):                          859.52    
Median TTFT (ms):                        757.37    
P50 TTFT (ms):                           757.37    
P90 TTFT (ms):                           1203.85   
P95 TTFT (ms):                           1579.30   
P99 TTFT (ms):                           3387.55   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          110.59    
Median TPOT (ms):                        112.11    
P50 TPOT (ms):                           112.11    
P90 TPOT (ms):                           117.44    
P95 TPOT (ms):                           120.87    
P99 TPOT (ms):                           139.86    
---------------Inter-token Latency----------------
Mean ITL (ms):                           109.32    
Median ITL (ms):                         91.41     
P50 ITL (ms):                            91.41     
P90 ITL (ms):                            109.50    
P95 ITL (ms):                            201.16    
P99 ITL (ms):                            637.93    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          55574.87  
Median E2EL (ms):                        54252.16  
P50 E2EL (ms):                           54252.16  
P90 E2EL (ms):                           98848.72  
P95 E2EL (ms):                           103069.97 
P99 E2EL (ms):                           107345.90 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

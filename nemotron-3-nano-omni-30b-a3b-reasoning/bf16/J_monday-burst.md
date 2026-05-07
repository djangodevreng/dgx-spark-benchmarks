# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-03 15:03:16
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1210.53   
Total input tokens:                      1203008   
Total generated tokens:                  150317    
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         124.17    
Peak output token throughput (tok/s):    176.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1117.96   
---------------Time to First Token----------------
Mean TTFT (ms):                          1281.70   
Median TTFT (ms):                        1129.54   
P50 TTFT (ms):                           1129.54   
P90 TTFT (ms):                           1794.76   
P95 TTFT (ms):                           2203.48   
P99 TTFT (ms):                           5184.42   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          194.45    
Median TPOT (ms):                        196.56    
P50 TPOT (ms):                           196.56    
P90 TPOT (ms):                           205.24    
P95 TPOT (ms):                           208.57    
P99 TPOT (ms):                           231.04    
---------------Inter-token Latency----------------
Mean ITL (ms):                           192.21    
Median ITL (ms):                         171.97    
P50 ITL (ms):                            171.97    
P90 ITL (ms):                            182.45    
P95 ITL (ms):                            192.57    
P99 ITL (ms):                            939.04    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          97480.07  
Median E2EL (ms):                        95190.94  
P50 E2EL (ms):                           95190.94  
P90 E2EL (ms):                           173379.19 
P95 E2EL (ms):                           179519.26 
P99 E2EL (ms):                           189200.87 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

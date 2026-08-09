# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-06 02:37:48
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1188.09   
Total input tokens:                      1203008   
Total generated tokens:                  150317    
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         126.52    
Peak output token throughput (tok/s):    150.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1139.08   
---------------Time to First Token----------------
Mean TTFT (ms):                          1254.74   
Median TTFT (ms):                        1111.01   
P50 TTFT (ms):                           1111.01   
P90 TTFT (ms):                           1656.93   
P95 TTFT (ms):                           2043.36   
P99 TTFT (ms):                           5170.83   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          191.02    
Median TPOT (ms):                        193.02    
P50 TPOT (ms):                           193.02    
P90 TPOT (ms):                           200.59    
P95 TPOT (ms):                           204.06    
P99 TPOT (ms):                           230.40    
---------------Inter-token Latency----------------
Mean ITL (ms):                           293.99    
Median ITL (ms):                         170.16    
P50 ITL (ms):                            170.16    
P90 ITL (ms):                            323.35    
P95 ITL (ms):                            416.79    
P99 ITL (ms):                            985.44    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          95750.44  
Median E2EL (ms):                        94181.57  
P50 E2EL (ms):                           94181.57  
P90 E2EL (ms):                           169791.04 
P95 E2EL (ms):                           177020.52 
P99 E2EL (ms):                           182774.05 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

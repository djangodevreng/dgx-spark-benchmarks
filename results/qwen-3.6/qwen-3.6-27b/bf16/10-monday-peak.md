# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-14 05:08:51
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3065.37   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         49.04     
Peak output token throughput (tok/s):    77.00     
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          440.89    
---------------Time to First Token----------------
Mean TTFT (ms):                          8342.20   
Median TTFT (ms):                        5421.85   
P50 TTFT (ms):                           5421.85   
P90 TTFT (ms):                           10147.18  
P95 TTFT (ms):                           28294.76  
P99 TTFT (ms):                           74364.67  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          483.38    
Median TPOT (ms):                        483.98    
P50 TPOT (ms):                           483.98    
P90 TPOT (ms):                           523.77    
P95 TPOT (ms):                           552.20    
P99 TPOT (ms):                           639.53    
---------------Inter-token Latency----------------
Mean ITL (ms):                           476.49    
Median ITL (ms):                         346.32    
P50 ITL (ms):                            346.32    
P90 ITL (ms):                            1069.46   
P95 ITL (ms):                            1621.63   
P99 ITL (ms):                            1871.55   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          246903.97 
Median E2EL (ms):                        239206.79 
P50 E2EL (ms):                           239206.79 
P90 E2EL (ms):                           434741.53 
P95 E2EL (ms):                           452052.42 
P99 E2EL (ms):                           484486.06 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

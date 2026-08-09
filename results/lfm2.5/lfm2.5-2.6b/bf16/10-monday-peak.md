# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-08 17:28:05
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model LiquidAI/LFM2.5-2.6B --tokenizer LiquidAI/LFM2.5-2.6B --served-model-name lfm2-5-2-6b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  311.96    
Total input tokens:                      1201060   
Total generated tokens:                  150317    
Request throughput (req/s):              0.96      
Output token throughput (tok/s):         481.84    
Peak output token throughput (tok/s):    725.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          4331.87   
---------------Time to First Token----------------
Mean TTFT (ms):                          482.61    
Median TTFT (ms):                        454.18    
P50 TTFT (ms):                           454.18    
P90 TTFT (ms):                           728.76    
P95 TTFT (ms):                           956.49    
P99 TTFT (ms):                           1503.43   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          48.13     
Median TPOT (ms):                        48.55     
P50 TPOT (ms):                           48.55     
P90 TPOT (ms):                           51.88     
P95 TPOT (ms):                           54.14     
P99 TPOT (ms):                           60.93     
---------------Inter-token Latency----------------
Mean ITL (ms):                           47.65     
Median ITL (ms):                         34.93     
P50 ITL (ms):                            34.93     
P90 ITL (ms):                            37.01     
P95 ITL (ms):                            40.28     
P99 ITL (ms):                            472.37    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          24360.15  
Median E2EL (ms):                        24051.74  
P50 E2EL (ms):                           24051.74  
P90 E2EL (ms):                           43474.90  
P95 E2EL (ms):                           44880.75  
P99 E2EL (ms):                           46925.91  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

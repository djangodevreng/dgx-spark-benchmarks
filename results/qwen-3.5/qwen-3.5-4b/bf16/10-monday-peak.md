# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-07 18:33:51
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  577.49    
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.52      
Output token throughput (tok/s):         260.30    
Peak output token throughput (tok/s):    401.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2340.29   
---------------Time to First Token----------------
Mean TTFT (ms):                          1137.01   
Median TTFT (ms):                        980.28    
P50 TTFT (ms):                           980.28    
P90 TTFT (ms):                           1761.24   
P95 TTFT (ms):                           2362.68   
P99 TTFT (ms):                           5327.14   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          90.54     
Median TPOT (ms):                        91.01     
P50 TPOT (ms):                           91.01     
P90 TPOT (ms):                           98.42     
P95 TPOT (ms):                           102.32    
P99 TPOT (ms):                           125.66    
---------------Inter-token Latency----------------
Mean ITL (ms):                           89.47     
Median ITL (ms):                         65.62     
P50 ITL (ms):                            65.62     
P90 ITL (ms):                            131.82    
P95 ITL (ms):                            335.22    
P99 ITL (ms):                            350.54    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          45898.68  
Median E2EL (ms):                        44785.48  
P50 E2EL (ms):                           44785.48  
P90 E2EL (ms):                           81976.46  
P95 E2EL (ms):                           84943.45  
P99 E2EL (ms):                           89442.35  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

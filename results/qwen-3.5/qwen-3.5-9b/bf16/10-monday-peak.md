# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-07 22:53:10
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  944.55    
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.32      
Output token throughput (tok/s):         159.14    
Peak output token throughput (tok/s):    251.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          1430.83   
---------------Time to First Token----------------
Mean TTFT (ms):                          2118.73   
Median TTFT (ms):                        1650.73   
P50 TTFT (ms):                           1650.73   
P90 TTFT (ms):                           2992.42   
P95 TTFT (ms):                           5591.39   
P99 TTFT (ms):                           14331.86  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          148.53    
Median TPOT (ms):                        148.67    
P50 TPOT (ms):                           148.67    
P90 TPOT (ms):                           160.75    
P95 TPOT (ms):                           169.32    
P99 TPOT (ms):                           196.61    
---------------Inter-token Latency----------------
Mean ITL (ms):                           146.46    
Median ITL (ms):                         107.22    
P50 ITL (ms):                            107.22    
P90 ITL (ms):                            205.15    
P95 ITL (ms):                            555.08    
P99 ITL (ms):                            569.74    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          75454.28  
Median E2EL (ms):                        72840.69  
P50 E2EL (ms):                           72840.69  
P90 E2EL (ms):                           133020.20 
P95 E2EL (ms):                           138382.44 
P99 E2EL (ms):                           146652.15 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

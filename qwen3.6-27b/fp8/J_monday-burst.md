# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-04 19:50:26
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1883.79   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.16      
Output token throughput (tok/s):         79.80     
Peak output token throughput (tok/s):    151.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          717.43    
---------------Time to First Token----------------
Mean TTFT (ms):                          5462.92   
Median TTFT (ms):                        3881.69   
P50 TTFT (ms):                           3881.69   
P90 TTFT (ms):                           7113.98   
P95 TTFT (ms):                           14788.26  
P99 TTFT (ms):                           40693.85  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          296.89    
Median TPOT (ms):                        299.50    
P50 TPOT (ms):                           299.50    
P90 TPOT (ms):                           327.25    
P95 TPOT (ms):                           347.13    
P99 TPOT (ms):                           416.97    
---------------Inter-token Latency----------------
Mean ITL (ms):                           293.85    
Median ITL (ms):                         177.56    
P50 ITL (ms):                            177.56    
P90 ITL (ms):                            672.62    
P95 ITL (ms):                            1184.96   
P99 ITL (ms):                            1783.22   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          151810.81 
Median E2EL (ms):                        144861.72 
P50 E2EL (ms):                           144861.72 
P90 E2EL (ms):                           268296.97 
P95 E2EL (ms):                           279854.48 
P99 E2EL (ms):                           300138.06 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

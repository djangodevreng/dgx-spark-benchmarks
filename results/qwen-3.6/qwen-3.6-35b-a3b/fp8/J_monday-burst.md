# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-04 22:45:53
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  846.69    
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.35      
Output token throughput (tok/s):         177.53    
Peak output token throughput (tok/s):    287.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          1596.19   
---------------Time to First Token----------------
Mean TTFT (ms):                          1487.84   
Median TTFT (ms):                        1352.43   
P50 TTFT (ms):                           1352.43   
P90 TTFT (ms):                           2072.04   
P95 TTFT (ms):                           2761.22   
P99 TTFT (ms):                           7227.27   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          134.89    
Median TPOT (ms):                        135.86    
P50 TPOT (ms):                           135.86    
P90 TPOT (ms):                           144.70    
P95 TPOT (ms):                           150.37    
P99 TPOT (ms):                           163.43    
---------------Inter-token Latency----------------
Mean ITL (ms):                           133.70    
Median ITL (ms):                         105.61    
P50 ITL (ms):                            105.61    
P90 ITL (ms):                            257.13    
P95 ITL (ms):                            396.12    
P99 ITL (ms):                            435.14    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          68095.65  
Median E2EL (ms):                        66884.33  
P50 E2EL (ms):                           66884.33  
P90 E2EL (ms):                           121250.35 
P95 E2EL (ms):                           125960.60 
P99 E2EL (ms):                           133346.42 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

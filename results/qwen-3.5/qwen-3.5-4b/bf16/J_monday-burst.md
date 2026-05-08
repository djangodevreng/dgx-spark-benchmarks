# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-07 22:45:56
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  565.69    
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.53      
Output token throughput (tok/s):         265.72    
Peak output token throughput (tok/s):    425.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2389.11   
---------------Time to First Token----------------
Mean TTFT (ms):                          1176.31   
Median TTFT (ms):                        1031.83   
P50 TTFT (ms):                           1031.83   
P90 TTFT (ms):                           1757.89   
P95 TTFT (ms):                           2193.16   
P99 TTFT (ms):                           5442.49   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          88.27     
Median TPOT (ms):                        88.80     
P50 TPOT (ms):                           88.80     
P90 TPOT (ms):                           96.32     
P95 TPOT (ms):                           100.55    
P99 TPOT (ms):                           123.62    
---------------Inter-token Latency----------------
Mean ITL (ms):                           87.39     
Median ITL (ms):                         61.19     
P50 ITL (ms):                            61.19     
P90 ITL (ms):                            153.06    
P95 ITL (ms):                            348.15    
P99 ITL (ms):                            365.30    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          44921.45  
Median E2EL (ms):                        43700.02  
P50 E2EL (ms):                           43700.02  
P90 E2EL (ms):                           79782.29  
P95 E2EL (ms):                           83211.57  
P99 E2EL (ms):                           87553.77  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

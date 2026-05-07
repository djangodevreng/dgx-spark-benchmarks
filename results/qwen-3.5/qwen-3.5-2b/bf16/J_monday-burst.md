# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-07 14:57:18
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  250.50    
Total input tokens:                      1201770   
Total generated tokens:                  150317    
Request throughput (req/s):              1.20      
Output token throughput (tok/s):         600.07    
Peak output token throughput (tok/s):    940.00    
Peak concurrent requests:                30.00     
Total token throughput (tok/s):          5397.56   
---------------Time to First Token----------------
Mean TTFT (ms):                          475.83    
Median TTFT (ms):                        470.08    
P50 TTFT (ms):                           470.08    
P90 TTFT (ms):                           731.75    
P95 TTFT (ms):                           899.16    
P99 TTFT (ms):                           1049.39   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          37.85     
Median TPOT (ms):                        38.36     
P50 TPOT (ms):                           38.36     
P90 TPOT (ms):                           40.80     
P95 TPOT (ms):                           42.05     
P99 TPOT (ms):                           45.31     
---------------Inter-token Latency----------------
Mean ITL (ms):                           38.22     
Median ITL (ms):                         27.27     
P50 ITL (ms):                            27.27     
P90 ITL (ms):                            65.57     
P95 ITL (ms):                            145.67    
P99 ITL (ms):                            154.11    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19366.91  
Median E2EL (ms):                        19063.11  
P50 E2EL (ms):                           19063.11  
P90 E2EL (ms):                           34422.25  
P95 E2EL (ms):                           35981.94  
P99 E2EL (ms):                           37261.96  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

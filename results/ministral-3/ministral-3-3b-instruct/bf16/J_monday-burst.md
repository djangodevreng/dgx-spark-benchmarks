# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-07 16:22:20
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  383.18    
Total input tokens:                      1198815   
Total generated tokens:                  150317    
Request throughput (req/s):              0.78      
Output token throughput (tok/s):         392.29    
Peak output token throughput (tok/s):    601.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          3520.91   
---------------Time to First Token----------------
Mean TTFT (ms):                          545.23    
Median TTFT (ms):                        514.07    
P50 TTFT (ms):                           514.07    
P90 TTFT (ms):                           799.03    
P95 TTFT (ms):                           982.88    
P99 TTFT (ms):                           1449.79   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          59.86     
Median TPOT (ms):                        60.67     
P50 TPOT (ms):                           60.67     
P90 TPOT (ms):                           65.33     
P95 TPOT (ms):                           67.95     
P99 TPOT (ms):                           72.36     
---------------Inter-token Latency----------------
Mean ITL (ms):                           59.42     
Median ITL (ms):                         44.96     
P50 ITL (ms):                            44.96     
P90 ITL (ms):                            57.38     
P95 ITL (ms):                            144.46    
P99 ITL (ms):                            462.95    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          30312.31  
Median E2EL (ms):                        29494.32  
P50 E2EL (ms):                           29494.32  
P90 E2EL (ms):                           54442.20  
P95 E2EL (ms):                           56816.38  
P99 E2EL (ms):                           59675.62  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

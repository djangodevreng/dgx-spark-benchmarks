# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-12 12:08:39
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  2668.57   
Total input tokens:                      1214714   
Total generated tokens:                  150317    
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         56.33     
Peak output token throughput (tok/s):    100.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          511.52    
---------------Time to First Token----------------
Mean TTFT (ms):                          6074.99   
Median TTFT (ms):                        3842.02   
P50 TTFT (ms):                           3842.02   
P90 TTFT (ms):                           6727.62   
P95 TTFT (ms):                           23125.37  
P99 TTFT (ms):                           53593.73  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          420.90    
Median TPOT (ms):                        419.22    
P50 TPOT (ms):                           419.22    
P90 TPOT (ms):                           453.07    
P95 TPOT (ms):                           484.78    
P99 TPOT (ms):                           576.57    
---------------Inter-token Latency----------------
Mean ITL (ms):                           430.95    
Median ITL (ms):                         301.93    
P50 ITL (ms):                            301.93    
P90 ITL (ms):                            308.91    
P95 ITL (ms):                            607.96    
P99 ITL (ms):                            4045.17   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          213915.68 
Median E2EL (ms):                        208726.83 
P50 E2EL (ms):                           208726.83 
P90 E2EL (ms):                           376081.32 
P95 E2EL (ms):                           391684.47 
P99 E2EL (ms):                           419990.49 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

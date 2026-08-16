# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-15 20:30:50
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B --tokenizer Qwen/Qwen3.8-27B --served-model-name qwen3.8-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3053.07   
Total input tokens:                      1213770   
Total generated tokens:                  150317    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         49.23     
Peak output token throughput (tok/s):    76.00     
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          446.79    
---------------Time to First Token----------------
Mean TTFT (ms):                          8348.08   
Median TTFT (ms):                        5393.80   
P50 TTFT (ms):                           5393.80   
P90 TTFT (ms):                           10589.83  
P95 TTFT (ms):                           28039.69  
P99 TTFT (ms):                           73914.67  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          481.30    
Median TPOT (ms):                        481.78    
P50 TPOT (ms):                           481.78    
P90 TPOT (ms):                           520.40    
P95 TPOT (ms):                           549.15    
P99 TPOT (ms):                           638.34    
---------------Inter-token Latency----------------
Mean ITL (ms):                           474.51    
Median ITL (ms):                         343.25    
P50 ITL (ms):                            343.25    
P90 ITL (ms):                            1087.95   
P95 ITL (ms):                            1616.54   
P99 ITL (ms):                            1860.83   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          245847.86 
Median E2EL (ms):                        237886.93 
P50 E2EL (ms):                           237886.93 
P90 E2EL (ms):                           430941.20 
P95 E2EL (ms):                           448648.23 
P99 E2EL (ms):                           483722.27 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-17 04:50:26
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  564.13    
Total input tokens:                      1200884   
Total generated tokens:                  150317    
Request throughput (req/s):              0.53      
Output token throughput (tok/s):         266.46    
Peak output token throughput (tok/s):    425.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2395.19   
---------------Time to First Token----------------
Mean TTFT (ms):                          976.52    
Median TTFT (ms):                        808.65    
P50 TTFT (ms):                           808.65    
P90 TTFT (ms):                           1379.89   
P95 TTFT (ms):                           2021.93   
P99 TTFT (ms):                           5289.65   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          88.74     
Median TPOT (ms):                        88.61     
P50 TPOT (ms):                           88.61     
P90 TPOT (ms):                           96.44     
P95 TPOT (ms):                           101.02    
P99 TPOT (ms):                           129.70    
---------------Inter-token Latency----------------
Mean ITL (ms):                           87.35     
Median ITL (ms):                         62.32     
P50 ITL (ms):                            62.32     
P90 ITL (ms):                            64.26     
P95 ITL (ms):                            71.95     
P99 ITL (ms):                            939.37    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          44743.19  
Median E2EL (ms):                        43695.74  
P50 E2EL (ms):                           43695.74  
P90 E2EL (ms):                           79706.14  
P95 E2EL (ms):                           82590.52  
P99 E2EL (ms):                           86863.90  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

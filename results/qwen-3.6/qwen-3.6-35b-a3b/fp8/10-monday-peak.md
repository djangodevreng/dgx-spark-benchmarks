# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-14 16:55:14
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  871.43    
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.34      
Output token throughput (tok/s):         172.49    
Peak output token throughput (tok/s):    288.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1550.88   
---------------Time to First Token----------------
Mean TTFT (ms):                          1928.01   
Median TTFT (ms):                        1542.16   
P50 TTFT (ms):                           1542.16   
P90 TTFT (ms):                           2738.98   
P95 TTFT (ms):                           4932.00   
P99 TTFT (ms):                           12421.37  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          138.61    
Median TPOT (ms):                        139.34    
P50 TPOT (ms):                           139.34    
P90 TPOT (ms):                           151.25    
P95 TPOT (ms):                           157.26    
P99 TPOT (ms):                           177.81    
---------------Inter-token Latency----------------
Mean ITL (ms):                           136.50    
Median ITL (ms):                         101.64    
P50 ITL (ms):                            101.64    
P90 ITL (ms):                            288.28    
P95 ITL (ms):                            488.63    
P99 ITL (ms):                            532.08    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          70233.84  
Median E2EL (ms):                        68267.39  
P50 E2EL (ms):                           68267.39  
P90 E2EL (ms):                           125128.35 
P95 E2EL (ms):                           130084.28 
P99 E2EL (ms):                           138544.25 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

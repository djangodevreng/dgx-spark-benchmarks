# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-14 13:30:13
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  488.82    
Total input tokens:                      1216617   
Total generated tokens:                  138550    
Request throughput (req/s):              0.61      
Output token throughput (tok/s):         283.44    
Peak output token throughput (tok/s):    325.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2772.33   
---------------Time to First Token----------------
Mean TTFT (ms):                          903.65    
Median TTFT (ms):                        748.93    
P50 TTFT (ms):                           748.93    
P90 TTFT (ms):                           1327.54   
P95 TTFT (ms):                           1936.71   
P99 TTFT (ms):                           4738.32   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          82.56     
Median TPOT (ms):                        82.74     
P50 TPOT (ms):                           82.74     
P90 TPOT (ms):                           89.59     
P95 TPOT (ms):                           94.48     
P99 TPOT (ms):                           122.49    
---------------Inter-token Latency----------------
Mean ITL (ms):                           282.40    
Median ITL (ms):                         57.73     
P50 ITL (ms):                            57.73     
P90 ITL (ms):                            62.88     
P95 ITL (ms):                            177.47    
P99 ITL (ms):                            1023.56   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          38745.73  
Median E2EL (ms):                        37034.27  
P50 E2EL (ms):                           37034.27  
P90 E2EL (ms):                           73674.30  
P95 E2EL (ms):                           76826.33  
P99 E2EL (ms):                           81645.71  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

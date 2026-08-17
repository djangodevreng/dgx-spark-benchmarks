# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-16 17:23:37
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  702.02    
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.43      
Output token throughput (tok/s):         214.12    
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1926.44   
---------------Time to First Token----------------
Mean TTFT (ms):                          1191.29   
Median TTFT (ms):                        969.38    
P50 TTFT (ms):                           969.38    
P90 TTFT (ms):                           1865.06   
P95 TTFT (ms):                           2480.96   
P99 TTFT (ms):                           6604.40   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          111.49    
Median TPOT (ms):                        111.67    
P50 TPOT (ms):                           111.67    
P90 TPOT (ms):                           120.82    
P95 TPOT (ms):                           126.99    
P99 TPOT (ms):                           152.46    
---------------Inter-token Latency----------------
Mean ITL (ms):                           109.78    
Median ITL (ms):                         81.59     
P50 ITL (ms):                            81.59     
P90 ITL (ms):                            84.48     
P95 ITL (ms):                            88.90     
P99 ITL (ms):                            1107.82   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          56196.36  
Median E2EL (ms):                        55020.62  
P50 E2EL (ms):                           55020.62  
P90 E2EL (ms):                           100379.38 
P95 E2EL (ms):                           103861.04 
P99 E2EL (ms):                           108628.75 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 22:06:50
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  735.59    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         131.99    
Peak output token throughput (tok/s):    295.00    
Peak concurrent requests:                33.00     
Total token throughput (tok/s):          1239.70   
---------------Time to First Token----------------
Mean TTFT (ms):                          2061.18   
Median TTFT (ms):                        1865.02   
P50 TTFT (ms):                           1865.02   
P90 TTFT (ms):                           3803.38   
P95 TTFT (ms):                           4280.11   
P99 TTFT (ms):                           5143.46   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          137.95    
Median TPOT (ms):                        140.74    
P50 TPOT (ms):                           140.74    
P90 TPOT (ms):                           159.77    
P95 TPOT (ms):                           172.77    
P99 TPOT (ms):                           193.33    
---------------Inter-token Latency----------------
Mean ITL (ms):                           136.08    
Median ITL (ms):                         103.89    
P50 ITL (ms):                            103.89    
P90 ITL (ms):                            132.61    
P95 ITL (ms):                            551.59    
P99 ITL (ms):                            572.27    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          68105.80  
Median E2EL (ms):                        67495.67  
P50 E2EL (ms):                           67495.67  
P90 E2EL (ms):                           115984.57 
P95 E2EL (ms):                           130975.08 
P99 E2EL (ms):                           141732.26 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-15 00:38:32
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     249       
Failed requests:                         1         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  894.02    
Total input tokens:                      57057     
Total generated tokens:                  52017     
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         58.18     
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                18.00     
Total token throughput (tok/s):          122.00    
---------------Time to First Token----------------
Mean TTFT (ms):                          876.31    
Median TTFT (ms):                        759.92    
P50 TTFT (ms):                           759.92    
P90 TTFT (ms):                           1642.53   
P95 TTFT (ms):                           1848.61   
P99 TTFT (ms):                           2345.87   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          154.33    
Median TPOT (ms):                        151.40    
P50 TPOT (ms):                           151.40    
P90 TPOT (ms):                           163.33    
P95 TPOT (ms):                           179.10    
P99 TPOT (ms):                           256.86    
---------------Inter-token Latency----------------
Mean ITL (ms):                           152.18    
Median ITL (ms):                         138.75    
P50 ITL (ms):                            138.75    
P90 ITL (ms):                            146.37    
P95 ITL (ms):                            164.86    
P99 ITL (ms):                            653.87    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          32664.87  
Median E2EL (ms):                        21848.49  
P50 E2EL (ms):                           21848.49  
P90 E2EL (ms):                           78113.39  
P95 E2EL (ms):                           98484.34  
P99 E2EL (ms):                           126872.80 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-15 00:23:27
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B-FP8 --tokenizer Qwen/Qwen3.6-27B-FP8 --served-model-name qwen3.6-27b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1776.05   
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         54.67     
Peak output token throughput (tok/s):    328.00    
Peak concurrent requests:                196.00    
Total token throughput (tok/s):          513.45    
---------------Time to First Token----------------
Mean TTFT (ms):                          404082.58 
Median TTFT (ms):                        419515.81 
P50 TTFT (ms):                           419515.81 
P90 TTFT (ms):                           713146.30 
P95 TTFT (ms):                           747800.62 
P99 TTFT (ms):                           797253.88 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          2008.52   
Median TPOT (ms):                        1964.65   
P50 TPOT (ms):                           1964.65   
P90 TPOT (ms):                           3527.22   
P95 TPOT (ms):                           3568.37   
P99 TPOT (ms):                           3625.49   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1653.88   
Median ITL (ms):                         676.06    
P50 ITL (ms):                            676.06    
P90 ITL (ms):                            3644.43   
P95 ITL (ms):                            3671.35   
P99 ITL (ms):                            3692.02   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1206354.54
Median E2EL (ms):                        1225730.47
P50 E2EL (ms):                           1225730.47
P90 E2EL (ms):                           1522371.67
P95 E2EL (ms):                           1605870.61
P99 E2EL (ms):                           1659387.24
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

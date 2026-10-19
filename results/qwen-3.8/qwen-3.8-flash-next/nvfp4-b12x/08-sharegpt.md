# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-10-18 16:34:05
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-Flash-Next-FP4-Local --tokenizer nvidia/Qwen3.8-Flash-Next-FP4-Local --served-model-name qwen3.8-flash-next --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  840.42    
Total input tokens:                      67729     
Total generated tokens:                  52014     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.89     
Peak output token throughput (tok/s):    65.00     
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          142.48    
---------------Time to First Token----------------
Mean TTFT (ms):                          651.26    
Median TTFT (ms):                        618.68    
P50 TTFT (ms):                           618.68    
P90 TTFT (ms):                           977.73    
P95 TTFT (ms):                           1076.69   
P99 TTFT (ms):                           1382.92   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          70.69     
Median TPOT (ms):                        71.61     
P50 TPOT (ms):                           71.61     
P90 TPOT (ms):                           102.28    
P95 TPOT (ms):                           110.43    
P99 TPOT (ms):                           128.53    
---------------Inter-token Latency----------------
Mean ITL (ms):                           158.50    
Median ITL (ms):                         154.18    
P50 ITL (ms):                            154.18    
P90 ITL (ms):                            222.08    
P95 ITL (ms):                            243.16    
P99 ITL (ms):                            531.95    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          16283.46  
Median E2EL (ms):                        8874.42   
P50 E2EL (ms):                           8874.42   
P90 E2EL (ms):                           40621.48  
P95 E2EL (ms):                           50885.28  
P99 E2EL (ms):                           72771.91  
---------------Speculative Decoding---------------
Acceptance rate (%):                     37.65     
Acceptance length:                       2.13      
Drafts:                                  24406     
Draft tokens:                            73218     
Accepted tokens:                         27565     
Per-position acceptance (%):
  Position 0:                            58.79     
  Position 1:                            33.89     
  Position 2:                            20.26     
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

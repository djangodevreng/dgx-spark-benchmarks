# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-10-18 16:53:10
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-Flash-Next-FP4-Local --tokenizer nvidia/Qwen3.8-Flash-Next-FP4-Local --served-model-name qwen3.8-flash-next --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1139.98   
Total input tokens:                      57622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         183.60    
Peak output token throughput (tok/s):    105.00    
Peak concurrent requests:                47.00     
Total token throughput (tok/s):          234.15    
---------------Time to First Token----------------
Mean TTFT (ms):                          147116.99 
Median TTFT (ms):                        1734.46   
P50 TTFT (ms):                           1734.46   
P90 TTFT (ms):                           411941.10 
P95 TTFT (ms):                           457854.55 
P99 TTFT (ms):                           475760.91 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          115.54    
Median TPOT (ms):                        115.51    
P50 TPOT (ms):                           115.51    
P90 TPOT (ms):                           146.13    
P95 TPOT (ms):                           159.08    
P99 TPOT (ms):                           171.99    
---------------Inter-token Latency----------------
Mean ITL (ms):                           302.08    
Median ITL (ms):                         322.81    
P50 ITL (ms):                            322.81    
P90 ITL (ms):                            334.77    
P95 ITL (ms):                            338.02    
P99 ITL (ms):                            762.22    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          601750.50 
Median E2EL (ms):                        613969.94 
P50 E2EL (ms):                           613969.94 
P90 E2EL (ms):                           889292.68 
P95 E2EL (ms):                           909912.40 
P99 E2EL (ms):                           926758.74 
---------------Speculative Decoding---------------
Acceptance rate (%):                     59.45     
Acceptance length:                       2.78      
Drafts:                                  75200     
Draft tokens:                            225600    
Accepted tokens:                         134110    
Per-position acceptance (%):
  Position 0:                            79.12     
  Position 1:                            64.82     
  Position 2:                            34.40     
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

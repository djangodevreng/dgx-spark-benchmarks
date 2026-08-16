# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-15 07:54:21
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  851.30    
Total input tokens:                      58416     
Total generated tokens:                  51465     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         60.45     
Peak output token throughput (tok/s):    52.00     
Peak concurrent requests:                18.00     
Total token throughput (tok/s):          129.07    
---------------Time to First Token----------------
Mean TTFT (ms):                          1135.29   
Median TTFT (ms):                        1089.43   
P50 TTFT (ms):                           1089.43   
P90 TTFT (ms):                           1521.62   
P95 TTFT (ms):                           1790.27   
P99 TTFT (ms):                           1990.92   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          130.39    
Median TPOT (ms):                        135.14    
P50 TPOT (ms):                           135.14    
P90 TPOT (ms):                           165.96    
P95 TPOT (ms):                           180.11    
P99 TPOT (ms):                           200.31    
---------------Inter-token Latency----------------
Mean ITL (ms):                           345.71    
Median ITL (ms):                         344.05    
P50 ITL (ms):                            344.05    
P90 ITL (ms):                            416.50    
P95 ITL (ms):                            471.87    
P99 ITL (ms):                            789.17    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          29339.91  
Median E2EL (ms):                        17722.20  
P50 E2EL (ms):                           17722.20  
P90 E2EL (ms):                           74848.65  
P95 E2EL (ms):                           88796.64  
P99 E2EL (ms):                           116544.60 
---------------Speculative Decoding---------------
Acceptance rate (%):                     51.79     
Acceptance length:                       2.55      
Drafts:                                  20152     
Draft tokens:                            60456     
Accepted tokens:                         31308     
Per-position acceptance (%):
  Position 0:                            73.41     
  Position 1:                            50.07     
  Position 2:                            31.88     
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

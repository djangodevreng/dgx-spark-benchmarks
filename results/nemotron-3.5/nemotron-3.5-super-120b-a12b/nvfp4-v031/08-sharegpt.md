# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-10-18 10:14:57
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --served-model-name nemotron-3.5-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  838.50    
Total input tokens:                      58416     
Total generated tokens:                  51879     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.87     
Peak output token throughput (tok/s):    54.00     
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          131.54    
---------------Time to First Token----------------
Mean TTFT (ms):                          651.88    
Median TTFT (ms):                        653.22    
P50 TTFT (ms):                           653.22    
P90 TTFT (ms):                           925.89    
P95 TTFT (ms):                           992.47    
P99 TTFT (ms):                           1070.73   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          69.90     
Median TPOT (ms):                        71.01     
P50 TPOT (ms):                           71.01     
P90 TPOT (ms):                           95.60     
P95 TPOT (ms):                           101.96    
P99 TPOT (ms):                           114.86    
---------------Inter-token Latency----------------
Mean ITL (ms):                           199.57    
Median ITL (ms):                         203.21    
P50 ITL (ms):                            203.21    
P90 ITL (ms):                            278.36    
P95 ITL (ms):                            299.42    
P99 ITL (ms):                            395.44    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          14852.25  
Median E2EL (ms):                        8895.70   
P50 E2EL (ms):                           8895.70   
P90 E2EL (ms):                           37215.68  
P95 E2EL (ms):                           42203.96  
P99 E2EL (ms):                           59593.66  
---------------Speculative Decoding---------------
Acceptance rate (%):                     65.06     
Acceptance length:                       2.95      
Drafts:                                  17587     
Draft tokens:                            52761     
Accepted tokens:                         34325     
Per-position acceptance (%):
  Position 0:                            81.78     
  Position 1:                            64.21     
  Position 2:                            49.18     
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-09 12:43:53
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-Cascade-2-30B-A3B --tokenizer nvidia/Nemotron-Cascade-2-30B-A3B --served-model-name nemotron-cascade-2-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  858.35    
Total input tokens:                      62488     
Total generated tokens:                  52471     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         61.13     
Peak output token throughput (tok/s):    114.00    
Peak concurrent requests:                19.00     
Total token throughput (tok/s):          133.93    
---------------Time to First Token----------------
Mean TTFT (ms):                          491.20    
Median TTFT (ms):                        489.13    
P50 TTFT (ms):                           489.13    
P90 TTFT (ms):                           646.43    
P95 TTFT (ms):                           700.40    
P99 TTFT (ms):                           743.20    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          124.35    
Median TPOT (ms):                        134.12    
P50 TPOT (ms):                           134.12    
P90 TPOT (ms):                           156.37    
P95 TPOT (ms):                           161.31    
P99 TPOT (ms):                           185.56    
---------------Inter-token Latency----------------
Mean ITL (ms):                           125.28    
Median ITL (ms):                         136.24    
P50 ITL (ms):                            136.24    
P90 ITL (ms):                            157.60    
P95 ITL (ms):                            178.50    
P99 ITL (ms):                            281.48    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          26785.40  
Median E2EL (ms):                        15803.81  
P50 E2EL (ms):                           15803.81  
P90 E2EL (ms):                           67588.67  
P95 E2EL (ms):                           81485.73  
P99 E2EL (ms):                           111120.20 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

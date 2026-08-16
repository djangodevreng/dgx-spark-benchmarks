# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-13 18:10:23
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Kwaipilot/KAT-Coder-V2.5-Dev --tokenizer Kwaipilot/KAT-Coder-V2.5-Dev --served-model-name kat-coder-v2-5-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  840.11    
Total input tokens:                      57229     
Total generated tokens:                  51737     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.58     
Peak output token throughput (tok/s):    135.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          129.70    
---------------Time to First Token----------------
Mean TTFT (ms):                          386.42    
Median TTFT (ms):                        386.45    
P50 TTFT (ms):                           386.45    
P90 TTFT (ms):                           539.95    
P95 TTFT (ms):                           574.37    
P99 TTFT (ms):                           727.63    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          90.33     
Median TPOT (ms):                        87.28     
P50 TPOT (ms):                           87.28     
P90 TPOT (ms):                           130.59    
P95 TPOT (ms):                           132.36    
P99 TPOT (ms):                           143.13    
---------------Inter-token Latency----------------
Mean ITL (ms):                           90.63     
Median ITL (ms):                         82.89     
P50 ITL (ms):                            82.89     
P90 ITL (ms):                            128.88    
P95 ITL (ms):                            132.65    
P99 ITL (ms):                            232.48    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19142.66  
Median E2EL (ms):                        10005.50  
P50 E2EL (ms):                           10005.50  
P90 E2EL (ms):                           48322.91  
P95 E2EL (ms):                           66161.45  
P99 E2EL (ms):                           83661.68  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

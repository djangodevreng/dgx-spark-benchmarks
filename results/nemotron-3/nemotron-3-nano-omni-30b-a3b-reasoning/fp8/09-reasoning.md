# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-06 05:13:59
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --served-model-name nemotron-3-nano-omni-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  699.25    
Total input tokens:                      55836     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         299.33    
Peak output token throughput (tok/s):    224.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          379.18    
---------------Time to First Token----------------
Mean TTFT (ms):                          794.34    
Median TTFT (ms):                        815.82    
P50 TTFT (ms):                           815.82    
P90 TTFT (ms):                           1099.14   
P95 TTFT (ms):                           1423.10   
P99 TTFT (ms):                           1461.38   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          83.34     
Median TPOT (ms):                        83.89     
P50 TPOT (ms):                           83.89     
P90 TPOT (ms):                           95.01     
P95 TPOT (ms):                           98.18     
P99 TPOT (ms):                           101.66    
---------------Inter-token Latency----------------
Mean ITL (ms):                           190.93    
Median ITL (ms):                         85.07     
P50 ITL (ms):                            85.07     
P90 ITL (ms):                            163.93    
P95 ITL (ms):                            187.46    
P99 ITL (ms):                            211.26    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          340560.74 
Median E2EL (ms):                        349402.46 
P50 E2EL (ms):                           349402.46 
P90 E2EL (ms):                           500200.21 
P95 E2EL (ms):                           550173.34 
P99 E2EL (ms):                           574298.62 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

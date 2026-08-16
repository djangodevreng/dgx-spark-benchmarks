# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-13 18:33:54
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Kwaipilot/KAT-Coder-V2.5-Dev --tokenizer Kwaipilot/KAT-Coder-V2.5-Dev --served-model-name kat-coder-v2-5-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1399.87   
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         149.52    
Peak output token throughput (tok/s):    246.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          189.18    
---------------Time to First Token----------------
Mean TTFT (ms):                          706.55    
Median TTFT (ms):                        711.60    
P50 TTFT (ms):                           711.60    
P90 TTFT (ms):                           934.59    
P95 TTFT (ms):                           1018.60   
P99 TTFT (ms):                           1073.72   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          198.58    
Median TPOT (ms):                        197.56    
P50 TPOT (ms):                           197.56    
P90 TPOT (ms):                           222.89    
P95 TPOT (ms):                           226.82    
P99 TPOT (ms):                           231.46    
---------------Inter-token Latency----------------
Mean ITL (ms):                           193.03    
Median ITL (ms):                         206.35    
P50 ITL (ms):                            206.35    
P90 ITL (ms):                            231.40    
P95 ITL (ms):                            243.56    
P99 ITL (ms):                            260.44    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          808741.63 
Median E2EL (ms):                        819852.87 
P50 E2EL (ms):                           819852.87 
P90 E2EL (ms):                           1173330.64
P95 E2EL (ms):                           1260841.35
P99 E2EL (ms):                           1297081.48
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

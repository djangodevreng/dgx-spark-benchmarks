# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 03:17:43
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1219.85   
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.16      
Output token throughput (tok/s):         79.59     
Peak output token throughput (tok/s):    328.00    
Peak concurrent requests:                175.00    
Total token throughput (tok/s):          747.55    
---------------Time to First Token----------------
Mean TTFT (ms):                          81481.57  
Median TTFT (ms):                        82171.42  
P50 TTFT (ms):                           82171.42  
P90 TTFT (ms):                           141781.37 
P95 TTFT (ms):                           149996.11 
P99 TTFT (ms):                           169012.02 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1280.79   
Median TPOT (ms):                        1258.14   
P50 TPOT (ms):                           1258.14   
P90 TPOT (ms):                           2001.32   
P95 TPOT (ms):                           2039.54   
P99 TPOT (ms):                           2094.06   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1104.65   
Median ITL (ms):                         642.16    
P50 ITL (ms):                            642.16    
P90 ITL (ms):                            2114.79   
P95 ITL (ms):                            2137.29   
P99 ITL (ms):                            2166.02   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          617303.90 
Median E2EL (ms):                        619407.00 
P50 E2EL (ms):                           619407.00 
P90 E2EL (ms):                           914721.17 
P95 E2EL (ms):                           983166.02 
P99 E2EL (ms):                           1047452.89
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

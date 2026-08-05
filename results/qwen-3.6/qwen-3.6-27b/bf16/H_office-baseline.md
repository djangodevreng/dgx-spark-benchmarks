# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-10 00:53:58
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1553.82   
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.13      
Output token throughput (tok/s):         62.49     
Peak output token throughput (tok/s):    268.00    
Peak concurrent requests:                186.00    
Total token throughput (tok/s):          586.88    
---------------Time to First Token----------------
Mean TTFT (ms):                          183195.28 
Median TTFT (ms):                        150986.59 
P50 TTFT (ms):                           150986.59 
P90 TTFT (ms):                           464243.19 
P95 TTFT (ms):                           496152.58 
P99 TTFT (ms):                           548599.56 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1651.97   
Median TPOT (ms):                        1708.60   
P50 TPOT (ms):                           1708.60   
P90 TPOT (ms):                           2506.32   
P95 TPOT (ms):                           2729.58   
P99 TPOT (ms):                           2909.53   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1446.19   
Median ITL (ms):                         629.02    
P50 ITL (ms):                            629.02    
P90 ITL (ms):                            3290.44   
P95 ITL (ms):                            3311.12   
P99 ITL (ms):                            3340.34   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          880409.32 
Median E2EL (ms):                        903206.02 
P50 E2EL (ms):                           903206.02 
P90 E2EL (ms):                           1219583.93
P95 E2EL (ms):                           1289753.57
P99 E2EL (ms):                           1354266.55
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

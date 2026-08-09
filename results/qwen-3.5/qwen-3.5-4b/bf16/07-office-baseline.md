# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 17:58:51
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  696.69    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         139.36    
Peak output token throughput (tok/s):    300.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1308.91   
---------------Time to First Token----------------
Mean TTFT (ms):                          1026.65   
Median TTFT (ms):                        961.29    
P50 TTFT (ms):                           961.29    
P90 TTFT (ms):                           1744.18   
P95 TTFT (ms):                           2163.37   
P99 TTFT (ms):                           2685.26   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          54.97     
Median TPOT (ms):                        54.67     
P50 TPOT (ms):                           54.67     
P90 TPOT (ms):                           63.90     
P95 TPOT (ms):                           67.76     
P99 TPOT (ms):                           73.10     
---------------Inter-token Latency----------------
Mean ITL (ms):                           54.73     
Median ITL (ms):                         45.88     
P50 ITL (ms):                            45.88     
P90 ITL (ms):                            50.52     
P95 ITL (ms):                            59.93     
P99 ITL (ms):                            329.45    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          27577.28  
Median E2EL (ms):                        27476.73  
P50 E2EL (ms):                           27476.73  
P90 E2EL (ms):                           47636.79  
P95 E2EL (ms):                           52356.34  
P99 E2EL (ms):                           55766.89  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

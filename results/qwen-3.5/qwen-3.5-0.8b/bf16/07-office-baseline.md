# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 09:46:42
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  669.89    
Total input tokens:                      815212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         144.94    
Peak output token throughput (tok/s):    551.00    
Peak concurrent requests:                6.00      
Total token throughput (tok/s):          1361.87   
---------------Time to First Token----------------
Mean TTFT (ms):                          219.19    
Median TTFT (ms):                        213.17    
P50 TTFT (ms):                           213.17    
P90 TTFT (ms):                           354.52    
P95 TTFT (ms):                           381.62    
P99 TTFT (ms):                           500.70    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          9.04      
Median TPOT (ms):                        8.85      
P50 TPOT (ms):                           8.85      
P90 TPOT (ms):                           9.86      
P95 TPOT (ms):                           10.33     
P99 TPOT (ms):                           11.42     
---------------Inter-token Latency----------------
Mean ITL (ms):                           9.00      
Median ITL (ms):                         8.61      
P50 ITL (ms):                            8.61      
P90 ITL (ms):                            9.89      
P95 ITL (ms):                            10.39     
P99 ITL (ms):                            12.70     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4586.04   
Median E2EL (ms):                        4543.96   
P50 E2EL (ms):                           4543.96   
P90 E2EL (ms):                           7913.53   
P95 E2EL (ms):                           8395.82   
P99 E2EL (ms):                           8814.11   
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

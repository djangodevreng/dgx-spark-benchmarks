# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-04 23:27:50
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  669.97    
Total input tokens:                      815212    
Total generated tokens:                  97092     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         144.92    
Peak output token throughput (tok/s):    547.00    
Peak concurrent requests:                6.00      
Total token throughput (tok/s):          1361.71   
---------------Time to First Token----------------
Mean TTFT (ms):                          234.18    
Median TTFT (ms):                        223.66    
P50 TTFT (ms):                           223.66    
P90 TTFT (ms):                           372.20    
P95 TTFT (ms):                           451.44    
P99 TTFT (ms):                           811.54    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          9.22      
Median TPOT (ms):                        9.06      
P50 TPOT (ms):                           9.06      
P90 TPOT (ms):                           10.04     
P95 TPOT (ms):                           10.51     
P99 TPOT (ms):                           11.64     
---------------Inter-token Latency----------------
Mean ITL (ms):                           9.25      
Median ITL (ms):                         8.77      
P50 ITL (ms):                            8.77      
P90 ITL (ms):                            9.70      
P95 ITL (ms):                            10.19     
P99 ITL (ms):                            21.93     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4688.10   
Median E2EL (ms):                        4621.30   
P50 E2EL (ms):                           4621.30   
P90 E2EL (ms):                           8057.72   
P95 E2EL (ms):                           8514.24   
P99 E2EL (ms):                           9040.13   
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

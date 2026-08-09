# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 17:15:04
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model LiquidAI/LFM2.5-2.6B --tokenizer LiquidAI/LFM2.5-2.6B --served-model-name lfm2-5-2-6b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  838.31    
Total input tokens:                      56970     
Total generated tokens:                  51916     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.93     
Peak output token throughput (tok/s):    287.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          129.89    
---------------Time to First Token----------------
Mean TTFT (ms):                          86.52     
Median TTFT (ms):                        85.80     
P50 TTFT (ms):                           85.80     
P90 TTFT (ms):                           112.56    
P95 TTFT (ms):                           123.28    
P99 TTFT (ms):                           142.18    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          25.88     
Median TPOT (ms):                        25.03     
P50 TPOT (ms):                           25.03     
P90 TPOT (ms):                           29.80     
P95 TPOT (ms):                           30.33     
P99 TPOT (ms):                           30.56     
---------------Inter-token Latency----------------
Mean ITL (ms):                           25.63     
Median ITL (ms):                         24.87     
P50 ITL (ms):                            24.87     
P90 ITL (ms):                            30.33     
P95 ITL (ms):                            30.93     
P99 ITL (ms):                            32.16     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          5408.06   
Median E2EL (ms):                        3591.96   
P50 E2EL (ms):                           3591.96   
P90 E2EL (ms):                           12904.04  
P95 E2EL (ms):                           16824.94  
P99 E2EL (ms):                           20651.13  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-08 17:22:41
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model LiquidAI/LFM2.5-2.6B --tokenizer LiquidAI/LFM2.5-2.6B --served-model-name lfm2-5-2-6b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  445.94    
Total input tokens:                      55505     
Total generated tokens:                  209303    
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         469.36    
Peak output token throughput (tok/s):    797.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          593.82    
---------------Time to First Token----------------
Mean TTFT (ms):                          166.81    
Median TTFT (ms):                        173.73    
P50 TTFT (ms):                           173.73    
P90 TTFT (ms):                           223.16    
P95 TTFT (ms):                           227.53    
P99 TTFT (ms):                           240.03    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          31.86     
Median TPOT (ms):                        32.45     
P50 TPOT (ms):                           32.45     
P90 TPOT (ms):                           34.08     
P95 TPOT (ms):                           34.32     
P99 TPOT (ms):                           34.40     
---------------Inter-token Latency----------------
Mean ITL (ms):                           31.90     
Median ITL (ms):                         32.65     
P50 ITL (ms):                            32.65     
P90 ITL (ms):                            35.21     
P95 ITL (ms):                            35.98     
P99 ITL (ms):                            38.92     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          133696.17 
Median E2EL (ms):                        128325.79 
P50 E2EL (ms):                           128325.79 
P90 E2EL (ms):                           212356.15 
P95 E2EL (ms):                           233295.10 
P99 E2EL (ms):                           242677.43 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

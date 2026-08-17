# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-17 06:50:09
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  419.02    
Total input tokens:                      55484     
Total generated tokens:                  209303    
Request throughput (req/s):              0.12      
Output token throughput (tok/s):         499.51    
Peak output token throughput (tok/s):    850.00    
Peak concurrent requests:                25.00     
Total token throughput (tok/s):          631.93    
---------------Time to First Token----------------
Mean TTFT (ms):                          186.91    
Median TTFT (ms):                        187.35    
P50 TTFT (ms):                           187.35    
P90 TTFT (ms):                           243.25    
P95 TTFT (ms):                           250.21    
P99 TTFT (ms):                           279.51    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          27.86     
Median TPOT (ms):                        28.45     
P50 TPOT (ms):                           28.45     
P90 TPOT (ms):                           29.76     
P95 TPOT (ms):                           29.92     
P99 TPOT (ms):                           30.07     
---------------Inter-token Latency----------------
Mean ITL (ms):                           27.90     
Median ITL (ms):                         28.63     
P50 ITL (ms):                            28.63     
P90 ITL (ms):                            30.42     
P95 ITL (ms):                            30.98     
P99 ITL (ms):                            39.44     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          116979.05 
Median E2EL (ms):                        111590.02 
P50 E2EL (ms):                           111590.02 
P90 E2EL (ms):                           186593.49 
P95 E2EL (ms):                           204226.39 
P99 E2EL (ms):                           213956.09 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

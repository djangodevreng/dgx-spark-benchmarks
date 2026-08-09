# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-06 10:16:33
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1069.90   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.05      
Output token throughput (tok/s):         195.63    
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          247.68    
---------------Time to First Token----------------
Mean TTFT (ms):                          579.96    
Median TTFT (ms):                        569.98    
P50 TTFT (ms):                           569.98    
P90 TTFT (ms):                           738.33    
P95 TTFT (ms):                           752.35    
P99 TTFT (ms):                           930.24    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          143.96    
Median TPOT (ms):                        145.13    
P50 TPOT (ms):                           145.13    
P90 TPOT (ms):                           160.86    
P95 TPOT (ms):                           164.35    
P99 TPOT (ms):                           167.58    
---------------Inter-token Latency----------------
Mean ITL (ms):                           139.63    
Median ITL (ms):                         139.37    
P50 ITL (ms):                            139.37    
P90 ITL (ms):                            170.27    
P95 ITL (ms):                            172.36    
P99 ITL (ms):                            177.21    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          585089.92 
Median E2EL (ms):                        590365.02 
P50 E2EL (ms):                           590365.02 
P90 E2EL (ms):                           851658.70 
P95 E2EL (ms):                           919430.93 
P99 E2EL (ms):                           952588.62 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-14 16:40:30
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  866.86    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.06      
Output token throughput (tok/s):         241.45    
Peak output token throughput (tok/s):    368.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          305.50    
---------------Time to First Token----------------
Mean TTFT (ms):                          502.31    
Median TTFT (ms):                        493.37    
P50 TTFT (ms):                           493.37    
P90 TTFT (ms):                           669.84    
P95 TTFT (ms):                           760.21    
P99 TTFT (ms):                           799.77    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          108.10    
Median TPOT (ms):                        109.34    
P50 TPOT (ms):                           109.34    
P90 TPOT (ms):                           123.36    
P95 TPOT (ms):                           125.81    
P99 TPOT (ms):                           129.39    
---------------Inter-token Latency----------------
Mean ITL (ms):                           106.68    
Median ITL (ms):                         109.18    
P50 ITL (ms):                            109.18    
P90 ITL (ms):                            131.15    
P95 ITL (ms):                            132.45    
P99 ITL (ms):                            136.32    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          446924.55 
Median E2EL (ms):                        457771.63 
P50 E2EL (ms):                           457771.63 
P90 E2EL (ms):                           668975.36 
P95 E2EL (ms):                           720974.62 
P99 E2EL (ms):                           746958.37 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

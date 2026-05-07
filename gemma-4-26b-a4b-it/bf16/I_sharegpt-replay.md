# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 22:07:07
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  839.10    
Total input tokens:                      60269     
Total generated tokens:                  51299     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.14     
Peak output token throughput (tok/s):    123.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          132.96    
---------------Time to First Token----------------
Mean TTFT (ms):                          375.70    
Median TTFT (ms):                        352.93    
P50 TTFT (ms):                           352.93    
P90 TTFT (ms):                           468.61    
P95 TTFT (ms):                           509.38    
P99 TTFT (ms):                           637.02    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          93.06     
Median TPOT (ms):                        95.32     
P50 TPOT (ms):                           95.32     
P90 TPOT (ms):                           117.34    
P95 TPOT (ms):                           123.12    
P99 TPOT (ms):                           134.73    
---------------Inter-token Latency----------------
Mean ITL (ms):                           93.70     
Median ITL (ms):                         93.22     
P50 ITL (ms):                            93.22     
P90 ITL (ms):                            120.79    
P95 ITL (ms):                            129.34    
P99 ITL (ms):                            206.96    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19600.43  
Median E2EL (ms):                        10922.65  
P50 E2EL (ms):                           10922.65  
P90 E2EL (ms):                           49525.50  
P95 E2EL (ms):                           63036.36  
P99 E2EL (ms):                           82596.97  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

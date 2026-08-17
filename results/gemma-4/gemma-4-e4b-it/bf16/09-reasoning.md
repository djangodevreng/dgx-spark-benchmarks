# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-17 04:40:50
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  638.96    
Total input tokens:                      55484     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         327.57    
Peak output token throughput (tok/s):    645.00    
Peak concurrent requests:                43.00     
Total token throughput (tok/s):          414.40    
---------------Time to First Token----------------
Mean TTFT (ms):                          329.22    
Median TTFT (ms):                        317.82    
P50 TTFT (ms):                           317.82    
P90 TTFT (ms):                           439.64    
P95 TTFT (ms):                           450.67    
P99 TTFT (ms):                           468.40    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          61.65     
Median TPOT (ms):                        62.10     
P50 TPOT (ms):                           62.10     
P90 TPOT (ms):                           65.88     
P95 TPOT (ms):                           66.87     
P99 TPOT (ms):                           68.16     
---------------Inter-token Latency----------------
Mean ITL (ms):                           61.58     
Median ITL (ms):                         62.18     
P50 ITL (ms):                            62.18     
P90 ITL (ms):                            69.05     
P95 ITL (ms):                            70.42     
P99 ITL (ms):                            79.76     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          258118.39 
Median E2EL (ms):                        250096.44 
P50 E2EL (ms):                           250096.44 
P90 E2EL (ms):                           400208.23 
P95 E2EL (ms):                           438962.11 
P99 E2EL (ms):                           450848.54 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

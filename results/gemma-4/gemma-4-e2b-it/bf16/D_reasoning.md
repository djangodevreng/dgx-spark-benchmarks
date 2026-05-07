# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-06 12:26:13
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  422.53    
Total input tokens:                      55484     
Total generated tokens:                  209303    
Request throughput (req/s):              0.12      
Output token throughput (tok/s):         495.36    
Peak output token throughput (tok/s):    857.00    
Peak concurrent requests:                26.00     
Total token throughput (tok/s):          626.67    
---------------Time to First Token----------------
Mean TTFT (ms):                          180.20    
Median TTFT (ms):                        180.91    
P50 TTFT (ms):                           180.91    
P90 TTFT (ms):                           230.97    
P95 TTFT (ms):                           250.80    
P99 TTFT (ms):                           303.56    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          28.24     
Median TPOT (ms):                        28.66     
P50 TPOT (ms):                           28.66     
P90 TPOT (ms):                           29.94     
P95 TPOT (ms):                           29.98     
P99 TPOT (ms):                           30.13     
---------------Inter-token Latency----------------
Mean ITL (ms):                           28.26     
Median ITL (ms):                         28.70     
P50 ITL (ms):                            28.70     
P90 ITL (ms):                            30.61     
P95 ITL (ms):                            31.26     
P99 ITL (ms):                            40.50     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          118485.79 
Median E2EL (ms):                        112799.81 
P50 E2EL (ms):                           112799.81 
P90 E2EL (ms):                           187780.13 
P95 E2EL (ms):                           206104.12 
P99 E2EL (ms):                           215255.55 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.

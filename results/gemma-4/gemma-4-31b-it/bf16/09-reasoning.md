# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-06 21:41:40
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  3138.08   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         66.70     
Peak output token throughput (tok/s):    151.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          84.44     
---------------Time to First Token----------------
Mean TTFT (ms):                          2099.62   
Median TTFT (ms):                        2091.18   
P50 TTFT (ms):                           2091.18   
P90 TTFT (ms):                           2858.29   
P95 TTFT (ms):                           3206.86   
P99 TTFT (ms):                           3597.44   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          443.13    
Median TPOT (ms):                        449.68    
P50 TPOT (ms):                           449.68    
P90 TPOT (ms):                           463.31    
P95 TPOT (ms):                           467.94    
P99 TPOT (ms):                           471.08    
---------------Inter-token Latency----------------
Mean ITL (ms):                           434.59    
Median ITL (ms):                         448.29    
P50 ITL (ms):                            448.29    
P90 ITL (ms):                            464.28    
P95 ITL (ms):                            466.52    
P99 ITL (ms):                            470.87    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1821332.71
Median E2EL (ms):                        1763693.65
P50 E2EL (ms):                           1763693.65
P90 E2EL (ms):                           2740835.52
P95 E2EL (ms):                           2937623.95
P99 E2EL (ms):                           3004571.68
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

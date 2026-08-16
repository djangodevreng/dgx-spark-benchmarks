# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-14 04:17:33
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  2611.07   
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         80.16     
Peak output token throughput (tok/s):    150.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          101.42    
---------------Time to First Token----------------
Mean TTFT (ms):                          1873.13   
Median TTFT (ms):                        1777.00   
P50 TTFT (ms):                           1777.00   
P90 TTFT (ms):                           2587.08   
P95 TTFT (ms):                           2865.71   
P99 TTFT (ms):                           3200.72   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          365.54    
Median TPOT (ms):                        371.09    
P50 TPOT (ms):                           371.09    
P90 TPOT (ms):                           381.44    
P95 TPOT (ms):                           385.90    
P99 TPOT (ms):                           390.82    
---------------Inter-token Latency----------------
Mean ITL (ms):                           358.79    
Median ITL (ms):                         367.79    
P50 ITL (ms):                            367.79    
P90 ITL (ms):                            379.66    
P95 ITL (ms):                            381.32    
P99 ITL (ms):                            403.01    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1503170.21
Median E2EL (ms):                        1455182.43
P50 E2EL (ms):                           1455182.43
P90 E2EL (ms):                           2259298.97
P95 E2EL (ms):                           2428817.89
P99 E2EL (ms):                           2482488.39
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

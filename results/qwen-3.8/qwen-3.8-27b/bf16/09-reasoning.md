# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-15 19:39:44
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B --tokenizer Qwen/Qwen3.8-27B --served-model-name qwen3.8-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  2616.66   
Total input tokens:                      57622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         79.99     
Peak output token throughput (tok/s):    150.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          102.01    
---------------Time to First Token----------------
Mean TTFT (ms):                          1889.96   
Median TTFT (ms):                        1797.45   
P50 TTFT (ms):                           1797.45   
P90 TTFT (ms):                           2624.52   
P95 TTFT (ms):                           2874.47   
P99 TTFT (ms):                           3157.65   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          365.28    
Median TPOT (ms):                        370.94    
P50 TPOT (ms):                           370.94    
P90 TPOT (ms):                           379.81    
P95 TPOT (ms):                           382.86    
P99 TPOT (ms):                           387.58    
---------------Inter-token Latency----------------
Mean ITL (ms):                           358.96    
Median ITL (ms):                         363.81    
P50 ITL (ms):                            363.81    
P90 ITL (ms):                            376.22    
P95 ITL (ms):                            378.19    
P99 ITL (ms):                            742.45    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1504049.94
Median E2EL (ms):                        1455660.58
P50 E2EL (ms):                           1455660.58
P90 E2EL (ms):                           2263712.96
P95 E2EL (ms):                           2433987.04
P99 E2EL (ms):                           2487832.65
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

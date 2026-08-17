# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 13:48:48
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  838.68    
Total input tokens:                      60269     
Total generated tokens:                  51230     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.08     
Peak output token throughput (tok/s):    123.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          132.95    
---------------Time to First Token----------------
Mean TTFT (ms):                          366.79    
Median TTFT (ms):                        364.13    
P50 TTFT (ms):                           364.13    
P90 TTFT (ms):                           474.15    
P95 TTFT (ms):                           503.97    
P99 TTFT (ms):                           585.64    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          94.55     
Median TPOT (ms):                        96.44     
P50 TPOT (ms):                           96.44     
P90 TPOT (ms):                           122.94    
P95 TPOT (ms):                           128.57    
P99 TPOT (ms):                           138.76    
---------------Inter-token Latency----------------
Mean ITL (ms):                           95.52     
Median ITL (ms):                         95.12     
P50 ITL (ms):                            95.12     
P90 ITL (ms):                            124.04    
P95 ITL (ms):                            131.89    
P99 ITL (ms):                            210.08    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19941.21  
Median E2EL (ms):                        10769.47  
P50 E2EL (ms):                           10769.47  
P90 E2EL (ms):                           49908.92  
P95 E2EL (ms):                           66398.36  
P99 E2EL (ms):                           88473.83  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 09:58:34
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  839.03    
Total input tokens:                      60269     
Total generated tokens:                  51352     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.20     
Peak output token throughput (tok/s):    128.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          133.04    
---------------Time to First Token----------------
Mean TTFT (ms):                          359.77    
Median TTFT (ms):                        353.52    
P50 TTFT (ms):                           353.52    
P90 TTFT (ms):                           474.39    
P95 TTFT (ms):                           510.01    
P99 TTFT (ms):                           563.97    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          95.80     
Median TPOT (ms):                        98.60     
P50 TPOT (ms):                           98.60     
P90 TPOT (ms):                           122.64    
P95 TPOT (ms):                           128.81    
P99 TPOT (ms):                           139.42    
---------------Inter-token Latency----------------
Mean ITL (ms):                           96.87     
Median ITL (ms):                         96.15     
P50 ITL (ms):                            96.15     
P90 ITL (ms):                            124.25    
P95 ITL (ms):                            131.93    
P99 ITL (ms):                            214.10    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          20258.37  
Median E2EL (ms):                        10923.95  
P50 E2EL (ms):                           10923.95  
P90 E2EL (ms):                           50990.11  
P95 E2EL (ms):                           68698.03  
P99 E2EL (ms):                           89016.55  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

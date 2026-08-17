# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-17 06:42:58
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.72    
Total input tokens:                      59269     
Total generated tokens:                  51329     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.57     
Peak output token throughput (tok/s):    315.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          132.66    
---------------Time to First Token----------------
Mean TTFT (ms):                          99.67     
Median TTFT (ms):                        90.04     
P50 TTFT (ms):                           90.04     
P90 TTFT (ms):                           148.03    
P95 TTFT (ms):                           170.38    
P99 TTFT (ms):                           334.15    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          22.77     
Median TPOT (ms):                        22.22     
P50 TPOT (ms):                           22.22     
P90 TPOT (ms):                           24.94     
P95 TPOT (ms):                           25.11     
P99 TPOT (ms):                           25.32     
---------------Inter-token Latency----------------
Mean ITL (ms):                           22.58     
Median ITL (ms):                         22.01     
P50 ITL (ms):                            22.01     
P90 ITL (ms):                            25.25     
P95 ITL (ms):                            25.80     
P99 ITL (ms):                            32.75     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4736.74   
Median E2EL (ms):                        2933.79   
P50 E2EL (ms):                           2933.79   
P90 E2EL (ms):                           11475.97  
P95 E2EL (ms):                           15264.77  
P99 E2EL (ms):                           19457.40  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 10:00:48
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.71    
Total input tokens:                      57729     
Total generated tokens:                  50063     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         59.98     
Peak output token throughput (tok/s):    638.00    
Peak concurrent requests:                6.00      
Total token throughput (tok/s):          129.14    
---------------Time to First Token----------------
Mean TTFT (ms):                          35.83     
Median TTFT (ms):                        35.69     
P50 TTFT (ms):                           35.69     
P90 TTFT (ms):                           48.48     
P95 TTFT (ms):                           51.40     
P99 TTFT (ms):                           69.59     
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          8.45      
Median TPOT (ms):                        8.49      
P50 TPOT (ms):                           8.49      
P90 TPOT (ms):                           8.74      
P95 TPOT (ms):                           8.83      
P99 TPOT (ms):                           9.24      
---------------Inter-token Latency----------------
Mean ITL (ms):                           8.33      
Median ITL (ms):                         8.31      
P50 ITL (ms):                            8.31      
P90 ITL (ms):                            9.39      
P95 ITL (ms):                            9.77      
P99 ITL (ms):                            10.64     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1703.93   
Median E2EL (ms):                        1103.98   
P50 E2EL (ms):                           1103.98   
P90 E2EL (ms):                           4142.98   
P95 E2EL (ms):                           5470.40   
P99 E2EL (ms):                           6789.68   
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

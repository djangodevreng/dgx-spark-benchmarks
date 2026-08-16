# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-15 18:55:59
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.8-27B --tokenizer Qwen/Qwen3.8-27B --served-model-name qwen3.8-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  958.68    
Total input tokens:                      67729     
Total generated tokens:                  51929     
Request throughput (req/s):              0.26      
Output token throughput (tok/s):         54.17     
Peak output token throughput (tok/s):    100.00    
Peak concurrent requests:                34.00     
Total token throughput (tok/s):          124.82    
---------------Time to First Token----------------
Mean TTFT (ms):                          1072.41   
Median TTFT (ms):                        1008.21   
P50 TTFT (ms):                           1008.21   
P90 TTFT (ms):                           1494.92   
P95 TTFT (ms):                           1599.18   
P99 TTFT (ms):                           1916.34   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          330.10    
Median TPOT (ms):                        341.48    
P50 TPOT (ms):                           341.48    
P90 TPOT (ms):                           358.12    
P95 TPOT (ms):                           372.22    
P99 TPOT (ms):                           389.21    
---------------Inter-token Latency----------------
Mean ITL (ms):                           329.40    
Median ITL (ms):                         324.69    
P50 ITL (ms):                            324.69    
P90 ITL (ms):                            374.13    
P95 ITL (ms):                            459.70    
P99 ITL (ms):                            716.51    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          69438.87  
Median E2EL (ms):                        43541.95  
P50 E2EL (ms):                           43541.95  
P90 E2EL (ms):                           169503.61 
P95 E2EL (ms):                           214353.05 
P99 E2EL (ms):                           282161.35 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

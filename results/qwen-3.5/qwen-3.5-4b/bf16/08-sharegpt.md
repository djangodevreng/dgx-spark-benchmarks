# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-07 18:13:02
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  840.02    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         62.96     
Peak output token throughput (tok/s):    216.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.09    
---------------Time to First Token----------------
Mean TTFT (ms):                          150.36    
Median TTFT (ms):                        145.76    
P50 TTFT (ms):                           145.76    
P90 TTFT (ms):                           195.50    
P95 TTFT (ms):                           228.77    
P99 TTFT (ms):                           250.67    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          41.53     
Median TPOT (ms):                        41.25     
P50 TPOT (ms):                           41.25     
P90 TPOT (ms):                           43.29     
P95 TPOT (ms):                           45.27     
P99 TPOT (ms):                           48.03     
---------------Inter-token Latency----------------
Mean ITL (ms):                           41.31     
Median ITL (ms):                         40.69     
P50 ITL (ms):                            40.69     
P90 ITL (ms):                            43.53     
P95 ITL (ms):                            47.94     
P99 ITL (ms):                            55.91     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          8887.09   
Median E2EL (ms):                        5891.39   
P50 E2EL (ms):                           5891.39   
P90 E2EL (ms):                           20757.12  
P95 E2EL (ms):                           27277.01  
P99 E2EL (ms):                           34892.54  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

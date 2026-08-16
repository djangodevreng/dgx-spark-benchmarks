# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 16:25:55
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B-FP8 --tokenizer Qwen/Qwen3.6-35B-A3B-FP8 --served-model-name qwen3.6-35b-a3b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  836.39    
Total input tokens:                      57229     
Total generated tokens:                  52850     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         63.19     
Peak output token throughput (tok/s):    168.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.61    
---------------Time to First Token----------------
Mean TTFT (ms):                          192.77    
Median TTFT (ms):                        187.74    
P50 TTFT (ms):                           187.74    
P90 TTFT (ms):                           288.13    
P95 TTFT (ms):                           312.56    
P99 TTFT (ms):                           375.55    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          33.99     
Median TPOT (ms):                        32.17     
P50 TPOT (ms):                           32.17     
P90 TPOT (ms):                           48.01     
P95 TPOT (ms):                           51.08     
P99 TPOT (ms):                           68.88     
---------------Inter-token Latency----------------
Mean ITL (ms):                           32.89     
Median ITL (ms):                         31.10     
P50 ITL (ms):                            31.10     
P90 ITL (ms):                            47.00     
P95 ITL (ms):                            48.13     
P99 ITL (ms):                            82.06     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7143.92   
Median E2EL (ms):                        4265.91   
P50 E2EL (ms):                           4265.91   
P90 E2EL (ms):                           17381.66  
P95 E2EL (ms):                           20890.37  
P99 E2EL (ms):                           31100.50  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

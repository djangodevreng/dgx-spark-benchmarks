# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 08:33:33
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  837.04    
Total input tokens:                      57229     
Total generated tokens:                  52890     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         63.19     
Peak output token throughput (tok/s):    195.00    
Peak concurrent requests:                9.00      
Total token throughput (tok/s):          131.56    
---------------Time to First Token----------------
Mean TTFT (ms):                          154.15    
Median TTFT (ms):                        144.34    
P50 TTFT (ms):                           144.34    
P90 TTFT (ms):                           226.18    
P95 TTFT (ms):                           243.98    
P99 TTFT (ms):                           292.18    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          29.57     
Median TPOT (ms):                        28.76     
P50 TPOT (ms):                           28.76     
P90 TPOT (ms):                           38.05     
P95 TPOT (ms):                           39.23     
P99 TPOT (ms):                           42.78     
---------------Inter-token Latency----------------
Mean ITL (ms):                           29.20     
Median ITL (ms):                         28.03     
P50 ITL (ms):                            28.03     
P90 ITL (ms):                            37.96     
P95 ITL (ms):                            38.84     
P99 ITL (ms):                            58.98     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          6332.03   
Median E2EL (ms):                        3957.23   
P50 E2EL (ms):                           3957.23   
P90 E2EL (ms):                           15309.85  
P95 E2EL (ms):                           18025.24  
P99 E2EL (ms):                           26216.60  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

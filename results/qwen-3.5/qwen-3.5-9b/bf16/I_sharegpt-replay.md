# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-09 16:34:43
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  858.43    
Total input tokens:                      57229     
Total generated tokens:                  52755     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         61.46     
Peak output token throughput (tok/s):    169.00    
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          128.12    
---------------Time to First Token----------------
Mean TTFT (ms):                          250.70    
Median TTFT (ms):                        244.22    
P50 TTFT (ms):                           244.22    
P90 TTFT (ms):                           314.27    
P95 TTFT (ms):                           344.99    
P99 TTFT (ms):                           399.23    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          76.50     
Median TPOT (ms):                        75.90     
P50 TPOT (ms):                           75.90     
P90 TPOT (ms):                           78.55     
P95 TPOT (ms):                           79.92     
P99 TPOT (ms):                           87.54     
---------------Inter-token Latency----------------
Mean ITL (ms):                           75.78     
Median ITL (ms):                         74.96     
P50 ITL (ms):                            74.96     
P90 ITL (ms):                            77.56     
P95 ITL (ms):                            78.55     
P99 ITL (ms):                            114.27    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          16235.85  
Median E2EL (ms):                        10723.75  
P50 E2EL (ms):                           10723.75  
P90 E2EL (ms):                           38409.17  
P95 E2EL (ms):                           49597.11  
P99 E2EL (ms):                           63053.72  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

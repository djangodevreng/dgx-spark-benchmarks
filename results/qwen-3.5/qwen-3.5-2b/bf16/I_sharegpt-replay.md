# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-07 14:52:53
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  836.94    
Total input tokens:                      57729     
Total generated tokens:                  50473     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.31     
Peak output token throughput (tok/s):    371.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          129.28    
---------------Time to First Token----------------
Mean TTFT (ms):                          80.53     
Median TTFT (ms):                        75.93     
P50 TTFT (ms):                           75.93     
P90 TTFT (ms):                           112.18    
P95 TTFT (ms):                           126.04    
P99 TTFT (ms):                           175.59    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          19.59     
Median TPOT (ms):                        18.78     
P50 TPOT (ms):                           18.78     
P90 TPOT (ms):                           22.69     
P95 TPOT (ms):                           22.79     
P99 TPOT (ms):                           23.04     
---------------Inter-token Latency----------------
Mean ITL (ms):                           19.39     
Median ITL (ms):                         18.46     
P50 ITL (ms):                            18.46     
P90 ITL (ms):                            22.87     
P95 ITL (ms):                            23.25     
P99 ITL (ms):                            28.81     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          3992.48   
Median E2EL (ms):                        2586.62   
P50 E2EL (ms):                           2586.62   
P90 E2EL (ms):                           9636.10   
P95 E2EL (ms):                           12873.73  
P99 E2EL (ms):                           16987.49  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

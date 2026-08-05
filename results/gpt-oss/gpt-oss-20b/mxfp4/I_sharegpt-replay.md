# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-26 11:12:24
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  835.07    
Total input tokens:                      69764     
Total generated tokens:                  44889     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         53.75     
Peak output token throughput (tok/s):    149.00    
Peak concurrent requests:                8.00      
Total token throughput (tok/s):          137.30    
---------------Time to First Token----------------
Mean TTFT (ms):                          122.88    
Median TTFT (ms):                        118.16    
P50 TTFT (ms):                           118.16    
P90 TTFT (ms):                           171.34    
P95 TTFT (ms):                           183.73    
P99 TTFT (ms):                           206.12    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          28.38     
Median TPOT (ms):                        29.08     
P50 TPOT (ms):                           29.08     
P90 TPOT (ms):                           35.57     
P95 TPOT (ms):                           36.73     
P99 TPOT (ms):                           39.08     
---------------Inter-token Latency----------------
Mean ITL (ms):                           32.13     
Median ITL (ms):                         24.78     
P50 ITL (ms):                            24.78     
P90 ITL (ms):                            35.58     
P95 ITL (ms):                            37.62     
P99 ITL (ms):                            68.03     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          5270.27   
Median E2EL (ms):                        3189.07   
P50 E2EL (ms):                           3189.07   
P90 E2EL (ms):                           13425.00  
P95 E2EL (ms):                           15480.67  
P99 E2EL (ms):                           21985.09  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

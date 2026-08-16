# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 13:12:39
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.98    
Total input tokens:                      69630     
Total generated tokens:                  45680     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         54.71     
Peak output token throughput (tok/s):    170.00    
Peak concurrent requests:                9.00      
Total token throughput (tok/s):          138.10    
---------------Time to First Token----------------
Mean TTFT (ms):                          124.47    
Median TTFT (ms):                        120.18    
P50 TTFT (ms):                           120.18    
P90 TTFT (ms):                           168.12    
P95 TTFT (ms):                           182.75    
P99 TTFT (ms):                           201.14    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          52.41     
Median TPOT (ms):                        28.33     
P50 TPOT (ms):                           28.33     
P90 TPOT (ms):                           34.20     
P95 TPOT (ms):                           36.77     
P99 TPOT (ms):                           39.80     
---------------Inter-token Latency----------------
Mean ITL (ms):                           30.99     
Median ITL (ms):                         26.07     
P50 ITL (ms):                            26.07     
P90 ITL (ms):                            35.33     
P95 ITL (ms):                            37.32     
P99 ITL (ms):                            65.41     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          5298.94   
Median E2EL (ms):                        3102.33   
P50 E2EL (ms):                           3102.33   
P90 E2EL (ms):                           13357.68  
P95 E2EL (ms):                           15729.19  
P99 E2EL (ms):                           23211.64  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

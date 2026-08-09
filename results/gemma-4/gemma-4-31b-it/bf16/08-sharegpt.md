# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 20:49:13
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  999.43    
Total input tokens:                      60269     
Total generated tokens:                  50876     
Request throughput (req/s):              0.25      
Output token throughput (tok/s):         50.91     
Peak output token throughput (tok/s):    100.00    
Peak concurrent requests:                34.00     
Total token throughput (tok/s):          111.21    
---------------Time to First Token----------------
Mean TTFT (ms):                          1126.24   
Median TTFT (ms):                        1049.51   
P50 TTFT (ms):                           1049.51   
P90 TTFT (ms):                           1547.43   
P95 TTFT (ms):                           1686.04   
P99 TTFT (ms):                           1999.68   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          360.24    
Median TPOT (ms):                        367.59    
P50 TPOT (ms):                           367.59    
P90 TPOT (ms):                           383.56    
P95 TPOT (ms):                           392.46    
P99 TPOT (ms):                           443.15    
---------------Inter-token Latency----------------
Mean ITL (ms):                           358.99    
Median ITL (ms):                         356.42    
P50 ITL (ms):                            356.42    
P90 ITL (ms):                            365.07    
P95 ITL (ms):                            374.76    
P99 ITL (ms):                            826.28    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          74182.54  
Median E2EL (ms):                        45682.27  
P50 E2EL (ms):                           45682.27  
P90 E2EL (ms):                           188422.53 
P95 E2EL (ms):                           224412.53 
P99 E2EL (ms):                           313655.59 
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

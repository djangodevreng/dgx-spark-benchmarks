# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-13 11:45:16
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Mistral-Small-4-119B-2603-NVFP4 --tokenizer mistralai/Mistral-Small-4-119B-2603-NVFP4 --served-model-name mistral-small-4-119b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  855.52    
Total input tokens:                      57988     
Total generated tokens:                  50273     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         58.76     
Peak output token throughput (tok/s):    108.00    
Peak concurrent requests:                13.00     
Total token throughput (tok/s):          126.54    
---------------Time to First Token----------------
Mean TTFT (ms):                          405.13    
Median TTFT (ms):                        402.31    
P50 TTFT (ms):                           402.31    
P90 TTFT (ms):                           566.33    
P95 TTFT (ms):                           624.36    
P99 TTFT (ms):                           679.24    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          77.29     
Median TPOT (ms):                        79.75     
P50 TPOT (ms):                           79.75     
P90 TPOT (ms):                           105.25    
P95 TPOT (ms):                           113.98    
P99 TPOT (ms):                           138.93    
---------------Inter-token Latency----------------
Mean ITL (ms):                           75.79     
Median ITL (ms):                         76.03     
P50 ITL (ms):                            76.03     
P90 ITL (ms):                            102.48    
P95 ITL (ms):                            108.13    
P99 ITL (ms):                            257.30    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          15646.26  
Median E2EL (ms):                        8603.75   
P50 E2EL (ms):                           8603.75   
P90 E2EL (ms):                           39658.39  
P95 E2EL (ms):                           47360.99  
P99 E2EL (ms):                           64523.24  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

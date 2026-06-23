# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 05:12:43
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-mtp --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  835.25    
Total input tokens:                      60269     
Total generated tokens:                  51340     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.47     
Peak output token throughput (tok/s):    66.00     
Peak concurrent requests:                12.00     
Total token throughput (tok/s):          133.62    
---------------Time to First Token----------------
Mean TTFT (ms):                          406.65    
Median TTFT (ms):                        409.19    
P50 TTFT (ms):                           409.19    
P90 TTFT (ms):                           532.40    
P95 TTFT (ms):                           576.82    
P99 TTFT (ms):                           640.31    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          50.61     
Median TPOT (ms):                        49.63     
P50 TPOT (ms):                           49.63     
P90 TPOT (ms):                           67.12     
P95 TPOT (ms):                           77.32     
P99 TPOT (ms):                           121.23    
---------------Inter-token Latency----------------
Mean ITL (ms):                           132.08    
Median ITL (ms):                         136.89    
P50 ITL (ms):                            136.89    
P90 ITL (ms):                            171.83    
P95 ITL (ms):                            189.78    
P99 ITL (ms):                            251.57    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          10026.06  
Median E2EL (ms):                        6110.34   
P50 E2EL (ms):                           6110.34   
P90 E2EL (ms):                           25221.25  
P95 E2EL (ms):                           30037.99  
P99 E2EL (ms):                           43119.19  
---------------Speculative Decoding---------------
Acceptance rate (%):                     46.59     
Acceptance length:                       2.86      
Drafts:                                  17958     
Draft tokens:                            71832     
Accepted tokens:                         33463     
Per-position acceptance (%):
  Position 0:                            72.63     
  Position 1:                            51.49     
  Position 2:                            36.13     
  Position 3:                            26.09     
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

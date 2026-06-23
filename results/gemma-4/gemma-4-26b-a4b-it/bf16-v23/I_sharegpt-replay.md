# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 01:11:16
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  838.42    
Total input tokens:                      60269     
Total generated tokens:                  51083     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.93     
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          132.81    
---------------Time to First Token----------------
Mean TTFT (ms):                          331.48    
Median TTFT (ms):                        327.05    
P50 TTFT (ms):                           327.05    
P90 TTFT (ms):                           430.67    
P95 TTFT (ms):                           456.10    
P99 TTFT (ms):                           507.19    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          86.86     
Median TPOT (ms):                        89.20     
P50 TPOT (ms):                           89.20     
P90 TPOT (ms):                           110.44    
P95 TPOT (ms):                           115.31    
P99 TPOT (ms):                           126.37    
---------------Inter-token Latency----------------
Mean ITL (ms):                           86.90     
Median ITL (ms):                         87.23     
P50 ITL (ms):                            87.23     
P90 ITL (ms):                            110.91    
P95 ITL (ms):                            115.69    
P99 ITL (ms):                            200.96    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          18087.39  
Median E2EL (ms):                        9845.55   
P50 E2EL (ms):                           9845.55   
P90 E2EL (ms):                           45499.76  
P95 E2EL (ms):                           58387.64  
P99 E2EL (ms):                           76117.64  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

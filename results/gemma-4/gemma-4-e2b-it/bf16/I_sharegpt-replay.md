# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 12:59:25
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E2B-it --tokenizer google/gemma-4-E2B-it --served-model-name gemma-4-e2b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.73    
Total input tokens:                      59269     
Total generated tokens:                  51199     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.41     
Peak output token throughput (tok/s):    276.00    
Peak concurrent requests:                7.00      
Total token throughput (tok/s):          132.50    
---------------Time to First Token----------------
Mean TTFT (ms):                          97.82     
Median TTFT (ms):                        85.44     
P50 TTFT (ms):                           85.44     
P90 TTFT (ms):                           158.00    
P95 TTFT (ms):                           195.31    
P99 TTFT (ms):                           285.98    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          23.84     
Median TPOT (ms):                        23.53     
P50 TPOT (ms):                           23.53     
P90 TPOT (ms):                           25.61     
P95 TPOT (ms):                           25.73     
P99 TPOT (ms):                           26.03     
---------------Inter-token Latency----------------
Mean ITL (ms):                           23.65     
Median ITL (ms):                         23.23     
P50 ITL (ms):                            23.23     
P90 ITL (ms):                            25.74     
P95 ITL (ms):                            26.09     
P99 ITL (ms):                            32.96     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4942.06   
Median E2EL (ms):                        3085.58   
P50 E2EL (ms):                           3085.58   
P90 E2EL (ms):                           12044.84  
P95 E2EL (ms):                           15917.53  
P99 E2EL (ms):                           20394.68  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

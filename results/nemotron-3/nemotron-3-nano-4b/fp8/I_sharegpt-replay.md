# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 18:37:53
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.67    
Total input tokens:                      58416     
Total generated tokens:                  51216     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.43     
Peak output token throughput (tok/s):    267.00    
Peak concurrent requests:                8.00      
Total token throughput (tok/s):          131.51    
---------------Time to First Token----------------
Mean TTFT (ms):                          97.20     
Median TTFT (ms):                        93.03     
P50 TTFT (ms):                           93.03     
P90 TTFT (ms):                           142.79    
P95 TTFT (ms):                           151.50    
P99 TTFT (ms):                           177.08    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          23.77     
Median TPOT (ms):                        23.48     
P50 TPOT (ms):                           23.48     
P90 TPOT (ms):                           25.34     
P95 TPOT (ms):                           25.90     
P99 TPOT (ms):                           27.54     
---------------Inter-token Latency----------------
Mean ITL (ms):                           23.56     
Median ITL (ms):                         23.30     
P50 ITL (ms):                            23.30     
P90 ITL (ms):                            25.17     
P95 ITL (ms):                            25.85     
P99 ITL (ms):                            29.55     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4924.34   
Median E2EL (ms):                        3196.66   
P50 E2EL (ms):                           3196.66   
P90 E2EL (ms):                           11737.21  
P95 E2EL (ms):                           14794.93  
P99 E2EL (ms):                           19481.43  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

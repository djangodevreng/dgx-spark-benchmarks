# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-03 12:18:49
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --served-model-name nemotron-3-nano-omni-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.79    
Total input tokens:                      58416     
Total generated tokens:                  51232     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.44     
Peak output token throughput (tok/s):    152.00    
Peak concurrent requests:                12.00     
Total token throughput (tok/s):          131.51    
---------------Time to First Token----------------
Mean TTFT (ms):                          225.88    
Median TTFT (ms):                        220.04    
P50 TTFT (ms):                           220.04    
P90 TTFT (ms):                           315.66    
P95 TTFT (ms):                           352.99    
P99 TTFT (ms):                           422.19    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          39.37     
Median TPOT (ms):                        37.54     
P50 TPOT (ms):                           37.54     
P90 TPOT (ms):                           57.87     
P95 TPOT (ms):                           61.72     
P99 TPOT (ms):                           73.64     
---------------Inter-token Latency----------------
Mean ITL (ms):                           38.85     
Median ITL (ms):                         36.15     
P50 ITL (ms):                            36.15     
P90 ITL (ms):                            55.75     
P95 ITL (ms):                            67.86     
P99 ITL (ms):                            100.32    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          8173.09   
Median E2EL (ms):                        4697.56   
P50 E2EL (ms):                           4697.56   
P90 E2EL (ms):                           19935.76  
P95 E2EL (ms):                           25082.78  
P99 E2EL (ms):                           32847.18  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

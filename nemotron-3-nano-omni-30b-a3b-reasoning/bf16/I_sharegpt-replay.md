# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-03 14:42:56
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  843.21    
Total input tokens:                      58416     
Total generated tokens:                  50924     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.39     
Peak output token throughput (tok/s):    113.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          129.67    
---------------Time to First Token----------------
Mean TTFT (ms):                          439.99    
Median TTFT (ms):                        432.93    
P50 TTFT (ms):                           432.93    
P90 TTFT (ms):                           594.01    
P95 TTFT (ms):                           652.73    
P99 TTFT (ms):                           713.10    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          111.51    
Median TPOT (ms):                        118.47    
P50 TPOT (ms):                           118.47    
P90 TPOT (ms):                           149.10    
P95 TPOT (ms):                           155.20    
P99 TPOT (ms):                           166.76    
---------------Inter-token Latency----------------
Mean ITL (ms):                           112.25    
Median ITL (ms):                         101.05    
P50 ITL (ms):                            101.05    
P90 ITL (ms):                            149.02    
P95 ITL (ms):                            157.06    
P99 ITL (ms):                            271.21    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          23267.90  
Median E2EL (ms):                        12886.03  
P50 E2EL (ms):                           12886.03  
P90 E2EL (ms):                           58423.24  
P95 E2EL (ms):                           71216.50  
P99 E2EL (ms):                           98107.64  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

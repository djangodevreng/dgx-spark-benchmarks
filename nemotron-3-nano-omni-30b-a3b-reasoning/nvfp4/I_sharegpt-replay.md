# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-03 10:39:49
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.70    
Total input tokens:                      58416     
Total generated tokens:                  51085     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.28     
Peak output token throughput (tok/s):    199.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.34    
---------------Time to First Token----------------
Mean TTFT (ms):                          210.77    
Median TTFT (ms):                        157.33    
P50 TTFT (ms):                           157.33    
P90 TTFT (ms):                           258.88    
P95 TTFT (ms):                           310.00    
P99 TTFT (ms):                           1360.81   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          26.33     
Median TPOT (ms):                        26.38     
P50 TPOT (ms):                           26.38     
P90 TPOT (ms):                           36.41     
P95 TPOT (ms):                           38.63     
P99 TPOT (ms):                           43.52     
---------------Inter-token Latency----------------
Mean ITL (ms):                           26.23     
Median ITL (ms):                         23.30     
P50 ITL (ms):                            23.30     
P90 ITL (ms):                            37.09     
P95 ITL (ms):                            38.70     
P99 ITL (ms):                            54.54     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          5554.74   
Median E2EL (ms):                        3260.52   
P50 E2EL (ms):                           3260.52   
P90 E2EL (ms):                           13793.66  
P95 E2EL (ms):                           16247.68  
P99 E2EL (ms):                           23595.57  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.

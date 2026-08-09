# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 05:02:09
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8 --served-model-name nemotron-3-nano-omni-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  834.10    
Total input tokens:                      58416     
Total generated tokens:                  51237     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.43     
Peak output token throughput (tok/s):    152.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.46    
---------------Time to First Token----------------
Mean TTFT (ms):                          277.93    
Median TTFT (ms):                        196.26    
P50 TTFT (ms):                           196.26    
P90 TTFT (ms):                           672.73    
P95 TTFT (ms):                           707.61    
P99 TTFT (ms):                           1118.86   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          35.70     
Median TPOT (ms):                        33.53     
P50 TPOT (ms):                           33.53     
P90 TPOT (ms):                           53.88     
P95 TPOT (ms):                           57.25     
P99 TPOT (ms):                           73.56     
---------------Inter-token Latency----------------
Mean ITL (ms):                           35.18     
Median ITL (ms):                         33.03     
P50 ITL (ms):                            33.03     
P90 ITL (ms):                            51.70     
P95 ITL (ms):                            57.53     
P99 ITL (ms):                            104.25    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7366.15   
Median E2EL (ms):                        4419.10   
P50 E2EL (ms):                           4419.10   
P90 E2EL (ms):                           17847.03  
P95 E2EL (ms):                           22968.64  
P99 E2EL (ms):                           30055.96  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-08 01:52:05
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --served-model-name nemotron-3-nano-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  642.86    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         325.58    
Peak output token throughput (tok/s):    608.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          412.39    
---------------Time to First Token----------------
Mean TTFT (ms):                          598.12    
Median TTFT (ms):                        619.98    
P50 TTFT (ms):                           619.98    
P90 TTFT (ms):                           745.80    
P95 TTFT (ms):                           842.88    
P99 TTFT (ms):                           1033.76   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          82.73     
Median TPOT (ms):                        81.57     
P50 TPOT (ms):                           81.57     
P90 TPOT (ms):                           100.71    
P95 TPOT (ms):                           105.16    
P99 TPOT (ms):                           109.75    
---------------Inter-token Latency----------------
Mean ITL (ms):                           78.06     
Median ITL (ms):                         77.09     
P50 ITL (ms):                            77.09     
P90 ITL (ms):                            110.35    
P95 ITL (ms):                            112.76    
P99 ITL (ms):                            122.72    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          327374.14 
Median E2EL (ms):                        347086.56 
P50 E2EL (ms):                           347086.56 
P90 E2EL (ms):                           466951.76 
P95 E2EL (ms):                           497688.84 
P99 E2EL (ms):                           529198.23 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

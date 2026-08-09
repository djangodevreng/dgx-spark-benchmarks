# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-07 13:42:36
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  469.79    
Total input tokens:                      55836     
Total generated tokens:                  209303    
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         445.52    
Peak output token throughput (tok/s):    191.00    
Peak concurrent requests:                35.00     
Total token throughput (tok/s):          564.38    
---------------Time to First Token----------------
Mean TTFT (ms):                          531.45    
Median TTFT (ms):                        587.71    
P50 TTFT (ms):                           587.71    
P90 TTFT (ms):                           727.31    
P95 TTFT (ms):                           824.42    
P99 TTFT (ms):                           967.31    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          42.66     
Median TPOT (ms):                        43.42     
P50 TPOT (ms):                           43.42     
P90 TPOT (ms):                           48.88     
P95 TPOT (ms):                           49.37     
P99 TPOT (ms):                           50.76     
---------------Inter-token Latency----------------
Mean ITL (ms):                           183.08    
Median ITL (ms):                         43.52     
P50 ITL (ms):                            43.52     
P90 ITL (ms):                            84.23     
P95 ITL (ms):                            91.46     
P99 ITL (ms):                            134.38    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          176543.11 
Median E2EL (ms):                        183733.74 
P50 E2EL (ms):                           183733.74 
P90 E2EL (ms):                           268046.91 
P95 E2EL (ms):                           302423.31 
P99 E2EL (ms):                           318083.89 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

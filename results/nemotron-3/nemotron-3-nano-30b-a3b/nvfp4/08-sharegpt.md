# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-13 14:58:41
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --served-model-name nemotron-3-nano-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.98    
Total input tokens:                      58416     
Total generated tokens:                  51605     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.88     
Peak output token throughput (tok/s):    202.00    
Peak concurrent requests:                9.00      
Total token throughput (tok/s):          131.92    
---------------Time to First Token----------------
Mean TTFT (ms):                          150.12    
Median TTFT (ms):                        137.91    
P50 TTFT (ms):                           137.91    
P90 TTFT (ms):                           215.63    
P95 TTFT (ms):                           236.27    
P99 TTFT (ms):                           513.13    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          22.59     
Median TPOT (ms):                        21.05     
P50 TPOT (ms):                           21.05     
P90 TPOT (ms):                           32.92     
P95 TPOT (ms):                           35.72     
P99 TPOT (ms):                           37.67     
---------------Inter-token Latency----------------
Mean ITL (ms):                           22.19     
Median ITL (ms):                         18.29     
P50 ITL (ms):                            18.29     
P90 ITL (ms):                            33.85     
P95 ITL (ms):                            35.07     
P99 ITL (ms):                            48.21     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          4728.95   
Median E2EL (ms):                        2762.57   
P50 E2EL (ms):                           2762.57   
P90 E2EL (ms):                           11822.39  
P95 E2EL (ms):                           13703.96  
P99 E2EL (ms):                           19965.41  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

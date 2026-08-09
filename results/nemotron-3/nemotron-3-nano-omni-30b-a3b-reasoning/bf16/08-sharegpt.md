# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 02:00:14
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  841.75    
Total input tokens:                      58416     
Total generated tokens:                  51153     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.77     
Peak output token throughput (tok/s):    111.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          130.17    
---------------Time to First Token----------------
Mean TTFT (ms):                          442.25    
Median TTFT (ms):                        432.84    
P50 TTFT (ms):                           432.84    
P90 TTFT (ms):                           588.46    
P95 TTFT (ms):                           635.37    
P99 TTFT (ms):                           765.83    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          110.76    
Median TPOT (ms):                        114.95    
P50 TPOT (ms):                           114.95    
P90 TPOT (ms):                           148.33    
P95 TPOT (ms):                           154.55    
P99 TPOT (ms):                           164.39    
---------------Inter-token Latency----------------
Mean ITL (ms):                           113.34    
Median ITL (ms):                         99.93     
P50 ITL (ms):                            99.93     
P90 ITL (ms):                            148.38    
P95 ITL (ms):                            170.06    
P99 ITL (ms):                            287.54    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          23244.27  
Median E2EL (ms):                        13000.71  
P50 E2EL (ms):                           13000.71  
P90 E2EL (ms):                           57978.88  
P95 E2EL (ms):                           71769.00  
P99 E2EL (ms):                           97520.58  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.

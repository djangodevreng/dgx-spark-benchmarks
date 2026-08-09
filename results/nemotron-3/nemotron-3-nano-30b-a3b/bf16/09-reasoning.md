# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-09 05:06:35
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --served-model-name nemotron-3-nano-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  927.90    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.05      
Output token throughput (tok/s):         225.57    
Peak output token throughput (tok/s):    400.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          285.71    
---------------Time to First Token----------------
Mean TTFT (ms):                          646.82    
Median TTFT (ms):                        662.49    
P50 TTFT (ms):                           662.49    
P90 TTFT (ms):                           787.73    
P95 TTFT (ms):                           843.00    
P99 TTFT (ms):                           885.21    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          135.20    
Median TPOT (ms):                        134.42    
P50 TPOT (ms):                           134.42    
P90 TPOT (ms):                           169.18    
P95 TPOT (ms):                           181.30    
P99 TPOT (ms):                           184.43    
---------------Inter-token Latency----------------
Mean ITL (ms):                           125.57    
Median ITL (ms):                         109.32    
P50 ITL (ms):                            109.32    
P90 ITL (ms):                            182.42    
P95 ITL (ms):                            198.90    
P99 ITL (ms):                            212.81    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          526301.68 
Median E2EL (ms):                        550507.89 
P50 E2EL (ms):                           550507.89 
P90 E2EL (ms):                           730032.57 
P95 E2EL (ms):                           786492.06 
P99 E2EL (ms):                           823460.31 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

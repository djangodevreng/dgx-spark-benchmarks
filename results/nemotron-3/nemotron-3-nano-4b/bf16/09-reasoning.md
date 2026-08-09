# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-06 07:04:45
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  615.51    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         340.05    
Peak output token throughput (tok/s):    588.00    
Peak concurrent requests:                42.00     
Total token throughput (tok/s):          430.71    
---------------Time to First Token----------------
Mean TTFT (ms):                          285.58    
Median TTFT (ms):                        280.71    
P50 TTFT (ms):                           280.71    
P90 TTFT (ms):                           383.82    
P95 TTFT (ms):                           410.88    
P99 TTFT (ms):                           422.41    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          62.15     
Median TPOT (ms):                        63.49     
P50 TPOT (ms):                           63.49     
P90 TPOT (ms):                           69.87     
P95 TPOT (ms):                           70.47     
P99 TPOT (ms):                           73.03     
---------------Inter-token Latency----------------
Mean ITL (ms):                           61.71     
Median ITL (ms):                         63.70     
P50 ITL (ms):                            63.70     
P90 ITL (ms):                            74.00     
P95 ITL (ms):                            75.76     
P99 ITL (ms):                            98.36     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          258619.27 
Median E2EL (ms):                        259735.54 
P50 E2EL (ms):                           259735.54 
P90 E2EL (ms):                           394346.04 
P95 E2EL (ms):                           434184.43 
P99 E2EL (ms):                           448196.98 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

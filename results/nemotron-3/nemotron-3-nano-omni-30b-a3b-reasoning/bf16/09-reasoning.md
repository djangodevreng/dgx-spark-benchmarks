# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-06 02:17:47
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 --served-model-name nemotron-3-nano-omni-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1044.40   
Total input tokens:                      55836     
Total generated tokens:                  209303    
Request throughput (req/s):              0.05      
Output token throughput (tok/s):         200.41    
Peak output token throughput (tok/s):    133.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          253.87    
---------------Time to First Token----------------
Mean TTFT (ms):                          651.77    
Median TTFT (ms):                        650.31    
P50 TTFT (ms):                           650.31    
P90 TTFT (ms):                           803.44    
P95 TTFT (ms):                           835.59    
P99 TTFT (ms):                           907.54    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          145.08    
Median TPOT (ms):                        146.35    
P50 TPOT (ms):                           146.35    
P90 TPOT (ms):                           167.67    
P95 TPOT (ms):                           170.72    
P99 TPOT (ms):                           175.09    
---------------Inter-token Latency----------------
Mean ITL (ms):                           379.71    
Median ITL (ms):                         160.95    
P50 ITL (ms):                            160.95    
P90 ITL (ms):                            271.99    
P95 ITL (ms):                            317.42    
P99 ITL (ms):                            372.34    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          582602.37 
Median E2EL (ms):                        590266.99 
P50 E2EL (ms):                           590266.99 
P90 E2EL (ms):                           835922.34 
P95 E2EL (ms):                           903200.08 
P99 E2EL (ms):                           939497.39 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

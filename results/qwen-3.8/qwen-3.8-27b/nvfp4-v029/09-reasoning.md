# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-09-18 18:55:48
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-27B-NVFP4 --tokenizer nvidia/Qwen3.8-27B-NVFP4 --served-model-name qwen3.8-27b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1193.14   
Total input tokens:                      57622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         175.42    
Peak output token throughput (tok/s):    304.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          223.72    
---------------Time to First Token----------------
Mean TTFT (ms):                          2331.13   
Median TTFT (ms):                        2124.08   
P50 TTFT (ms):                           2124.08   
P90 TTFT (ms):                           3761.28   
P95 TTFT (ms):                           4051.92   
P99 TTFT (ms):                           4928.64   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          161.36    
Median TPOT (ms):                        163.47    
P50 TPOT (ms):                           163.47    
P90 TPOT (ms):                           176.31    
P95 TPOT (ms):                           181.94    
P99 TPOT (ms):                           188.52    
---------------Inter-token Latency----------------
Mean ITL (ms):                           157.04    
Median ITL (ms):                         157.82    
P50 ITL (ms):                            157.82    
P90 ITL (ms):                            169.49    
P95 ITL (ms):                            172.96    
P99 ITL (ms):                            341.92    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          654913.43 
Median E2EL (ms):                        650959.36 
P50 E2EL (ms):                           650959.36 
P90 E2EL (ms):                           953783.87 
P95 E2EL (ms):                           1036544.98
P99 E2EL (ms):                           1073365.95
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

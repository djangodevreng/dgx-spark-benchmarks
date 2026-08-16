# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-14 08:19:24
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  692.50    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         140.21    
Peak output token throughput (tok/s):    304.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1316.83   
---------------Time to First Token----------------
Mean TTFT (ms):                          1183.08   
Median TTFT (ms):                        1083.14   
P50 TTFT (ms):                           1083.14   
P90 TTFT (ms):                           1970.39   
P95 TTFT (ms):                           2388.60   
P99 TTFT (ms):                           3232.88   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          54.45     
Median TPOT (ms):                        54.38     
P50 TPOT (ms):                           54.38     
P90 TPOT (ms):                           67.81     
P95 TPOT (ms):                           73.10     
P99 TPOT (ms):                           82.76     
---------------Inter-token Latency----------------
Mean ITL (ms):                           54.08     
Median ITL (ms):                         49.52     
P50 ITL (ms):                            49.52     
P90 ITL (ms):                            53.76     
P95 ITL (ms):                            59.38     
P99 ITL (ms):                            364.10    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          27369.12  
Median E2EL (ms):                        26092.46  
P50 E2EL (ms):                           26092.46  
P90 E2EL (ms):                           48332.46  
P95 E2EL (ms):                           54772.59  
P99 E2EL (ms):                           60292.97  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

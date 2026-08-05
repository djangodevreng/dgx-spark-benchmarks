# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-08 13:54:13
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-31B-IT-NVFP4 --tokenizer nvidia/Gemma-4-31B-IT-NVFP4 --served-model-name gemma-4-31b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1123.27   
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.18      
Output token throughput (tok/s):         86.44     
Peak output token throughput (tok/s):    271.00    
Peak concurrent requests:                164.00    
Total token throughput (tok/s):          812.35    
---------------Time to First Token----------------
Mean TTFT (ms):                          37078.64  
Median TTFT (ms):                        15563.84  
P50 TTFT (ms):                           15563.84  
P90 TTFT (ms):                           132963.90 
P95 TTFT (ms):                           143671.22 
P99 TTFT (ms):                           158332.87 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1148.76   
Median TPOT (ms):                        1163.87   
P50 TPOT (ms):                           1163.87   
P90 TPOT (ms):                           1717.15   
P95 TPOT (ms):                           1863.45   
P99 TPOT (ms):                           2066.57   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1013.84   
Median ITL (ms):                         664.46    
P50 ITL (ms):                            664.46    
P90 ITL (ms):                            2572.73   
P95 ITL (ms):                            4661.80   
P99 ITL (ms):                            6336.13   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          529255.07 
Median E2EL (ms):                        524909.54 
P50 E2EL (ms):                           524909.54 
P90 E2EL (ms):                           821973.39 
P95 E2EL (ms):                           904768.29 
P99 E2EL (ms):                           966178.98 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

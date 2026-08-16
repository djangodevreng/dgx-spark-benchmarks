# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-13 14:44:26
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --served-model-name nemotron-3-nano-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  687.26    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         141.27    
Peak output token throughput (tok/s):    315.00    
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          1328.51   
---------------Time to First Token----------------
Mean TTFT (ms):                          963.56    
Median TTFT (ms):                        884.06    
P50 TTFT (ms):                           884.06    
P90 TTFT (ms):                           1684.33   
P95 TTFT (ms):                           2085.59   
P99 TTFT (ms):                           2561.48   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          41.58     
Median TPOT (ms):                        41.29     
P50 TPOT (ms):                           41.29     
P90 TPOT (ms):                           55.30     
P95 TPOT (ms):                           60.48     
P99 TPOT (ms):                           68.40     
---------------Inter-token Latency----------------
Mean ITL (ms):                           41.02     
Median ITL (ms):                         33.65     
P50 ITL (ms):                            33.65     
P90 ITL (ms):                            46.36     
P95 ITL (ms):                            48.40     
P99 ITL (ms):                            221.63    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          20875.16  
Median E2EL (ms):                        19903.24  
P50 E2EL (ms):                           19903.24  
P90 E2EL (ms):                           38010.45  
P95 E2EL (ms):                           44299.17  
P99 E2EL (ms):                           48275.74  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 04:47:26
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1217.77   
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.16      
Output token throughput (tok/s):         79.73     
Peak output token throughput (tok/s):    61.00     
Peak concurrent requests:                102.00    
Total token throughput (tok/s):          749.75    
---------------Time to First Token----------------
Mean TTFT (ms):                          227131.11 
Median TTFT (ms):                        247721.91 
P50 TTFT (ms):                           247721.91 
P90 TTFT (ms):                           421591.10 
P95 TTFT (ms):                           446373.61 
P99 TTFT (ms):                           470738.26 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          235.01    
Median TPOT (ms):                        240.12    
P50 TPOT (ms):                           240.12    
P90 TPOT (ms):                           267.93    
P95 TPOT (ms):                           287.92    
P99 TPOT (ms):                           314.45    
---------------Inter-token Latency----------------
Mean ITL (ms):                           597.23    
Median ITL (ms):                         425.33    
P50 ITL (ms):                            425.33    
P90 ITL (ms):                            1327.03   
P95 ITL (ms):                            1339.52   
P99 ITL (ms):                            1398.56   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          338413.65 
Median E2EL (ms):                        335719.12 
P50 E2EL (ms):                           335719.12 
P90 E2EL (ms):                           534097.12 
P95 E2EL (ms):                           565517.20 
P99 E2EL (ms):                           588168.74 
---------------Speculative Decoding---------------
Acceptance rate (%):                     53.98     
Acceptance length:                       2.62      
Drafts:                                  37085     
Draft tokens:                            111255    
Accepted tokens:                         60052     
Per-position acceptance (%):
  Position 0:                            76.70     
  Position 1:                            51.51     
  Position 2:                            33.72     
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

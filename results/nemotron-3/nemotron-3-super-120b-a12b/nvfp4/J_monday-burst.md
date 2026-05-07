# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-05 05:33:36
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1869.43   
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.16      
Output token throughput (tok/s):         80.41     
Peak output token throughput (tok/s):    61.00     
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          723.84    
---------------Time to First Token----------------
Mean TTFT (ms):                          34710.68  
Median TTFT (ms):                        33368.32  
P50 TTFT (ms):                           33368.32  
P90 TTFT (ms):                           46270.26  
P95 TTFT (ms):                           49617.69  
P99 TTFT (ms):                           69799.94  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          237.06    
Median TPOT (ms):                        236.59    
P50 TPOT (ms):                           236.59    
P90 TPOT (ms):                           271.68    
P95 TPOT (ms):                           283.73    
P99 TPOT (ms):                           309.93    
---------------Inter-token Latency----------------
Mean ITL (ms):                           601.04    
Median ITL (ms):                         425.67    
P50 ITL (ms):                            425.67    
P90 ITL (ms):                            1328.07   
P95 ITL (ms):                            1339.92   
P99 ITL (ms):                            1407.39   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          150963.71 
Median E2EL (ms):                        151665.88 
P50 E2EL (ms):                           151665.88 
P90 E2EL (ms):                           240891.49 
P95 E2EL (ms):                           250589.88 
P99 E2EL (ms):                           274598.85 
---------------Speculative Decoding---------------
Acceptance rate (%):                     53.39     
Acceptance length:                       2.60      
Drafts:                                  57790     
Draft tokens:                            173370    
Accepted tokens:                         92569     
Per-position acceptance (%):
  Position 0:                            76.31     
  Position 1:                            50.89     
  Position 2:                            32.98     
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

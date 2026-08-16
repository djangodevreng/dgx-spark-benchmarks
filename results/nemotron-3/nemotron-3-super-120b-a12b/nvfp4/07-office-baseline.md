# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-15 07:39:56
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1429.40   
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.14      
Output token throughput (tok/s):         67.92     
Peak output token throughput (tok/s):    61.00     
Peak concurrent requests:                119.00    
Total token throughput (tok/s):          638.75    
---------------Time to First Token----------------
Mean TTFT (ms):                          326344.45 
Median TTFT (ms):                        339386.60 
P50 TTFT (ms):                           339386.60 
P90 TTFT (ms):                           607244.62 
P95 TTFT (ms):                           640622.64 
P99 TTFT (ms):                           672869.32 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          269.83    
Median TPOT (ms):                        274.51    
P50 TPOT (ms):                           274.51    
P90 TPOT (ms):                           314.20    
P95 TPOT (ms):                           325.56    
P99 TPOT (ms):                           346.22    
---------------Inter-token Latency----------------
Mean ITL (ms):                           687.61    
Median ITL (ms):                         450.03    
P50 ITL (ms):                            450.03    
P90 ITL (ms):                            1721.47   
P95 ITL (ms):                            1732.28   
P99 ITL (ms):                            1781.74   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          456244.83 
Median E2EL (ms):                        453335.79 
P50 E2EL (ms):                           453335.79 
P90 E2EL (ms):                           734352.85 
P95 E2EL (ms):                           765615.19 
P99 E2EL (ms):                           796107.91 
---------------Speculative Decoding---------------
Acceptance rate (%):                     52.76     
Acceptance length:                       2.58      
Drafts:                                  37600     
Draft tokens:                            112800    
Accepted tokens:                         59511     
Per-position acceptance (%):
  Position 0:                            75.68     
  Position 1:                            50.33     
  Position 2:                            32.26     
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

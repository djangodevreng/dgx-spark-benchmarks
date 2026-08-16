# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-15 08:54:13
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  2125.74   
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.14      
Output token throughput (tok/s):         70.71     
Peak output token throughput (tok/s):    61.00     
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          636.57    
---------------Time to First Token----------------
Mean TTFT (ms):                          40014.02  
Median TTFT (ms):                        38453.01  
P50 TTFT (ms):                           38453.01  
P90 TTFT (ms):                           52512.56  
P95 TTFT (ms):                           56834.12  
P99 TTFT (ms):                           84930.34  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          272.84    
Median TPOT (ms):                        272.57    
P50 TPOT (ms):                           272.57    
P90 TPOT (ms):                           322.19    
P95 TPOT (ms):                           346.69    
P99 TPOT (ms):                           408.23    
---------------Inter-token Latency----------------
Mean ITL (ms):                           688.95    
Median ITL (ms):                         449.94    
P50 ITL (ms):                            449.94    
P90 ITL (ms):                            1720.32   
P95 ITL (ms):                            1730.27   
P99 ITL (ms):                            1797.06   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          172341.33 
Median E2EL (ms):                        171906.22 
P50 E2EL (ms):                           171906.22 
P90 E2EL (ms):                           268743.75 
P95 E2EL (ms):                           286221.11 
P99 E2EL (ms):                           315207.49 
---------------Speculative Decoding---------------
Acceptance rate (%):                     53.93     
Acceptance length:                       2.62      
Drafts:                                  57441     
Draft tokens:                            172323    
Accepted tokens:                         92929     
Per-position acceptance (%):
  Position 0:                            76.68     
  Position 1:                            51.19     
  Position 2:                            33.91     
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

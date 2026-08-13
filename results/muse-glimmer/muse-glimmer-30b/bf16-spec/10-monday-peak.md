# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-12 20:22:25
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16-spec --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  3760.82   
Total input tokens:                      1214714   
Total generated tokens:                  150317    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         39.97     
Peak output token throughput (tok/s):    54.00     
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          362.96    
---------------Time to First Token----------------
Mean TTFT (ms):                          7343.04   
Median TTFT (ms):                        4857.40   
P50 TTFT (ms):                           4857.40   
P90 TTFT (ms):                           8468.75   
P95 TTFT (ms):                           28022.20  
P99 TTFT (ms):                           59273.13  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          597.52    
Median TPOT (ms):                        710.23    
P50 TPOT (ms):                           710.23    
P90 TPOT (ms):                           781.44    
P95 TPOT (ms):                           796.06    
P99 TPOT (ms):                           910.54    
---------------Inter-token Latency----------------
Mean ITL (ms):                           775.33    
Median ITL (ms):                         629.23    
P50 ITL (ms):                            629.23    
P90 ITL (ms):                            657.10    
P95 ITL (ms):                            1662.06   
P99 ITL (ms):                            4598.74   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          300383.29 
Median E2EL (ms):                        253171.91 
P50 E2EL (ms):                           253171.91 
P90 E2EL (ms):                           619580.80 
P95 E2EL (ms):                           672133.60 
P99 E2EL (ms):                           730068.80 
---------------Speculative Decoding---------------
Acceptance rate (%):                     2.10      
Acceptance length:                       1.31      
Drafts:                                  114260    
Draft tokens:                            1713900   
Accepted tokens:                         35933     
Per-position acceptance (%):
  Position 0:                            17.45     
  Position 1:                            7.47      
  Position 2:                            3.33      
  Position 3:                            1.44      
  Position 4:                            0.69      
  Position 5:                            0.35      
  Position 6:                            0.19      
  Position 7:                            0.13      
  Position 8:                            0.09      
  Position 9:                            0.07      
  Position 10:                           0.06      
  Position 11:                           0.05      
  Position 12:                           0.05      
  Position 13:                           0.04      
  Position 14:                           0.04      
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

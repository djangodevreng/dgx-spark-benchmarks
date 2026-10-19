# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-10-18 17:17:14
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-Flash-Next-FP4-Local --tokenizer nvidia/Qwen3.8-Flash-Next-FP4-Local --served-model-name qwen3.8-flash-next --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1434.24   
Total input tokens:                      1213774   
Total generated tokens:                  150317    
Request throughput (req/s):              0.21      
Output token throughput (tok/s):         104.81    
Peak output token throughput (tok/s):    102.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          951.09    
---------------Time to First Token----------------
Mean TTFT (ms):                          6987.01   
Median TTFT (ms):                        5348.54   
P50 TTFT (ms):                           5348.54   
P90 TTFT (ms):                           13341.98  
P95 TTFT (ms):                           17208.05  
P99 TTFT (ms):                           33863.55  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          226.72    
Median TPOT (ms):                        230.72    
P50 TPOT (ms):                           230.72    
P90 TPOT (ms):                           275.31    
P95 TPOT (ms):                           295.55    
P99 TPOT (ms):                           342.51    
---------------Inter-token Latency----------------
Mean ITL (ms):                           456.29    
Median ITL (ms):                         301.57    
P50 ITL (ms):                            301.57    
P90 ITL (ms):                            1245.45   
P95 ITL (ms):                            1643.28   
P99 ITL (ms):                            1867.95   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          116245.13 
Median E2EL (ms):                        111992.26 
P50 E2EL (ms):                           111992.26 
P90 E2EL (ms):                           199928.51 
P95 E2EL (ms):                           218874.72 
P99 E2EL (ms):                           237805.16 
---------------Speculative Decoding---------------
Acceptance rate (%):                     36.65     
Acceptance length:                       2.10      
Drafts:                                  71569     
Draft tokens:                            214707    
Accepted tokens:                         78697     
Per-position acceptance (%):
  Position 0:                            58.53     
  Position 1:                            33.61     
  Position 2:                            17.82     
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

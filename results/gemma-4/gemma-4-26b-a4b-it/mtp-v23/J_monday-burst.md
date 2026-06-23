# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-06-23 05:27:26
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-mtp --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  872.34    
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.34      
Output token throughput (tok/s):         172.32    
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          1550.32   
---------------Time to First Token----------------
Mean TTFT (ms):                          1981.63   
Median TTFT (ms):                        1684.48   
P50 TTFT (ms):                           1684.48   
P90 TTFT (ms):                           2913.37   
P95 TTFT (ms):                           3870.47   
P99 TTFT (ms):                           8935.82   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          131.88    
Median TPOT (ms):                        119.89    
P50 TPOT (ms):                           119.89    
P90 TPOT (ms):                           198.49    
P95 TPOT (ms):                           235.91    
P99 TPOT (ms):                           278.44    
---------------Inter-token Latency----------------
Mean ITL (ms):                           314.19    
Median ITL (ms):                         244.04    
P50 ITL (ms):                            244.04    
P90 ITL (ms):                            343.55    
P95 ITL (ms):                            951.54    
P99 ITL (ms):                            1592.51   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          68720.64  
Median E2EL (ms):                        57582.81  
P50 E2EL (ms):                           57582.81  
P90 E2EL (ms):                           130696.37 
P95 E2EL (ms):                           178874.49 
P99 E2EL (ms):                           225094.64 
---------------Speculative Decoding---------------
Acceptance rate (%):                     34.25     
Acceptance length:                       2.37      
Drafts:                                  63425     
Draft tokens:                            253700    
Accepted tokens:                         86881     
Per-position acceptance (%):
  Position 0:                            61.01     
  Position 1:                            35.39     
  Position 2:                            22.97     
  Position 3:                            17.61     
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

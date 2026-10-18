# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-10-18 00:06:31
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --served-model-name nemotron-3.5-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1068.12   
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.28      
Output token throughput (tok/s):         140.73    
Peak output token throughput (tok/s):    100.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1266.88   
---------------Time to First Token----------------
Mean TTFT (ms):                          4604.86   
Median TTFT (ms):                        3420.28   
P50 TTFT (ms):                           3420.28   
P90 TTFT (ms):                           6267.56   
P95 TTFT (ms):                           12024.94  
P99 TTFT (ms):                           29370.44  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          168.84    
Median TPOT (ms):                        168.94    
P50 TPOT (ms):                           168.94    
P90 TPOT (ms):                           194.23    
P95 TPOT (ms):                           205.51    
P99 TPOT (ms):                           250.66    
---------------Inter-token Latency----------------
Mean ITL (ms):                           486.74    
Median ITL (ms):                         341.64    
P50 ITL (ms):                            341.64    
P90 ITL (ms):                            898.38    
P95 ITL (ms):                            924.66    
P99 ITL (ms):                            935.89    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          86085.57  
Median E2EL (ms):                        84070.44  
P50 E2EL (ms):                           84070.44  
P90 E2EL (ms):                           145520.48 
P95 E2EL (ms):                           158585.47 
P99 E2EL (ms):                           168198.49 
---------------Speculative Decoding---------------
Acceptance rate (%):                     66.85     
Acceptance length:                       3.01      
Drafts:                                  50052     
Draft tokens:                            150156    
Accepted tokens:                         100373    
Per-position acceptance (%):
  Position 0:                            82.53     
  Position 1:                            66.14     
  Position 2:                            51.86     
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

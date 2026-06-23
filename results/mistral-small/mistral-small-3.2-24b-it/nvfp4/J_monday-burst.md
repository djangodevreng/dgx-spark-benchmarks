# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-06-23 13:17:33
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --tokenizer RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --served-model-name mistral-small-3.2-24b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1866.58   
Total input tokens:                      1385714   
Total generated tokens:                  150317    
Request throughput (req/s):              0.16      
Output token throughput (tok/s):         80.53     
Peak output token throughput (tok/s):    251.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          822.91    
---------------Time to First Token----------------
Mean TTFT (ms):                          8341.48   
Median TTFT (ms):                        4841.76   
P50 TTFT (ms):                           4841.76   
P90 TTFT (ms):                           9706.46   
P95 TTFT (ms):                           37713.42  
P99 TTFT (ms):                           79779.56  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          294.98    
Median TPOT (ms):                        292.66    
P50 TPOT (ms):                           292.66    
P90 TPOT (ms):                           342.11    
P95 TPOT (ms):                           383.99    
P99 TPOT (ms):                           518.19    
---------------Inter-token Latency----------------
Mean ITL (ms):                           287.30    
Median ITL (ms):                         112.99    
P50 ITL (ms):                            112.99    
P90 ITL (ms):                            117.57    
P95 ITL (ms):                            1805.51   
P99 ITL (ms):                            3804.60   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          152294.91 
Median E2EL (ms):                        143186.86 
P50 E2EL (ms):                           143186.86 
P90 E2EL (ms):                           270740.85 
P95 E2EL (ms):                           284532.92 
P99 E2EL (ms):                           326374.87 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

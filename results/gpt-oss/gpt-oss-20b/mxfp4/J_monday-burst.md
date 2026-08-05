# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-06-26 11:20:44
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  484.85    
Total input tokens:                      1216349   
Total generated tokens:                  136381    
Request throughput (req/s):              0.62      
Output token throughput (tok/s):         281.28    
Peak output token throughput (tok/s):    358.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2789.99   
---------------Time to First Token----------------
Mean TTFT (ms):                          880.16    
Median TTFT (ms):                        744.96    
P50 TTFT (ms):                           744.96    
P90 TTFT (ms):                           1215.70   
P95 TTFT (ms):                           1829.43   
P99 TTFT (ms):                           4502.35   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          82.45     
Median TPOT (ms):                        83.67     
P50 TPOT (ms):                           83.67     
P90 TPOT (ms):                           90.91     
P95 TPOT (ms):                           92.57     
P99 TPOT (ms):                           106.78    
---------------Inter-token Latency----------------
Mean ITL (ms):                           263.21    
Median ITL (ms):                         57.52     
P50 ITL (ms):                            57.52     
P90 ITL (ms):                            63.08     
P95 ITL (ms):                            184.20    
P99 ITL (ms):                            1035.28   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          38397.75  
Median E2EL (ms):                        36420.75  
P50 E2EL (ms):                           36420.75  
P90 E2EL (ms):                           73548.91  
P95 E2EL (ms):                           77978.48  
P99 E2EL (ms):                           81684.78  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

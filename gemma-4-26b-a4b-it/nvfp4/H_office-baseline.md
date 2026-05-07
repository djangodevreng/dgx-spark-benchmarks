# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 11:17:01
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  700.57    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.59    
Peak output token throughput (tok/s):    272.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1302.49   
---------------Time to First Token----------------
Mean TTFT (ms):                          1100.36   
Median TTFT (ms):                        1005.68   
P50 TTFT (ms):                           1005.68   
P90 TTFT (ms):                           1889.20   
P95 TTFT (ms):                           2327.69   
P99 TTFT (ms):                           2893.45   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          63.47     
Median TPOT (ms):                        63.76     
P50 TPOT (ms):                           63.76     
P90 TPOT (ms):                           75.92     
P95 TPOT (ms):                           79.72     
P99 TPOT (ms):                           87.41     
---------------Inter-token Latency----------------
Mean ITL (ms):                           63.08     
Median ITL (ms):                         52.07     
P50 ITL (ms):                            52.07     
P90 ITL (ms):                            59.27     
P95 ITL (ms):                            60.93     
P99 ITL (ms):                            589.76    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          31724.89  
Median E2EL (ms):                        31340.81  
P50 E2EL (ms):                           31340.81  
P90 E2EL (ms):                           55241.18  
P95 E2EL (ms):                           61037.20  
P99 E2EL (ms):                           64068.42  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

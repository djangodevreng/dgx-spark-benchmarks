# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 21:52:43
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  750.91    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         129.30    
Peak output token throughput (tok/s):    245.00    
Peak concurrent requests:                36.00     
Total token throughput (tok/s):          1215.18   
---------------Time to First Token----------------
Mean TTFT (ms):                          1395.46   
Median TTFT (ms):                        1285.83   
P50 TTFT (ms):                           1285.83   
P90 TTFT (ms):                           2283.63   
P95 TTFT (ms):                           2644.45   
P99 TTFT (ms):                           3316.41   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          176.60    
Median TPOT (ms):                        181.62    
P50 TPOT (ms):                           181.62    
P90 TPOT (ms):                           192.90    
P95 TPOT (ms):                           201.54    
P99 TPOT (ms):                           214.00    
---------------Inter-token Latency----------------
Mean ITL (ms):                           174.11    
Median ITL (ms):                         149.49    
P50 ITL (ms):                            149.49    
P90 ITL (ms):                            163.96    
P95 ITL (ms):                            172.83    
P99 ITL (ms):                            1188.14   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          85921.30  
Median E2EL (ms):                        85306.40  
P50 E2EL (ms):                           85306.40  
P90 E2EL (ms):                           150191.92 
P95 E2EL (ms):                           162374.87 
P99 E2EL (ms):                           171350.73 
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

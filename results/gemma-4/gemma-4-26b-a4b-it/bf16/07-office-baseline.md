# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 13:34:33
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  750.09    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         129.44    
Peak output token throughput (tok/s):    234.00    
Peak concurrent requests:                39.00     
Total token throughput (tok/s):          1216.50   
---------------Time to First Token----------------
Mean TTFT (ms):                          1577.96   
Median TTFT (ms):                        1434.65   
P50 TTFT (ms):                           1434.65   
P90 TTFT (ms):                           2573.07   
P95 TTFT (ms):                           3077.46   
P99 TTFT (ms):                           3914.26   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          191.17    
Median TPOT (ms):                        192.04    
P50 TPOT (ms):                           192.04    
P90 TPOT (ms):                           212.64    
P95 TPOT (ms):                           218.26    
P99 TPOT (ms):                           231.23    
---------------Inter-token Latency----------------
Mean ITL (ms):                           188.16    
Median ITL (ms):                         156.40    
P50 ITL (ms):                            156.40    
P90 ITL (ms):                            172.61    
P95 ITL (ms):                            196.73    
P99 ITL (ms):                            1347.57   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          92922.93  
Median E2EL (ms):                        93331.53  
P50 E2EL (ms):                           93331.53  
P90 E2EL (ms):                           161293.30 
P95 E2EL (ms):                           178313.05 
P99 E2EL (ms):                           187416.14 
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

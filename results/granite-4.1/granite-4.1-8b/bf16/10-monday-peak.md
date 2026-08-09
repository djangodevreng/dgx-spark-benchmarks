# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-09 09:09:18
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model ibm-granite/granite-4.1-8b --tokenizer ibm-granite/granite-4.1-8b --served-model-name granite-4-1-8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1108.75   
Total input tokens:                      1200458   
Total generated tokens:                  150317    
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         135.57    
Peak output token throughput (tok/s):    201.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1218.28   
---------------Time to First Token----------------
Mean TTFT (ms):                          1930.22   
Median TTFT (ms):                        1489.86   
P50 TTFT (ms):                           1489.86   
P90 TTFT (ms):                           2487.83   
P95 TTFT (ms):                           4944.12   
P99 TTFT (ms):                           12800.91  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          175.86    
Median TPOT (ms):                        175.65    
P50 TPOT (ms):                           175.65    
P90 TPOT (ms):                           188.40    
P95 TPOT (ms):                           199.16    
P99 TPOT (ms):                           233.22    
---------------Inter-token Latency----------------
Mean ITL (ms):                           173.36    
Median ITL (ms):                         133.57    
P50 ITL (ms):                            133.57    
P90 ITL (ms):                            138.97    
P95 ITL (ms):                            147.73    
P99 ITL (ms):                            1514.69   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          88793.07  
Median E2EL (ms):                        86317.72  
P50 E2EL (ms):                           86317.72  
P90 E2EL (ms):                           158057.75 
P95 E2EL (ms):                           164563.02 
P99 E2EL (ms):                           173935.34 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

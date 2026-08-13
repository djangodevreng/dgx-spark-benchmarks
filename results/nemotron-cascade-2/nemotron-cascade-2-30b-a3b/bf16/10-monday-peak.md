# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-09 13:30:02
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-Cascade-2-30B-A3B --tokenizer nvidia/Nemotron-Cascade-2-30B-A3B --served-model-name nemotron-cascade-2-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1331.63   
Total input tokens:                      1207814   
Total generated tokens:                  150317    
Request throughput (req/s):              0.23      
Output token throughput (tok/s):         112.88    
Peak output token throughput (tok/s):    151.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1019.90   
---------------Time to First Token----------------
Mean TTFT (ms):                          1298.22   
Median TTFT (ms):                        1140.20   
P50 TTFT (ms):                           1140.20   
P90 TTFT (ms):                           1826.51   
P95 TTFT (ms):                           2191.51   
P99 TTFT (ms):                           5119.77   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          212.80    
Median TPOT (ms):                        215.17    
P50 TPOT (ms):                           215.17    
P90 TPOT (ms):                           220.86    
P95 TPOT (ms):                           224.75    
P99 TPOT (ms):                           231.84    
---------------Inter-token Latency----------------
Mean ITL (ms):                           210.78    
Median ITL (ms):                         190.97    
P50 ITL (ms):                            190.97    
P90 ITL (ms):                            202.91    
P95 ITL (ms):                            230.33    
P99 ITL (ms):                            910.72    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          106909.66 
Median E2EL (ms):                        107370.20 
P50 E2EL (ms):                           107370.20 
P90 E2EL (ms):                           190074.92 
P95 E2EL (ms):                           197509.09 
P99 E2EL (ms):                           204455.04 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

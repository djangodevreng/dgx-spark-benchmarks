# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-06 07:13:39
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  522.34    
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.57      
Output token throughput (tok/s):         287.77    
Peak output token throughput (tok/s):    426.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          2590.58   
---------------Time to First Token----------------
Mean TTFT (ms):                          953.48    
Median TTFT (ms):                        823.11    
P50 TTFT (ms):                           823.11    
P90 TTFT (ms):                           1556.77   
P95 TTFT (ms):                           1843.18   
P99 TTFT (ms):                           3996.96   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          81.63     
Median TPOT (ms):                        82.25     
P50 TPOT (ms):                           82.25     
P90 TPOT (ms):                           88.00     
P95 TPOT (ms):                           91.57     
P99 TPOT (ms):                           96.91     
---------------Inter-token Latency----------------
Mean ITL (ms):                           80.80     
Median ITL (ms):                         61.31     
P50 ITL (ms):                            61.31     
P90 ITL (ms):                            113.81    
P95 ITL (ms):                            275.33    
P99 ITL (ms):                            290.78    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          41439.07  
Median E2EL (ms):                        40772.70  
P50 E2EL (ms):                           40772.70  
P90 E2EL (ms):                           73312.95  
P95 E2EL (ms):                           76424.93  
P99 E2EL (ms):                           80550.89  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

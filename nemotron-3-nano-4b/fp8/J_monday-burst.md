# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-05 18:44:25
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  380.80    
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.79      
Output token throughput (tok/s):         394.74    
Peak output token throughput (tok/s):    575.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          3553.49   
---------------Time to First Token----------------
Mean TTFT (ms):                          678.76    
Median TTFT (ms):                        623.61    
P50 TTFT (ms):                           623.61    
P90 TTFT (ms):                           1042.40   
P95 TTFT (ms):                           1448.15   
P99 TTFT (ms):                           2146.67   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          59.11     
Median TPOT (ms):                        59.91     
P50 TPOT (ms):                           59.91     
P90 TPOT (ms):                           63.38     
P95 TPOT (ms):                           65.69     
P99 TPOT (ms):                           71.18     
---------------Inter-token Latency----------------
Mean ITL (ms):                           58.62     
Median ITL (ms):                         45.05     
P50 ITL (ms):                            45.05     
P90 ITL (ms):                            86.03     
P95 ITL (ms):                            190.85    
P99 ITL (ms):                            222.56    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          30050.06  
Median E2EL (ms):                        29421.32  
P50 E2EL (ms):                           29421.32  
P90 E2EL (ms):                           53299.67  
P95 E2EL (ms):                           55614.27  
P99 E2EL (ms):                           58564.42  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

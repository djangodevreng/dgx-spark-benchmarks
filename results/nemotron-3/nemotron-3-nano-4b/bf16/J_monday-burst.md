# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-05 16:17:58
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  482.02    
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.62      
Output token throughput (tok/s):         311.85    
Peak output token throughput (tok/s):    451.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2807.31   
---------------Time to First Token----------------
Mean TTFT (ms):                          841.93    
Median TTFT (ms):                        775.07    
P50 TTFT (ms):                           775.07    
P90 TTFT (ms):                           1212.68   
P95 TTFT (ms):                           1570.01   
P99 TTFT (ms):                           3442.22   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          75.05     
Median TPOT (ms):                        75.67     
P50 TPOT (ms):                           75.67     
P90 TPOT (ms):                           80.94     
P95 TPOT (ms):                           83.51     
P99 TPOT (ms):                           89.49     
---------------Inter-token Latency----------------
Mean ITL (ms):                           74.36     
Median ITL (ms):                         57.17     
P50 ITL (ms):                            57.17     
P90 ITL (ms):                            93.30     
P95 ITL (ms):                            252.48    
P99 ITL (ms):                            266.17    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          38102.01  
Median E2EL (ms):                        37910.46  
P50 E2EL (ms):                           37910.46  
P90 E2EL (ms):                           67394.59  
P95 E2EL (ms):                           70047.88  
P99 E2EL (ms):                           73965.53  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

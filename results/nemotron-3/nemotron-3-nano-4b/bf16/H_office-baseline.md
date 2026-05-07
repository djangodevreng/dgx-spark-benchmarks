# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 15:55:40
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  690.84    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         140.54    
Peak output token throughput (tok/s):    330.00    
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          1321.61   
---------------Time to First Token----------------
Mean TTFT (ms):                          743.41    
Median TTFT (ms):                        706.41    
P50 TTFT (ms):                           706.41    
P90 TTFT (ms):                           1227.34   
P95 TTFT (ms):                           1419.78   
P99 TTFT (ms):                           1966.00   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          44.73     
Median TPOT (ms):                        44.66     
P50 TPOT (ms):                           44.66     
P90 TPOT (ms):                           50.66     
P95 TPOT (ms):                           52.73     
P99 TPOT (ms):                           57.49     
---------------Inter-token Latency----------------
Mean ITL (ms):                           44.57     
Median ITL (ms):                         39.63     
P50 ITL (ms):                            39.63     
P90 ITL (ms):                            43.50     
P95 ITL (ms):                            45.67     
P99 ITL (ms):                            242.38    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          22381.55  
Median E2EL (ms):                        22023.10  
P50 E2EL (ms):                           22023.10  
P90 E2EL (ms):                           38719.57  
P95 E2EL (ms):                           41666.87  
P99 E2EL (ms):                           45056.02  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

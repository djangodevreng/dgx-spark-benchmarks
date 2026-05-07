# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-03 10:24:52
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --tokenizer nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 --served-model-name nemotron-3-nano-omni-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  687.17    
Total input tokens:                      816039    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         141.29    
Peak output token throughput (tok/s):    315.00    
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          1328.82   
---------------Time to First Token----------------
Mean TTFT (ms):                          763.60    
Median TTFT (ms):                        617.80    
P50 TTFT (ms):                           617.80    
P90 TTFT (ms):                           1380.85   
P95 TTFT (ms):                           1948.29   
P99 TTFT (ms):                           3235.05   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          39.74     
Median TPOT (ms):                        39.09     
P50 TPOT (ms):                           39.09     
P90 TPOT (ms):                           52.37     
P95 TPOT (ms):                           54.67     
P99 TPOT (ms):                           61.17     
---------------Inter-token Latency----------------
Mean ITL (ms):                           39.35     
Median ITL (ms):                         34.42     
P50 ITL (ms):                            34.42     
P90 ITL (ms):                            47.97     
P95 ITL (ms):                            50.81     
P99 ITL (ms):                            169.72    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19817.71  
Median E2EL (ms):                        18924.41  
P50 E2EL (ms):                           18924.41  
P90 E2EL (ms):                           35490.34  
P95 E2EL (ms):                           40327.49  
P99 E2EL (ms):                           43670.82  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.

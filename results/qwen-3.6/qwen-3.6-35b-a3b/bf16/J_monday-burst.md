# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-05 14:01:52
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1418.33   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.21      
Output token throughput (tok/s):         105.98    
Peak output token throughput (tok/s):    175.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          952.87    
---------------Time to First Token----------------
Mean TTFT (ms):                          2625.18   
Median TTFT (ms):                        2152.97   
P50 TTFT (ms):                           2152.97   
P90 TTFT (ms):                           3636.09   
P95 TTFT (ms):                           5832.10   
P99 TTFT (ms):                           16236.38  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          226.11    
Median TPOT (ms):                        228.21    
P50 TPOT (ms):                           228.21    
P90 TPOT (ms):                           241.00    
P95 TPOT (ms):                           247.87    
P99 TPOT (ms):                           265.86    
---------------Inter-token Latency----------------
Mean ITL (ms):                           224.23    
Median ITL (ms):                         182.73    
P50 ITL (ms):                            182.73    
P90 ITL (ms):                            375.60    
P95 ITL (ms):                            636.42    
P99 ITL (ms):                            685.45    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          114502.24 
Median E2EL (ms):                        111326.13 
P50 E2EL (ms):                           111326.13 
P90 E2EL (ms):                           203974.62 
P95 E2EL (ms):                           212059.51 
P99 E2EL (ms):                           223030.65 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

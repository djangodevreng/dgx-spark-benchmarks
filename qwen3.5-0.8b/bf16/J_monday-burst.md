# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-04 23:45:39
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  209.25    
Total input tokens:                      1201770   
Total generated tokens:                  150317    
Request throughput (req/s):              1.43      
Output token throughput (tok/s):         718.35    
Peak output token throughput (tok/s):    1238.00   
Peak concurrent requests:                23.00     
Total token throughput (tok/s):          6461.49   
---------------Time to First Token----------------
Mean TTFT (ms):                          274.35    
Median TTFT (ms):                        268.86    
P50 TTFT (ms):                           268.86    
P90 TTFT (ms):                           434.67    
P95 TTFT (ms):                           483.47    
P99 TTFT (ms):                           592.65    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          15.06     
Median TPOT (ms):                        14.86     
P50 TPOT (ms):                           14.86     
P90 TPOT (ms):                           18.49     
P95 TPOT (ms):                           20.18     
P99 TPOT (ms):                           22.89     
---------------Inter-token Latency----------------
Mean ITL (ms):                           14.98     
Median ITL (ms):                         11.65     
P50 ITL (ms):                            11.65     
P90 ITL (ms):                            15.81     
P95 ITL (ms):                            32.68     
P99 ITL (ms):                            87.85     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7724.84   
Median E2EL (ms):                        7321.90   
P50 E2EL (ms):                           7321.90   
P90 E2EL (ms):                           13535.17  
P95 E2EL (ms):                           14494.94  
P99 E2EL (ms):                           15913.89  
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.

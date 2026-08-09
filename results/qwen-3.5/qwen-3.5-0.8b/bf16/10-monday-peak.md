# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-07 10:09:41
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  208.86    
Total input tokens:                      1201770   
Total generated tokens:                  150317    
Request throughput (req/s):              1.44      
Output token throughput (tok/s):         719.69    
Peak output token throughput (tok/s):    1309.00   
Peak concurrent requests:                22.00     
Total token throughput (tok/s):          6473.57   
---------------Time to First Token----------------
Mean TTFT (ms):                          256.09    
Median TTFT (ms):                        251.92    
P50 TTFT (ms):                           251.92    
P90 TTFT (ms):                           406.47    
P95 TTFT (ms):                           447.72    
P99 TTFT (ms):                           558.50    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          14.13     
Median TPOT (ms):                        14.12     
P50 TPOT (ms):                           14.12     
P90 TPOT (ms):                           16.83     
P95 TPOT (ms):                           17.94     
P99 TPOT (ms):                           20.61     
---------------Inter-token Latency----------------
Mean ITL (ms):                           13.98     
Median ITL (ms):                         11.45     
P50 ITL (ms):                            11.45     
P90 ITL (ms):                            14.40     
P95 ITL (ms):                            27.49     
P99 ITL (ms):                            80.27     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7260.50   
Median E2EL (ms):                        7034.11   
P50 E2EL (ms):                           7034.11   
P90 E2EL (ms):                           12566.26  
P95 E2EL (ms):                           13706.77  
P99 E2EL (ms):                           14858.65  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

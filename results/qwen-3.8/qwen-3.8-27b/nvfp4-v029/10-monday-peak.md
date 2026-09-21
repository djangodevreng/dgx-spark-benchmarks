# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-09-18 19:34:42
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-27B-NVFP4 --tokenizer nvidia/Qwen3.8-27B-NVFP4 --served-model-name qwen3.8-27b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  2321.41   
Total input tokens:                      1213770   
Total generated tokens:                  150317    
Request throughput (req/s):              0.13      
Output token throughput (tok/s):         64.75     
Peak output token throughput (tok/s):    201.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          587.61    
---------------Time to First Token----------------
Mean TTFT (ms):                          11364.35  
Median TTFT (ms):                        6771.14   
P50 TTFT (ms):                           6771.14   
P90 TTFT (ms):                           14524.22  
P95 TTFT (ms):                           41179.61  
P99 TTFT (ms):                           108503.36 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          365.22    
Median TPOT (ms):                        363.35    
P50 TPOT (ms):                           363.35    
P90 TPOT (ms):                           428.04    
P95 TPOT (ms):                           473.25    
P99 TPOT (ms):                           617.94    
---------------Inter-token Latency----------------
Mean ITL (ms):                           356.16    
Median ITL (ms):                         134.89    
P50 ITL (ms):                            134.89    
P90 ITL (ms):                            1301.54   
P95 ITL (ms):                            2322.01   
P99 ITL (ms):                            2601.47   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          189616.60 
Median E2EL (ms):                        177939.62 
P50 E2EL (ms):                           177939.62 
P90 E2EL (ms):                           335882.76 
P95 E2EL (ms):                           352618.67 
P99 E2EL (ms):                           407715.61 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

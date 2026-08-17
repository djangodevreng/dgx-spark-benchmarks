# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-17 00:46:07
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-31B-IT-NVFP4 --tokenizer nvidia/Gemma-4-31B-IT-NVFP4 --served-model-name gemma-4-31b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  2951.45   
Total input tokens:                      1202084   
Total generated tokens:                  150317    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         50.93     
Peak output token throughput (tok/s):    126.00    
Peak concurrent requests:                27.00     
Total token throughput (tok/s):          458.22    
---------------Time to First Token----------------
Mean TTFT (ms):                          10903.12  
Median TTFT (ms):                        5964.17   
P50 TTFT (ms):                           5964.17   
P90 TTFT (ms):                           11574.73  
P95 TTFT (ms):                           47260.45  
P99 TTFT (ms):                           109729.61 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          466.68    
Median TPOT (ms):                        465.01    
P50 TPOT (ms):                           465.01    
P90 TPOT (ms):                           524.55    
P95 TPOT (ms):                           581.57    
P99 TPOT (ms):                           751.75    
---------------Inter-token Latency----------------
Mean ITL (ms):                           456.80    
Median ITL (ms):                         246.40    
P50 ITL (ms):                            246.40    
P90 ITL (ms):                            256.37    
P95 ITL (ms):                            2256.14   
P99 ITL (ms):                            5082.10   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          239787.67 
Median E2EL (ms):                        226702.29 
P50 E2EL (ms):                           226702.29 
P90 E2EL (ms):                           426169.47 
P95 E2EL (ms):                           443575.26 
P99 E2EL (ms):                           495132.20 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

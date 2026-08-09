# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-08 02:05:36
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --served-model-name nemotron-3-nano-30b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  798.86    
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.38      
Output token throughput (tok/s):         188.16    
Peak output token throughput (tok/s):    288.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1693.88   
---------------Time to First Token----------------
Mean TTFT (ms):                          1078.37   
Median TTFT (ms):                        985.62    
P50 TTFT (ms):                           985.62    
P90 TTFT (ms):                           1453.01   
P95 TTFT (ms):                           1759.37   
P99 TTFT (ms):                           3586.08   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          127.93    
Median TPOT (ms):                        130.00    
P50 TPOT (ms):                           130.00    
P90 TPOT (ms):                           135.63    
P95 TPOT (ms):                           139.50    
P99 TPOT (ms):                           151.75    
---------------Inter-token Latency----------------
Mean ITL (ms):                           126.23    
Median ITL (ms):                         101.85    
P50 ITL (ms):                            101.85    
P90 ITL (ms):                            108.36    
P95 ITL (ms):                            331.76    
P99 ITL (ms):                            680.34    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          64328.29  
Median E2EL (ms):                        63619.97  
P50 E2EL (ms):                           63619.97  
P90 E2EL (ms):                           115509.71 
P95 E2EL (ms):                           118837.86 
P99 E2EL (ms):                           123222.35 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

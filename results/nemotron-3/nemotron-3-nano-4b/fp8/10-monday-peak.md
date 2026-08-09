# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-08 10:46:22
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  427.33    
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.70      
Output token throughput (tok/s):         351.76    
Peak output token throughput (tok/s):    576.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          3166.56   
---------------Time to First Token----------------
Mean TTFT (ms):                          840.95    
Median TTFT (ms):                        774.09    
P50 TTFT (ms):                           774.09    
P90 TTFT (ms):                           1334.11   
P95 TTFT (ms):                           1726.35   
P99 TTFT (ms):                           2167.16   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          66.71     
Median TPOT (ms):                        67.95     
P50 TPOT (ms):                           67.95     
P90 TPOT (ms):                           73.02     
P95 TPOT (ms):                           77.62     
P99 TPOT (ms):                           81.54     
---------------Inter-token Latency----------------
Mean ITL (ms):                           66.03     
Median ITL (ms):                         45.77     
P50 ITL (ms):                            45.77     
P90 ITL (ms):                            87.95     
P95 ITL (ms):                            193.35    
P99 ITL (ms):                            498.97    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          33927.19  
Median E2EL (ms):                        33184.18  
P50 E2EL (ms):                           33184.18  
P90 E2EL (ms):                           60985.37  
P95 E2EL (ms):                           63045.29  
P99 E2EL (ms):                           65736.93  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.

# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-16 16:46:10
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  698.87    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         138.93    
Peak output token throughput (tok/s):    272.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1305.66   
---------------Time to First Token----------------
Mean TTFT (ms):                          1166.14   
Median TTFT (ms):                        1096.33   
P50 TTFT (ms):                           1096.33   
P90 TTFT (ms):                           2049.70   
P95 TTFT (ms):                           2454.56   
P99 TTFT (ms):                           3096.11   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          63.57     
Median TPOT (ms):                        64.39     
P50 TPOT (ms):                           64.39     
P90 TPOT (ms):                           76.72     
P95 TPOT (ms):                           80.05     
P99 TPOT (ms):                           89.51     
---------------Inter-token Latency----------------
Mean ITL (ms):                           63.11     
Median ITL (ms):                         51.87     
P50 ITL (ms):                            51.87     
P90 ITL (ms):                            58.62     
P95 ITL (ms):                            60.05     
P99 ITL (ms):                            626.62    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          31802.98  
Median E2EL (ms):                        30621.74  
P50 E2EL (ms):                           30621.74  
P90 E2EL (ms):                           55286.50  
P95 E2EL (ms):                           60993.98  
P99 E2EL (ms):                           65044.23  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.

# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-05 03:40:44
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1471.68   
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         142.22    
Peak output token throughput (tok/s):    61.00     
Peak concurrent requests:                48.00     
Total token throughput (tok/s):          180.14    
---------------Time to First Token----------------
Mean TTFT (ms):                          255764.88 
Median TTFT (ms):                        281808.30 
P50 TTFT (ms):                           281808.30 
P90 TTFT (ms):                           616334.35 
P95 TTFT (ms):                           659230.50 
P99 TTFT (ms):                           727515.09 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          118.11    
Median TPOT (ms):                        115.02    
P50 TPOT (ms):                           115.02    
P90 TPOT (ms):                           141.72    
P95 TPOT (ms):                           147.82    
P99 TPOT (ms):                           159.34    
---------------Inter-token Latency----------------
Mean ITL (ms):                           386.15    
Median ITL (ms):                         404.33    
P50 ITL (ms):                            404.33    
P90 ITL (ms):                            423.89    
P95 ITL (ms):                            428.11    
P99 ITL (ms):                            679.33    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          730035.75 
Median E2EL (ms):                        759621.22 
P50 E2EL (ms):                           759621.22 
P90 E2EL (ms):                           1158035.87
P95 E2EL (ms):                           1193521.31
P99 E2EL (ms):                           1248319.49
---------------Speculative Decoding---------------
Acceptance rate (%):                     80.36     
Acceptance length:                       3.41      
Drafts:                                  61366     
Draft tokens:                            184098    
Accepted tokens:                         147946    
Per-position acceptance (%):
  Position 0:                            90.36     
  Position 1:                            79.48     
  Position 2:                            71.25     
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.

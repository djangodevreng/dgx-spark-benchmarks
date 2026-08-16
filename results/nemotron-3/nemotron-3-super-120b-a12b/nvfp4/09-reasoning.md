# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-15 08:18:34
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1440.79   
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         145.27    
Peak output token throughput (tok/s):    64.00     
Peak concurrent requests:                48.00     
Total token throughput (tok/s):          184.00    
---------------Time to First Token----------------
Mean TTFT (ms):                          266828.83 
Median TTFT (ms):                        284459.11 
P50 TTFT (ms):                           284459.11 
P90 TTFT (ms):                           653846.58 
P95 TTFT (ms):                           673895.06 
P99 TTFT (ms):                           737928.34 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          119.58    
Median TPOT (ms):                        118.35    
P50 TPOT (ms):                           118.35    
P90 TPOT (ms):                           138.63    
P95 TPOT (ms):                           157.59    
P99 TPOT (ms):                           168.45    
---------------Inter-token Latency----------------
Mean ITL (ms):                           394.74    
Median ITL (ms):                         408.37    
P50 ITL (ms):                            408.37    
P90 ITL (ms):                            442.35    
P95 ITL (ms):                            446.89    
P99 ITL (ms):                            823.21    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          743187.44 
Median E2EL (ms):                        788425.38 
P50 E2EL (ms):                           788425.38 
P90 E2EL (ms):                           1139031.87
P95 E2EL (ms):                           1189419.14
P99 E2EL (ms):                           1212066.83
---------------Speculative Decoding---------------
Acceptance rate (%):                     82.37     
Acceptance length:                       3.47      
Drafts:                                  60305     
Draft tokens:                            180915    
Accepted tokens:                         149023    
Per-position acceptance (%):
  Position 0:                            91.94     
  Position 1:                            81.80     
  Position 2:                            73.37     
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

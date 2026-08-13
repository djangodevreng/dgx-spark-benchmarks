# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-13 12:11:46
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Mistral-Small-4-119B-2603-NVFP4 --tokenizer mistralai/Mistral-Small-4-119B-2603-NVFP4 --served-model-name mistral-small-4-119b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1579.75   
Total input tokens:                      55708     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         132.49    
Peak output token throughput (tok/s):    196.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          167.76    
---------------Time to First Token----------------
Mean TTFT (ms):                          775.14    
Median TTFT (ms):                        763.22    
P50 TTFT (ms):                           763.22    
P90 TTFT (ms):                           1057.83   
P95 TTFT (ms):                           1069.06   
P99 TTFT (ms):                           1158.85   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          230.92    
Median TPOT (ms):                        231.56    
P50 TPOT (ms):                           231.56    
P90 TPOT (ms):                           263.21    
P95 TPOT (ms):                           265.04    
P99 TPOT (ms):                           270.48    
---------------Inter-token Latency----------------
Mean ITL (ms):                           224.83    
Median ITL (ms):                         249.56    
P50 ITL (ms):                            249.56    
P90 ITL (ms):                            273.30    
P95 ITL (ms):                            276.84    
P99 ITL (ms):                            287.53    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          941921.59 
Median E2EL (ms):                        963871.99 
P50 E2EL (ms):                           963871.99 
P90 E2EL (ms):                           1364522.08
P95 E2EL (ms):                           1442413.28
P99 E2EL (ms):                           1478563.46
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

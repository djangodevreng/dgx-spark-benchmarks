# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-08 14:39:17
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1386.75   
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         150.93    
Peak output token throughput (tok/s):    246.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          190.97    
---------------Time to First Token----------------
Mean TTFT (ms):                          710.09    
Median TTFT (ms):                        698.41    
P50 TTFT (ms):                           698.41    
P90 TTFT (ms):                           907.39    
P95 TTFT (ms):                           929.75    
P99 TTFT (ms):                           1105.02   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          194.46    
Median TPOT (ms):                        194.99    
P50 TPOT (ms):                           194.99    
P90 TPOT (ms):                           218.67    
P95 TPOT (ms):                           219.79    
P99 TPOT (ms):                           223.49    
---------------Inter-token Latency----------------
Mean ITL (ms):                           190.14    
Median ITL (ms):                         205.86    
P50 ITL (ms):                            205.86    
P90 ITL (ms):                            226.99    
P95 ITL (ms):                            231.55    
P99 ITL (ms):                            248.00    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          796299.18 
Median E2EL (ms):                        803042.52 
P50 E2EL (ms):                           803042.52 
P90 E2EL (ms):                           1162839.63
P95 E2EL (ms):                           1246215.85
P99 E2EL (ms):                           1281821.93
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

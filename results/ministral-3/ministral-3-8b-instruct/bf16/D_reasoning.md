# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-07 17:46:59
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  710.31    
Total input tokens:                      55108     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         294.66    
Peak output token throughput (tok/s):    559.00    
Peak concurrent requests:                43.00     
Total token throughput (tok/s):          372.25    
---------------Time to First Token----------------
Mean TTFT (ms):                          285.35    
Median TTFT (ms):                        264.30    
P50 TTFT (ms):                           264.30    
P90 TTFT (ms):                           380.46    
P95 TTFT (ms):                           403.82    
P99 TTFT (ms):                           566.92    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          68.58     
Median TPOT (ms):                        70.56     
P50 TPOT (ms):                           70.56     
P90 TPOT (ms):                           77.23     
P95 TPOT (ms):                           78.06     
P99 TPOT (ms):                           78.75     
---------------Inter-token Latency----------------
Mean ITL (ms):                           69.64     
Median ITL (ms):                         71.77     
P50 ITL (ms):                            71.77     
P90 ITL (ms):                            79.47     
P95 ITL (ms):                            86.78     
P99 ITL (ms):                            95.40     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          291798.53 
Median E2EL (ms):                        274209.64 
P50 E2EL (ms):                           274209.64 
P90 E2EL (ms):                           473433.68 
P95 E2EL (ms):                           499054.71 
P99 E2EL (ms):                           523363.36 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.

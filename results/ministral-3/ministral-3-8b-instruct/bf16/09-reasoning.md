# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-07 04:41:29
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-8B-Instruct-2512 --tokenizer mistralai/Ministral-3-8B-Instruct-2512 --served-model-name ministral-3-8b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  696.47    
Total input tokens:                      55108     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         300.52    
Peak output token throughput (tok/s):    560.00    
Peak concurrent requests:                43.00     
Total token throughput (tok/s):          379.65    
---------------Time to First Token----------------
Mean TTFT (ms):                          528.84    
Median TTFT (ms):                        591.80    
P50 TTFT (ms):                           591.80    
P90 TTFT (ms):                           715.43    
P95 TTFT (ms):                           751.83    
P99 TTFT (ms):                           997.70    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          68.84     
Median TPOT (ms):                        70.66     
P50 TPOT (ms):                           70.66     
P90 TPOT (ms):                           77.10     
P95 TPOT (ms):                           78.18     
P99 TPOT (ms):                           78.99     
---------------Inter-token Latency----------------
Mean ITL (ms):                           69.60     
Median ITL (ms):                         71.29     
P50 ITL (ms):                            71.29     
P90 ITL (ms):                            80.19     
P95 ITL (ms):                            83.33     
P99 ITL (ms):                            93.39     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          291868.53 
Median E2EL (ms):                        277532.72 
P50 E2EL (ms):                           277532.72 
P90 E2EL (ms):                           465512.62 
P95 E2EL (ms):                           498529.79 
P99 E2EL (ms):                           519225.63 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.

# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-07 15:40:33
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model mistralai/Ministral-3-3B-Instruct-2512 --tokenizer mistralai/Ministral-3-3B-Instruct-2512 --served-model-name ministral-3-3b-instruct-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  470.31    
Total input tokens:                      55108     
Total generated tokens:                  209303    
Request throughput (req/s):              0.11      
Output token throughput (tok/s):         445.03    
Peak output token throughput (tok/s):    744.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          562.20    
---------------Time to First Token----------------
Mean TTFT (ms):                          184.35    
Median TTFT (ms):                        160.51    
P50 TTFT (ms):                           160.51    
P90 TTFT (ms):                           221.26    
P95 TTFT (ms):                           261.60    
P99 TTFT (ms):                           640.83    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          34.62     
Median TPOT (ms):                        36.44     
P50 TPOT (ms):                           36.44     
P90 TPOT (ms):                           41.05     
P95 TPOT (ms):                           41.52     
P99 TPOT (ms):                           42.21     
---------------Inter-token Latency----------------
Mean ITL (ms):                           35.13     
Median ITL (ms):                         35.88     
P50 ITL (ms):                            35.88     
P90 ITL (ms):                            43.08     
P95 ITL (ms):                            44.60     
P99 ITL (ms):                            53.61     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          147255.70 
Median E2EL (ms):                        140722.50 
P50 E2EL (ms):                           140722.50 
P90 E2EL (ms):                           241192.25 
P95 E2EL (ms):                           258444.22 
P99 E2EL (ms):                           277892.95 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.

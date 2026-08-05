# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-09 15:03:29
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  893.30    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.06      
Output token throughput (tok/s):         234.30    
Peak output token throughput (tok/s):    452.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          296.46    
---------------Time to First Token----------------
Mean TTFT (ms):                          526.91    
Median TTFT (ms):                        517.55    
P50 TTFT (ms):                           517.55    
P90 TTFT (ms):                           729.89    
P95 TTFT (ms):                           749.43    
P99 TTFT (ms):                           919.94    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          101.04    
Median TPOT (ms):                        101.15    
P50 TPOT (ms):                           101.15    
P90 TPOT (ms):                           106.70    
P95 TPOT (ms):                           107.20    
P99 TPOT (ms):                           109.12    
---------------Inter-token Latency----------------
Mean ITL (ms):                           103.83    
Median ITL (ms):                         100.71    
P50 ITL (ms):                            100.71    
P90 ITL (ms):                            108.96    
P95 ITL (ms):                            109.99    
P99 ITL (ms):                            290.48    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          420382.28 
Median E2EL (ms):                        408333.50 
P50 E2EL (ms):                           408333.50 
P90 E2EL (ms):                           643415.69 
P95 E2EL (ms):                           701673.96 
P99 E2EL (ms):                           720614.29 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
